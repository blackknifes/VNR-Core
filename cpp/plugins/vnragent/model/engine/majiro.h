#pragma once

// majiro.h
// 4/20/2014 jichi

#include "model/engine.h"

class MajiroEngine : public AbstractEngine
{
  SK_EXTEND_CLASS(MajiroEngine, AbstractEngine)
  SK_DISABLE_COPY(MajiroEngine)

public:
  MajiroEngine() : Base("Majiro", "SHIFT-JIS") {}

  static bool match();
  bool inject() override;
};

// EOF
