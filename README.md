# EPICS.webrouter
A web page "router" driven by EPICS PVs. An EPICS IOC acts a "controller" used to control the URL that a browser points to. This can be used to remotely control the webpage shown by a browser on multiple headless display monitors.

### Configuring the controller IOC

#### Adding new monitors
```
cd controller
configure.py --prefix ROUTER --add-monitor M1
configure.py --prefix ROUTER --add-monitor M2
```

#### Adding new URLs
```
cd controller
configure.py --prefix ROUTER --add-url http://localhost:8080/beam_status.html --with-name STATUS
configure.py --prefix ROUTER --add-url http://localhost:8080/vacuum_sys.html --with-name VACUUM
```

### Running the controller IOC

```
cd controller/iocBoot/iocrouter/
./st.cmd
```

```
epics> dbl
ROUTER:M1:RELOAD
ROUTER:M2:RELOAD
ROUTER:M1:CURRENT_PAGE
ROUTER:M2:CURRENT_PAGE
ROUTER:URL:STATUS
ROUTER:URL:VACUUM
ROUTER:MONITORS
ROUTER:PAGES
```

### Running the browser driver script

A python script is used to drive (i.e. launch and control) the browser (firefox)

```
cd monitor
./monitor.py --name M1 --prefix ROUTER --fullscreen
```

### Using the system

Once both the controller IOC and the browser drivers are running on each monitor displays, it's easy to change what each browser is pointing at, by simply using the PVs available on the controller IOC as such:

* Pointing browser on monitor M1 to the vacuum URL: ```caput ROUTER:M1:CURRENT_PAGE VACUUM```
* Pointing browser on monitor M2 to the status URL: ```caput ROUTER:M2:CURRENT_PAGE STATUS```
* By default, a browser does not point to any specific URL and display a generic page with the organisation's logo. Pointing the ```CURRENT_PAGE``` PV to an empty string will show that default page: ```caput ROUTER:M1:CURRENT_PAGE STATUS ""```
* Show list of available URLS: ```caget ROUTER:PAGES```
* Show list of available monitors: ```caget ROUTER:MONITORS```


