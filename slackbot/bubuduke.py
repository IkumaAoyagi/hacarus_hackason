import slack
import os
import pickle

OAUTH_TOKEN = "your access token"
client = slack.WebClient(token=OAUTH_TOKEN)

def load_workers():
    if not os.path.exists('data/workers.pickle'):
        print('create workers')
        return {}
    else:
        print('load workers')
        with open('data/workers.pickle', 'rb') as f:
            workers = pickle.load(f)
        return workers

workers = load_workers()

for user in workers.keys():
    res = client.conversations_open(users=[user])
    res = client.chat_postMessage(
                channel=user,
                text="ぶぶ漬けでもどうどす？")

    print(res['ok'])

