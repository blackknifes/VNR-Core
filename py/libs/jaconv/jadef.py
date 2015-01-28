# coding: utf8
# jadef.py
# 10/18/2014 jichi
# See: http://sakuradite.com/wiki/en/Furigana

# Hepburn standard is used.
# See: https://en.wikipedia.org/wiki/Romanization_of_Japanese
# See: Transliterate/translation_maps.py
# Single っ is not handled, which will be processed later
EN = u"""
#Single
あ:a		い:i		う:u		え:e		お:o
か:ka		き:ki		く:ku		け:ke		こ:ko
さ:sa		し:shi		す:su		せ:se		そ:so
た:ta		ち:chi		つ:tsu		て:te		と:to
な:na		に:ni		ぬ:nu		ね:ne		の:no
は:ha		ひ:hi		ふ:fu		へ:he		ほ:ho
ま:ma		み:mi		む:mu		め:me		も:mo
や:ya				ゆ:yu				よ:yo
ら:ra		り:ri		る:ru		れ:re		ろ:ro
わ:wa								を:wo
		ゐ:wyi				ゑ:wye
ん:n

が:ga		ぎ:gi		ぐ:gu		げ:ge		ご:go
ざ:za		じ:ji		ず:zu		ぜ:ze		ぞ:zo
だ:da		ぢ:ji		づ:zu		で:de		ど:do
ば:ba		び:bi		ぶ:bu		べ:be		ぼ:bo
ぱ:pa		ぴ:pi		ぷ:pu		ぺ:pe		ぽ:po

#Smaller
ぁ:a		ぃ:i		ぅ:u		ぇ:e		ぉ:o
ゃ:ya				ゅ:yu				ょ:yo
ゎ:wa
ゕ:ka						ゖ:ke

#Composite
						いぇ:ye
うぁ:wha	うぃ:whi			うぇ:whe	うぉ:who
すぁ:swa	すぃ:swi	すぅ:swu	すぇ:swe	すぉ:swo
つぁ:tsa	つぃ:tsi	つぅ:tsu	つぇ:the	つぉ:tho
とぁ:twa	とぃ:twi	とぅ:twu	とぇ:twe	とぉ:two
ふぁ:fa		ふぃ:fi		ふぅ:fuu	ふぇ:fe		ふぉ:fo

ゔぁ:va		ゔぃ:vi		ゔ:vu		ゔぇ:ve		ゔぉ:vo
どぁ:dwa	どぃ:dwi	どぅ:dwu	どぇ:dwe	どぉ:dwo

きゃ:kya	きぃ:kyi	きゅ:kyu	きぇ:kye	きょ:kyo
しゃ:sha	しぃ:shi	しゅ:shu	しぇ:she	しょ:sho
ちゃ:cha	ちぃ:chi	ちゅ:chu	ちぇ:che	ちょ:cho
てゃ:tha	てぃ:thi	てゅ:thu	てぇ:the	てょ:tho
にゃ:nya	にぃ:nyi	にゅ:nyu	にぇ:nye	にょ:nyo
ひゃ:hya	ひぃ:hyi	ひゅ:hyu	ひぇ:hye	ひょ:hyo
ふゃ:fya			ふゅ:fyu			ふょ:fyo
みゃ:mya	みぃ:myi	みゅ:myu	みぇ:mye	みょ:myo
りゃ:rya	りぃ:ryi	りゅ:ryu	りぇ:rye	りょ:ryo

ゔゃ:vya			ゔゅ:vyu			ゔょ:vyo
ぎゃ:gya	ぎぃ:gyi	ぎゅ:gyu	ぎぇ:gye	ぎょ:gyo
じゃ:ja		じぃ:ji		じゅ:ju		じぇ:je		じょ:jo
ぢゃ:dya	ぢぃ:dyi	ぢゅ:dyu	ぢぇ:dye	ぢょ:dyo
でゃ:dha	でぃ:dhi	でゅ:dhu	でぇ:dhe	でょ:dho
びゃ:bya	びぃ:byi	びゅ:byu	びぇ:bye	びょ:byo
ぴゃ:pya	ぴぃ:pyi	ぴゅ:pyu	ぴぇ:pye	ぴょ:pyo
"""

