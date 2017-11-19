import dispatch
from swipe import swipe

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

def recommend(messageDictionary):
    resultDictionary = {}
    resultDictionary[u"gameStatus"] = {}
    if u"moves" not in messageDictionary:
        move_step = 0
    else:
        move_tmp = messageDictionary[u"moves"]
        if type(move_tmp) is int:
            move_step = move_tmp
        else:
            return buildErrorString('invalid moves')
    resultDictionary[u"score"] = 0
    resultDictionary[u"board"] = {}
    column = messageDictionary[u"board"][u"columnCount"]
    row = messageDictionary[u"board"][u"rowCount"]
    resultDictionary[u"board"][u"columnCount"] = column
    resultDictionary[u"board"][u"rowCount"] = row
    length = column * row
    resultDictionary[u"board"][u"grid"] = [0] * length

    resultDictionary[u"gameStatus"] = "underway"
    move_step = 1 if move_step == 0 else move_step
    new_msg = {}
    new_msg[u"score"] = 0
    new_msg[u"board"] = messageDictionary[u"board"]
    for i in range(move_step):
        new_msg = swipeAll(new_msg)
        if new_msg[u"score"] == 0:
            break
    if new_msg[u"score"] == 0:
        return buildErrorString('no tiles can be shifted in 1 move')
    else:
        resultDictionary[u"score"] = new_msg[u"score"]
        resultDictionary[u"board"] = new_msg[u"board"]
        resultDictionary[u"gameStatus"] = "underway"

    return resultDictionary
