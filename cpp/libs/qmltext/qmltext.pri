# qmltext.pri
# 4/5/2014 jichi
#include(../../../config.pri)
#include($$LIBDIR/imageutil/imageutil.pri)
DEFINES += WITH_LIB_QMLTEXT

DEPENDPATH += $$PWD

HEADERS += \
  $$PWD/contouredtextedit.h

SOURCES += \
  $$PWD/contouredtextedit.cc

#INCLUDEPATH     += $$QT_SRC

QT      += core gui

# EOF
