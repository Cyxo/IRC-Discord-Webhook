# -*- coding: utf-8 -*-
import irc3
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

WEBHOOK_URL = config['discord']['webhook_url']

@irc3.plugin
class Plugin:

    def __init__(self, bot):
        self.bot = bot

    @irc3.event(irc3.rfc.PRIVMSG)
    def recv(self, mask=None, data=None,**kw):
        if mask is not None:
            username = mask.split("!")[0]
        else:
            username = "User"

        if data is not None:
            embed_message = {
                "username": username,
                "avatar_url": 'https://www.root-me.org/IMG/auton0.png',
                "content": data
            }
            requests.post(WEBHOOK_URL, data=embed_message)