# http://en.wikipedia.org/wiki/Russian_alphabet
# http://ru.wikipedia.org/wiki/Кана
# http://ru.wikipedia.org/wiki/Хирагана
# http://ru.wikipedia.org/wiki/Катакана
#
# a: а
# i: и(individual), not й(composite, delay to fix later after ауэояё
# e: э
# o: о
#
# u: у except yu
# yu: ю
#
# k: к
# ts: ц
# s: с
# ch: ч
# sh: с  or ш
#
# m: м
# n: н
# t: т
# h: х
# r: р
# f: ф
# p: п
# g: г
# z: З
# d: д
# b: б
# p: п
# v: иэ
#
# wa: ва
#
# ji: зи
# ya: я
# yo: ё
# ye: йё
#
# wh: у
# sw: су
# tw: ту
# dw: до
# th: ц / тэ
# dh: дэ
#
# Definitions different from wiki:
# - cha/chu/cho: ча/чу/чо is used instead of тя/тю/тё
# - з is used instead of дз
RU = u"""
#Single
あ:а		い:и		う:у		え:э		お:о
か:ка		き:ки		く:ку		け:кэ		こ:ко
さ:са		し:си		す:су		せ:сэ		そ:со
た:та		ち:ти		つ:цу		て:тэ		と:то
な:на		に:ни		ぬ:ну		ね:нэ		の:но
は:ха		ひ:хи		ふ:фу		へ:хэ		ほ:хо
ま:ма		み:ми		む:му		め:мэ		も:мо
や:я				ゆ:ю				よ:ё
ら:ра		り:ри		る:ру		れ:рэ		ろ:ро
わ:ва								を:о
		ゐ:ви				ゑ:вэ
ん:н

が:га		ぎ:ги		ぐ:гу		げ:гэ		ご:го
ざ:за		じ:зи		ず:зу		ぜ:зэ		ぞ:зо
だ:да		ぢ:зи		づ:зу		で:дэ		ど:до
ば:ба		び:би		ぶ:бу		べ:бэ		ぼ:бо
ぱ:па		ぴ:пи		ぷ:пу		ぺ:пэ		ぽ:по

#Small
ぁ:а		ぃ:и		ぅ:у		ぇ:э		ぉ:о
ゃ:я				ゅ:ю				ょ:ё
ゎ:wа
ゕ:ка						ゖ:кэ

#Composite
						#いぇ:иэ
つぁ:ца		つぃ:ци				つぇ:цэ		つぉ:цо
ふぁ:фа		ふぃ:фи				ふぇ:фэ		ふぉ:фо

ゔぁ:ва		ゔぃ:ви		ゔ:ву		ゔぇ:вэ		ゔぉ:во

きゃ:кя				きゅ:кю				きょ:кё
しゃ:ся		しぃ:ши		しゅ:сю		しぇ:шэ		しょ:сё
ちゃ:ча		ちぃ:чи		ちゅ:чу		ちぇ:чэ		ちょ:чо
にゃ:ня				にゅ:ню				にょ:нё
ひゃ:хя				ひゅ:хю				ひょ:хё
みゃ:мя				みゅ:мю				みょ:мё
りゃ:ря				りゅ:рю				りょ:рё

ゔゃ:уя				ゔゅ:вю				ゔょ:вё
ぎゃ:гя				ぎゅ:гю				ぎょ:гё
じゃ:зя				じゅ:зю				じょ:зё
ぢゃ:зя				ぢゅ:зю				ぢょ:зё
びゃ:бя				びゅ:бю				びょ:бё
ぴゃ:пя				ぴゅ:пю				ぴょ:пё
"""

