import gspread
from oauth2client.service_account import ServiceAccountCredentials

arg = []
outputs = []

def runScript(path, args):
    
    # read file and store into a string
    py_file = open(path)
    file_content =  py_file.read()
    py_file.close()

    # make connection
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('pyfarm-hh').sheet1

    # push script
    new_row = [file_content]
    sheet.append_row(new_row)

    # push args

    # wait for response

    print("run")


def input(num):
    return arg[num]


def setInput(listArgs):
    arg = listArgs

def output(val):
    outputs.append(val)


