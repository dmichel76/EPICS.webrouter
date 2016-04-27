#!/usr/bin/env bash

echo configuring monitors
python configure.py --clean -p ROUTER -m MONITOR_1
python configure.py -p ROUTER -m MONITOR_2

echo configuring urls
python configure.py --clean -p ROUTER -u http://localhost:8080/leds.html -n LED
python configure.py -p ROUTER -u http://localhost:8080/buttons.html -n BUTTONS



