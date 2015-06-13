#pragma once

// age.h
// 6/1/2014 jichi

#include "engine/enginemodel.h"

class ARCGameEngine : public EngineModel
{
  SK_EXTEND_CLASS(ARCGameEngine, EngineModel)
  static bool attach();
  static QString textFilter(const QString &text, int role);
public:
  ARCGameEngine()
  {
    name = "EmbedARCGameEngine";
    dynamicEncoding = true;
    matchFiles << "AGERC.DLL"; // the process name is AGE.EXE.
    attachFunction = &Self::attach;
    textFilterFunction = &Self::textFilter;
  }
};

// EOF