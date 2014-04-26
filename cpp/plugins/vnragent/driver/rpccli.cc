// rpccli.cc
// 2/1/2013 jichi

#include "driver/rpccli.h"
#include "driver/rpccli_p.h"
#include "growl.h"
//#include "qtmetacall/metacallpropagator.h"
#include <QtCore/QHash>

/** Private class */

RpcClientPrivate::RpcClientPrivate(Q *q)
  : Base(q), q_(q), r(new RpcPropagator(this))
{
  reconnectTimer = new QTimer(q);
  reconnectTimer->setSingleShot(true);
  reconnectTimer->setInterval(ReconnectInterval);
  connect(reconnectTimer, SIGNAL(timeout()), SLOT(reconnect()));

  connect(r, SIGNAL(agentMessageReceived(QString,QString)), SLOT(onMessage(QString)));
  //connect(r, SIGNAL(updateClientData(QString)), q, SIGNAL(dataReceived(QString)));
  //connect(r, SIGNAL(callClient(QString)), SLOT(onCall(QString)));

  //connect(r, SIGNAL(disconnected()), SLOT(reconnect()), Qt::QueuedConnection);
  //connect(r, SIGNAL(socketError()), SLOT(reconnect()), Qt::QueuedConnection);
}

bool RpcClientPrivate::reconnect()
{
  if (r->isActive())
    return true;
  r->stop();
  if (start()) {
    r->waitForReady();
    pingServer();
    return true;
  } else
    return false;
}

void RpcClientPrivate::onMessage(const QString &cmd, const QString &param)
{
  enum { // pre-computed qHash values
    H_PING          = 487495,   // "ping"
    H_UI_ENABLE     = 79990437,     // "ui.enable"
    H_UI_DISABLE    = 184943013,    // "ui.disable"
    H_UI_CLEAR      = 206185698,    // "ui.clear"
    H_UI_CLEAR      = 197504020     // "ui.text"
  };

  switch (qHash(cmd)) {
  case H_UI_CLEAR:      q_->emit clearUiRequested(); break;
  case H_UI_ENABLE:     q_->emit enableUiRequested(true); break;
  case H_UI_DISABLE:    q_->emit enableUiRequested(false); break;
  case H_UI_TEXT:       q_->emit uiTranslationReceived(param); break;

  case H_PING:
  default: ;
  }
}

/** Public class */

// - Construction -

RpcClient::RpcClient(QObject *parent)
  : Base(parent), d_(new D(this))
{
  if (!d_->reconnect())
    growl::warn(QString().sprintf("Visual Novel Reader is not ready! Maybe the port %i is blocked?", D::PORT));

  d_->reconnectTimer->start();
}

RpcClient::~RpcClient() { delete d_; }

bool RpcClient::isActive() const
{ return d_->r->isActive(); }

// - API -
void RpcClient::requestUiTranslation(const QString &json)
{ d_->sendUiTexts(json); }

void RpcClient::showMessage(const QString &t) { d_->growlServer(t, D::GrowlMessage); }
void RpcClient::showWarning(const QString &t) { d_->growlServer(t, D::GrowlWarning); }
void RpcClient::showError(const QString &t) { d_->growlServer(t, D::GrowlError); }

// EOF
