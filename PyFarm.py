import gspread
from oauth2client.service_account import ServiceAccountCredentials

arg = []
outputs = []

def runScript(path, args):
    # make connection
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('pyfarm-hh').sheet1
    new_row = [path, 'foo']
    sheet.append_row(new_row)
    #sheet.update_cell(4, 1, path)

    # push script
    server_storage = path
    # push args
    # wait for response
    print("run")
    print(server_storage)


def input(num):
    return arg[num]


def setInput(listArgs):
    arg = listArgs

def output(val):
    outputs.append(val)


