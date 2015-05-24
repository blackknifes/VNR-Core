#pragma once
// hijackdriver.h
// 5/1/2013 jichi

#include "sakurakit/skglobal.h"
#include <QtCore/QObject>

class HijackDriverPrivate;
// Root object for all qobject
class HijackDriver : public QObject
{
  Q_OBJECT
  Q_DISABLE_COPY(HijackDriver)
  SK_EXTEND_CLASS(HijackDriver, QObject)
  SK_DECLARE_PRIVATE(HijackDriverPrivate)
public:
  explicit HijackDriver(QObject *parent = nullptr);
  ~HijackDriver();

  void unload();

public slots:
  void setEncoding(const QString &v);
  void setFontFamily(const QString &v);
  void setFontCharSet(int v);

private slots:
  void refresh();
};


// EOF
