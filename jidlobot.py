# -*- coding: utf-8 -*-

from datetime import datetime
from bs4 import BeautifulSoup
import yaml
import urllib2
import locale
import re
import socket

locale.setlocale(locale.LC_ALL, "cs_CZ.UTF-8")

with open("plugins/jidlobot/jidlobot.conf", 'r') as conf_file:
    config = yaml.load(conf_file)

outputs = []


def fetch_menu():
    """
    Gets today's menu.
    """

    def brana():
        """
        U Malické brány
        """

        menu = ""
        amounts = []
        names = []
        prices = []
        url = "http://www.plzen-info.cz/umalickebrany/index.php?akce=tydenni_nabidka"

        try:
            html = BeautifulSoup(urllib2.urlopen(url, timeout=config["HTTP_TIMEOUT"]).read(), "html5lib")
            for i in html.findAll("table", {"width": "99%"}):
                x = 0
                for j in i.findAll("td", {"width": "10%"}):
                    if x % 2 != 0:
                        prices.append(u"" + j.text.replace(u",-  Kč", u" Kč").strip())
                    else:
                        amounts.append(j.text.strip())
                    x += 1

                for j in i.findAll("td", {"width": "53%"}):
                    names.append(j.text.strip())

            x = 0
            while x < len(names):
                line = u"• " + re.sub(r"^g$", r"", amounts[x]) + " " + names[x] + " " + prices[x]
                line = re.sub(r"\s{2,}", r" ", line) + "\n"
                menu += line
                x += 1

            return u"*U Malické brány:*\n" + menu
        except socket.timeout, e:
            return u"*U Malické brány:*\n timeout :angry:\n"

    def excelent():
        """
        Excelent Comix Pub
        """

        menu = ""
        url = "https://www.zomato.com/plzen/comix-excelent-urban-pub-plze%C5%88"

        try:
            html = BeautifulSoup(urllib2.urlopen(url, timeout=config["HTTP_TIMEOUT"]).read(), "html5lib")
            for i in html.findAll("div", {"class": "tmi-daily"}):
                line = u"• " + re.sub(r"\s{2,}", r" ", i.text.strip()) + "\n"
                line = re.sub(r"\s{2,}", r" ", line)
                menu += line

            return u"*Excelent Comix Pub:*\n" + menu
        except socket.timeout, e:
            return u"*Excelent Comix Pub:*\n timeout :angry:\n"

    def vegetka():
        """
        Vegetka
        """

        menu = ""
        names = []
        prices = []
        url = "http://www.menicka.cz/1615-vegetka-zdrava-vyziva.html"

        try:
            html = BeautifulSoup(urllib2.urlopen(url, timeout=config["HTTP_TIMEOUT"]).read(), "html5lib")
            day = html.findAll("div", {"class": "menicka"})[0]

            for j in day.findAll("div", {"class": "nabidka_1"}):
                names.append(j.text.strip())

            for j in day.findAll("div", {"class": "cena"}):
                prices.append(j.text.strip())

            x = 0
            while x < len(names):
                line = u"• " + names[x] + " " + prices[x]
                menu += line + "\n"
                x += 1

            return u"*Vegetka:*\n" + menu
        except socket.timeout, e:
            return u"*Vegetka:*\n timeout :angry:\n"

    return brana() + "\n" + excelent() + "\n" + vegetka()

date = datetime.strftime(datetime.now(), u"%A %-d.%-m.".encode("utf-8")).decode("utf-8").lower()
header = u"<!channel> *Obědy – " + date + ":*\n\n"
menu = header + fetch_menu()
outputs.append([config["CHANNEL"], menu])
