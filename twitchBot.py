import json, requests, sys

from itertools import islice

from irc.bot import SingleServerIRCBot
from requests import get  #lib to simplify talking to a server/website

twitchString = ""

NAME = ""
OWNER = ""

class Bot(SingleServerIRCBot): #inherits from singleserverIRCbot so it has all the parents class functions
    def __init__(self):  #init is ran on the creation of an object of this class
        self.HOST = "irc.chat.twitch.tv"
        self.PORT = 6667 #always 6667 (This is the protocol for IRC Chat)
        self.USERNAME = NAME.lower()
        self.CLIENT_ID = ""
        self.TOKEN = ""
        self.CHANNEL = f"#{OWNER.lower()}"

        url = f"https://api.twitch.tv/kraken/users?login={self.USERNAME}"
        headers = {"Client-ID": self.CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json"}
        #print(headers)
        resp = get(url, headers=headers).json() #makes a req containing the headers to the server and returns bot info
        print(70*"#")
        #print(resp)
        print(70*"#")
        self.channel_id = resp["users"][0]["_id"] #output: 'users': [{'display_name': 'TaZR2', '_id': '69281381', ....
        #print(self.channel_id)
        print(70*"#")
        #print([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")]) #need to send OAuth keys with "oauth:key"
        print(70*"#")
        super().__init__([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")], self.USERNAME, self.USERNAME) #passes this to the parent class


    def on_welcome(self, cxn, event):
        for req in ("membership", "tags", "commands"): #no idea what this does but we need it
            cxn.cap('REQ', f":twitch.tv/{req}")

        cxn.join(self.CHANNEL) #tells the conection object to join self.channel
        self.send_message(f"Bot: {self.USERNAME} IRC Bot Version: {self.get_version()} Now Online!") #twitch takes out extra spaces
        '''Bot: tazr2 IRC Bot Version: Python irc.bot (18.0.0) Now Online!'''

    def on_pubmsg(self, cxn, event):
        global twitchString
        print(f"\n\n\n\n #######{event.tags}###### \n\n\n\n\n")
        ''' [{'key': 'badge-info', 'value': None}, {'key': 'badges', 'value': 'broadcaster/1'}, {'key': 'color', 'value': None}, 
        {'key': 'display-name', 'value': 'geekygamer1134'}, {'key': 'emotes', 'value': None}, {'key': 'flags', 'value': None}, 
        {'key': 'id', 'value': 'c427f8a6-d014-4211-bfb2-0c8ef77fb1e9'}, {'key': 'mod', 'value': '0'}, {'key': 'room-id', 'value': '501482905'}, 
        {'key': 'subscriber', 'value': '0'}, {'key': 'tmi-sent-ts', 'value': '1587690735306'}, 
        {'key': 'turbo', 'value': '0'}, {'key': 'user-id', 'value': '501482905'}, {'key': 'user-type', 'value': None}] '''

        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags} #Creates a tag dict containing keys and vals
        print(f"\n\n\n\n these are the event tags: \n\n {tags} \n\n\n\n")
        '''{'badge-info': None, 'badges': 'broadcaster/1', 'color': None, 'display-name': 'geekygamer1134',
         'emotes': None, 'flags': None, 'id': 'd6b6219f-aae0-4e2d-a486-cb7a068bdf0a', 'mod': '0', 'room-id': '501482905',
         'subscriber': '0', 'tmi-sent-ts': '1587692274522', 'turbo': '0', 'user-id': '501482905', 'user-type': None} '''

        twitchString = event.arguments[0] #returns ['messageSentInTwitchChat']
        #if tags["display-name"] != OWNER:
            #cmds.process(bot, user, message)
        
        print(f"Message from {tags['display-name']}: {twitchString}")

    def send_message(self, message):
        print(self.connection.privmsg(self.CHANNEL, message))
        self.connection.privmsg(self.CHANNEL, message)
        #self.send_message("test.") #needs to see if message is from bot



if __name__ == "__main__":
    """bot2 = SingleServerIRCBot([("irc.chat.twitch.tv", 6667, f"oauth:7x6kyurubli3ald0tm5gve9xfiuyac")], "tazr2", "tazr2")
    print(dir(bot2))
    print(help(bot2.connect))
    bot2.start()"""
    bot = Bot()
    print(__name__)
    print(30*"#")
    print(30*"#")
    #print(dir(SingleServerIRCBot))
    bot.start()























#client = TwitchHelix(client_id='<cl9wra9o2gqfyij9tfijuo4cri7bn5>')
#streams_iterator = client.get_streams(page_size=100)
#for stream in islice(streams_iterator, 0, 500):
    #print(stream)


#client = TwitchClient(client_id='<cl9wra9o2gqfyij9tfijuo4cri7bn5>')
#channel = client.channels.get_by_id(44322889)

###
#print(channel.id)
#print(channel.name)
#print(channel.display_name)
####
#oauthtoken: nzgt3rrsza0yjjd9jooat7547e0w7u