# wmptest.pro
# 10/1/2014

include(../../../config.pri)
#include($$LIBDIR/winmp/winmp.pri)

# Source

TEMPLATE = app
TARGET = wmptest

INCLUDEPATH += $$WMSDK_HOME/include
LIBS  += -lole32

DEPENDPATH += .
INCLUDEPATH += .

#HEADERS += main.h
SOURCES += main.cc

# EOF
