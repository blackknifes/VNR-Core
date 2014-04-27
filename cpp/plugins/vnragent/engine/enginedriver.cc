// enginedriver.cc
// 4/26/2014 jichi

#include "growl.h"
#include "engine/enginedriver.h"
#include "engine/enginemanager.h"
#include "model/engine.h"

/** Private class */

class EngineDriverPrivate
{
public:
  bool enabled;
  EngineManager *manager;
  //AbstractEngine *engine;

  explicit EngineDriverPrivate(QObject *parent)
    : enabled(true), manager(new EngineManager(parent)) {}
};

/** Public class */

//static EngineDriver *instance_;
//EngineDriver *EngineDriver::instance() { return instance_; }

EngineDriver::EngineDriver(QObject *parent)
  : Base(parent), d_(new D(this))
{
  connect(d_->manager, SIGNAL(textsReceived(QString)), SIGNAL(textsReceived(QString)),
          Qt::QueuedConnection); // queued is indispensible, as this signal could be triggered by non-QThread engine

  if (auto p = AbstractEngine::instance())
    //p->setParent(this);
    if (p->inject()) {
      //d_->engine = p;
      //connect(d_->engine, SIGNAL(textReceived(QString,qint64,int,void*)), d_->manager, SLOT(addText(QString,qint64,int,void*)));
      // FIXME: Only one instance can be send at a time?!
      //growl::notify(tr("Recognize game engine: %1").arg(p->name()));
    }


  //::instance_ = this;
}

EngineDriver::~EngineDriver()
{
  //::instance_ = nullptr;
  delete d_;
}

void EngineDriver::updateTranslation(const QString &json) { d_->manager->updateTranslation(json); }
void EngineDriver::clearTranslation() { d_->manager->clearTranslation(); }

bool EngineDriver::isEnabled() const { return d_->enabled; }
void EngineDriver::setEnable(bool t) { d_->enabled = t; }

// EOF
