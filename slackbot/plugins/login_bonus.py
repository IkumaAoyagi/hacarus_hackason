import datetime

from slackbot.bot import respond_to
from slacker import Slacker

from slackbot_settings import API_TOKEN


total_worked_days_record = {}
last_worked_day_record = {}

REWARDS = {
    1: "resources/IMG_1939.HEIC",
    3: "resources/IMG_1928.HEIC",
    7: "resources/IMG_1934.HEIC",
    30: "resources/IMG_1937.HEIC"
    }

@respond_to('作業開始します')
def return_login_bonus(message):
    real_name = message.user["real_name"]

    # if the user logs in for the first time
    if total_worked_days_record.get(real_name) is None:
        total_worked_days_record[real_name] = 0
        last_worked_day_record[real_name] = 0

    # if the user has already logged in today
    if last_worked_day_record[real_name] == datetime.date.today():
        message.reply("ログインボーナスは取得済みです。")
        return

    # update the records
    total_worked_days_record[real_name] += 1
    total_worked_days = total_worked_days_record[real_name]
    last_worked_day_record[real_name] = datetime.date.today()

    reply = f"\n⭐️⭐️⭐️ログイン{total_worked_days}日目⭐️⭐️⭐️\n"

    # login bonus
    reward_file = REWARDS.get(total_worked_days)
    if reward_file is not None:
        reply += f"🎁{total_worked_days}日目のログインボーナスです🎁"
        message.reply(reply)

        # upload an image (login bonus)
        slacker = Slacker(API_TOKEN)
        channels = message.channel._client.channels[message.body['channel']]['name']
        slacker.files.upload(file_=reward_file, channels=channels)
    else:
        message.reply(reply)
