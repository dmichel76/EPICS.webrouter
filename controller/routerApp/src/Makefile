TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = router
# router.dbd will be created and installed
DBD += router.dbd

# router.dbd will be made up from these files:
router_DBD += base.dbd

# Include dbd files from all support applications:
#router_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#router_LIBS += xxx

# router_registerRecordDeviceDriver.cpp derives from router.dbd
router_SRCS += router_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
router_SRCS_DEFAULT += routerMain.cpp
router_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#router_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
router_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

