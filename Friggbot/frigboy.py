import zenon

token = "MzUyMjI2MDQ1MjI4ODc1Nzg2.YnhbAA.G_yITzIf18Eu6p7Y29grnKqBlHs"


def on_message():
    while True:
        chatid = "551246526924455937"
        message = client.get_message(chatid)
        if message == "!test":
            client.send_message(chatid, "lorem ipsum")
        
if __name__ == '__main__':
    client = zenon.Client(token)
    # client = zenon.Client(token, proxy = "ip:port")
    client.func_loop(on_message)