# -*- coding: utf-8 -*-
#From By İxel

import telebot
from telebot import types
bot = telebot.TeleBot("1470628993:AAHOjzwU5D0vAzEMomYbCbHVr8LjjyfoseY")


feedbackstat = 0
replystat = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,
"""_Salam!_ [{}](tg://user?id={}), _Editizim FeedBack Botuna Xoşgeldin!
/mesaj <Mesaj> Yazarağ adminlərlə əlaqəyə keçə bilərsən!_
""".format(message.from_user.first_name, message.from_user.id), parse_mode='MarkDown')
@bot.message_handler(commands=['mesaj'])
def feedback(message):
    uname = message.from_user.first_name
    uid = message.from_user.id
    with open("admin.txt","r") as f:
       a = f.read()
    with open("users.txt","r") as user:
        b = user.read()
    if str(uid) in a:
        bot.reply_to(message, "_Özünə geri bildirim göndərə bilməzsən!_", parse_mode= 'MarkDown')
    else:
        text = message.text.replace("/mesaj", "")[1:]
        if str(uid) in b:
            pass
        else:
            if str(uid) in a:
                pass
            else:
                with open("users.txt","a") as users:
                    users.write("{}\n".format(uid))
        if text == "":
            bot.reply_to(message, """
_Xaiş edirem mesajı boş buraxmayın!

Misal: /mesaj adminlərlə əlaqəyə keçmək istəyirəm_""", parse_mode= 'MarkDown')

        else:
            global feedbackstat
            feedbackstat +=1
            bot.send_message(uid, "_Geri bildirim uğurla göndərildi!!_", parse_mode= 'MarkDown')
            with open("admin.txt","r") as msg:
                for ids in msg:
                    bot.send_message(ids, text="""
*Gönderen*: [{}](tg://user?id={})
*ID*: `{}`
*FeedBack*: _{}_
""".format(uname, uid, uid, text), parse_mode= 'MarkDown')

@bot.message_handler(commands=['send'])
def reply(message):
    if message.chat.id == -477158117:
        with open("admin.txt","r") as f:
            adm = f.read()
        if str(message.from_user.id) in adm:
            uid = message.text.split(" ")[1]
            with open("users.txt","r") as us:
                user = us.read()
            if str(uid) in user:
                utext = str(message.text.split(" ")[2:])
                utext = str(utext.replace("'", ""))
                utext = str(utext.replace(",",""))
                utext = utext.replace("[","")
                utext = utext.replace("]","")
                global replystat
                replystat += 1
                bot.reply_to(message, "_Cavap uğurlu şəkildə_ [EDİTİZM](tg://user?id={}) _şəxsinə göndərildi!!_".format(uid), parse_mode= 'MarkDown')
                bot.send_message(uid, "*Admin Cavabı*\n_{}_".format(utext), parse_mode= 'MarkDown')
            else:
                bot.reply_to(message, "_Belə bir isdifadəci veri tabanında tapılmadı!_", parse_mode='MarkDown')

        else:
            bot.reply_to(message, "_Səlahiyyətin yoxdur kimi görürəm!!_", parse_mode='MarkDown')
    else:
        pass
@bot.message_handler(commands=['users'])
def stat(message):
    uid = message.from_user.id
    with open("admin.txt","r") as adm:
        adm = adm.read()
    if str(uid) in adm:
        with open("users.txt","r") as user:
            data = user.readlines()
        data = len(data)
        bot.reply_to(message,"_Cəmi_ `{}` _isdifadəci mövcuddur_".format(data), parse_mode='MarkDown')
    else:
        bot.reply_to(message, "_Səlahiyyətin yoxdur kimi görürəm!_", parse_mode='MarkDown')


@bot.message_handler(commands=['stats'])
def stats(message):
    uid = message.from_user.id
    with open("admin.txt","r") as adm:
        adm = adm.read()
    if str(uid) in adm:
        global feedbackstat
        global replystat
        bot.reply_to(message,"_Toplam_ `{}` FeedBack\n_Toplam_ `{}` _Yanıt Mevcut_".format(feedbackstat,replystat), parse_mode='MarkDown')
    else:
        bot.reply_to(message, "_Səlahiyyətin yoxdur kimi görürəm!_", parse_mode='MarkDown')


print("BOT AKTİF!!!")

bot.polling(none_stop= True)
