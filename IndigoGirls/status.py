import dispatch
import swipe

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
def status(messageDictionary):
    resultDictionary = {}
    resultDictionary[u"gameStatus"] = {}

    column = messageDictionary[u"board"][u"columnCount"]
    row = messageDictionary[u"board"][u"rowCount"]
    msg_grid = messageDictionary[u"board"][u"grid"]
    length = column * row
    tile = 0
    if u"tile" not in messageDictionary:
        tile = 2 ** length * 0.6875
    else:
        tile = messageDictionary[u"tile"]
    if tile < 2 or tile > 2 ** length:
        return buildErrorString("invalid tile value")

    max_item = max(msg_grid)

    new_msg = {}
    new_msg[u"score"] = 0
    new_msg[u"board"] = messageDictionary[u"board"]
    new_msg = swipeAll(new_msg)

    score = new_msg[u"score"]
    if (2 ** max_item) >= tile:
        resultDictionary[u"gameStatus"] = "win"
    else:
        if score == 0:
            resultDictionary[u"gameStatus"] = "lose"
        else:
            resultDictionary[u"gameStatus"] = "underway"

    return resultDictionary