import json
import random


'''
Created September 22, 2017

@author David Umphress & Mason Glover

'''



def dispatch(messageJson=None):
    """
        dispatch is the microservice dispatcher for IndigoGirls, a 2048-like game.  It routes
        requests for game state transformations to the appropriate functions
        :param
            messageJson: JSON string that describes the state of the game needed for the
                        requested transformation
            :return:    A JSON string that describes the state of the game after the requested transformation
                        has taken place.
    """

    def buildErrorString(diagnostic=None):
        """
            returns a dictionary containing the specified key and accompanying diagnostic information
            :param
                diagnostic:     A string that describes the error
            :return:    A dictionary that contains the specified error key having a value that
                        consists of the specfied error string followed by a free-form diagnostic message
        """
        ERROR_PROPERTY = u'gameStatus'
        ERROR_PREFIX = u'error:  '
        return {ERROR_PROPERTY:  ERROR_PREFIX + diagnostic}


    def InitializeGame(messageDictionary):
        resultDictionary = {}

        resultDictionary[u"score"]=0
        resultDictionary[u"board"]={}

        if (u"columnCount" not in messageDictionary):
            resultDictionary[u"board"][u"columnCount"] = 4
        elif not isinstance(messageDictionary[u"columnCount"], int):
            return buildErrorString('columnCount is not an integer')
        elif not (messageDictionary[u"columnCount"]>1 and messageDictionary[u"columnCount"]<100):
            return buildErrorString('columnCount is out of bounds')
        else:
            resultDictionary[u"board"][u"columnCount"] = messageDictionary[u"columnCount"]

        if (u"rowCount" not in messageDictionary):
            resultDictionary[u"board"][u"rowCount"] = 4
        elif not isinstance(messageDictionary[u"rowCount"], int):
            return buildErrorString('rowCount is not an integer')
        elif not (messageDictionary[u"rowCount"]>1 and messageDictionary[u"rowCount"]<100):
            return buildErrorString('rowCount is out of bounds')
        else:
            resultDictionary[u"board"][u"rowCount"] = messageDictionary[u"rowCount"]

        length=resultDictionary[u"board"][u"columnCount"] * resultDictionary[u"board"][u"rowCount"]
        resultDictionary[u"board"][u"grid"] = [0] * length
        index=random.sample(range(length),2)
        for i in index:
            if random.random()>0.25:
                resultDictionary[u"board"][u"grid"][i] = 1
            else:
                resultDictionary[u"board"][u"grid"][i] = 2

        resultDictionary[u"gameStatus"] = "underway"
        return resultDictionary

    def merge(array):
        score=0
        n = len(array)
        temp = []
        for i in range(n):
            if array[i] != 0:
                temp.append(array[i])
        i = 0
        while i < len(temp) - 1:
            if temp[i] == 0:
                del temp[i]
            else:
                if temp[i] == temp[i + 1]:
                    temp[i] += 1
                    score += 2 ** temp[i]
                    del temp[i + 1]
                i += 1
        m = n - len(temp)
        for i in range(m):
            temp.append(0)
        for i in range(n):
            array[i] = temp[i]
        return score

    def Swipe(messageDictionary):
        resultDictionary = {}

        resultDictionary[u"score"]=0
        resultDictionary[u"board"]={}

        column=messageDictionary[u"board"][u"columnCount"]
        row=messageDictionary[u"board"][u"rowCount"]
        resultDictionary[u"board"][u"columnCount"] = column
        resultDictionary[u"board"][u"rowCount"] = row
        length=column * row
        resultDictionary[u"board"][u"grid"] = [0] * length

        if (u"direction" not in messageDictionary):
            return buildErrorString('missing direction')
        elif messageDictionary[u"direction"] not in ['up','down','left','right']:
            return buildErrorString('invalid direction')

        if length!=len(messageDictionary[u"board"][u"grid"]):
            return buildErrorString('invalid board')

        temp_board = []
        msg_grid = messageDictionary[u"board"][u"grid"]

        if messageDictionary[u"direction"] == 'right':
            for i in range(row):
                temp_row = []
                for j in range(column):
                    temp_row.append(msg_grid[i * column + j])
                temp_board.append(temp_row[::-1])

            for i in range(row):
                score = merge(temp_board[i])
                resultDictionary[u"score"] += score
                temp_board[i] = temp_board[i][::-1]
            for i in range(row):
                for j in range(column):
                    resultDictionary[u"board"][u"grid"][i * column + j] = temp_board[i][j]

        elif messageDictionary[u"direction"] == 'left':
            for i in range(row):
                temp_row = []
                for j in range(column):
                    temp_row.append(msg_grid[i * column + j])
                temp_board.append(temp_row)

            for i in range(row):
                score = merge(temp_board[i])
                resultDictionary[u"score"] += score
            for i in range(row):
                for j in range(column):
                    resultDictionary[u"board"][u"grid"][i * column + j] = temp_board[i][j]

        elif messageDictionary[u"direction"] == 'up':
            for j in range(column):
                temp_column = []
                for i in range(row):
                    temp_column.append(msg_grid[i * column + j])
                temp_board.append(temp_column)

            for i in range(row):
                score = merge(temp_board[i])
                resultDictionary[u"score"] += score

            for j in range(column):
                for i in range(row):
                    resultDictionary[u"board"][u"grid"][i + j * row] = temp_board[i][j]

        elif messageDictionary[u"direction"] == 'down':
            for j in range(column):
                temp_column = []
                for i in range(row):
                    temp_column.append(msg_grid[i * column + j])
                temp_board.append(temp_column[::-1])

            for i in range(row):
                score = merge(temp_board[i])
                resultDictionary[u"score"] += score
                temp_board[i] = temp_board[i][::-1]

            for j in range(column):
                for i in range(row):
                    resultDictionary[u"board"][u"grid"][i + j * row] = temp_board[i][j]

        if resultDictionary[u"board"][u"grid"] == msg_grid:
            return buildErrorString('no tiles can be shifted')

        while True:
            index = random.randint(0, length - 1)
            if resultDictionary[u"board"][u"grid"][index] == 0:
                if random.random() > 0.25:
                    resultDictionary[u"board"][u"grid"][index] = 1
                else:
                    resultDictionary[u"board"][u"grid"][index] = 2
                break

        resultDictionary[u"gameStatus"] = "underway"
        return resultDictionary

    #Validate JSONness of input be converting the string to an equivalent dictionary
    try:
        messageDictionary = json.loads(messageJson)

    except:
        resultDictionary = json.dumps(buildErrorString('input string is not valid JSON'))

        return resultDictionary

    #Validate presence of dispatching code
    if(u"op" not in messageDictionary):
        resultDictionary = json.dumps(buildErrorString('op is missing'))
        return resultDictionary


    #Perform the game transformation as directed by the value of the "op" key
    #  input to each function:  a dictionary containing the name-value pairs of the input JSON string
    #  output of each function:  a dictionary containing name-value pairs to be encoded as a JSON string
    if(messageDictionary[u"op"] == u"initializeGame"):
        resultDictionary = InitializeGame(messageDictionary)
    elif(messageDictionary[u"op"] == u"swipe"):
        resultDictionary = Swipe(messageDictionary)
    else:
        resultDictionary = buildErrorString('op is invalid')

    #Covert the dictionary back to a string in JSON format
    resultJson = json.dumps(resultDictionary)
    return resultJson