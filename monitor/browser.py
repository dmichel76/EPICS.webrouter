from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urltools
import os

class Browser(object):
	""" Class that controls the browser
	"""

	def __init__(self, browser_name):

		if browser_name.lower() == "chrome":
			options = webdriver.ChromeOptions()
			options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
			self.browser = webdriver.Chrome(chrome_options=options)

		if browser_name.lower() == "firefox":
			self.browser = webdriver.Firefox()

	def fullscreen(self):
		body = self.browser.find_element_by_tag_name('body')
		body.send_keys(Keys.F11)

	def refresh(self):
		self.browser.refresh()

	def point(self,url):
		self.browser.get(url)

	def current_url(self):
		return urltools.normalize(self.browser.current_url)

	def set_default(self, file):
		self.default = "file://" + os.path.join(os.path.dirname(os.path.abspath(__file__)), file) 

	def get_default(self):
		return self.default
