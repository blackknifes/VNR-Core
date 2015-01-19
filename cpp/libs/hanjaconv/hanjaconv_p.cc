// hanjaconv_p.cc
// 1/6/2015 jichi

#include "hanjaconv/hanjaconv_p.h"
#include "hanjaconv/hanjaconfig.h"
#include "hanjaconv/hanjachars.h"
#include <boost/algorithm/string.hpp>

#ifdef __clang__
# pragma clang diagnostic ignored "-Wparentheses"
#endif // __clang

// Public:

void HanjaConverterPrivate::replace(std::wstring &text) const // beginning of word
{
  if (text.size() < HANJA_MIN_SIZE)
    return;
  size_t pos = 0,
         len;
  while (pos <= text.size() - HANJA_MIN_SIZE)
    if (len = replace_first(text, pos))
      pos += len;
    else
      pos++;
}

void HanjaConverterPrivate::collect(const std::wstring &text, const Q::collect_fun_t &fun) const
{
  if (text.size() < HANJA_MIN_SIZE)
    return;
  size_t pos = 0,
         lastpos = 0,
         len;
  while (pos <= text.size() - HANJA_MIN_SIZE)
    if (len = collect_first(text, pos, lastpos, fun)) {
      pos += len;
      lastpos = pos;
    } else
      pos++;
  if (lastpos < text.size())
    fun(lastpos, text.size() - lastpos, nullptr);
    //collect_hangul(text, lastpos, text.size() - lastpos, fun);
}

// Private:

size_t HanjaConverterPrivate::replace_first(std::wstring &text, size_t start) const
{
  if (text.size() < HANJA_MIN_SIZE || start > text.size() - HANJA_MIN_SIZE ||
      !::is_hangul(text[start]) || !::is_hangul(text[start + 1]))
    return 0;
  for (size_t ei = 0; ei < entry_count; ei++) {
    const auto &e = entries[ei];
    if (boost::starts_with(text.c_str() + start, e.hangul)) {
      if (e.hangul.size() == e.hanja.size())
        for (size_t i = 0; i < e.hanja.size(); i++)
          text[start + i] = e.hanja[i];
      else // as this should never happen, it is implemented inefficiently
        boost::replace_first(text, e.hangul, e.hanja);
      return e.hanja.size();
    }
  }
  return 0;
}

size_t HanjaConverterPrivate::collect_first(const std::wstring &text, size_t start, size_t last, const Q::collect_fun_t &fun) const
{
  if (text.size() < HANJA_MIN_SIZE || start > text.size() - HANJA_MIN_SIZE ||
      !::is_hangul(text[start]) || !::is_hangul(text[start + 1]))
    return 0;
  for (size_t ei = 0; ei < entry_count; ei++) {
    const auto &e = entries[ei];
    if (boost::starts_with(text.c_str() + start, e.hangul)) {
      if (last < start)
        fun(last, start - last, nullptr);
        //collect_hangul(text, last, start - last, fun);
      fun(start, e.hangul.size(), e.hanja.c_str());
      return e.hanja.size();
    }
  }
  return 0;
}

// EOF

/*

struct ParseIndex
{
  size_t start,
         length;
  const wchar_t *hanja; // use pointer instead of wstring to avoid copying

  explicit ParseIndex(size_t start = std::string::npos, size_t length = 0, const wchar_t *hanja = nullptr)
    : start(start), length(length) , hanja(hanja) {}
};

  // Return position of matched beginning of word, or npos is failed
  size_t find_bow(const std::wstring text, size_t start) const
  {
    if (text.size() < HANJA_MIN_SIZE || start > text.size() - HANJA_MIN_SIZE)
      return std::string::npos;
    if (start == 0)
      return 0;
    for (size_t pos = start; pos < text.size(); pos++)
      if (!::is_hangul(text[pos - 1]))
        return pos;
    return std::string::npos;
  }

  // Parse all indices whose hanja is nullptr
  void parse_all(const std::wstring &text, index_list &indices) const
  {
    bool erased = false;
    auto ip = indices.begin();
    while (ip != indices.end()) {
      erased = false;
      if (!ip->hanja && ip->length >= HANJA_MIN_SIZE)
        for (auto ep = entries.begin(); ep != entries.end(); ++ep) {
          auto begin = text.begin() + ip->start,
               end = begin + ip->length;
          auto r = boost::make_iterator_range(begin, end);
          if (auto found = boost::find_first(r, ep->hangul)) {
            size_t offset = found.begin() - text.begin();
            auto next = std::next(ip);
            // Insert reversely
            size_t i = offset + ep->hangul.length();
            if (i < ip->start + ip->length)
              next = indices.insert(next, index_type(i, ip->start + ip->length - i));
            next = indices.insert(next, index_type(offset, ep->hangul.length(), ep->hanja.c_str()));
            if (offset > ip->start) { // delete this ip
              ip->length = offset - ip->start;
              if (ip->length < HANJA_MIN_SIZE) {
                ++ip;
                break;
              }
            } else {
              ip = indices.erase(ip);
              erased = true;
              break;
            }
          }
        }
      if (!erased)
        ++ip;
    }
  }

*/