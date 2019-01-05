import gspread
from oauth2client.service_account import ServiceAccountCredentials

arg = []
outputs = []
idnum = 0
sheet = None

def runScript(path, args):
    # make connection
    py_file = open(path)
    file_content =  py_file.read()
    py_file.close()

    new_row = [file_content]
    sheet.append_row(new_row)

    # push script
    # push args
    # wait for response
    print("run")

def makeConnection():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    global sheet
    sheet = client.open('pyfarm-hh').get_worksheet(1)
    print(sheet.cell(1,1).value)
    



def input(num):
    return arg[num]


def setInput(listArgs):
    arg = listArgs

def output(val):
    outputs.append(val)


