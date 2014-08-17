# coding: utf8
# iciba.py
# 8/7/2014 jichi
# See: jp.iciba.com
# Only en-ja-zhs are supported.

if __name__ == '__main__':
  import sys
  sys.path.append('..')

import json
import requests
from sakurakit.skdebug import dwarn, derror

session = requests # global session

# Either of the two are OK.
# But the difault type are different
ICIBA_API = "http://jp.iciba.com/api.php"
#ICIBA_API = "http://fy.iciba.com/api.php"

# Coffeescript extracted from the HTML:
#  _query = ->
#    return false  if jQuery.trim(jQuery("#inputC").val()).length is 0
#    jQuery("#copy-botton").css "display", "none"
#    jQuery.ajax
#      type: "post"
#      dataType: "json"
#      url: "api.php"
#      data: "q=" + encodeURIComponent(jQuery(".inputC").val()) + "&type=" + jQuery.mod
#      success: (msg) ->
#
# Request: q=%E4%BD%A0%E5%A5%BD&type=zh-jp
# Response: {"error":0,"outstr":0,"from":"jp","to":"zh","type":"\u65e5 -> \u4e2d","ret":"\u4f60\u597d\u3002<br \/><br \/>","retcopy":"\u4f60\u597d\u3002"}

_LANG = {
  'en': 'en',
  'ja': 'jp',
  'zhs': 'zh',
  'zht': 'zh',
}
def _lang(lang): return _LANG.get(lang) or 'en' # str -> str

def translate(text, to='zhs', fr='ja'):
  """Return translated text, which is NOT in unicode format
  @param  text  unicode not None
  @param  fr  unicode not None, must be valid language code
  @param  to  unicode not None, must be valid language code
  @return  unicode or None
  """
  try:
    api = ICIBA_API
    r = session.post(api, data={
      'q': text,
      'type': '-'.join((
        _lang(fr),
        _lang(to),
      ))
    })

    ret = r.content
    if r.ok and len(ret) > 20 and ret[0] == '{' and ret[-1] == '}':
      #ret = ret.decode('utf8')
      js = json.loads(ret)
      return js['retcopy']

  #except socket.error, e:
  #  dwarn("socket error", e.args)
  except requests.ConnectionError, e:
    dwarn("connection error", e.args)
  except requests.HTTPError, e:
    dwarn("http error", e.args)
  #except UnicodeDecodeError, e:
  #  dwarn("unicode decode error", e)
  except (ValueError, KeyError, IndexError, TypeError), e:
    dwarn("json format error", e)
  except Exception, e:
    derror(e)
  dwarn("failed")
  try: dwarn(r.url)
  except: pass

if __name__ == "__main__":
  #t = translate(u"こん\nにちは！", to='zhs', fr='ja')
  #t = translate(u"你好！", to='zhs', fr='ja')
  #t = translate(u"こん\nにちは！", to='en', fr='ja')
  #print t

  s = u"""
オープニングやエンディングのアニメーションは単純に主人公を入れ替えた程度の物ではなく、タイトルロゴはもちろん金時や定春の行動や表情、登場する道具（万事屋の面々が乗る車のデザインなど）やクレジット文字など、細部に渡って変更がなされた。更に、坂田金時が『銀魂'』を最終回に追い込み新しいアニメ『まんたま』を始めようとした時にはエンディングや提供表示の煽りコメントが最終回を思わせる演出となり、『まんたま』でも専用のタイトルロゴとオープニングアニメーション（スタッフクレジット付き）が新造され、偽物の提供クレジットまで表示されるなど随所に至るまで徹底的な演出が行われた。また、テレビ欄では金魂篇終了回は『金魂'』最終回として、その翌週は新番組「銀魂'」として案内された。
"""

  from sakurakit.skprofiler import SkProfiler

  session = requests.Session()
  with SkProfiler():
    for i in range(10):
      t = translate(s, to='zhs', fr='ja')
  #print t

  session = requests
  with SkProfiler():
    for i in range(10):
      t = translate(s, to='zhs', fr='ja')
  #print t

# EOF