from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import configparser
import os
import sys
import csv
import traceback
import time
import random

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

print (re+"╔╦╗┌─┐┬  ┌─┐╔═╗  ╔═╗┌┬┐┌┬┐┌─┐┬─┐")
print (gr+" ║ ├┤ │  ├┤ ║ ╦  ╠═╣ ││ ││├┤ ├┬┘")
print (re+" ╩ └─┘┴─┘└─┘╚═╝  ╩ ╩─┴┘─┴┘└─┘┴└─")

print (cy+"version : 1.01")
print (cy+"Make sure you Subscribed Termux Professor On Youtube")
print (cy+"www.youtube.com/c/TermuxProfessorYT")

print (re+"NOTE :")
print ("1. Telegram only allow to add 200 members in group by one user.")
print ("2. You can Use multiple Telegram accounts for add more members.")
print ("3. Add only 50 members in group each time otherwise you will get flood error.")
print ("4. Then wait for 15-30 miniute then add members again.")
print ("5. Make sure you enable Add User Permission in your group")

cpass = [[],[],[],[],[],[],[],[],[],[]]
client = [[],[],[],[],[],[],[],[],[],[]]

for x in range(0, 10):
    a = "config"
    b = str(x)+".data"
    c = a+b
    cpass[x] = configparser.RawConfigParser()
    cpass[x].read(c)

    try:
        api_id = cpass[x]['cred']['id']
        api_hash = cpass[x]['cred']['hash']
        phone = cpass[x]['cred']['phone']
        client[x] = TelegramClient(phone, api_id, api_hash)
    except KeyError:
        os.system('clear')
        print(re+"[!] run python setup.py first !!\n")
        sys.exit(1)

    client[x].connect()
    if not client[x].is_user_authorized():
        client[x].send_code_request(phone)
        os.system('clear')
        client[x].sign_in(phone, input(gr+'[+] Enter the code: '+re))

users = []
with open(r"members.csv", encoding='UTF-8') as f:  #Enter your file name
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = [[],[],[],[],[],[],[],[],[],[]]
last_date = None
chunk_size = 200
groups = [[],[],[],[],[],[],[],[],[],[]]
        
for x in range(0, 10):
    result = client[x](GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats[x].extend(result.chats)

    for chat in chats[x]:
        try:
            if chat.megagroup == True:
                groups[x].append(chat)
        except:
            continue

print(gr+'Choose a group to add members:'+cy)
i = 0
for group in groups[0]:
    print(str(i) + '- ' + group.title)
    i += 1

g_index = input(gr+"Enter a Number: "+re)
target_group = groups[0][int(g_index)]
target_group_title = target_group.title

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

mode = int(input(gr+"Enter 1 to add by username or 2 to add by ID: "+cy))

n = 0
m = 0

for user in users:
    n += 1
    cl = client[m]
    index = 0
    for group in groups[m]:
        if group.title == target_group_title:
            g_index = index
            break
        else:
            g_index = 0
        index += 1
    target_group = groups[m][int(g_index)]
    target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)
    m += 1
    if m == 10:
        m = 0
    if n % 80 == 0:
        time.sleep(60)
    try:
        print("Adding {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = cl.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Invalid Mode Selected. Please Try Again.")
        cl(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("Waiting for 10 Seconds...")
        time.sleep(10)
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        print("Waiting for 10 Seconds...")
        time.sleep(10)
    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping.")
        print("Waiting for 10 Seconds...")
        time.sleep(10)
    except:
        traceback.print_exc()
        print("Unexpected Error")
        print("Waiting for 10 Seconds...")
        time.sleep(10)
        continue
