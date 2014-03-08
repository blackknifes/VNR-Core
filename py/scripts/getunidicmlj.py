# coding: utf8
# getunidicmlj.py
# 2/24/2014 jichi

if __name__ == '__main__':
  import initrc
  initrc.chcwd()
  initrc.initenv()

import os
from sakurakit.skdebug import dprint, dwarn
from sakurakit.skprofiler import SkProfiler

import initdefs
TARGET_DIR = initdefs.CACHE_UNIDICMLJ_RELPATH
TMP_DIR = initdefs.TMP_RELPATH

# http://www2.ninjal.ac.jp/lrc/index.php?UniDic%2F%B6%E1%C2%E5%CA%B8%B8%ECUniDic
# https://docs.google.com/file/d/0ByoM4WpH84qIS2Q1UU9tbnRDVk0/edit?pli=1
#UNIDIC_URL = 'http://sakurakit.org/pub/unidic-mlj/unidic-MLJ_13.zip'
#UNIDIC_URL = 'http://%s/pub/unidic-mlj/unidic-MLJ_13.zip' % initdefs.DOMAIN_ORG
UNIDIC_URL = "http://%s/pub/unidic-mlj/unidic-MLJ-1.3.7z" % initdefs.DOMAIN_ORG
#UNIDIC_FILESIZE = 104344408
UNIDIC_FILENAME = 'unidicmlj'
UNIDIC_SUFFIX = '.7z'
#UNIDIC_RELPATH = '/Files/dic/unidic-mecab'

MIN_FILESIZE = 40000000 # 40 < 49 MB

def init():
  for it in TMP_DIR:
    if not os.path.exists(it):
      os.makedirs(it)

def get(): # return bool
  url = UNIDIC_URL
  path = TMP_DIR + '/' + UNIDIC_FILENAME + UNIDIC_SUFFIX
  minsize = MIN_FILESIZE

  dprint("enter: url = %s" % url)

  from sakurakit import skfileio
  if os.path.exists(path) and skfileio.filesize(path) > minsize:
    dprint("leave: already downloaded")
    return True

  from sakurakit import sknetio
  ok = False
  with SkProfiler():
    if sknetio.getfile(url, path, flush=False): # flush=false to use more memory to reduce disk access
      ok = skfileio.filesize(path) > minsize
  if not ok and os.path.exists(path):
    os.remove(path)
  dprint("leave: ok = %s" % ok)
  return ok

def extract():
  dprint("enter")

  srcpath = TMP_DIR + '/' + UNIDIC_FILENAME + UNIDIC_SUFFIX
  tmppath = TMP_DIR + '/' + UNIDIC_FILENAME
  targetpath = TARGET_DIR

  import shutil
  from sakurakit import skfileio
  ok = skfileio.extract7z(srcpath, tmppath)
  if ok:
    if os.path.exists(targetpath):
      shutil.rmtree(targetpath)
    child = skfileio.getfirstchilddir(tmppath)
    os.renames(child, targetpath)
  if os.path.exists(tmppath):
    shutil.rmtree(tmppath)
  os.remove(srcpath)

  dprint("leave: ok = %s" % ok)
  return ok

def main():
  """
  @param  argv  [unicode]
  @return  int
  """
  dprint("enter")
  ok = False
  try:
    init()
    ok = get() and extract()
    if ok:
      from sakurakit import skos
      skos.open_location(os.path.abspath(TARGET_DIR))
  except Exception, e:
    dwarn(e)
  ret = 0 if ok else 1
  dprint("leave: ret = %s" % ret)
  return ret

if __name__ == '__main__':
  import sys
  if not initrc.lock('unidicmlj.lock'):
    dwarn("multiple instances")
    sys.exit(1)
  ret = main()
  sys.exit(ret)

# EOF
