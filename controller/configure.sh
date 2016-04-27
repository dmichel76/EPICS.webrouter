#!/usr/bin/env bash

echo configuring monitors
python configure.py --clean -p ROUTER -m MONITOR_1 -d routerApp/Db/monitors.db -l iocBoot/iocrouter/monitors.list
python configure.py -p ROUTER -m MONITOR_2 -d routerApp/Db/monitors.db -l iocBoot/iocrouter/monitors.list

echo configuring urls
python configure.py --clean -p ROUTER -u http://localhost:8080/leds.html -n LED -d routerApp/Db/urls.db -l iocBoot/iocrouter/pages.list
python configure.py -p ROUTER -u http://localhost:8080/buttons.html -n BUTTONS -d routerApp/Db/urls.db -l iocBoot/iocrouter/pages.list


