
# Full Automate VPN

In this repo I tried to make ShadowsockR installation easier for those who have many users.

I built this project with Django in backend side and I used Django Rest Framework for it endpoint.

1. Build a Sheet of your users exactly like this:
https://docs.google.com/spreadsheets/d/1yKTZpSU0ds_N7HdYz8X0kkj4W4LFEWa9s3GqGxExvXw/edit?usp=sharing
and save the share link URL and I should mention that the sheet must be available for all with the link.

2. Create an SSH key from this website then download the files of keys so you should have an file.key.pub and file.key in the main directory of this project.

3. go forward with this link and create a credential file
https://medium.com/@a.marenkov/how-to-get-credentials-for-google-sheets-456b7e88c430

4. download it json file the name should be client_secret.json and it must be in the main folder.

5. Build a SECRET.py file and pase this code bellow and replace your parameters.
EMAIL_SENDER = "sepehr0sohrabi@gmail.com"
EMAIL_PASSWORD = "bqftieladkxyvogy"
HETZNER_API_KEY = "TKNBIpRqbUFkUIKtgT80BHN8Ae50XXWlKtHIwLSyZai0zK0m55PIb1Y4DI2Vlb4i"
HETZNER_SSH_KEY_NAME = "noname"
SHADOWSOCKSR_PASSWORD = "wE4#@1mM0ngTh3P@ssW0rd"
MY_GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/13xnkSSflSR1VF6qolJVBS3la3c8ZDnPI7cXCifs_7zU/edit?usp=sharing"
SSH_PRIVATE_KEY_PASS = "SepehrVPN#19971375"

6. now create a python virtual environment with these codes.
go to the project directory and run this code:
python -m venv .venv

7. activate the environment by this code:
source .venv/bin/activate

8. by this script you can run the project:
python run.py


-- if you have a tunnel server you must input the ip if not input the main server's ip