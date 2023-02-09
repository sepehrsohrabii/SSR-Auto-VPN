# Full Automate VPN

This repository aims to simplify the process of installing ShadowsockR for individuals or organizations with multiple users. The solution is specifically designed to work with Hetzner cloud virtual private servers (VPSs) and automates the entire process from start to finish. The system retrieves user names and email addresses from a pre-prepared Google Sheet, creates a Hetzner Cloud VPS in the location of your choice, connects to the server via SSH, installs ShadowsockR, and creates the users specified in the Google Sheet. Finally, the system sends each user their credentials via email through Gmail.

-----
## Requirements
1. Google Account
2. Hetzner Verified Account

## Prerequisites

1. Build a Google Sheet of your users in the following format:
   https://docs.google.com/spreadsheets/d/1yKTZpSU0ds_N7HdYz8X0kkj4W4LFEWa9s3GqGxExvXw/edit?usp=sharing

   (Make sure the sheet is accessible to all with the link.)

2. Create an SSH key from this website and download the key files (file.key.pub and file.key).

3. Go to Hetzner panel, add the SSH key, and make it the default.

4. Create a new Hetzner API token.

5. Get the Google credentials by following this link:
   https://medium.com/@a.marenkov/how-to-get-credentials-for-google-sheets-456b7e88c430

6. Download the Google credentials as a JSON file and name it `client_secret.json`.

7. Configure your Google account and create an APP key.

8. Create a `SECRET.py` file and paste the following code, replacing the parameters with your own:

```python
EMAIL_SENDER = "your gmail address"
EMAIL_PASSWORD = "your app key password"
HETZNER_API_KEY = "hetzner API key"
HETZNER_SSH_KEY_NAME = "Hetzner SSH key name"
SHADOWSOCKSR_PASSWORD = "desired password"
MY_GOOGLE_SHEET_URL = "google sheet share link"
SSH_PRIVATE_KEY_PASS = "SSH private key password"
```
-----
## Running the Project

1. Create a Python virtual environment by running the following command in the project directory:
```bash
  python -m venv .venv
```

2. Activate the environment with the following command:
```bash
  source .venv/bin/activate
```
3. Install the packages from `requirements.txt`:
```bash
  pip install -r requirements. txt
```
4. Run the project with the following command:
```bash
  python run.py
```
* Input the IP address of either the tunnel server or the main server, as needed. (The script will want it in the running process.)

-----
## Create a Tunnel Server if needed
Just replate `TUNNEl_SERVER_IP` and `MAIN_SERVER_IP` with Your servers. and then run it in your tunnel server.
```bash
sysctl net.ipv4.ip_forward=1
iptables -t nat -A PREROUTING -p tcp --dport 22 -j DNAT --to-destination TUNNEl_SERVER_IP
iptables -t nat -A PREROUTING -j DNAT --to-destination MAIN_SERVER_IP
iptables -t nat -A POSTROUTING -j MASQUERADE
```