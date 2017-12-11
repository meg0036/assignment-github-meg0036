import json
import random
import swipe
import status
import recommend
import predict

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
        resultDictionary = swipe.swipe(messageDictionary)
    elif (messageDictionary[u"op"] == u"recommend"):
        resultDictionary = recommend.recommend(messageDictionary)
    elif (messageDictionary[u"op"] == u"status"):
        resultDictionary = status.status(messageDictionary)
    elif (messageDictionary[u"op"] == u"predict"):
        resultDictionary = predict.predict(messageDictionary)
    else:
        resultDictionary = buildErrorString('op is invalid')

    #Covert the dictionary back to a string in JSON format
    resultJson = json.dumps(resultDictionary)
    return resultJson