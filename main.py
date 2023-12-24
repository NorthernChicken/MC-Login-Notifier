from mcstatus import JavaServer
import time
import http.client, urllib
from secrets import token, user

'''
* Made by NorthernChicken
*Repo: https://github.com/NorthernChicken/MC-Login-Notifier
* Desc: Playing on servers is only fun if you are playing with others. This script sends me a notification if someone logs on.
'''

def send_notif():

    conn = http.client.HTTPSConnection("api.pushover.net:443")

    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": token,
        "user": user,
        "title": "GET ON",
        "message": "SOMEBODY GOT ONLINE!!",
        "url": "",
        "priority": "0" 
    }), { "Content-type": "application/x-www-form-urlencoded" })

    conn.getresponse()

with open('ip.txt', 'r') as file:
    ip = file.read()

server = JavaServer.lookup(ip)

while True:
    players = server.status()
    if players.players.online == 0:
        print("No one is online.")
        time.sleep(3)
    elif players.players.online > 0:
        send_notif()
        print("Someone is online!")
        break
