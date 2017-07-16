from ast import literal_eval

from cfg.config import TOKEN, dumpName
import telepot
from telepot.loop import MessageLoop
import pickle

last_command = "Не получено никакой информации"
subscribers = set()


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    global subscribers
    #print(content_type, chat_type, chat_id)
    if content_type != 'text':
        bot.sendMessage(chat_id, "Отправьте команду")
        return
    command = msg['text'].strip().lower()

    if command == '/start':
        bot.sendMessage(chat_id, "Welcome to build notification bot")

    elif command == '/last':
        bot.sendMessage(chat_id, last_command)

    elif command == '/subscribe':
        if chat_id in subscribers:
            bot.sendMessage(chat_id, "Вы уже подписаны на рассылку сообщений")
        else:
            subscribers.add(chat_id)
            bot.sendMessage(chat_id, "Вы были подписаны на рассылку сообщений")
            updateSubscribersDump()

    elif command == '/unsubscribe':
        if chat_id in subscribers:
            subscribers.remove(chat_id)
            bot.sendMessage(chat_id, "Вы были отписаны от рассылку сообщений")
            updateSubscribersDump()
        else:
            bot.sendMessage(chat_id, "Вы уже отписаны от рассылки сообщений")


bot = telepot.Bot(TOKEN)

def updateSubscribersDump(data=subscribers):
    print("Rewrite dump")
    subscribersList = open(dumpName, 'wb')
    pickle.dump(data, subscribersList)
    subscribersList.close()


# Метод, ретранслирующий полученное сообщение в telegram
def fire_event(message):
    #print(subscribers)
    global last_command
    last_command=message
    for subscriber in subscribers:
        bot.sendMessage(subscriber, message)


def initBot():
    print("Bot initializing")
    try:
        print("Try load subscribers list")
        subscribersList = open(dumpName, "rb")
        global subscribers
        subscribers = pickle.load(subscribersList)
        subscribersList.close()
    except:
        print("File is not exists, skipping")
    MessageLoop(bot, handle).run_as_thread()