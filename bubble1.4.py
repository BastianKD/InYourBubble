# -*- coding: utf-8 -*-

import sys, re, os
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class BubbleBrowser(QMainWindow):

    List = [
    "https://i.pinimg.com/originals/e1/22/86/e12286e92b2b739d7b65853ffe4b7af3.jpg",
    "https://heystorytellers.files.wordpress.com/2013/05/vw-lemon.jpg",
    "http://naotw-pd.s3.amazonaws.com/images/lego-assinado_01.jpg",
    "https://www.theguardian.com/international",
    "http://www.wisebread.com/47-cheap-fun-things-to-do-this-weekend",
    "https://en.wikipedia.org/wiki/Main_Page",
    "https://www.nationalgeographic.com/science/space/solar-system/earth/",
    "https://reve-en-vert.com/",
    "https://i.pinimg.com/originals/59/2f/67/592f6721d635a50686fe09ef5db52924.jpg",
    "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/bettercaullsaul-lospolloshermanos.jpg",
    "http://www.bcboxes.com/flasherjj.html",
    "https://www.yr.no/place/Germany/Hamburg/Hamburg/hour_by_hour.html",
    "https://www.16personalities.com/free-personality-test",
    "https://www.nasa.gov/"
    ]


    def __init__(self):
        super(BubbleBrowser, self).__init__()
        self.homeUrl = QUrl.fromLocalFile(os.path.abspath("home.html"))
        self.addressRegex = re.compile("http?(s):\/\/?(www?.\.)([^/]+)")
        self.initGUI()

    def initGUI(self):
        self.backAct = QAction(QIcon.fromTheme('go-left'), 'Back', self)
        self.backAct.setShortcut('Alt+Left')
        self.backAct.triggered.connect(self.back)
        self.backAct.setEnabled(False)

        self.homeAct = QAction(QIcon.fromTheme('go-home'), 'Home', self)
        self.homeAct.setShortcut('Alt+Up')
        self.homeAct.triggered.connect(self.home)

        self.nextAct = QAction(QIcon.fromTheme('go-right'), 'Next', self)
        self.nextAct.setShortcut('Alt+Right')
        self.nextAct.triggered.connect(self.next)
        self.nextAct.setEnabled(False)

        self.toolbar = self.addToolBar('Navigation')
        self.toolbar.addAction(self.backAct)
        self.toolbar.addAction(self.homeAct)
        self.toolbar.addAction(self.nextAct)

        self.web = QWebView()
        self.web.urlChanged.connect(self.url_changed)
        self.web.titleChanged.connect(self.title_changed)
        self.web.load(self.homeUrl)
        self.setCentralWidget(self.web)

        self.show()


    def back(self):
        page = self.web.page()
        history = page.history()
        self.newURL = QUrl(BubbleBrowser.List[randint(0, len(self.List)-1)])
        self.web.load(self.newURL)
        self.check_buttons(history)

    def home(self):
        self.web.load(self.homeUrl)

    def next(self):
        page = self.web.page()
        history = page.history()
        self.newURL = QUrl(BubbleBrowser.List[randint(0, len(self.List)-1)])
        self.web.load(self.newURL)
        self.check_buttons(history)

    def check_buttons(self,history):
        if history.canGoForward():
            self.nextAct.setEnabled(True)
        else:
            self.nextAct.setEnabled(True)
        if history.canGoBack():
            self.backAct.setEnabled(True)
        else:
            self.backAct.setEnabled(False)

    def url_changed(self):
        page = self.web.page()
        history = page.history()
        self.check_buttons(history)

    def title_changed(self):
        try:
            title = self.addressRegex.match(self.web.url().toString()).group(3)
        except:
            title = self.web.title()
        self.setWindowTitle(title + " in your bubble!")


if __name__=="__main__":
    app = QApplication(sys.argv)
    win = BubbleBrowser()
    win.show()

sys.exit(app.exec_())
