# FINTOPIO BOT
# Author    : @fakinsit
# Date      : 30/08/24

import os
import time
import sys
import re
import json
import requests
from urllib.parse import unquote
from pyfiglet import Figlet
from colorama import Fore
from onlylog import Log


header = {
      "Accept-Language": "en-US,en;q=0.9",
      "Referer": "https://bot-coin.0x13.work/",
      "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128", "Microsoft Edge WebView2";v="128"',
      "Sec-Ch-Ua-Mobile": "?0",
      "Sec-Ch-Ua-Platform": "Windows",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    }

def banner():
    os.system("title STARLIGHT BOT" if os.name == "nt" else "clear")
    os.system("cls" if os.name == "nt" else "clear")
    custom_fig = Figlet(font='slant')
    print('')
    print(custom_fig.renderText(' STARLIGHT'));
    print(Fore.RED + '[#] [C] R E G E X    ' + Fore.GREEN + '[STARLIGHT BOT] $$ ' + Fore.RESET)
    print(Fore.GREEN +'[#] Welcome & Enjoy !', Fore.RESET)
    print(Fore.YELLOW +'[#] Having Troubles? PM Telegram [t.me/fakinsit] ', Fore.RESET)
    print('')

def runforeva(): 
    with open('quentod.txt', 'r') as file:
        queryh = file.read().splitlines()
    try:
            value = True
            while (value):
                for index, query_id in enumerate(queryh, start=1):
                    getname(query_id)
                    postrequest(query_id)
    except:
        Log.error('[MAIN] error, restarting')
        runforeva()

def getlogin(querybro):
    try:
        url = "https://bot.0x13.work/v1/profile"
        s = requests.Session()
        s.headers.update({"At":getid(querybro),"Tg":querybro})
        response = s.get(url, headers=header)
        jData=response.json()
        jsondata =  jData['data']
        jsonbalance =  jsondata['balance']
        jsonbal =  jsonbalance['$numberDecimal']
        Log.success('login success')
        Log.success('xp balance : ' + jsonbal)

    except:
        Log.error('[getlogin] error, check your qeury_id / user_id maybe expired')

def getname(querybro):
    try:
        found = re.search('user=([^&]*)', querybro).group(1)
        decodedUserPart = unquote(found)
        userObj = json.loads(decodedUserPart)
        Log.success('username : @' + userObj['username'])
    except:
        Log.error('[decodedUsername] error')

def getid(querybro):
    try:
        found = re.search('user=([^&]*)', querybro).group(1)
        decodedUserPart = unquote(found)
        userObj = json.loads(decodedUserPart)
        return str(userObj['id'])
    except:
        Log.error('[decodedUserid] error')

def playgame(tomket, tix):
    n = tix

    for i in range(0, n):
        try:
            url = "https://bot.0x13.work/v1/game/start"
            urlstop = "https://bot.0x13.work/v1/game/stop"
            redropindo = {"xp":2000,"height":660000,"somersault":60000,"time":"60000"}
            s = requests.Session()
            s.headers.update({"At":getid(tomket),"Tg":tomket})
            response = s.post(url, headers=header)
            sleep(5)
            if response.text != '{"status":"ok","data":{"status":true}}':
                Log.error('[startgame] failed, restarting')

            elif response.text == '{"message":"The game is already running","error":"Bad Request","statusCode":400}':
                res = s.post(urlstop, headers=header, json=redropindo)
                if res.text == '{"status":"ok","data":{"status":true}}':
                    Log.success('succes play game, reward : 2000 xp [MAX]')
            else:
                res = s.post(urlstop, headers=header, json=redropindo)
                if res.text == '{"status":"ok","data":{"status":true}}':
                    Log.success('succes play game, reward : 2000 xp [MAX]')
        except:
            Log.error('[playgame] failed, restarting')


def gettask(tomket):
    try:
        urltasks = "https://bot.0x13.work/v1/profile/tasks?page=1&limit=50"
        s = requests.Session()
        s.headers.update({"At":getid(tomket),"Tg":tomket})
        response = s.get(urltasks, headers=header)
        jData=response.json()
        jdat=jData['data']
        jDocs=jdat['docs']

        for item in jDocs: 
            if item['status'] == 'pending':
                list_id = []
                list_name = []
                list_id.append(item['_id'])
                list_name.append(item['title'])
                anjoy = list_id + list_name
                urlstart = 'https://bot.0x13.work/v1/profile/tasks/'+str(anjoy[0])
                s.post(urlstart, headers=header)
                Log.warn('task ' + anjoy[1] + ' started!')
            elif item['status'] == 'completed':
                list_id = []
                list_name = []
                list_bonus = []
                list_id.append(item['_id'])
                list_name.append(item['title'])
                list_reward = item['bonus']
                list_bonus.append(list_reward['$numberDecimal'])
                
                anjoy = list_id + list_name + list_bonus
                urlclaim = 'https://bot.0x13.work/v1/profile/tasks/'+str(anjoy[0])+'/claim'
                responseclaim = s.post(urlclaim, headers=header)
                if (responseclaim.text == '{"status":"ok","data":{"status":"ok"}}'):
                    Log.success('task ' + anjoy[1] + ' claimed ' + str(anjoy[2]) + ' points')
            

    except:
        Log.error('[getTask] failed, restarting')

def sleep(num):
    for i in range(num):
        print("wait {} seconds".format(num - i), end='\r')
        time.sleep(1)


def postrequest(bearer):
    urlticket = 'https://bot.0x13.work/v1/game/attempts-left'
    urlstartendfarm = 'https://bot.0x13.work/v1/profile/farm-coin'


    s = requests.Session()
    s.headers.update({"At":getid(bearer),"Tg":bearer})


    try:
        getlogin(bearer)
        
        r = s.get(urlticket, headers=header)
        jData=r.json()
        jsondata =  jData['data']
        jsoncanPlay =  jsondata['canPlay']
        jsonquantity =  jsondata['quantity']
        Log.warn('tickets : ' + str(jsonquantity))
        if jsoncanPlay == True:
            Log.warn('have a game tickets!')
            Log.warn('start playing..')
            playgame(bearer, jsonquantity)
        
        gettask(bearer)

    except:
        Log.error('[playgame] error restarting')
        time.sleep(5)
        runforeva()

    try:
        r2 = s.post(urlstartendfarm, headers=header)
        wkwk = r2.json()
        if wkwk == {'message': "Can't start farming", 'error': 'Bad Request', 'statusCode': 400}:
            Log.warn("can't claim farming yet!")
        else:
            Log.success('start / end farming success!')

    except:
        Log.error('[farming] error restarting')
        time.sleep(5)
        runforeva()
    print('===================[STARLIGHT]===================')
    sleep(30)


# NYALAIN SENDIRI ABANGKUHH
if __name__ == "__main__":
    try:
        banner()
        runforeva()
    except KeyboardInterrupt:
        sys.exit()


#{"message":"Can't start farming","error":"Bad Request","statusCode":400}
#{'status': 'ok', 'data': {'status': 'ok', 'exp': 28800000}}
