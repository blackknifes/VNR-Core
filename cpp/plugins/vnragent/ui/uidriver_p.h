#pragma once

// uidriver_p.h
// 2/1/2013 jichi

#include "sakurakit/skglobal.h"
#include <QtCore/QObject>
#include <qt_windows.h>

QT_FORWARD_DECLARE_CLASS(QTimer)

class UiManager;
//class UiDriver;
class UiDriverPrivate : public QObject
{
  Q_OBJECT
  Q_DISABLE_COPY(UiDriverPrivate)
  //SK_DECLARE_PUBLIC(UiDriver)
  SK_EXTEND_CLASS(UiDriverPrivate, QObject)

  QTimer *retransTimer,
         *rehookTimer;
public:
  bool enabled;
  UiManager *manager;

  //static Self *instance();
  explicit UiDriverPrivate(QObject *parent=nullptr);
  ~UiDriverPrivate();

private:
  void updateWindow(HWND hWnd);
  void updateContextMenu(HMENU hMenu, HWND hWnd);

  bool updateWindow(HWND hWnd, LPWSTR buffer, int bufferSize); // window
  bool updateListView(HWND hWnd, LPWSTR buffer, int bufferSize); // SysListView
  bool updateTabControl(HWND hWnd, LPWSTR buffer, int bufferSize); // SysTabControl
  bool updateMenu(HMENU hMenu, HWND hWnd, LPWSTR buffer, int bufferSize); // MenuItem
  bool updateTabView();

  static void updateProcessWindows(DWORD processId = 0);
  static void updateThreadWindows(DWORD threadId = 0);

private slots:
  void retrans();
  void rehook();
};

// EOF
