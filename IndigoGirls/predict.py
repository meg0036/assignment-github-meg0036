import dispatch
from swipe import swipe
import copy


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

def swipeAll2(messageDictionary):
        resultDictionary = {}
        msg_board = messageDictionary[u"board"]
        directions = ['left', 'right', 'up', 'down']
        new_msg = {}
        scores = []
        boards = []
        new_msg[u"board"] = msg_board
        new_msg[u"op"] = u"swipe"
        for i in range(4):
            new_msg[u"direction"] = directions[i]
            result_test = swipe(new_msg)
            if result_test[u"board"] != new_msg[u"board"]:
                boards.append(result_test[u"board"])
                scores.append(result_test[u"score"])
            else:
                boards.append(new_msg[u"board"])
                scores.append(0)

        resultDictionary[u"score"] = scores
        resultDictionary[u"board"] = boards
        return resultDictionary

def predict(messageDictionary):
    resultDictionary = {}
    resultDictionary[u"gameStatus"] = {}
    if u"direction" not in messageDictionary:
        return buildErrorString('missing direction')
    elif messageDictionary[u"direction"] not in ['up', 'down', 'left', 'right']:
        return buildErrorString('invalid direction')
    else:
        direction = messageDictionary[u"direction"]
    move_step = 0
    if u"moves" not in messageDictionary:
        move_step = 1
    else:
        move_tmp = messageDictionary[u"moves"]
        if type(move_tmp) is int:
            if move_tmp < 0:
                return buildErrorString('invalid moves')
            elif move_tmp == 0:
                move_step = 1
            else:
                move_step = move_tmp


        else:
            return buildErrorString('invalid moves')

    if u"board" not in messageDictionary:
        return buildErrorString('missing board')
    elif u"columnCount" not in messageDictionary[u"board"]:
        return buildErrorString('missing columnCount')
    elif u"rowCount" not in messageDictionary[u"board"]:
        return buildErrorString('missing rowCount')
    elif u"grid" not in messageDictionary[u"board"]:
        return buildErrorString('missing grid')
    else:
        column = messageDictionary[u"board"][u"columnCount"]
        row = messageDictionary[u"board"][u"rowCount"]
        if not isinstance(column, int):
            return buildErrorString('columnCount is not an integer')
        elif not (column > 1 and column < 100):
            return buildErrorString('columnCount is out of bounds')
        if not isinstance(row, int):
            return buildErrorString('rowCount is not an integer')
        elif not (row > 1 and row < 100):
            return buildErrorString('rowCount is out of bounds')
    length = column * row
    if length != len(messageDictionary[u"board"][u"grid"]):
        return buildErrorString('invalid board')
    msg_grid = messageDictionary[u"board"][u"grid"]

    if (max(msg_grid) > length):
        return buildErrorString('Tile Out Of Bounds')


    first_msg = {}
    first_msg[u"board"] = messageDictionary[u"board"]
    first_msg[u"direction"] = messageDictionary[u"direction"]
    new_msg_dict = swipe(first_msg)
    if new_msg_dict[u"board"][u"grid"] == first_msg[u"board"][u"grid"]:
        return buildErrorString('no tiles can be shifted')
    score = new_msg_dict[u"score"]
    NewListDict = newDictionary(new_msg_dict)

    highScore = lowScore = avgscore = score

    while move_step > 1:
        count = len(NewListDict)
        scorelist = []
        nextListDict = []
        for i in range(count):
            new_msg_dict = swipeAll2(NewListDict[i])
            score = new_msg_dict[u"score"]

            scorelist.extend(score)

            for j in range(4):
                tmp = {}
                tmp[u"board"] = new_msg_dict[u"board"][j]
                nextListDict.extend(newDictionary(tmp))

        max_score = max(scorelist)
        min_score = min(scorelist)
        sumscore = 0
        for j in range(count * 4):
            if j < (count * 2):
                sumscore += (scorelist[j] * 3)
            else:
                sumscore += (scorelist[j] * 1)
        avg_score = sumscore / (count * 8)
        avg_score = int(round(avg_score))
        avgscore += avg_score
        highScore += max_score
        lowScore += min_score
        move_step -= 1
        NewListDict = nextListDict
    resultDictionary[u"highScore"] = highScore
    resultDictionary[u"lowScore"] = lowScore
    resultDictionary[u"averageScore"] = avgscore
    resultDictionary[u"gameStatus"] = "underway"
    return resultDictionary


def newDictionary (messageDictionary):
    NewListDict = []
    column = messageDictionary[u"board"][u"columnCount"]
    row = messageDictionary[u"board"][u"rowCount"]
    for i in range(column * row):
        if messageDictionary[u"board"][u"grid"][i] == 0:
            NewGrid = copy.deepcopy(messageDictionary)
            NewGrid[u"board"][u"grid"][i] = 1
            NewListDict.append(NewGrid)
    for i in range(column * row):
        if messageDictionary[u"board"][u"grid"][i] == 0:
            NewGrid = copy.deepcopy(messageDictionary)
            NewGrid[u"board"][u"grid"][i] = 2
            NewListDict.append(NewGrid)
    return NewListDict