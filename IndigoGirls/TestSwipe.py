import unittest
import IndigoGirls.dispatch as IndigoGirls
import json


def test_100_010_invalidDirection(self):
    msg = '{"op":"swipe","direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": [3, 3, 3, 3, 1, 1, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0]}}'
    errorMsg = {self.key: self.error + 'invalid direction'}
    self.assertEqual(IndigoGirls.dispatch(msg), json.dumps(errorMsg))

def test_200_020_missingDirection(self):
        msg = '{"op":"swipe", "board": {"columnCount": 4, "rowCount": 4, "grid": [3, 3, 3, 3, 1, 1, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0]}}'
        errorMsg = {self.key: self.error + 'missing direction'}
        self.assertEqual(IndigoGirls.dispatch(msg), json.dumps(errorMsg))

def test_200_030_cannotShift(self):
        msg = '{"op":"swipe", "direction": "left", "board": {"columnCount": 4, "rowCount": 4, "grid": [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]}}'
        errorMsg = {self.key: self.error + 'no tiles can be shifted'}
        self.assertEqual(IndigoGirls.dispatch(msg), json.dumps(errorMsg))

def test_200_040_boardInvalid(self):
        msg = '{"op":"swipe", "direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": [1, 2]}}'
        errorMsg = {self.key: self.error + 'invalid board'}
        self.assertEqual(IndigoGirls.dispatch(msg), json.dumps(errorMsg))


def test_200_050_canMove(self):
    msg = '{"op":"swipe","direction": "left", "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]}}'
    playingGridDict = json.loads(IndigoGirls.dispatch(msg))
    gridScore = playingGridDict['score']
    gridListDict = playingGridDict['board']
    gridList = gridListDict["grid"]
    self.assertEqual(gridScore, 0)
    self.assertEqual(gridListDict["columnCount"], 4)
    self.assertEqual(gridListDict["rowCount"], 4)
    self.assertEqual(playingGridDict["gameStatus"], 'underway')
    self.assertEqual(gridListDict["rowCount"], 4)
    count = 0
    correct = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    for i in range(len(correct)):
        if gridList[i] != correct[i]:
            count += 1
    self.assertEqual(count, 1)


def test_200_060_canCombine(self):
    msg = '{"op":"swipe","direction":"left", "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0]}}'
    playingGridDict = json.loads(IndigoGirls.dispatch(msg))
    gridScore = playingGridDict['score']
    gridListDict = playingGridDict['board']
    gridList = gridListDict["grid"]
    self.assertEqual(gridScore, 4)
    self.assertEqual(gridListDict["columnCount"], 4)
    self.assertEqual(gridListDict["rowCount"], 4)
    self.assertEqual(playingGridDict["gameStatus"], 'underway')
    self.assertEqual(gridListDict["rowCount"], 4)
    count = 0
    correct = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0]
    for i in range(len(correct)):
        if gridList[i] != correct[i]:
            count += 1
    self.assertEqual(count, 1)


def test_200_070_keepScore(self):
    msg = '{"op":"swipe","direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0]}}'
    playingGridDict = json.loads(IndigoGirls.dispatch(msg))
    gridScore = playingGridDict['score']
    gridListDict = playingGridDict['board']
    gridList = gridListDict["grid"]
    self.assertEqual(gridScore, 4)
    self.assertEqual(gridListDict["columnCount"], 4)
    self.assertEqual(gridListDict["rowCount"], 4)
    self.assertEqual(playingGridDict["gameStatus"], 'underway')
    self.assertEqual(gridListDict["rowCount"], 4)
    count = 0
    correct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2]
    for i in range(len(correct)):
        if gridList[i] != correct[i]:
            count += 1
    self.assertEqual(count, 1)


def test_200_080_calculateScore(self):
    msg = '{"op":"swipe","direction": "up", "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2]}}'
    playingGridDict = json.loads(IndigoGirls.dispatch(msg))
    gridScore = playingGridDict['score']
    gridListDict = playingGridDict['board']
    gridList = gridListDict["grid"]
    self.assertEqual(gridScore, 8)
    self.assertEqual(gridListDict["columnCount"], 4)
    self.assertEqual(gridListDict["rowCount"], 4)
    self.assertEqual(playingGridDict["gameStatus"], 'underway')
    self.assertEqual(gridListDict["rowCount"], 4)
    count = 0
    correct = [0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(correct)):
        if gridList[i] != correct[i]:
            count += 1
    self.assertEqual(count, 1)


def test_200_090_swipeRight(self):
    msg = '{"op":"swipe","direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": [3, 3, 3, 3, 1, 1, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0]}}'
    playingGridDict = json.loads(IndigoGirls.dispatch(msg))
    gridScore = playingGridDict['score']
    gridListDict = playingGridDict['board']
    gridList = gridListDict["grid"]
    self.assertEqual(gridScore, 36)
    self.assertEqual(gridListDict["columnCount"], 4)
    self.assertEqual(gridListDict["rowCount"], 4)
    self.assertEqual(playingGridDict["gameStatus"], 'underway')
    self.assertEqual(gridListDict["rowCount"], 4)
    count = 0
    correct = [0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 1, 0, 0, 0, 0]
    for i in range(len(correct)):
        if gridList[i] != correct[i]:
            count += 1
    self.assertEqual(count, 1)