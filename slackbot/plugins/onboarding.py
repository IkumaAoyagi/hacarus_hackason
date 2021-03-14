# coding: utf-8

import pickle
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# projectsを読み込み
pkl_file = 'projects.pkl'    #your saved pkl file at init_projects.py
with open(pkl_file, 'rb') as f:
    projects = pickle.load(f)

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
@respond_to(r'^upload ')
def mention_func(message):
    text = message.body['text']
    temp, pro_name, pro_url = text.split(None, 2)
    projects[pro_name] = pro_url
    message.reply(pro_name + ' をリストに追加しました。') 
    # pklファイルに追加
    with open(pkl_file,"wb") as f:
        pickle.dump(projects, f)
    
# projectの一覧を表示
@respond_to(r'list')
def mention_func(message):
    message.reply('Here is the project list : ' )
    for pro_name in projects.keys():
        message.reply(pro_name)
