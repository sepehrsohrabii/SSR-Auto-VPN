from configure_server import configure_server
from get_users_from_googlesheets import get_users


# list divider
def divide_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


# 1.Get Users from Google Sheets
users_list = get_users()

# 2.How many users do you want to be in one server
users_per_server = int(input('How many users do you want to be in one server? (Enter 0 for unlimited) '))
divided_users_list = divide_list(users_list, users_per_server)

# 3.Configure servers
if users_per_server == 0:
    configure_server()
elif users_per_server > 0:
    i = 1
    for list in divided_users_list:
        server_name = f'server{i}'
        check = int(input(f'If you want to skip {server_name}\'s configuration press 0 if not press 1: '))
        if check == 1:
            configure_server(list, server_name)
        i += 1
