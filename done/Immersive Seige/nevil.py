import r6sapi as api
import asyncio, time
auth = api.Auth('ekhadley@gmail.com', 'dexterspike1')
while 1:
    def run():
        print("collecting...")
        player = yield from auth.get_player("ElasButt", api.Platforms.UPLAY)
        operator = yield from player.get_operator('jackal')
        mnm = operator.kills
        shot = operator.deaths
        print(mnm, shot)
    time.sleep(0)
    asyncio.get_event_loop().run_until_complete(run())
