import gspread
from oauth2client.service_account import ServiceAccountCredentials
from SECRETS import MY_GOOGLE_SHEET_URL


def get_users():
    sheet_link = MY_GOOGLE_SHEET_URL
    # setup credentials
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

    # authorize and open the sheet
    gc = gspread.authorize(creds)
    sheet = gc.open_by_url(sheet_link).sheet1

    # get all rows
    rows = sheet.get_all_values()

    # skip the first row as it contains headers
    rows = rows[1:]

    # extract the names and email addresses and save them in a list
    accounts = []
    for row in rows:
        name = row[1]
        email = row[2]
        if name != '' and email != '':
            accounts.append({'name': name, 'email': email})

    # print the list of accounts
    print(accounts)
    check_accounts = input("If the accounts list is ok, press 1 and if it is not, press 0 and then press Enter: ")
    if check_accounts != "1":
        exit()
    print("Users have gotten from the google sheet successfully.")
    return accounts
