from mcstatus import JavaServer
import time
import http.client
import urllib
from secrets import token, user

'''
* Made by NorthernChicken
* Repo: https://github.com/NorthernChicken/MC-Login-Notifier
* Desc: Playing on servers is only fun if you are playing with others. This script sends me a notification if someone logs on.
'''

notification_sent = False

def send_notif():
    global notification_sent
    if not notification_sent:
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
                     urllib.parse.urlencode({
                         "token": token,
                         "user": user,
                         "title": "GET ON",
                         "message": "SOMEBODY GOT ONLINE!!",
                         "url": "",
                         "priority": "0"
                     }), {"Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()
        print("Someone is online!")
        notification_sent = True

with open('ip.txt', 'r') as file:
    ip = file.read()

server = JavaServer.lookup(ip)

while True:
    players = server.status()
    if players.players.online == 0:
        print("No one is online.")
        notification_sent = False
        time.sleep(3)
    elif players.players.online > 0:
        send_notif()
