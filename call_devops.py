from twilio.rest import Client
from requests import get
from dotenv import load_dotenv
from time import sleep
import os

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

from_number = os.getenv('FROM_NUMBER')
devops_number = os.getenv('DEVOPS_NUMBER')

health_check = os.getenv('HEALTH_CHECK')

boss_voice_url = os.getenv('BOSS_VOICE_URL')

client = Client(account_sid, auth_token)

failed_requests = 0

while (failed_requests <= 3):
    r = get(health_check)
    status = r.json()
    if(status == "OK"):
        print("FUCK")
        failed_requests += 1
    else:
        print("OK")
        failed_requests = 0
    sleep(5)

call = client.calls.create(
    url=boss_voice_url,
    to=devops_number,
    from_=from_number
)
