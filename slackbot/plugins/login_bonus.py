import datetime

from slackbot.bot import respond_to
import pandas as pd

LOGIN_RECORD = pd.DataFrame()
LOGIN_RECORD = LOGIN_RECORD.columns(['total_working_days', 'last_worked_day'])
LOGIN_RECORD.loc["osamu"] = {'total_working_days': 0, 'last_worked_day': 0}
print(LOGIN_RECORD)

@respond_to('作業開始します')
def return_login_bonus(message):
    print("message received.")
    print(message)
    real_name = message.user["real_name"]
    print(real_name)
    try:
        total_working_days = LOGIN_RECORD.loc['real_name', 'total_working_days']
        print(total_working_days)
    except KeyError:
        LOGIN_RECORD.loc['real_name'] = [0, datetime.datetime.now()]
    print(total_working_days)
    message.reply(f'ログイン1日目: {real_name}')