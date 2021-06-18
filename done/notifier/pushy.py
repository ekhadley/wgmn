import requests, time, websocket
from datetime import datetime
from blinkstick import blinkstick

ws = websocket.WebSocket()
ws.connect("wss://stream.pushbullet.com/websocket/o.GfFQafU2ftZ3FtYmi8QKeDPlmKO3vhnS")

def getPart(msg, mode):
    msg = msg[1].decode("utf-8") 

    start = 0 
    end = 0 
    final = ''
    try:
        if mode == 'body':
            for i in range(0, len(msg)-5):
                cut = [msg[i], msg[i + 1], msg[i + 2], msg[i + 3], msg[i + 4]]
                if cut == ['d', 'y', '"', ':', '"']:
                    start = i + 5
                    for j in range(start, len(msg)-1):
                        if [msg[j], msg[j + 1]] == ['"', ","]:
                            end = j
            for i in range(start, end):
                final += msg[i]
            if 'Sent from your Twilio trial account - ' in final:
                tmp = final
                final = ''
                for i in range(38, len(tmp)):
                    final += tmp[i]

        if mode == 'sender':
            for i in range(0, len(msg)-5):
                cut = [msg[i], msg[i + 1], msg[i + 2], msg[i + 3], msg[i + 4]]
                if cut == ['l', 'e', '"', ':', '"']:
                    start = i + 5
                    for j in range(start, len(msg)-1):
                        if [msg[j], msg[j + 1]] == ['"', ","]:
                            end = j
                            break
            for i in range(start, end):
                final += msg[i]

        return(final)
    
    except IndexError:
        print('unknown notification type') 

def giveType(raw):
    msg = str(raw[1].decode("utf-8"))
    if 'ions":[{"th' in msg:
        return('sms')
    if 'client_version' in msg:
        return('email')
    if 'ions":[]}' in msg:
        return('general push')
    if 'ype": "no' in msg:
        return('no noti')
    else:
        return('unknown type')

s = time.time()
while 1:
    try:  
        check = ws.recv_data()
        checkType = giveType(check)

        if checkType != 'no noti':
            now = datetime.now()
            time = now.strftime("%H:%M:%S")

            if checkType == 'sms':
                print('(' + time + ') ' + getPart(check, 'sender') + ': ' + getPart(check, 'body'))
            if checkType == 'email': 
                print('(' + time + ') ' + 'YOU HAVE MAIL!')
            if checkType == 'general push':
                print('general push')

    except TimeoutError:
        now = datetime.now()
        print('DISCONNECTED AT' + now.strftime("%H:%M:%S"))

        ws = websocket.WebSocket() 
        ws.connect("wss://stream.pushbullet.com/websocket/o.GfFQafU2ftZ3FtYmi8QKeDPlmKO3vhnS")
















































