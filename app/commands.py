from app import bot, logger, db, ma
from app.models import users, coins
from app.serializer import UserSchema
from datetime import datetime


@bot.message_handler(commands=['start'])
def command_start(message):
    if message.chat.type == "private":
        user = users.query.filter_by(UTGId=message.from_user.id).first()
        if user == None:
            user = users(UTGId=message.from_user.id, ULastUseDatetime=datetime.now())
            db.session.add(user)
            db.session.commit()
            bot.send_message(message.from_user.id, f"哈囉! {message.from_user.first_name},\n"
                                                   f"歡迎來到虛擬貨幣提醒機器人！\n\n"
                                                   f"下面是本機器人的使用方法：\n"
                                                   f"(可以點擊下面按鈕與回覆關鍵字)\n\n"
                                                   f"/set - 設定通知秒數\n")
        else:
            bot.send_message(message.from_user.id, f"哈囉! {message.from_user.first_name},\n"
                                                   f"歡迎回到虛擬貨幣提醒機器人！\n\n143.24"
                                                   f"下面是本機器人的使用方法：\n"
                                                   f"(可以點擊下面按鈕與回覆關鍵字)\n\n"
                                                   f"/set - 設定通知秒數\n")


@bot.message_handler(commands=['set'])
def handle_text(message):
    cid = message.chat.id
    MsgTime = bot.send_message(cid, '設定你想設定提醒的時間:')
    bot.register_next_step_handler(MsgTime, step_Set_Price)


def step_Set_Price(message):
    cid = message.chat.id
    userPrice = int(message.text)
    if not int(userPrice):
        bot.send_message(cid, "你輸入的好像不是數字唷！\n"
                              "請再輸入一次。\n"
                              "\set")
    else:
        user = users.query.filter_by(UTGId=cid).first()
        user.UNotificationInterval = userPrice
        db.session.commit()
        bot.send_message(cid, f"Hi! 您提醒時間已經變更為 {userPrice} 秒囉！")

# @bot.message_handler(commands=['coins'])
# def handle_text(message):
#     cid = message.chat.id
#     MsgTime = bot.send_message(cid, '設定你想關注的貨幣:')
#     bot.register_next_step_handler(MsgTime, step_Set_Coins)
#
# def step_Set_Coins(message):
#
