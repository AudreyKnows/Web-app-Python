from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MyWebBrowser(QMainWindow):
  def __init__(self, *args, **kwargs):
    super(MyWebBrowser, self).__init__(*args, **kwargs)
    self.window = QWidgets()
    self.window.setWindowTitle("Neural Nine Web Browser")
    self.url_bar = QTextEdits()
    self.url_bar.setMaximumHeight(30)
    self.go_btn = QPushButton("Go")
self.go_btn.setMinimumHeight(30)
self.back_btn = QPushButton("<")
self.back_btn.setMinimumHeight(30)
self.forward_btn = QPushButton(">")
self.forward_btn.setMinimumHeight(30)


self.layout = QVBoxLayout()
self.horizontal = QHBoxLayout()
self.horizontal.addWidget(self.url_bar)
self.horizontal.addWidget(self.go_btn)
self.horizontal.addWidget(self.back_btn)
self.horizontal.addWidget(self.forward_btn)

self.browser = QWebEngineView()
self.layout.addLayout(self.horizontal)
self.layout.addWidget(self.browser)

self.browser.setURl(QUrl("http://Google.com"))

self.window.setLayout(layout)
self.window.show()

app = QApplication()
window = MyWebBrowser()
app.exec_()


    
    
    