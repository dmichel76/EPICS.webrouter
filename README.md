# EPICS.webrouter
A web page "router" driven by EPICS PVs. An EPICS IOC acts a "controller" used to control the URL that a browser points to. This can be used to remotely control the webpage shown by a browser on multiple headless display monitors.


### Configuring the controller IOC

#### Adding a new monitor
```
configure.py --prefix ROUTER --add-monitor M1
```

#### Adding a new URL
```
configure.py --prefix ROUTER --add-url http://localhost:8080/leds.html --with-name LED
```
