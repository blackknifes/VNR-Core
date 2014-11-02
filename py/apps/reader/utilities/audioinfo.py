# coding: utf8
# audioinfo.py
# 11/2/2014 jichi

from pyaudio import PyAudio
from sakurakit.skdebug import dwarn
  #print '==== host info'
  #for i in range(a.get_host_api_count()):
  #  info = a.get_host_api_info_by_index(i)
  #  print i, '------'
  #  print info

  #print '==== device info'
  #for i in range(a.get_device_count()):
  #  info = a.get_device_info_by_index(i)
  #  if info['maxInputChannels'] > 0:
  #    print i, '------'
  #    print info

try:
  AUDIO = PyAudio()
  #AUDIO.terminate()

  HOST_INDEX = 0 # paMME
  HOST_INFO = AUDIO.get_host_api_info_by_index(HOST_INDEX)
  HOST_DEVICE_COUNT = HOST_INFO['deviceCount']

  INPUTDEVICES = None
  def inputdevices(): # yield dict
    global INPUTDEVICES
    if INPUTDEVICES is None:
      INPUTDEVICES = []
      for i in range(HOST_DEVICE_COUNT):
        info = AUDIO.get_device_info_by_host_api_device_index(HOST_INDEX, i)
        if info.get('name') and info.get('maxInputChannels'): # > 0
          INPUTDEVICES.append(info)
    return INPUTDEVICES

  OUTPUTDEVICES = None
  def outputdevices(): # [dict]
    if OUTPUTDEVICES is None:
      OUTPUTDEVICES = []
      for i in range(HOST_DEVICE_COUNT):
        info = get_device_info_by_host_api_device_index(HOST_INDEX, i)
        if info.get('name') and info.get('maxOutputChannels'): # > 0
          OUTPUTDEVICES.append(info)
    return OUTPUTDEVICES

except Exception, e:
  dwarn(e)

  AUDIO = None
  HOST_INFO = None
  HOST_DEVICE_COUNT = 0

  def inputdevices(): return []
  def outputdevices(): return []

# EOF
