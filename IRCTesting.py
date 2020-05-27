import socket

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a socket object
server = "chat.freenode.net" # Server
channel = "##bot-testing" # Channel
botnick = "IamaPythonBot" # Your bots nick
adminname = "OrderChaos23" #Your IRC nickname. On IRC (and most other places) I go by OrderChaos so that’s what I am using for this example.
exitcode = "bye " + botnick

ircsock.connect(("irc.chat.twitch.tv", 6667)) # Here we connect to the server using the port 6667
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "n", "UTF-8")) #We are basically filling out a form with this line and saying to set all the fields to the bot nickname.
ircsock.send(bytes("NICK "+ botnick +"n", "UTF-8")) # assign the nick to the bot

def joinchan(chan): # join channel(s).
  ircsock.send(bytes("JOIN "+ chan +"n", "UTF-8")) 
  ircmsg = ""
  while ircmsg.find("End of /NAMES list.") == -1:  
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('nr')
    print(ircmsg)