import selenium, time, random, requests, openai
from bs4 import BeautifulSoup as bs4
class bot:
    def __init__(self, driver):
        self.driver = driver
        self.lastSeen = msg()
        self.name = "FriggBot2000"
        self.responses = {
            "gaming":"GÅMING!",
            "lith":"https://cdn.discordapp.com/attachments/785014933758410796/785032262206226442/image0.jpg",
            "nefarious":"This computer is shared with others including parents. This is a parent speaking to you to now. Not sure what this group is up to. I have told my son that role playing d and d games are absolutely forbidden in out household. We do not mind him having online friendships with local people that he knows for legitimate purposes. Perhaps this is an innocent group. But, we expect transparency in our son's friendships and acquaintances. If you would like to identify yourself now and let me know what your purpose for this platform is this is fine. You are welcome to do so.",
            "avatars":"This computer is shared with others including parents. This is a parent speaking to you to now. Not sure what this group is up to. I have told my son that role playing d and d games are absolutely forbidden in out household. We do not mind him having online friendships with local people that he knows for legitimate purposes. Perhaps this is an innocent group. But, we expect transparency in our son's friendships and acquaintances. If you would like to identify yourself now and let me know what your purpose for this platform is this is fine. You are welcome to do so.",
            "cringe":"https://media.discordapp.net/attachments/551246526924455937/776278020507959296/image0.jpg?width=248&height=330",
            "patrick":"https://cdn.discordapp.com/attachments/785014933758410796/785218539350523944/nyooo.mp4",
            "weirdchamp":"https://cdn.discordapp.com/attachments/785015097927139348/785219023654354964/lmao.png",
            "nog":"https://cdn.discordapp.com/attachments/785014933758410796/785258888478851082/eggy.png",
            "wgmn":"https://cdn.discordapp.com/attachments/551246526924455937/783217821776740352/image0.gif",
        }

    def readLast(self):
        incoming = msg()
        while True:
            try:
                incoming.content = self.driver.find_elements_by_css_selector(".messageContent-2t3eCI")[-1].text
                incoming.sender = self.driver.find_elements_by_css_selector(".username-h_Y3Us")[-1].text
                incoming.time = self.driver.find_elements_by_css_selector("[datetime]")[-1].get_attribute("datetime")
                break
            except selenium.common.exceptions.StaleElementReferenceException:
                time.sleep(.01)
        if incoming != self.lastSeen and incoming.sender != self.name:
            self.lastSeen.copy(incoming)
            self.onMessage()

    def send(self, msg):
        print("typing . . .")
        self.driver.find_element_by_css_selector('[role=textbox]').send_keys(msg, selenium.webdriver.common.keys.Keys.ENTER)
        print("response finished . . .")


    def onMessage(self):
        m = self.lastSeen.content
        for i, e in enumerate(self.responses):
            if e in m.lower():
                self.send(self.responses[e])

        if "cemb cemb" in m.lower():
            self.send(random.choice(["yes", "no", "c'est possible"]))

        if "!lp" in m.lower():
            region = m[0:m.index(" ")].replace("!lp", "")
            name = m.replace(f"!lp{region} ", "")
            region = "na1" if region=="" else region
            try:
                page = bs4(requests.get(f"https://u.gg/lol/profile/{region}/{name}/overview").text, 'html.parser')
                page = list(str(page.find("div", class_="rank-text").text))
                report = name +' is in '
                for i in range(0, len(page)):
                    if page[i] == '/':
                        report += ' at '
                    else:
                        report += page[i]
                if "Unranked" in report:
                    report = f"{name} is not on the ranked grind"
                self.send(report)

            except AttributeError:
                self.send('https://tenor.com/view/who-dat-snoop-gif-15116696')

        if "!gpt3" in m:
            print("gpt request received. . .")
            openai.api_key = open("C:\\Users\\ekhad\\Desktop\\frig\\openaikey.txt").readline()
            resp = openai.Completion.create(
                prompt=m.replace("!gpt3 ",""),
                temperature=.5,
                engine="text-davinci-002",
                max_tokens=250,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0)
            print("request processed. . .")
            self.send(resp.choices[0].text)

class msg:
    def __init__(self):
        self.content = None
        self.sender = None
        self.time = None

    def __eq__(self, __o: object) -> bool:
        return (self.content == __o.content) and (self.sender == __o.sender) and (self.time == __o.time)

    def copy(self, new):
        self.content, self.sender, self.time = new.content, new.sender, new.time

    def clear(self):
        self.content = None
        self.sender = None
        self.time = None