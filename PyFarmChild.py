import pymysql
import PyFarm

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

def getArgs():
    # query for args
    # if there are args
    #   set args
    #   return true
    # else (there are no args to test)
    #   return false
    print("getArgs")


def callScript():
    # call the script
    # it should save all output to the module
    print("runScript")


def sendOutput():
    # get the outputs from the module
    # send the output to the server
    print("sendOutput")


    