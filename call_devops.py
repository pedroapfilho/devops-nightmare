from twilio.rest import Client
from requests import get
from dotenv import load_dotenv
from time import sleep
import os

load_dotenv()

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

FROM_NUMBER = os.getenv('FROM_NUMBER')
DEVOPS_NUMBER = os.getenv('DEVOPS_NUMBER')

HEALTH_CHECK = os.getenv('HEALTH_CHECK')

BOSS_VOICE_URL = os.getenv('BOSS_VOICE_URL')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

FAILED_REQUESTS = 0

while (FAILED_REQUESTS < 3):
    r = get(HEALTH_CHECK)
    status = r.status_code
    if(status != 200):
        print("FUCK")
        FAILED_REQUESTS += 1
    else:
        print("OK")
        failed_requests = 0
    sleep(5)

call = client.calls.create(
    url=BOSS_VOICE_URL,
    to=DEVOPS_NUMBER,
    from_=FROM_NUMBER
)
