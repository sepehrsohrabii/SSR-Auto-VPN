import requests
from SECRETS import HETZNER_API_KEY
import paramiko


def server_creator(server_name):
    # Define the API endpoint for retrieving locations and server types
    url_locations = "https://api.hetzner.cloud/v1/locations"
    url_server_types = "https://api.hetzner.cloud/v1/server_types?type=basic"

    # Define the API token to authenticate the request
    headers = {
        "Authorization": f"Bearer {HETZNER_API_KEY}",
        "Content-Type": "application/json",
    }

    # Retrieve the available locations from the API
    response = requests.get(url_locations, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        locations = response.json()["locations"]
    else:
        print("Failed to retrieve locations:")
        print(response.json())
        exit()

    # Ask the user to choose a location
    print("Available locations:")
    for i, location in enumerate(locations):
        print(f"{i + 1}: {location['name']} ({location['description']})")

    location_choice = input("Choose a location (1-{}): ".format(len(locations)))

    # Retrieve the available server types from the API for the chosen location
    response = requests.get(url_server_types + "&location=" + locations[int(location_choice) - 1]["name"],
                            headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        server_types = response.json()["server_types"]
    else:
        print("Failed to retrieve server types:")
        print(response.json())
        exit()

    # Select the cheapest server type
    print(server_types)
    cheapest_server_type = min(server_types, key=lambda x: x["prices"][0]["price_hourly"]["net"])
    server_type_choice = cheapest_server_type["name"]

    # Define the API endpoint for creating a server
    url_servers = "https://api.hetzner.cloud/v1/servers"
    # Define the payload for the server creation request

    data = {
        "name": f"{server_name}",
        "server_type": server_type_choice,
        "location": locations[int(location_choice) - 1]["name"],
        "image": "ubuntu-20.04",
        "start_after_create": True,
        "ssh_keys": ["noname"],
    }

    # Send the server creation request
    response = requests.post(url_servers, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code != 201:
        print(f"Error creating server: {response.text}")
        exit(1)

    print("Server created successfully:")
    server = response.json()['server']
    print(server)
    # Replace "YOUR_SERVER_ID" with the actual ID of your server
    server_id = server["id"]
    server_status = None
    while server_status != "running":
        response = requests.get(
            f"https://api.hetzner.cloud/v1/servers/{server_id}", headers=headers
        )
        server_status = response.json()["server"]["status"]
    '''
    # Retrieve the root password
    response = requests.post(
        f"https://api.hetzner.cloud/v1/servers/{server_id}/actions/reset_password",
        headers=headers,
    )

    if 'error' in response.json():
        print(f"Error resetting password: {response.text}")
        exit(1)

    root_password = response.json()["root_password"]

    print(f"Root password: {root_password}")
    '''
    # root_password = input('Please enter the root password that you recieved from email recently: ')
    login_info = {
            "server_id": server["id"],
            "server_name": server["name"],
            "server_ip": server["public_net"]["ipv4"]["ip"],
            # "root_password": root_password,
        }
    print("Server Created. Login information:")
    print(login_info)
    return login_info
