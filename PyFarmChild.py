import PyFarm

def getIdNum():
    id = 1
    cell = PyFarm.sheet.cell(id,1)
    while cell.value != '':
        id += 1
        cell =PyFarm.sheet.cell(id,1)
    PyFarm.sheet.update_cell(id,1,'Machine Connected')
    return id   

def waitForConnection():
    # wait for connection
    # when there is a connection begin runScript
    print("get connection")

def runScript():
    getScript()
    while getArgs():
        callScript()
        sendOutput()

def getScript():
    # query for script
    print("getScript")


testArgs = [[1],[2],[3]]
argsIndex = 0

def getArgs():
    # query for args
    # if there are args
    #   set args
    #   return true
    # else (there are no args to test)
    #   return false
    global argsIndex
    print("get args")
    if(argsIndex < len(testArgs)):
        PyFarm.setInput(testArgs[argsIndex])
        argsIndex += 1
        return True
    else:
        return False


def callScript():
    # call the script
    # it should save all output to the module
    print("runScript")
    PyFarm.output(PyFarm.input(0) *2)


def sendOutput():
    # get the outputs from the module
    # send the output to the server
    print("sendOutput")


PyFarm.makeConnection()
id = getIdNum()