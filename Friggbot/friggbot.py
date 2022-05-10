from bs4 import BeautifulSoup as bs4
import requests, discord, random

client = discord.Client()
grace = False

@client.event
async def on_message(message):  
    if "gaming" in message.content:
        await message.channel.send("GÅMING!")

    if "lith" in message.content:
        await message.channel.send("https://cdn.discordapp.com/attachments/785014933758410796/785032262206226442/image0.jpg")

    if "nefarious" in message.content or "avatars" in message.content:
        await message.channel.send("This computer is shared with others including parents. This is a parent speaking to you to now. Not sure what this group is up to. I have told my son that role playing d and d games are absolutely forbidden in out household. We do not mind him having online friendships with local people that he knows for legitimate purposes. Perhaps this is an innocent group. But, we expect transparency in our son's friendships and acquaintances. If you would like to identify yourself now and let me know what your purpose for this platform is this is fine. You are welcome to do so.")
        
    if "cringe" in message.content:
        await message.channel.send("https://media.discordapp.net/attachments/551246526924455937/776278020507959296/image0.jpg?width=248&height=330")

    if "patrick" in message.content:
        await message.channel.send("https://cdn.discordapp.com/attachments/785014933758410796/785218539350523944/nyooo.mp4")

    #if "ddd" in message.content:
    #    await message.channel.send("https://cdn.discordapp.com/attachments/785015097927139348/785218908252012564/ddd.mp4")

    if "weirdchamp" in message.content:
        await message.channel.send("https://cdn.discordapp.com/attachments/785015097927139348/785219023654354964/lmao.png")

    if "nog" in message.content:
        await message.channel.send("https://cdn.discordapp.com/attachments/785014933758410796/785258888478851082/eggy.png")

    if "wgmn" in message.content:
        if message.author.id == 546216485861851146:
            await message.channel.send("https://media.discordapp.net/attachments/551246526924455937/750147906828370071/unknown.png?width=440&height=244")
        else:
            await message.channel.send("https://media.discordapp.net/attachments/551246526924455937/783217821776740352/image0.gif?width=305&height=330")

    if "gracie" in message.content:
        if message.author.id == 345135505043750912:
            await message.channel.send("https://cdn.discordapp.com/attachments/785015097927139348/785219345290100786/gmaings.png")

    if "rocky" in message.content:
        await message.channel.send("!play https://www.youtube.com/watch?v=DhlPAj38rHc")

    if "cemb cemb" in message.content:
        choice = ''
        if random.randint(0, 2) == 0:
            choice = 'yes'
        if random.randint(0, 2) == 1:
            choice = 'nah'
        if random.randint(0, 2) == 2:
            choice = 'maybe'
        await message.channel.send(choice)

    if "!LP " in message.content or '!lp ' in message.content or '!Lp ' in message.content or '!lP ' in message.content:
        msg = list(message.content)
        name = ''
        for i in range(4, len(msg)):
            name += msg[i]

        try:
            page = bs4(requests.get('https://u.gg/lol/profile/na1/' + name + '/overview').text, 'html.parser')
            page = list(str(page.find("div", class_="rank-text").text))
            report = name +' is in '
            for i in range(0, len(page)):
                if page[i] == '/':
                    report += ' at '
                else:
                    report += page[i]
            if "Unranked" in report:
                await message.channel.send(name + ' is not on the ranked grind')
            else:
                if "eekay" in report:
                    report = "eekay is Rank 1 NA at " + str(random.randint(1000, 1600)) + "LP"
                await message.channel.send(report)

        except AttributeError:
            await message.channel.send('https://tenor.com/view/who-dat-snoop-gif-15116696')

key = open("C:\\Users\\ekhad\\Desktop\\frigkey.txt", "r")
#key = open("C:\\Users\\ek\\Desktop\\frigkey.txt", "r")
frigkey = key.readline()
client.run(frigkey)









































































