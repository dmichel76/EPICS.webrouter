#!/usr/bin/env python

# how to run:
# monitor.py --name M1 --prefix ROUTER -f

import time
import sys
import argparse
import urltools

from controller import Controller
from browser import Browser

DEFAULT_URL = "files/nothing.html"

# parse command line options
parser = argparse.ArgumentParser(description='monitor')
parser.add_argument("--name", dest="name", help="name of monitor")
parser.add_argument("--prefix", dest="prefix", help="PV prefix")
parser.add_argument("-f", action="store_true", dest="fullscreen", help="fullscreen flag")
args = parser.parse_args()
if not args.name: parser.error("Name of monitor not given")
if not args.prefix: parser.error("Controller prefix name not given")

# start and setup browser
browser = Browser("fierefox")
if (args.fullscreen): browser.fullscreen()
browser.set_default(DEFAULT_URL)
old_target_url = browser.current_url()

# Create Controller object that connects to controller (EPICS IOC)
controller = Controller(args.prefix, args.name)

# monitor routing PVs and point webbrowser to the right URL accordingly.
while(True):

	try:
		# get current desired page name
		page = controller.page

		# get URL of that page, using default when nothing is specified
		target_url = browser.get_default() if page=="" else controller.url(page)

		# if different from previously loaded URL, point browser to it
		if not urltools.compare(old_target_url, target_url):
			browser.point(target_url)
			old_target_url = target_url

		# reload browser if asked
		if 1 ==  controller.reload: 
			controller.reload = 0
			browser.refresh()

	except Exception as e:
		print e.message

	time.sleep(1)

