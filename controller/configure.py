#!/usr/bin/env python

# how to run:
# configure.py --prefix ROUTER --add-monitor M1 --clean --database database.db
# configure.py --prefix ROUTER --add-url http://localhost:8080/leds.html --with-name LED -d database.db

import sys
import os
import optparse
import epicsdbbuilder
import uuid

def write_db(outfile, clean):

	tempfile = str(uuid.uuid4())
	epicsdbbuilder.WriteRecords(tempfile, header="")

	if clean: 		
		f = open(outfile, 'w') # append to file
	else:
		f = open(outfile, 'a') # or clear the file empty

	t = open(tempfile, 'r')
	f.write(t.read())	
	f.close()
	t.close()
	os.remove(tempfile)

def write_to_list(name, outfile, clean):

	if clean: pages_list = open(outfile, 'w')
	else: pages_list = open(outfile, 'a')
	pages_list.write(name + "\n")
	pages_list.close()

if __name__ == "__main__":
	
	# parse command line arguments
	parser = optparse.OptionParser()
	parser.add_option("-l", "--list", dest="list", help="list file", type="string")
	parser.add_option("-d", "--database", dest="database", help="database file", type="string")
	parser.add_option("-p", "--prefix", dest="prefix", help="PV prefix", type="string")
	parser.add_option("-c", "--clean", action="store_true", dest="clean", help="clean database of existing entries")
	parser.add_option("-m", "--add-monitor", dest="monitor", help="add specified monitor to database", type="string")
	parser.add_option("-u", "--add-url", dest="url", help="add specified url to database", type="string")
	parser.add_option("-n", "--with-name", dest="name", help="name to use when adding url to database", type="string")

	(args, remainder) = parser.parse_args()

	if not args.list: parser.error("output list database file not specified")
	if not args.database: parser.error("output database file not specified")
	if not args.prefix: parser.error("Controller prefix name not given")
	if args.url and not args.name: parser.error("Name of URL not given")
	if not args.url and args.name: parser.error("Name for URL given, but not URL given")
	if args.url and args.monitor: parser.error("Cannot parse both URL and monitor at the same time")

	# check/find EPICS base directory
	EPICS_BASE_DIR = os.environ.get("EPICS_BASE")
	if EPICS_BASE_DIR == None: 
		print "Error: EPICS_BASE environment variable not set"
		sys.exit(1)

	# create/edit database
	epicsdbbuilder.InitialiseDbd(EPICS_BASE_DIR)
	epicsdbbuilder.SetSimpleRecordNames(prefix=args.prefix, separator=':')

	# adding monitor
	if args.monitor:

		pv_current_page = epicsdbbuilder.records.stringin(args.monitor + ":CURRENT_PAGE")
		pv_current_page.PINI = 'YES'
		pv_current_page.VAL = ''
		pv_current_page.DESC = 'page to be displayed on web browser'

		pv_reload = epicsdbbuilder.records.bi(args.monitor + ":RELOAD")
		pv_reload.PINI = 'YES'
		pv_reload.ZNAM = 'DO NOT RELOAD'
		pv_reload.ONAM = 'DO RELOAD'
		pv_reload.DESC = 'reload the browser'

		write_db(args.database, args.clean)
		write_to_list(args.monitor, args.list, args.clean)

	if args.url and args.name:
		
		pv_url = epicsdbbuilder.records.stringin("URL:" + args.name)
		pv_url.PINI = "YES"
		pv_url.VAL = args.url
		pv_url.DESC = "URL for page called " + args.name
	
		write_db(args.database, args.clean)
		write_to_list(args.name, args.list, args.clean)

	
