from IndigoGirls.dispatch import dispatch

validJson = '{"op":"predict","direction": "left", "moves":1, "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"predict","direction": "right", "moves":1, "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"predict","direction": "up", "moves":1, "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"predict","direction": "down", "moves":1, "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"predict","direction": "left", "moves":2, "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"predict","direction": "up", "moves":1, "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op":"predict","direction": "down", "moves":1, "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2]}}'
validResult = dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))
