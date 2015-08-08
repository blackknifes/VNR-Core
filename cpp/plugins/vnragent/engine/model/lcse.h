#pragma once

// lcse.h
// 8/6/2015 jichi

#include "engine/enginemodel.h"

class LCScriptEngine : public EngineModel
{
  SK_EXTEND_CLASS(LCScriptEngine, EngineModel)
  bool attach();
public:
  LCScriptEngine()
  {
    name = "EmbedLCScriptEngine";
    //enableDynamicEncoding = true; // dynamically update this value
    dynamicEncodingMinimumByte = 0x6; // skip 0x1,0x2,0x3 in case dynamic encoding could crash the game
    //enableDynamicFont = true;
    newLineString = "\x01";
    matchFiles << "lcsebody*";
    attachFunction = std::bind(&Self::attach, this);
    //textSeperators << "\x01" << "\x02\x03";
  }
};

// EOF
