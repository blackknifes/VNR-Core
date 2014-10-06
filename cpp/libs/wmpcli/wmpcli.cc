// wmpcli.cc
// 10/5/2014 jichi

#ifdef _MSC_VER
# pragma warning (disable:4800)   // C4800: forcing value to bool
#endif // _MSC_VER

#include "wmpcli/wmpcli.h"
#include <windows.h>
#include "wmp/wmp.h"
#include "wincom/wincomptr.h"

#define action(_objtype, _iname, _oname) \
  bool wmp_##_objtype##_##_iname(wmp_##_objtype##_t *obj) \
  { return SUCCEEDED(obj->_oname()); }

#define _setter(_objtype, _itype, _iname, _otype, _oname) \
  bool wmp_##_objtype##_set_##_iname(wmp_##_objtype##_t *obj, _itype val) \
  { return SUCCEEDED(obj->put_##_oname(val)); }

#define str_setter(_objtype, _iname, _oname) \
  bool wmp_##_objtype##_set_##_iname(wmp_##_objtype##_t *obj, const wchar_t *val) \
  { \
    WinCom::ScopedBstr p(val); \
    return SUCCEEDED(obj->put_##_oname(p.get())); \
  }

#define _getter(_objtype, _itype, _iname, _otype, _oname, _defval) \
  _itype wmp_##_objtype##_get_##_iname(wmp_##_objtype##_t *obj) \
  { \
    _otype val; \
    return SUCCEEDED(obj->get_##_oname(&val)) ? val : _defval; \
  }

#define bool_getter(_objtype, _iname, _oname) \
  bool wmp_##_objtype##_get_##_iname(wmp_##_objtype##_t *obj) \
  { \
    VARIANT_BOOL val; \
    return SUCCEEDED(obj->get_##_oname(&val)) && val; \
  }

#define _property(_objtype, _itype, _iname, _otype, _oname, _defval) \
  _getter(_objtype, _itype, _iname, _otype, _oname, _defval) \
  _setter(_objtype, _itype, _iname, _otype, _oname)

#define bool_setter(_objtype, _iname, _oname) \
  _setter(_objtype, bool, _iname, VARIANT_BOOL, _oname)

#define str_getter(_objtype, _iname, _oname) \
  _getter(_objtype, const wchar_t *, _iname, BSTR, _oname, nullptr) \

#define float_setter(_objtype, _iname, _oname) \
  _setter(_objtype, double, _iname, double, _oname)

#define float_getter(_objtype, _iname, _oname) \
  _getter(_objtype, double, _iname, double, _oname, 0) \

#define int_setter(_objtype, _iname, _oname) \
  _setter(_objtype, int, _iname, long, _oname)

#define int_getter(_objtype, _iname, _oname) \
  _getter(_objtype, int, _iname, long, _oname, 0) \

#define bool_property(_objtype, _iname, _oname) \
  bool_getter(_objtype, _iname, _oname) \
  bool_setter(_objtype, _iname, _oname)

#define str_property(_objtype, _iname, _oname) \
  str_getter(_objtype, _iname, _oname) \
  str_setter(_objtype, _iname, _oname)

#define float_property(_objtype, _iname, _oname) \
  float_getter(_objtype, _iname, _oname) \
  float_setter(_objtype, _iname, _oname)

#define int_property(_objtype, _iname, _oname) \
  int_getter(_objtype, _iname, _oname) \
  int_setter(_objtype, _iname, _oname)

// Construction

int wmp_player_release(wmp_player_t *p) { return p->Release(); }
int wmp_controls_release(wmp_controls_t *c) { return c->Release(); }
int wmp_settings_release(wmp_settings_t *s) { return s->Release(); }
int wmp_media_release(wmp_media_t *m) { return m->Release(); }

wmp_player_t *wmp_player_create()
{
  IWMPPlayer *p = nullptr;
  return SUCCEEDED(::CoCreateInstance(CLSID_WindowsMediaPlayer, nullptr, CLSCTX_INPROC_SERVER, IID_IWMPPlayer,
      reinterpret_cast<LPVOID *>(&p))) ? p : nullptr;
}

wmp_controls_t *wmp_player_get_controls(wmp_player_t *p)
{
  IWMPControls *c;
  return SUCCEEDED(p->get_controls(&c)) ? c : nullptr;
}

wmp_settings_t *wmp_player_get_settings(wmp_player_t *p)
{
  IWMPSettings *s;
  return SUCCEEDED(p->get_settings(&s)) ? s : nullptr;
}

// Player

action(player, close, close)

bool_property(player, enabled, enabled)
bool_property(player, fullscreen, fullScreen)
bool_property(player, contextmenuenabled, enableContextMenu)

str_property(player, uimode, uiMode)
str_property(player, url, URL)

// Settings

bool_property(settings, errordialogsenabled, enableErrorDialogs)
bool_property(settings, autostart, autoStart)
str_property(settings, baseurl, baseURL)
int_property(settings, volume, volume)
int_property(settings, balance, balance)
bool_property(settings, mute, mute)
float_property(settings, rate, rate)
int_property(settings, playcount, playCount)

// Shuffle the order
bool wmp_settings_set_shuffle(wmp_settings_t *s, bool t)
{ return SUCCEEDED(s->setMode(L"shuffle", t)); }

bool wmp_settings_get_shuffle(wmp_settings_t *s)
{
  VARIANT_BOOL t;
  return SUCCEEDED(s->getMode(L"shuffle", &t)) && t;
}

// Repeat the tracks
bool wmp_settings_set_repeat(wmp_settings_t *s, bool t)
{ return SUCCEEDED(s->setMode(L"loop", t)); }

bool wmp_settings_get_repeat(wmp_settings_t *s)
{
  VARIANT_BOOL t;
  return SUCCEEDED(s->getMode(L"loop", &t)) && t;
}

bool wmp_settings_set_autorewind(wmp_settings_t *s, bool t)
{ return SUCCEEDED(s->setMode(L"autoRewind", t)); }

bool wmp_settings_get_autorewind(wmp_settings_t *s)
{
  VARIANT_BOOL t;
  return SUCCEEDED(s->getMode(L"autoRewind", &t)) && t;
}

// Controls

action(controls, play, play)
action(controls, pause, pause)
action(controls, stop, stop)
action(controls, previous, previous)
action(controls, next, next)
action(controls, forward, fastForward)
action(controls, backward, fastReverse)

float_property(controls, pos, currentPosition)

bool wmp_controls_set_media(wmp_controls_t *c, wmp_media_t *m)
{ return SUCCEEDED(c->put_currentItem(m)); }

wmp_media_t *wmp_controls_get_media(wmp_controls_t *c)
{
  IWMPMedia *m;
  return SUCCEEDED(c->get_currentItem(&m)) ? m : nullptr;
}

// Media

bool wmp_media_equal(wmp_media_t *x, wmp_media_t *y)
{
  VARIANT_BOOL t;
  return x == y
      || x && y && SUCCEEDED(x->get_isIdentical(y, &t)) && t;
}

int_getter(media, imagewidth, imageSourceWidth)
int_getter(media, imageheight, imageSourceHeight)
float_getter(media, duration, duration)
str_getter(media, url, sourceURL)

str_property(media, name, name)

// EOF
