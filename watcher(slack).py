from riotwatcher import LolWatcher
from datetime import datetime, timedelta
import time
import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

myToken = "" # secret key of slack bot


lol_watcher = LolWatcher('') # secret key of Riot API
my_region = 'kr'
me = lol_watcher.summoner.by_name(my_region, 'dk showmaker')


while 1:
    print(datetime.now(), "확인 중...")

    try:
        spectator = lol_watcher.spectator.by_summoner(my_region, me['id'])

        start_time = datetime.fromtimestamp(spectator['gameStartTime'] / 1000) # Return value's unit is millisecond; Dividing by 1000 is essential
        
        if datetime.now() - start_time < timedelta(minutes=5):
            print('')
            print(start_time)
            post_message(myToken,"#qwer","삐용삐용삐용삐용삐용삐용삐용삐용삐용삐용!")
    except: 
        pass
    time.sleep(3)
