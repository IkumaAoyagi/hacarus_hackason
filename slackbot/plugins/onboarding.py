# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# projectを格納
projects = {'project_1': 'aaa', 'project_2': 'bbb', 'project_3': 'ccc'}

# projectのurlを確認
@respond_to(r'^join ')
def mention_func(message):
    text = message.body['text']
    temp, pro_name = text.split(None, 1)
    if pro_name in projects.keys():
        pro_url = projects[pro_name]
        message.reply('The project\'s url : ' + pro_url) 
    else:
        message.reply('We don\'t have the project : ' + pro_name + '\n')
        message.reply('Here is the project list : ' )
        for pro_name in projects.keys():
            message.reply(pro_name)

# projectのurlを更新
@respond_to(r'^update ')
def mention_func(message):
    text = message.body['text']
    temp, pro_name, pro_url = text.split(None, 2)
    projects[pro_name] = pro_url
    message.reply('Successfully saved : ' + pro_name + ', ' + 'url :' + pro_url) 
    
# projectの一覧を表示
@respond_to(r'list project')
def mention_func(message):
    message.reply('Here is the project list : ' )
    for pro_name in projects.keys():
        message.reply(pro_name)