# http://blog.naver.com/thinkstart/120072326990
# http://www.geocities.jp/p451640/moji/skm/gjo/utfgjo_02.html
# http://www.geocities.jp/p451640/moji/skm/gjo/gjo_02.html
# Ambiguity:
# - Use 語中 instead of 語頭: か, た
# - Use 語頭 instead of 語中: ち
# - Missing: だ
KO = u"""
#Single
あ:아		い:이		う:우		え:에		お:오
か:카		き:키		く:쿠		け:케		こ:코
さ:사		し:시		す:스		せ:세		そ:소
た:타		ち:치		つ:츠		て:테		と:토
な:나		に:니		ぬ:누		ね:네		の:노
は:하		ひ:히		ふ:후		へ:헤		ほ:호
ま:마		み:미		む:무		め:메		も:모
や:야				ゆ:유				よ:요
ら:라		り:리		る:루		れ:레		ろ:로
わ:와								を:오
		ゐ:이				ゑ:에
ん:응

が:가		ぎ:기		ぐ:구		げ:게		ご:고
ざ:자		じ:지		ず:즈		ぜ:제		ぞ:조
だ:다		ぢ:지		づ:즈		で:데		ど:도
ば:바		び:비		ぶ:부		べ:메		ぼ:보
ぱ:파		ぴ:피		ぷ:푸		ぺ:페		ぽ:포

#Small
ぁ:아		ぃ:이		ぅ:우		ぇ:에		ぉ:오
ゃ:야				ゅ:유				ょ:요
ゎ:와
ゕ:카						ゖ:케

#Composite
						いぇ:예
うぁ:와		うぃ:위				うぇ:웨		うぉ:워
すぁ:사		すぃ:시		すぅ:수		すぇ:세		すぉ:소
つぁ:차		つぃ:치		つぅ:추		つぇ:체		つぉ:초
とぁ:톼		とぃ:퇴		とぅ:토		とぇ:퇘		とぉ:토
ふぁ:하		ふぃ:휘		ふぅ:훗		ふぇ:훼		ふぉ:호

ゔぁ:바		ゔぃ:비		ゔ:부		ゔぇ:베		ゔぉ:보
どぁ:다		どぃ:디		どぅ:두		どぇ:데		どぉ:도

きゃ:캬		きぃ:키		きゅ:큐		きぇ:케		きょ:쿄
しゃ:샤		しぃ:시		しゅ:슈		しぇ:세		しょ:쇼
ちゃ:챠		ちぃ:치		ちゅ:츄		ちぇ:체		ちょ:쵸
てゃ:탸		てぃ:티		てゅ:튜		てぇ:테		てょ:툐
にゃ:냐		にぃ:니		にゅ:뉴		にぇ:네		にょ:뇨
ひゃ:햐		ひぃ:히		ひゅ:휴		ひぇ:헤		ひょ:효
ふゃ:햐				ふゅ:휴				ふょ:효
みゃ:먀		みぃ:미		みゅ:뮤		みぇ:메		みょ:묘
りゃ:랴		りぃ:리		りゅ:류		りぇ:레		りょ:료

ゔゃ:뱌				ゔゅ:뷰				ゔょ:뵤
ぎゃ:갸		ぎぃ:기		ぎゅ:규		ぎぇ:게		ぎょ:교
じゃ:자		じぃ:지		じゅ:쥬		じぇ:제		じょ:조
ぢゃ:자		ぢぃ:지		ぢゅ:쥬		ぢぇ:제		ぢょ:조
でゃ:댜		でぃ:디		でゅ:듀		でぇ:데		でょ:됴
びゃ:뱌		びぃ:비		びゅ:뷰		びぇ:메		びょ:뵤
ぴゃ:퍄		ぴぃ:피		ぴゅ:퓨		ぴぇ:페		ぴょ:표

#Eng
あん:앙		いん:인		うん:운		えん:엔		おん:온
かん:칸		きん:킨		くん:군		けん:켄		こん:콘
さん:산		しん:신		すん:슨		せん:센		そん:손
たん:탄		ちん:친		つん:츤		てん:텐		とん:톤
なん:난		にん:닌		ぬん:눈		ねん:넨		のん:논
はん:한		ひん:힌		ふん:훈		へん:헨		ほん:혼
まん:만		みん:민		むん:문		めん:멘		もん:몬
やん:얀								ゆん:윤								よん:욘
らん:란		りん:린		るん:룬		れん:렌		ろん:론
わん:완																				をん:온
		ゐん:인						ゑん:엔

がん:간		ぎん:긴		ぐん:군		げん:겐		ごん:곤
ざん:잔		じん:진		ずん:즌		ぜん:젠		ぞん:조
だん:단		ぢん:진		づん:즌		でん:덴		どん:돈
ばん:반		びん:빈		ぶん:분		べん:벤		ぼん:본
ぱん:판		ぴん:핀		ぷん:푼		ぺん:펜		ぽん:폰

#Composite
						いぇん:옌
うぁん:완	うぃん:윈			うぇん:웬	うぉん:온
すぁん:산	すぃん:신	すぅん:순	すぇん:센	すぉん:손
つぁん:찬	つぃん:친	つぅん:춘	つぇん:첸	つぉん:촌
とぁん:탄	とぃん:틴	とぅん:툰	とぇん:텐	とぉん:톤
ふぁん:한	ふぃん:힌	ふっん:훈	ふぇん:헨	ふぉん:혼

ゔぁん:반	ゔぃん:빈	ゔん:분		ゔぇん:벤	ゔぉん:본
どぁん:돤	どぃん:된	どぅん:둔	どぇん:덴	どぉん:돈

きゃん:캰	きぃん:킨	きゅん:큔	きぇん:켄	きょん:쿈
しゃん:샨	しぃん:신	しゅん:슌	しぇん:센	しょん:숀
ちゃん:챤	ちぃん:친	ちゅん:츈	ちぇん:첸	ちょん:쵼
てゃん:탼	てぃん:틴	てゅん:튠	てぇん:텐	てょん:툔
にゃん:냥	にぃん:닌	にゅん:뉸	にぇん:넨	にょん:뇬
ひゃん:햔	ひぃん:힌	ひゅん:휸	ひぇん:헨	ひょん:횬
ふゃん:햔			ふゅん:휸			ふょん:횬
みゃん:먄	みぃん:민	みゅん:뮨	みぇん:멘	みょん:묜
りゃん:랸	りぃん:린	りゅん:륜	りぇん:렌	りょん:룐

ゔゃん:뱐			ゔゅ:뷴				ゔょん:뵨
ぎゃん:갼	ぎぃん:긴	ぎゅ:균		ぎぇん:겐	ぎょん:굔
じゃん:쟌	じぃん:진	じゅ:쥰		じぇん:젠	じょん:죤
ぢゃん:쟌	ぢぃん:진	ぢゅ:쥰		ぢぇん:젠	ぢょん:죤
でゃん:댠	でぃん:딘	でゅ:듄		でぇん:덴	でょん:됸
びゃん:뱐	びぃん:빈	びゅ:뷴		びぇん:벤	びょん:뵨
ぴゃん:퍈	ぴぃん:핀	ぴゅ:퓬		ぴぇん:펜	ぴょん:푠
"""

