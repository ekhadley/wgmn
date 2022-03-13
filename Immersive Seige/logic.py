import time, serial, r6sapi, asyncio

Ard = serial.Serial('COM3') 
time.sleep(5)
auth = r6sapi.Auth('ekhadley@gmail.com', 'dexterspike1')
pav = 0
k2 = 0
d2 = 0

while 1:
    def run():
        k1 = k2
        d1 = d2

        print("checking...")
        player = yield from auth.get_player("ElasButt", r6sapi.Platforms.UPLAY)
#        operator = yield from player.get_operator("jackal")
        k1 = player.kills
        d1 = player.deaths
        print(mnm, shot)
    time.sleep(0)
    asyncio.get_event_loop().run_until_complete(run())

    if d2 != d1:
        pav = 1
    if k2 != k1:
        pav = 2

    print(k1, d1)
    pav = bytes(pav, encoding = 'utf-8')
    Ard.write(pav) 
    pav = 0