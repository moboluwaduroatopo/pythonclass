from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys


class webbrowser(QMainWindow):
	"""docstring for ClassName"""
	def __init__(self,*args,**kwargs):
		
		super(webbrowser, self).__init__(*args,**kwargs)
		self.setWindowTitle('web browser')
		# self.browser=QWebView()
		self.setUrl("http://www.google.com")
		# self.arg = arg
app=QApplication(sys.argv)		
web =webbrowser()
web.show()
app.exec_()