import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


def write_in_sheet(self, csv_file = "in.csv"):
    print("Attempting writing to google sheets...")
    df = pd.read_csv(csv_file)

    def convert_to_int(x):
        if x == pd.NA:
            return 0
        return int(float(x))

    df = df.fillna("")
    # df['Numeric_vol'] = df['Numeric_col'].apply(convert_to_int)

    data = df.values.tolist()

    # * Sheet linkers and work

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(f"service_account.json", scope)
    
    print("Authorizing Credentials...")
    try:
        client = gspread.authorize(creds)
        print("Credentials Authorized")
    except:
        print("Some error with Authorization.. exiting")
        return 0


    sheet = client.open_by_url("sheet_url").worksheet("Sheet_Name")
    print("Opened the sheet, now writing.")

    sheet.append_rows(data)
    
    print("Done Writing.")