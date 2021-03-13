# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない
#@respond_to('メンション')
#def mention_func(message):
#    message.reply('私にメンションと言ってどうするのだ') # メンション

import slack
import os
import pickle
from datetime import datetime, timedelta

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

def save_workers(workers):
    with open('data/workers.pickle', 'wb') as f:
        pickle.dump(workers, f)

def load_urls():
    if not os.path.exists('data/urls.pickle'):
        print('create urls')
        return {}
    else:
        print('load urls')
        with open('data/urls.pickle', 'rb') as f:
            urls = pickle.load(f)
        return urls

def save_urls(urls):
    with open('data/urls.pickle', 'wb') as f:
        pickle.dump(urls, f)


@respond_to(r'^(?=.*勤務)(?=.*開始).*$')
def start_func(message):
    workers = load_workers()

    user = message.body['user']

    if user in workers:
        message.react('thumbsup')

    else:
        workers[user] = [datetime.now()]
        save_workers(workers)

        real_name = message.user['real_name'] # 表示名を取得する
        #display_name = message.user['profile']['display_name']
        print(f"{real_name} starts at: {workers[user][0].strftime('%Y/%m/%d %H:%M:%S')}")

        message.reply('きびきび働けよ') 
        #print(message.body)
        #print(message.body['user'])


@respond_to(r'^(?=.*退勤).*$')
def end_func(message):
    workers = load_workers()
    urls = load_urls()

    user = message.body['user']

    timestamp = None

    if user in workers:
        workers[user].append(datetime.now())

        timestamp = workers[user]
        del workers[user]
        save_workers(workers)

    if user not in urls:
        message.reply('お疲れさまです。勤怠の入力をお忘れなく！')
    else:
        message.reply(f'お疲れさまです。勤怠の入力をお忘れなく！')

        start_time = f"開始: {timestamp[0].strftime('%Y/%m/%d %H:%M:%S')}"
        end_time = f"終了: {timestamp[1].strftime('%Y/%m/%d %H:%M:%S')}"

        user = message.body['user']
        res = client.conversations_open(users=[user])
        res = client.chat_postMessage(
                channel=user,
                text="勤怠の入力はこちらからどうぞ\n" + start_time + "\n" + end_time)
        res = client.chat_postMessage(
                channel=user,
                text=f"{urls[user]}")

        print(res['ok'])

@respond_to(r'^set')
def set_func(message):
    #print(message.body['text'])

    user = message.body['user']

    line = message.body['text'].split()
    if line[1] != 'kintai':
        print('unrecognized command')
    else:
        urls = load_urls()

        url = line[2]
        urls[user] = url

        save_urls(urls)


#@listen_to('リッスン')
#def listen_func(message):
#    message.send('誰かがリッスンと投稿したようだ')      # ただの投稿
#    message.reply('君だね？')                           # メンション

#@respond_to('かっこいい')
#def cool_func(message):
#    message.reply('ありがとう。スタンプ押しとくね')     # メンション
#    message.react('+1')     # リアクション
