# coding: utf8
# modiocr.py
# 8/13/2013 jichi

if __name__ == '__main__': # DEBUG
  import sys
  sys.path.append("..")

import os
from sakurakit.skclass import memoized

# This file must be consistent with modiocr.h
# enum modiocr_lang : unsigned long
#modiocr_lang_null = 0 # failed

LANG_JA = 1 << 0 # miLANG_JAPANESE = 17,

LANG_ZHS = 1 << 1 # miLANG_CHINESE_SIMPLIFIED = 2052
LANG_ZHT = 1 << 2 # miLANG_CHINESE_TRADITIONAL = 1028

LANG_KO = 1 << 3  # miLANG_KOREAN = 18,

LANG_CS = 1 << 4  # miLANG_CZECH = 5,
LANG_DA = 1 << 5  # miLANG_DANISH = 6,
LANG_NL = 1 << 6  # miLANG_DUTCH = 19,
LANG_FI = 1 << 7  # miLANG_FINNISH = 11,
LANG_FR = 1 << 8  # miLANG_FRENCH = 12,
LANG_DE = 1 << 9  # miLANG_GERMAN = 7,
LANG_EL = 1 << 10 # miLANG_GREEK = 8,
LANG_HU = 1 << 11 # miLANG_HUNGARIAN = 14,
LANG_IT = 1 << 12 # miLANG_ITALIAN = 16,
LANG_NB = 1 << 13 # miLANG_NORWEGIAN = 20,
LANG_PL = 1 << 14 # miLANG_POLISH = 21,
LANG_PT = 1 << 15 # miLANG_PORTUGUESE = 22,
LANG_RU = 1 << 16 # miLANG_RUSSIAN = 25,
LANG_ES = 1 << 17 # miLANG_SPANISH = 10,
LANG_SV = 1 << 18 # miLANG_SWEDISH = 29,
LANG_TR = 1 << 19 # miLANG_TURKISH = 31,

LANG_EN = 1 << 20 # miLANG_ENGLISH = 9,

LANG_DEFAULT = 1 << 21 # miLANG_SYSDEFAULT = 2048

from sakurakit import skpaths
DLL_PATH = os.path.join(skpaths.PROGRAMFILES, 'Common Files/Microsoft Shared/MODI/12.0/MDIVWCTL.dll')

from sakurakit import skos
if skos.WIN:
  from  pymodiocr import ModiOcr
  available = ModiOcr.isValid # -> bool
  # Note: the read functions might raise if the path does not on Windows XP
  readtext = ModiOcr.readText # (unicode path, int lang) -> unicode
  readtexts = ModiOcr.readTextList # (unicode path, int lang) -> [unicode]
else:
  def available(): return False
  def readtext(): return ''
  def readtexts(): return []

if __name__ == '__main__':
  import os, sys
  os.environ['PATH'] += os.path.pathsep + "../../../bin"
  sys.path.append("../../../bin")
  sys.path.append("..")

  import pythoncom

  if not available():
    print "not available"
  else:
    path = "./wiki.tiff"
    print readtext(path, LANG_JA)

# EOF