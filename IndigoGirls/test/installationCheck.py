import IndigoGirls.dispatch as dispatch

validJson = '{"op": "initializeGame"}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "rowCount": 2, "columnCount": 2}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "rowCount": 1, "columnCount": 1}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "rowCount": 101, "columnCount": 101}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "rowCount": 4}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "rowCount": 1}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "rowCount": "8"}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "rowCount": "mason"}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "columnCount": 1}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "columnCount": "2"}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "columnCount": 101}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

validJson = '{"op": "initializeGame", "columnCount": "glover"}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

errorJson = '{}'
errorResult = dispatch.dispatch(errorJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n\n").format(errorJson, errorResult))

errorJson = 10
errorResult = dispatch.dispatch(errorJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n\n").format(errorJson, errorResult))

errorJson = '{"op": "unknown"}'
errorResult = dispatch.dispatch(errorJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n\n").format(errorJson, errorResult))

