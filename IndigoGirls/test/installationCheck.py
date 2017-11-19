from IndigoGirls.dispatch import dispatch

#Assignment 6 clarifications

validJson = '{"op":"swipe","direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": ' \
            '[1, 2, 0, 0, 0, ' \
              '0, 0, 0, 0, 0, ' \
              '0, 0, 0, 0, 0,]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"swipe","direction": "right", "board": {"columnCount": 5, "rowCount": 4, "grid": ' \
             '[1, 2, 0, 0, 0, ' \
              '0, 0, 0, 0, 0, ' \
              '0, 0, 0, 0, 0, ' \
              '0, 0, 0, 0, 0]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"swipe","direction": "right", "board": {"columnCount": 10, "rowCount": 10, "grid": [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1,1, 1, 0, 0, 1, 0, 0, 0, 0, 1,1, 1, 0, 0, 1, 0, 0, 0, 0, 1,1, 1, 0, 0, 1, 0, 0, 0, 0, 1,1, 1, 0, 0, 1, 0, 0, 0, 0, 1,1, 1, 0, 0, 1, 0, 0, 0, 0, 1,1, 1, 0, 0, 1, 0, 0, 0, 0, 1,1, 1, 0, 0, 1, 0, 0, 0, 0, 1,1, 1, 0, 0, 1, 0, 0, 0, 0, 1]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"swipe","direction": "right", "board": {"columnCount": 4, "rowCount": 5, "grid": [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))


#Assignment 7 status Happy path
validJson = '{"op":"status", "tile": 2048,  "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"status",  "board": {"columnCount": 4, "rowCount": 4, "grid": [1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"status", "tile": 16,  "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

#Assignment 7 status Sad Path
validJson = '{"op":"status", "tile": 0,  "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

#Assignment 7 recommend Happy Path
validJson = '{"op":"recommend", "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"recommend", "moves": 0, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"recommend", "moves": 1, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"recommend", "moves":1, "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,0,0,2,2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

#Assignment 7 recommend Sad Path
validJson = '{"op":"status", "tile": 2048,  "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"status","board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,3]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"status", "tile": 16,  "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,4,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"status", "tile": 32,  "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,4,0,0,1,2,2,0,5,1,0,2,2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"status", "tile": -1,  "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"status", "tile": 0,  "board": {"columnCount": 4, "rowCount": 4, "grid": [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"status","board": {"columnCount": 4, "rowCount": 4, "grid": [1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))