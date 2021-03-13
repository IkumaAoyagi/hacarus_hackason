import slack
import os
import pickle

OAUTH_TOKEN = "xoxb-1852333648325-1868123261569-mBamhbOAGNkGkY7QRYGsJcyh"
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
                text="いつもよう仕事してはりますなぁ")

    print(res['ok'])