# http://th.wikipedia.org/wiki/ฮิระงะนะ
# http://th.wikipedia.org/wiki/คะตะกะนะ
# http://th.wikipedia.org/wiki/คะนะ
# http://en.wikipedia.org/wiki/Thai_alphabet
# http://www.itagaki.net/trv/thai/language/Japanese_syllabary.htm
# http://www.thaismile.jp/ThaiLanguage/6/aiueo.html
#
# http://th.wikipedia.org/wiki/เทนโจอิง_อาซึกะ
#
# The mapping for long sound (such as ふう) and Eng(-ん) are incomplete
TH = u"""
#Single
あ:อา		い:ย์		う:อุ		え:เอ		お:โอ
か:คา		き:กิ		く:คุ		け:เค		こ:โก
さ:ซา		し:ชิ		す:สึ		せ:เซ		そ:โซ
た:ตา		ち:จิ		つ:สึ		て:เท็		と:โท
な:นา		に:นิ		ぬ:นุ		ね:เนะ		の:โน
は:ฮา		ひ:ฮิ		ふ:ฟุ		へ:เฮะ		ほ:โฮ
ま:มา		み:มิ		む:มุ		め:เมะ		も:โม
や:ยา				ゆ:ยุ				よ:โย
ら:รา		り:ริ		る:รุ		れ:เร็		ろ:โร
わ:วะ								を:โว
		ゐ:ย์				ゑ:เอ
ん:น

が:คา		ぎ:คิ		ぐ:กุ		げ:เค		ご:โก
ざ:ซา		じ:จิ		ず:ซุ		ぜ:เซะ		ぞ:โซ
だ:ดา		ぢ:จิ		づ:ซึ		で:เท		ど:โด
ば:บา		び:บิ		ぶ:บึ		べ:เบ		ぼ:โบ
ぱ:พา		ぴ:พิ		ぷ:พึ		ぺ:เพ		ぽ:โพ

#Small
ぁ:อา		ぃ:ย์		ぅ:อุ		ぇ:เอ		ぉ:โอ
ゃ:ยา				ゅ:ยุ				ょ:โย
ゎ:ว
ゕ:คา						ゖ:เค

#Composite
						いぇ:เยะ
うぁ:วา		うぃ:วิ				うぇ:เวะ	うぉ:โว
すぁ:สา		すぃ:สิ		すぅ:สึ		すぇ:เสะ	すぉ:โส
つぁ:สา		つぃ:สิ		つぅ:สึ		つぇ:เสะ	つぉ:โส
とぁ:ทวะ	とぃ:ทวิ		とぅ:ทึ		とぇ:ทเวะ	とぉ:โท
ふぁ:ฟา		ふぃ:ฟิ		ふぅ:ฟู		ふぇ:เฟะ	ふぉ:โฟ

ゔぁ:วะ		ゔぃ:วิ		ゔ:วุ		ゔぇ:เวะ	ゔぉ:โว
どぁ:ทวะ	どぃ:ทวิ		どぅ:ทึ		どぇ:ทเวะ	どぉ:โท

きゃ:เคีย	きぃ:คี		きゅ:คิว		きぇ:กิเยะ	きょ:เคียว
しゃ:ชา		しぃ:ชี		しゅ:ชุ		しぇ:เชะ	しょ:โช
ちゃ:ชา		ちぃ:ชี		ちゅ:ชุ		ちぇ:เชะ	ちょ:โช
てゃ:เทีย	てぃ:ทิ		てゅ:ทิว		てぇ:เท		てょ:เทียว

にゃ:เนีย	#にぃ:にぃ	にゅ:นิว		#にぇ:にぇ	にょ:เนียว
ひゃ:เฮีย	#ひぃ:ひぃ	ひゅ:ฮิว		#ひぇ:ひぇ	ひょ:เฮียว
#ふゃ:ふゃ			ふゅ:ฟิว				#ふょ:ふょ
みゃ:เมีย	#みぃ:みぃ	みゅ:มิว		#みぇ:みぇ	みょ:เมียว
りゃ:เรีย	#りぃ:りぃ	りゅ:ริว		#りぇ:りぇ	りょ:เรียว

ゔゃ:ゔゃ				#ゔゅ:ゔゅ				#ゔょ:ゔょ
ぎゃ:เคีย	ぎぃ:คี		ぎゅ:คิว		#ぎぇ:ぎぇ	ぎょ:เคียว
じゃ:จา		#じぃ:じぃ	じゅ:จุ		じぇ:เจะ	じょ:โจ
ぢゃ:จา		#ぢぃ:ぢぃ	ぢゅ:จุ		ぢぇ:เจะ	ぢょ:โจ
でゃ:จา		#でぃ:でぃ	でゅ:จุ		#でぇ:でぇ	でょ:โจ
びゃ:เปีย	#びぃ:びぃ	びゅ:ปิว		#びぇ:びぇ	びょ:เปียว
ぴゃ:เปีย	#ぴぃ:ぴぃ	ぴゅ:ปิว		#ぴぇ:ぴぇ	ぴょ:เปียว

#Long
				ふう:ฟู

#Eng
さん:ซัง
ちゃん:จัง
"""

