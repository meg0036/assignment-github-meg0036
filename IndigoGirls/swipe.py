import random



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
    return {ERROR_PROPERTY: ERROR_PREFIX + diagnostic}


def merge(array):
    score = 0
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

def swipeAll(messageDictionary):
        resultDictionary = {}
        msg_board = messageDictionary[u"board"]
        directions = ['left', 'right', 'up', 'down']
        new_msg = {}
        max_score = 0
        max_board = {}
        new_msg[u"board"] = msg_board
        new_msg[u"op"] = u"swipe"
        for i in range(4):
            new_msg[u"direction"] = directions[i]
            result_test = swipe(new_msg)
            if result_test[u"gameStatus"] == "underway":
                score = result_test[u"score"]
                if score > max_score:
                    max_score = score
                    max_board = result_test[u"board"]
        resultDictionary[u"score"] = max_score
        resultDictionary[u"board"] = max_board
        return resultDictionary

def swipe(messageDictionary):
    resultDictionary = {}
    if (u"board" not in messageDictionary):
        return buildErrorString('missing board')
    if (u"direction" not in messageDictionary):
        return buildErrorString('missing direction')
    elif messageDictionary[u"direction"] not in ['up', 'down', 'left', 'right']:
        return buildErrorString('invalid direction')

    if (u"columnCount" not in messageDictionary[u"board"]):
        return buildErrorString('columnCount is not int the board')
    elif not isinstance(messageDictionary[u"board"][u"columnCount"], int):
        return buildErrorString('columnCount is not an integer')
    elif not (
                    messageDictionary[u"board"][u"columnCount"] > 1 and messageDictionary[u"board"][
                u"columnCount"] < 100):
        return buildErrorString('columnCount is out of bounds')
    else:
        column = messageDictionary[u"board"][u"columnCount"]

    if (u"rowCount" not in messageDictionary[u"board"]):
        return buildErrorString('rowCount is not in the board')
    elif not isinstance(messageDictionary[u"board"][u"rowCount"], int):
        return buildErrorString('rowCount is not an integer')
    elif not (messageDictionary[u"board"][u"rowCount"] > 1 and messageDictionary[u"board"][u"rowCount"] < 100):
        return buildErrorString('rowCount is out of bounds')
    else:
        row = messageDictionary[u"board"][u"rowCount"]

    if (u"grid" not in messageDictionary[u"board"]):
        return buildErrorString('grid is not in the board')

    resultDictionary[u"score"] = 0
    resultDictionary[u"board"] = {}

    resultDictionary[u"board"][u"columnCount"] = column
    resultDictionary[u"board"][u"rowCount"] = row
    length = column * row
    resultDictionary[u"board"][u"grid"] = [0] * length
    if length != len(messageDictionary[u"board"][u"grid"]):
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


