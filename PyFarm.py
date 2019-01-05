import gspread
import time
import PyFarmChild
from oauth2client.service_account import ServiceAccountCredentials

arg = []
outputs = []
idnum = 0
sheet = None
client = None
rowCount = None

def runScript(path, args):
    # Called by user; starts execution of the script 
    file_content = readFile(path)
    makeConnection()
    pushScript(file_content)
    pushArgs(args)
    #processOutput()        

    

def makeConnection():
    # Make the connection to the Google Spreadsheet
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    global client
    client = gspread.authorize(creds)  
   
def input(num):
    return arg[num]


def setInput(listArgs):
    global arg
    arg = listArgs

def output(val):
    outputs.append(val)

def readFile(path):
    # read file and store into a string
    py_file = open(path)
    scanned_text =  py_file.read()
    py_file.close()
    return scanned_text

def getWorkSheetOne():
    # Get the worksheet containing progress, args, and output
    global sheet
    sheet = client.open('pyfarm-hh').get_worksheet(0)
    return sheet

def getWorkSheetTwo():
    # Get the worksheet containing script, and machine ids
    global sheet
    sheet = client.open('pyfarm-hh').get_worksheet(1)
    return sheet

def pushScript(file_content):
    global sheet
    sheet = getWorkSheetTwo()
    sheet.update_cell(1, 1, file_content)

def pushArgs(args):
    global sheet
    sheet = getWorkSheetOne()
    i = 1
    for argument in args:
        j = 2
        for val in argument:
            sheet.update_cell(i, 1, "0")
            sheet.update_cell(i, j, val)
            j+=1
        sheet.update_cell(i, j, "N/A")    
        i+=1
    global rowCount    
    rowCount = i

def processOutput():
    # wait for response
    print("Waiting for output...")

    while outputs.__len__() != rowCount:
        time.sleep(5)

    print("Processing output...")
    for out in outputs:
        print(out)    