# http://en.wikipedia.org/wiki/Arabic_alphabet
AR = u"""
#Single
あ:a		い:i		う:u		え:e		お:o
か:ka		き:ki		く:ku		け:ke		こ:ko
さ:sa		し:shi		す:su		せ:se		そ:so
た:ta		ち:chi		つ:tsu		て:te		と:to
な:na		に:ni		ぬ:nu		ね:ne		の:no
は:ha		ひ:hi		ふ:fu		へ:he		ほ:ho
ま:ma		み:mi		む:mu		め:me		も:mo
や:ya				ゆ:yu				よ:yo
ら:ra		り:ri		る:ru		れ:re		ろ:ro
わ:wa								を:wo
		ゐ:wyi				ゑ:wye
ん:n

が:ga		ぎ:gi		ぐ:gu		げ:ge		ご:go
ざ:za		じ:ji		ず:zu		ぜ:ze		ぞ:zo
だ:da		ぢ:ji		づ:zu		で:de		ど:do
ば:ba		び:bi		ぶ:bu		べ:be		ぼ:bo
ぱ:pa		ぴ:pi		ぷ:pu		ぺ:pe		ぽ:po

#Smaller
ぁ:a		ぃ:i		ぅ:u		ぇ:e		ぉ:o
ゃ:ya				ゅ:yu				ょ:yo
ゎ:wa
ゕ:ka						ゖ:ke

#Composite
						いぇ:ye
うぁ:wha	うぃ:whi			うぇ:whe	うぉ:who
すぁ:swa	すぃ:swi	すぅ:swu	すぇ:swe	すぉ:swo
つぁ:tsa	つぃ:tsi	つぅ:tsu	つぇ:the	つぉ:tho
とぁ:twa	とぃ:twi	とぅ:twu	とぇ:twe	とぉ:two
ふぁ:fa		ふぃ:fi		ふぅ:fuu	ふぇ:fe		ふぉ:fo

ゔぁ:va		ゔぃ:vi		ゔ:vu		ゔぇ:ve		ゔぉ:vo
どぁ:dwa	どぃ:dwi	どぅ:dwu	どぇ:dwe	どぉ:dwo

きゃ:kya	きぃ:kyi	きゅ:kyu	きぇ:kye	きょ:kyo
しゃ:sha	しぃ:shi	しゅ:shu	しぇ:she	しょ:sho
ちゃ:cha	ちぃ:chi	ちゅ:chu	ちぇ:che	ちょ:cho
てゃ:tha	てぃ:thi	てゅ:thu	てぇ:the	てょ:tho
にゃ:nya	にぃ:nyi	にゅ:nyu	にぇ:nye	にょ:nyo
ひゃ:hya	ひぃ:hyi	ひゅ:hyu	ひぇ:hye	ひょ:hyo
ふゃ:fya			ふゅ:fyu			ふょ:fyo
みゃ:mya	みぃ:myi	みゅ:myu	みぇ:mye	みょ:myo
りゃ:rya	りぃ:ryi	りゅ:ryu	りぇ:rye	りょ:ryo

ゔゃ:vya			ゔゅ:vyu			ゔょ:vyo
ぎゃ:gya	ぎぃ:gyi	ぎゅ:gyu	ぎぇ:gye	ぎょ:gyo
じゃ:ja		じぃ:ji		じゅ:ju		じぇ:je		じょ:jo
ぢゃ:dya	ぢぃ:dyi	ぢゅ:dyu	ぢぇ:dye	ぢょ:dyo
でゃ:dha	でぃ:dhi	でゅ:dhu	でぇ:dhe	でょ:dho
びゃ:bya	びぃ:byi	びゅ:byu	びぇ:bye	びょ:byo
ぴゃ:pya	ぴぃ:pyi	ぴゅ:pyu	ぴぇ:pye	ぴょ:pyo
"""

TABLES = {
  'en': EN,
  'ru': RU,
  'ko': KO,
  'th': TH,
  'ar': AR,
}

#def table(key):
#  """
#  @param  s  unicode
#  @return  {unicode key:unicode value} or None
#  """
#  return TABLES.get(key)

def parse(s):
  """
  @param  s  unicode
  @return  {unicode key:unicode value}
  """
  ret = {}
  for it in s.split():
    if it and it[0] != '#':
      k,v = it.split(':')
      ret[k] = v
  return ret

if __name__ == '__main__':
  for t in TABLES.itervalues():
    parse(t)

# EOF
