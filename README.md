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

It'll ping the health_check endpoint each 5 seconds, if it fails 3 times, then it calls your DevOps engineer with the recording of your boss.
