import gspread
from oauth2client.service_account import ServiceAccountCredentials

arg = []
outputs = []
idnum = 0
sheet = None
client = None

def runScript(path, args):
    
    # read file and store into a string
    py_file = open(path)
    file_content =  py_file.read()
    py_file.close()

    makeConnection()

    global sheet
    sheet = client.open('pyfarm-hh').get_worksheet(1)
    
    # push script
    sheet.update_cell(1, 1, file_content)

    # push args
    sheet = client.open('pyfarm-hh').get_worksheet(0)
    progress = 0
    output = None
   # for argument in args:
   #     sheet.update_cell(sheet.row_count, 1, "0")
   #     for arg_index in range(argument.__len__()):
   #         sheet.update_cell(sheet.row_count, argument.col + 1, argument[arg_index])

    i = 1
    for argument in args:
        j = 2
        for val in argument:
            sheet.update_cell(i, 1, "-1")
            sheet.update_cell(i, j, val)
            j+=1
        sheet.update_cell(i, j, "N/A")    
        i+=1
        
            

    # wait for response

    print("Waiting for output...")

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


