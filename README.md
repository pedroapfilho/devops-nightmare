# DevOps Nightmare

Call your DevOps engineer whenever the server is down

You'll need a Twilio account and these keys on your environment:

```
ACCOUNT_SID='###'
AUTH_TOKEN='###'

FROM_NUMBER='###'
DEVOPS_NUMBER='###'

HEALTH_CHECK='###'

BOSS_VOICE_URL = '###
```

Then you:

1. Run `virtualenv venv` (creates virtual environment in current direction called 'env')
2. Run `source ./venv/bin/activate` (activates virtual environment)
3. Run `pip install -r requirements.txt`. If you have problems with this step (TLS/SSL error), then run `~ brew update && brew upgrade` followed by `python3 -m pip install --upgrade pip`, then retry the requirements.txt install

To run the script, simply run:

```
python3 call_devops.py
```

It'll ping the health_check endpoint each 5 seconds, if it fails 3 times, then it calls your DevOps engineer with the recording of your boss.
