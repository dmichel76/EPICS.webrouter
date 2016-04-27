from epics import pv
import urltools

class Controller(object):
	""" Class that reads PVs from the EPICS IOC controller
	"""

	def __init__(self, prefix, name):
		self.prefix = prefix
		self.name = name
		self.page_pv = pv.PV(prefix + ":" + name + ":CURRENT_PAGE")
		self.reload_pv = pv.PV(prefix + ":" + name + ":RELOAD")

	def close(self):
		self.page_pv.disconnect()
		self.reload_pv.disconnect()

	def url(self, page): 
		url_pv = pv.PV(self.prefix + ":URL:" + page)
		url = url_pv.get()
		url_pv.disconnect()
		return urltools.normalize(str(url))

	@property
	def page(self): return self.page_pv.get()

	@property
	def reload(self): return self.reload_pv.get()

	@reload.setter
	def reload(self, value): 
		self.reload_pv.put(value)


