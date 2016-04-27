#!../../bin/linux-x86_64/router

## You may have to change router to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/router.dbd"
router_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords("db/monitors.db")
dbLoadRecords("db/urls.db")
dbLoadRecords("db/lists.db")

cd "${TOP}/iocBoot/${IOC}"
iocInit


