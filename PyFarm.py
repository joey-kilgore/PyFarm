import gspread
from oauth2client.service_account import ServiceAccountCredentials

arg = []
outputs = []
sheet1 = None
sheet2 = None

def runScript(path, args):
    # make connection
    py_file = open(path)
    file_content =  py_file.read()
    py_file.close()

    new_row = [file_content]
    sheet1.append_row(new_row)

    # push script
    # push args
    # wait for response
    print("run")

def makeConnection():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    global sheet1
    global sheet2
    sheet1 = client.open('pyfarm-hh').get_worksheet(0)
    sheet2 = client.open('pyfarm-hh').get_worksheet(1)
    



def input(num):
    print(num)
    return arg[num]


def setInput(listArgs):
    global arg
    arg = listArgs

def output(val):
    global outputs
    outputs.append(val)
    print(val)

def sendOutput(argIndex, numArgs):
    makeConnection()
    for out in outputs:
        sheet1.update_cell(argIndex,numArgs, out)
        numArgs += 1

def clearOutput():
    global outputs
    outputs.clear()    



