import datetime

from slackbot.bot import respond_to
import slackbot_settings
from slacker import Slacker

TOTAL_WORKING_DAYS = {}
LAST_WORKED_DAY = {}

REWARD = {1: "resources/IMG_1939.HEIC",}

@respond_to('作業開始します')
def return_login_bonus(message):
    print("message received.")
    print(message.body )
    real_name = message.user["real_name"]
    if TOTAL_WORKING_DAYS.get(real_name) is None:
        TOTAL_WORKING_DAYS[real_name] = 1
        LAST_WORKED_DAY[real_name] = datetime.datetime.today()
    message.reply(f'ログイン{TOTAL_WORKING_DAYS[real_name]}日目')

    if REWARD.get(TOTAL_WORKING_DAYS[real_name]) is not None:
        slacker = Slacker(slackbot_settings.API_TOKEN)
        channel = message.channel._client.channels[message.body['channel']]
        channel_name = channel['name']
        print(channel_name)
        slacker.files.upload(file_=REWARD[TOTAL_WORKING_DAYS[real_name]], channels=channel_name)
