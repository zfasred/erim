--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

-- Started on 2025-09-01 12:16:31

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 5230 (class 0 OID 25662)
-- Dependencies: 247
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.auth_group (id, name) FROM stdin;
1	Firma Yönetici
2	Firma Personeli Yönetici
\.


--
-- TOC entry 5232 (class 0 OID 25670)
-- Dependencies: 249
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	65
2	1	33
3	1	34
4	1	35
5	1	36
6	1	66
7	1	67
8	1	68
9	2	128
10	2	125
11	2	126
12	2	127
\.


--
-- TOC entry 5228 (class 0 OID 25656)
-- Dependencies: 245
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add city	7	add_city
26	Can change city	7	change_city
27	Can delete city	7	delete_city
28	Can view city	7	view_city
29	Can add district	8	add_district
30	Can change district	8	change_district
31	Can delete district	8	delete_district
32	Can view district	8	view_district
33	Can add firm	9	add_firm
34	Can change firm	9	change_firm
35	Can delete firm	9	delete_firm
36	Can view firm	9	view_firm
37	Can add language	10	add_language
38	Can change language	10	change_language
39	Can delete language	10	delete_language
40	Can view language	10	view_language
41	Can add media	11	add_media
42	Can change media	11	change_media
43	Can delete media	11	delete_media
44	Can view media	11	view_media
45	Can add media type	12	add_mediatype
46	Can change media type	12	change_mediatype
47	Can delete media type	12	delete_mediatype
48	Can view media type	12	view_mediatype
49	Can add nace	13	add_nace
50	Can change nace	13	change_nace
51	Can delete nace	13	delete_nace
52	Can view nace	13	view_nace
53	Can add path	14	add_path
54	Can change path	14	change_path
55	Can delete path	14	delete_path
56	Can view path	14	view_path
57	Can add tax office	15	add_taxoffice
58	Can change tax office	15	change_taxoffice
59	Can delete tax office	15	delete_taxoffice
60	Can view tax office	15	view_taxoffice
61	Can add user	16	add_user
62	Can change user	16	change_user
63	Can delete user	16	delete_user
64	Can view user	16	view_user
65	Can add user firm	17	add_userfirm
66	Can change user firm	17	change_userfirm
67	Can delete user firm	17	delete_userfirm
68	Can view user firm	17	view_userfirm
69	Can add user group	18	add_usergroup
70	Can change user group	18	change_usergroup
71	Can delete user group	18	delete_usergroup
72	Can view user group	18	view_usergroup
73	Can add auth group	19	add_authgroup
74	Can change auth group	19	change_authgroup
75	Can delete auth group	19	delete_authgroup
76	Can view auth group	19	view_authgroup
77	Can add auth group permissions	20	add_authgrouppermissions
78	Can change auth group permissions	20	change_authgrouppermissions
79	Can delete auth group permissions	20	delete_authgrouppermissions
80	Can view auth group permissions	20	view_authgrouppermissions
81	Can add auth permission	21	add_authpermission
82	Can change auth permission	21	change_authpermission
83	Can delete auth permission	21	delete_authpermission
84	Can view auth permission	21	view_authpermission
85	Can add auth user	22	add_authuser
86	Can change auth user	22	change_authuser
87	Can delete auth user	22	delete_authuser
88	Can view auth user	22	view_authuser
89	Can add auth user groups	23	add_authusergroups
90	Can change auth user groups	23	change_authusergroups
91	Can delete auth user groups	23	delete_authusergroups
92	Can view auth user groups	23	view_authusergroups
93	Can add auth user user permissions	24	add_authuseruserpermissions
94	Can change auth user user permissions	24	change_authuseruserpermissions
95	Can delete auth user user permissions	24	delete_authuseruserpermissions
96	Can view auth user user permissions	24	view_authuseruserpermissions
97	Can add blood	25	add_blood
98	Can change blood	25	change_blood
99	Can delete blood	25	delete_blood
100	Can view blood	25	view_blood
101	Can add department	26	add_department
102	Can change department	26	change_department
103	Can delete department	26	delete_department
104	Can view department	26	view_department
105	Can add django admin log	27	add_djangoadminlog
106	Can change django admin log	27	change_djangoadminlog
107	Can delete django admin log	27	delete_djangoadminlog
108	Can view django admin log	27	view_djangoadminlog
109	Can add django content type	28	add_djangocontenttype
110	Can change django content type	28	change_djangocontenttype
111	Can delete django content type	28	delete_djangocontenttype
112	Can view django content type	28	view_djangocontenttype
113	Can add django migrations	29	add_djangomigrations
114	Can change django migrations	29	change_djangomigrations
115	Can delete django migrations	29	delete_djangomigrations
116	Can view django migrations	29	view_djangomigrations
117	Can add django session	30	add_djangosession
118	Can change django session	30	change_djangosession
119	Can delete django session	30	delete_djangosession
120	Can view django session	30	view_djangosession
121	Can add education	31	add_education
122	Can change education	31	change_education
123	Can delete education	31	delete_education
124	Can view education	31	view_education
125	Can add personnel	32	add_personnel
126	Can change personnel	32	change_personnel
127	Can delete personnel	32	delete_personnel
128	Can view personnel	32	view_personnel
129	Can add Emisyon Faktörü	33	add_emissionfactor
130	Can change Emisyon Faktörü	33	change_emissionfactor
131	Can delete Emisyon Faktörü	33	delete_emissionfactor
132	Can view Emisyon Faktörü	33	view_emissionfactor
133	Can add Katsayı Türü	34	add_coefficienttype
134	Can change Katsayı Türü	34	change_coefficienttype
135	Can delete Katsayı Türü	34	delete_coefficienttype
136	Can view Katsayı Türü	34	view_coefficienttype
137	Can add Girdi Kategorisi	35	add_inputcategory
138	Can change Girdi Kategorisi	35	change_inputcategory
139	Can delete Girdi Kategorisi	35	delete_inputcategory
140	Can view Girdi Kategorisi	35	view_inputcategory
141	Can add Karbon Girdi Verisi	36	add_inputdata
142	Can change Karbon Girdi Verisi	36	change_inputdata
143	Can delete Karbon Girdi Verisi	36	delete_inputdata
144	Can view Karbon Girdi Verisi	36	view_inputdata
145	Can add Karbon Raporu	37	add_report
146	Can change Karbon Raporu	37	change_report
147	Can delete Karbon Raporu	37	delete_report
148	Can view Karbon Raporu	37	view_report
149	Karbon Yönetim Görüntüleme Hakkı	33	view_management_carbon
150	Karbon Yönetim Görüntüleme Hakkı	34	view_management_carbon
151	Karbon Girdi Verisi Görüntüleme Hakkı	36	view_input_carbon
152	Karbon Rapor Görüntüleme Hakkı	37	view_report_carbon
153	Karbon için kullanıcı ve firma ilişkisi kurabilir	33	can_manage_user_firm_access
\.


--
-- TOC entry 5234 (class 0 OID 25676)
-- Dependencies: 251
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
10	pbkdf2_sha256$1000000$25SeOtNRNdjXGGjZRsT7Dl$WMFuaRgxsub5DkFThXk/3pjXCFovJP7rWjVBQUqGOTY=	\N	t	ekonaz	Ali	Bozdemir	bilgi@ekonaz.com.tr	t	t	2025-08-09 19:25:05+03
11	pbkdf2_sha256$1000000$3NCk6o0yqErMYlbuqRTcmm$wJzekY4emk4mnJ4b5sGkjDdJMtp6yDyMYww3tuceA34=	2025-08-31 12:40:30.011269+03	f	Muhasebeci				f	t	2025-08-29 15:26:38+03
9	pbkdf2_sha256$1000000$BZQkncOfqiqRpaV3fjEe8q$DhnJr4Nk9y333wdyaunNfN1b7/jgyd7084Snc2QqHrQ=	2025-08-31 12:40:42.654921+03	t	a				t	t	2025-08-09 10:23:23+03
\.


--
-- TOC entry 5236 (class 0 OID 25684)
-- Dependencies: 253
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
5	9	1
6	9	2
7	10	1
8	10	2
\.


--
-- TOC entry 5238 (class 0 OID 25690)
-- Dependencies: 255
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
257	10	1
258	10	2
259	10	3
260	10	4
261	10	5
262	10	6
263	10	7
264	10	8
265	10	9
266	10	10
267	10	11
268	10	12
269	10	13
270	10	14
271	10	15
272	10	16
273	10	17
274	10	18
275	10	19
276	10	20
277	10	21
278	10	22
279	10	23
280	10	24
281	10	25
282	10	26
283	10	27
284	10	28
285	10	29
286	10	30
287	10	31
288	10	32
289	10	33
290	10	34
291	10	35
292	10	36
293	10	37
294	10	38
295	10	39
296	10	40
297	10	41
298	10	42
299	10	43
300	10	44
301	10	45
302	10	46
303	10	47
304	10	48
305	10	49
306	10	50
307	10	51
308	10	52
309	10	53
310	10	54
311	10	55
312	10	56
313	10	57
314	10	58
315	10	59
316	10	60
317	10	61
318	10	62
319	10	63
320	10	64
321	10	65
322	10	66
323	10	67
324	10	68
325	10	69
326	10	70
327	10	71
328	10	72
329	10	73
330	10	74
331	10	75
332	10	76
333	10	77
334	10	78
335	10	79
336	10	80
337	10	81
338	10	82
339	10	83
340	10	84
341	10	85
342	10	86
343	10	87
344	10	88
345	10	89
346	10	90
347	10	91
348	10	92
349	10	93
350	10	94
351	10	95
352	10	96
353	10	97
354	10	98
355	10	99
356	10	100
357	10	101
358	10	102
359	10	103
360	10	104
361	10	105
362	10	106
363	10	107
364	10	108
365	10	109
366	10	110
367	10	111
368	10	112
369	10	113
370	10	114
371	10	115
372	10	116
373	10	117
374	10	118
375	10	119
376	10	120
377	10	121
378	10	122
379	10	123
380	10	124
381	10	125
382	10	126
383	10	127
384	10	128
129	9	1
130	9	2
131	9	3
132	9	4
133	9	5
134	9	6
135	9	7
136	9	8
137	9	9
138	9	10
139	9	11
140	9	12
141	9	13
142	9	14
143	9	15
144	9	16
145	9	17
146	9	18
147	9	19
148	9	20
149	9	21
150	9	22
151	9	23
152	9	24
153	9	25
154	9	26
155	9	27
156	9	28
157	9	29
158	9	30
159	9	31
160	9	32
161	9	33
162	9	34
163	9	35
164	9	36
165	9	37
166	9	38
167	9	39
168	9	40
169	9	41
170	9	42
171	9	43
172	9	44
173	9	45
174	9	46
175	9	47
176	9	48
177	9	49
178	9	50
179	9	51
180	9	52
181	9	53
182	9	54
183	9	55
184	9	56
185	9	57
186	9	58
187	9	59
188	9	60
189	9	61
190	9	62
191	9	63
192	9	64
193	9	65
194	9	66
195	9	67
196	9	68
197	9	69
198	9	70
199	9	71
200	9	72
201	9	73
202	9	74
203	9	75
204	9	76
205	9	77
206	9	78
207	9	79
208	9	80
209	9	81
210	9	82
211	9	83
212	9	84
213	9	85
214	9	86
215	9	87
216	9	88
217	9	89
218	9	90
219	9	91
220	9	92
221	9	93
222	9	94
223	9	95
224	9	96
225	9	97
226	9	98
227	9	99
228	9	100
229	9	101
230	9	102
231	9	103
232	9	104
233	9	105
234	9	106
235	9	107
236	9	108
237	9	109
238	9	110
239	9	111
240	9	112
241	9	113
242	9	114
243	9	115
244	9	116
245	9	117
246	9	118
247	9	119
248	9	120
249	9	121
250	9	122
251	9	123
252	9	124
253	9	125
254	9	126
255	9	127
256	9	128
385	10	129
386	10	130
387	10	131
388	10	132
389	10	133
390	10	134
391	10	135
392	10	136
393	10	137
394	10	138
395	10	139
396	10	140
397	10	141
398	10	142
399	10	143
400	10	144
401	10	145
402	10	146
403	10	147
404	10	148
405	10	149
406	10	150
407	10	151
408	10	152
409	9	129
410	9	130
411	9	131
412	9	132
413	9	133
414	9	134
415	9	135
416	9	136
417	9	137
418	9	138
419	9	139
420	9	140
421	9	141
422	9	142
423	9	143
424	9	144
425	9	145
426	9	146
427	9	147
428	9	148
429	9	149
430	9	150
431	9	151
432	9	152
436	11	129
437	11	130
438	11	131
439	11	132
440	11	133
441	11	134
442	11	135
443	11	136
444	11	137
445	11	138
446	11	139
447	11	140
448	11	141
449	11	142
450	11	143
451	11	144
452	11	145
453	11	146
454	11	147
455	11	148
456	11	149
457	11	150
458	11	151
459	11	152
\.


--
-- TOC entry 5245 (class 0 OID 33845)
-- Dependencies: 262
-- Data for Name: blood_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.blood_ (id, name_) FROM stdin;
1	0 Rh (-)
2	0 Rh (+)
3	A Rh (-)
4	A Rh (+)
5	B Rh (-)
6	B Rh (+)
7	AB Rh (-)
8	AB Rh (+)
\.


--
-- TOC entry 5253 (class 0 OID 42094)
-- Dependencies: 270
-- Data for Name: carbon_coefficienttype; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.carbon_coefficienttype (id, name, unit, description) FROM stdin;
1	Default Type	kgCO2/TJ	Geçici varsayılan katsayı türü
\.


--
-- TOC entry 5251 (class 0 OID 42088)
-- Dependencies: 268
-- Data for Name: carbon_emissionfactor; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.carbon_emissionfactor (id, name, category, value, valid_from, valid_to, source, type_id) FROM stdin;
2	Test Emisyon Faktör	KAPSAM_1	2.4	2023-04-23	2027-10-29	ESA	1
3	Üretimin dolaylı etkisi	KAPSAM_1	1.9	2020-01-01	2027-02-02	ESA	1
\.


--
-- TOC entry 5255 (class 0 OID 42102)
-- Dependencies: 272
-- Data for Name: carbon_inputcategory; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.carbon_inputcategory (id, name, scope) FROM stdin;
\.


--
-- TOC entry 5257 (class 0 OID 42114)
-- Dependencies: 274
-- Data for Name: carbon_inputdata; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.carbon_inputdata (id, value, unit, period_start, period_end, location, created_at, category_id, created_by_id, firm_id) FROM stdin;
\.


--
-- TOC entry 5259 (class 0 OID 42120)
-- Dependencies: 276
-- Data for Name: carbon_report; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.carbon_report (id, report_date, total_co2e, direct_ratio, indirect_ratio, json_details, generated_at, firm_id, generated_by_id) FROM stdin;
\.


--
-- TOC entry 5200 (class 0 OID 25464)
-- Dependencies: 217
-- Data for Name: city_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.city_ (id, name_) FROM stdin;
1	Adana
2	Adıyaman
3	Afyonkarahisar
4	Ağrı
5	Amasya
6	Ankara
7	Antalya
8	Artvin
9	Aydın
10	Balıkesir
11	Bilecik
12	Bingöl
13	Bitlis
14	Bolu
15	Burdur
16	Bursa
17	Çanakkale
18	Çankırı
19	Çorum
20	Denizli
21	Diyarbakır
22	Edirne
23	Elazığ
24	Erzincan
25	Erzurum
26	Eskişehir
27	Gaziantep
28	Giresun
29	Gümüşhane
30	Hakkari
31	Hatay
32	Isparta
33	Mersin
34	İstanbul
35	İzmir
36	Kars
37	Kastamonu
38	Kayseri
39	Kırklareli
40	Kırşehir
41	Kocaeli
42	Konya
43	Kütahya
44	Malatya
45	Manisa
46	Kahramanmaraş
47	Mardin
48	Muğla
49	Muş
50	Nevşehir
51	Niğde
52	Ordu
53	Rize
54	Sakarya
55	Samsun
56	Siirt
57	Sinop
58	Sivas
59	Tekirdağ
60	Tokat
61	Trabzon
62	Tunceli
63	Şanlıurfa
64	Uşak
65	Van
66	Yozgat
67	Zonguldak
68	Aksaray
69	Bayburt
70	Karaman
71	Kırıkkale
72	Batman
73	Şırnak
74	Bartın
75	Ardahan
76	Iğdır
77	Yalova
78	Karabük
79	Kilis
80	Osmaniye
81	Düzce
\.


--
-- TOC entry 5247 (class 0 OID 33857)
-- Dependencies: 264
-- Data for Name: department_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.department_ (id, firm_id, name_) FROM stdin;
1	3	Maliye
2	4	İnsan Kaynakları
3	4	ARGE Merkezi
\.


--
-- TOC entry 5202 (class 0 OID 25468)
-- Dependencies: 219
-- Data for Name: district_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.district_ (id, name_, city_id) FROM stdin;
1	ONDOKUZ MAYIS	55
2	ABANA	37
3	ACIGÖL	50
4	ACIPAYAM	20
5	ADAKLI	12
6	ADALAR	34
7	ADAPAZARI	54
8	ADİLCEVAZ	13
9	AFŞİN	46
10	AĞAÇÖREN	68
11	AĞIN	23
12	AĞLASUN	15
13	AĞLI	37
14	AHIRLI	42
15	AHLAT	13
16	AHMETLİ	45
17	AKÇAABAT	61
18	AKÇADAĞ	44
19	AKÇAKALE	63
20	AKÇAKENT	40
21	AKÇAKOCA	81
22	AKDAĞMADENİ	66
23	AKDENİZ	33
24	AKHİSAR	45
25	AKINCILAR	58
26	AKKIŞLA	38
27	AKKUŞ	52
28	AKÖREN	42
29	AKPINAR	40
30	AKSEKİ	7
31	AKSU	7
32	AKSU	32
33	AKŞEHİR	42
34	AKYAKA	36
35	AKYAZI	54
36	AKYURT	6
37	ALACA	19
38	ALACAKAYA	23
39	ALAÇAM	55
40	ALADAĞ	1
41	ALANYA	7
42	ALAPLI	67
43	ALAŞEHİR	45
44	ALİAĞA	35
45	ALMUS	60
46	ALPU	26
47	ALTIEYLÜL	10
48	ALTINDAĞ	6
49	ALTINEKİN	42
50	ALTINORDU	52
51	ALTINOVA	77
52	ALTINÖZÜ	31
53	ALTINTAŞ	43
54	ALTINYAYLA	15
55	ALTINYAYLA	58
56	ALTUNHİSAR	51
57	ALUCRA	28
58	AMASRA	74
59	ANAMUR	33
60	ANDIRIN	46
61	ANTAKYA	31
62	ARABAN	27
63	ARAÇ	37
64	ARAKLI	61
65	ARALIK	76
66	ARAPGİR	44
67	ARDANUÇ	8
68	ARDEŞEN	53
69	ARGUVAN	44
70	ARHAVİ	8
71	ARICAK	23
72	ARİFİYE	54
73	ARMUTLU	77
74	ARNAVUTKÖY	34
75	ARPAÇAY	36
76	ARSİN	61
77	ARSUZ	31
78	ARTOVA	60
79	ARTUKLU	47
80	ASARCIK	55
81	ASLANAPA	43
82	AŞKALE	25
83	ATABEY	32
84	ATAKUM	55
85	ATAŞEHİR	34
86	ATKARACALAR	18
87	AVANOS	50
88	AVCILAR	34
89	AYANCIK	57
90	AYAŞ	6
91	AYBASTI	52
92	AYDINCIK	33
93	AYDINCIK	66
94	AYDINTEPE	69
95	AYRANCI	70
96	AYVACIK	17
97	AYVACIK	55
98	AYVALIK	10
99	AZDAVAY	37
100	AZİZİYE	25
101	BABADAĞ	20
102	BABAESKİ	39
103	BAFRA	55
104	BAĞCILAR	34
105	BAĞLAR	21
106	BAHÇE	80
107	BAHÇELİEVLER	34
108	BAHÇESARAY	65
109	BAHŞİLİ	71
110	BAKIRKÖY	34
111	BAKLAN	20
112	BALA	6
113	BALÇOVA	35
114	BALIŞEYH	71
115	BALYA	10
116	BANAZ	64
117	BANDIRMA	10
118	BASKİL	23
119	BAŞAKŞEHİR	34
120	BAŞÇİFTLİK	60
121	BAŞİSKELE	41
122	BAŞKALE	65
123	BAŞMAKÇI	3
124	BAŞYAYLA	70
125	BATTALGAZİ	44
126	BAYAT	3
127	BAYAT	19
128	BAYINDIR	35
129	BAYKAN	56
130	BAYRAKLI	35
131	BAYRAMİÇ	17
132	BAYRAMÖREN	18
133	BAYRAMPAŞA	34
134	BEKİLLİ	20
135	BELEN	31
136	BERGAMA	35
137	BESNİ	2
138	BEŞİKDÜZÜ	61
139	BEŞİKTAŞ	34
140	BEŞİRİ	72
141	BEYAĞAÇ	20
142	BEYDAĞ	35
143	BEYKOZ	34
144	BEYLİKDÜZÜ	34
145	BEYLİKOVA	26
146	BEYOĞLU	34
147	BEYPAZARI	6
148	BEYŞEHİR	42
149	BEYTÜŞŞEBAP	73
150	BİGA	17
151	BİGADİÇ	10
152	BİRECİK	63
153	BİSMİL	21
154	BODRUM	48
155	BOĞAZKALE	19
156	BOĞAZLIYAN	66
157	BOLVADİN	3
158	BOR	51
159	BORÇKA	8
160	BORNOVA	35
161	BOYABAT	57
162	BOZCAADA	17
163	BOZDOĞAN	9
164	BOZKIR	42
165	BOZKURT	20
166	BOZKURT	37
167	BOZOVA	63
168	BOZTEPE	40
169	BOZÜYÜK	11
170	BOZYAZI	33
171	BUCA	35
172	BUCAK	15
173	BUHARKENT	9
174	BULANCAK	28
175	BULANIK	49
176	BULDAN	20
177	BURHANİYE	10
178	BÜNYAN	38
179	BÜYÜKÇEKMECE	34
180	BÜYÜKORHAN	16
181	CANİK	55
182	CEYHAN	1
183	CEYLANPINAR	63
184	CİDE	37
185	CİHANBEYLİ	42
186	CİZRE	73
187	CUMAYERİ	81
188	ÇAĞLAYANCERİT	46
189	ÇAL	20
190	ÇALDIRAN	65
191	ÇAMARDI	51
192	ÇAMAŞ	52
193	ÇAMELİ	20
194	ÇAMLIDERE	6
195	ÇAMLIHEMŞİN	53
196	ÇAMLIYAYLA	33
197	ÇAMOLUK	28
198	ÇAN	17
199	ÇANAKÇI	28
200	ÇANDIR	66
201	ÇANKAYA	6
202	ÇARDAK	20
203	ÇARŞAMBA	55
204	ÇARŞIBAŞI	61
205	ÇAT	25
206	ÇATAK	65
207	ÇATALCA	34
208	ÇATALPINAR	52
209	ÇATALZEYTİN	37
210	ÇAVDARHİSAR	43
211	ÇAVDIR	15
212	ÇAY	3
213	ÇAYBAŞI	52
214	ÇAYCUMA	67
215	ÇAYELİ	53
216	ÇAYIRALAN	66
217	ÇAYIRLI	24
218	ÇAYIROVA	41
219	ÇAYKARA	61
220	ÇEKEREK	66
221	ÇEKMEKÖY	34
222	ÇELEBİ	71
223	ÇELİKHAN	2
224	ÇELTİK	42
225	ÇELTİKÇİ	15
226	ÇEMİŞGEZEK	62
227	ÇERKEŞ	18
228	ÇERKEZKÖY	59
229	ÇERMİK	21
230	ÇEŞME	35
231	ÇILDIR	75
232	ÇINAR	21
233	ÇINARCIK	77
234	ÇİÇEKDAĞI	40
235	ÇİFTELER	26
236	ÇİFTLİK	51
237	ÇİFTLİKKÖY	77
238	ÇİĞLİ	35
239	ÇİLİMLİ	81
240	ÇİNE	9
241	ÇİVRİL	20
242	ÇOBANLAR	3
243	ÇORLU	59
244	ÇUBUK	6
245	ÇUKURCA	30
246	ÇUKUROVA	1
247	ÇUMRA	42
248	ÇÜNGÜŞ	21
249	DADAY	37
250	DALAMAN	48
251	DAMAL	75
252	DARENDE	44
253	DARGEÇİT	47
254	DARICA	41
255	DATÇA	48
256	DAZKIRI	3
257	DEFNE	31
258	DELİCE	71
259	DEMİRCİ	45
260	DEMİRKÖY	39
261	DEMİRÖZÜ	69
262	DEMRE	7
263	DERBENT	42
264	DEREBUCAK	42
265	DERELİ	28
266	DEREPAZARI	53
267	DERİK	47
268	DERİNCE	41
269	DERİNKUYU	50
270	DERNEKPAZARI	61
271	DEVELİ	38
272	DEVREK	67
273	DEVREKANİ	37
274	DİCLE	21
275	DİDİM	9
276	DİGOR	36
277	DİKİLİ	35
278	DİKMEN	57
279	DİLOVASI	41
280	DİNAR	3
281	DİVRİĞİ	58
282	DİYADİN	4
283	DODURGA	19
284	DOĞANHİSAR	42
285	DOĞANKENT	28
286	DOĞANŞAR	58
287	DOĞANŞEHİR	44
288	DOĞANYOL	44
289	DOĞANYURT	37
290	DOĞUBEYAZIT	4
291	DOMANİÇ	43
292	DÖRTDİVAN	14
293	DÖRTYOL	31
294	DÖŞEMEALTI	7
295	DULKADİROĞLU	46
296	DUMLUPINAR	43
297	DURAĞAN	57
298	DURSUNBEY	10
299	DÜZİÇİ	80
300	DÜZKÖY	61
301	ECEABAT	17
302	EDREMİT	10
303	EDREMİT	65
304	EFELER	9
305	EFLANİ	78
306	EĞİL	21
307	EĞİRDİR	32
308	EKİNÖZÜ	46
309	ELBEYLİ	79
310	ELBİSTAN	46
311	ELDİVAN	18
312	ELEŞKİRT	4
313	ELMADAĞ	6
314	ELMALI	7
315	EMET	43
316	EMİRDAĞ	3
317	EMİRGAZİ	42
318	ENEZ	22
319	ERBAA	60
320	ERCİŞ	65
321	ERDEK	10
322	ERDEMLİ	33
323	EREĞLİ	42
324	EREĞLİ	67
325	ERENLER	54
326	ERFELEK	57
327	ERGANİ	21
328	ERGENE	59
329	ERMENEK	70
330	ERUH	56
331	ERZİN	31
332	ESENLER	34
333	ESENYURT	34
334	ESKİL	68
335	ESKİPAZAR	78
336	ESPİYE	28
337	EŞME	64
338	ETİMESGUT	6
339	EVCİLER	3
340	EVREN	6
341	EYNESİL	28
342	EYÜP	34
343	EYYÜBİYE	63
344	EZİNE	17
345	FATİH	34
346	FATSA	52
347	FEKE	1
348	FELAHİYE	38
349	FERİZLİ	54
350	FETHİYE	48
351	FINDIKLI	53
352	FİNİKE	7
353	FOÇA	35
354	GAZİEMİR	35
355	GAZİOSMANPAŞA	34
356	GAZİPAŞA	7
357	GEBZE	41
358	GEDİZ	43
359	GELENDOST	32
360	GELİBOLU	17
361	GEMEREK	58
362	GEMLİK	16
363	GENÇ	12
364	GERCÜŞ	72
365	GEREDE	14
366	GERGER	2
367	GERMENCİK	9
368	GERZE	57
369	GEVAŞ	65
370	GEYVE	54
371	GÖKÇEADA	17
372	GÖKÇEBEY	67
373	GÖKSUN	46
374	GÖLBAŞI	2
375	GÖLBAŞI	6
376	GÖLCÜK	41
377	GÖLE	75
378	GÖLHİSAR	15
379	GÖLKÖY	52
380	GÖLMARMARA	45
381	GÖLOVA	58
382	GÖLPAZARI	11
383	GÖLYAKA	81
384	GÖMEÇ	10
385	GÖNEN	10
386	GÖNEN	32
387	GÖRDES	45
388	GÖRELE	28
389	GÖYNÜCEK	5
390	GÖYNÜK	14
391	GÜCE	28
392	GÜÇLÜKONAK	73
393	GÜDÜL	6
394	GÜLAĞAÇ	68
395	GÜLNAR	33
396	GÜLŞEHİR	50
397	GÜLYALI	52
398	GÜMÜŞHACIKÖY	5
399	GÜMÜŞOVA	81
400	GÜNDOĞMUŞ	7
401	GÜNEY	20
402	GÜNEYSINIR	42
403	GÜNEYSU	53
404	GÜNGÖREN	34
405	GÜNYÜZÜ	26
406	GÜRGENTEPE	52
407	GÜROYMAK	13
408	GÜRPINAR	65
409	GÜRSU	16
410	GÜRÜN	58
411	GÜZELBAHÇE	35
412	GÜZELYURT	68
413	HACIBEKTAŞ	50
414	HACILAR	38
415	HADİM	42
416	HAFİK	58
417	HALFETİ	63
418	HALİLİYE	63
419	HALKAPINAR	42
420	HAMAMÖZÜ	5
421	HAMUR	4
422	HAN	26
423	HANAK	75
424	HANİ	21
425	HANÖNÜ	37
426	HARMANCIK	16
427	HARRAN	63
428	HASANBEYLİ	80
429	HASANKEYF	72
430	HASKÖY	49
431	HASSA	31
432	HAVRAN	10
433	HAVSA	22
434	HAVZA	55
435	HAYMANA	6
436	HAYRABOLU	59
437	HAYRAT	61
438	HAZRO	21
439	HEKİMHAN	44
440	HEMŞİN	53
441	HENDEK	54
442	HINIS	25
443	HİLVAN	63
444	HİSARCIK	43
445	HİZAN	13
446	HOCALAR	3
447	HONAZ	20
448	HOPA	8
449	HORASAN	25
450	HOZAT	62
451	HÜYÜK	42
452	ILGAZ	18
453	ILGIN	42
454	İBRADI	7
455	İDİL	73
456	İHSANGAZİ	37
457	İHSANİYE	3
458	İKİZCE	52
459	İKİZDERE	53
460	İLİÇ	24
461	İLKADIM	55
462	İMAMOĞLU	1
463	İMRANLI	58
464	İNCESU	38
465	İNCİRLİOVA	9
466	İNEBOLU	37
467	İNEGÖL	16
468	İNHİSAR	11
469	İNÖNÜ	26
470	İPEKYOLU	65
471	İPSALA	22
472	İSCEHİSAR	3
473	İSKENDERUN	31
474	İSKİLİP	19
475	İSLAHİYE	27
476	İSPİR	25
477	İVRİNDİ	10
478	İYİDERE	53
479	İZMİT	41
480	İZNİK	16
481	KABADÜZ	52
482	KABATAŞ	52
483	KADIKÖY	34
484	KADINHANI	42
485	KADIŞEHRİ	66
486	KADİRLİ	80
487	KAĞITHANE	34
488	KAĞIZMAN	36
489	KAHRAMANKAZAN	6
490	KAHTA	2
491	KALE	20
492	KALE	44
493	KALECİK	6
494	KALKANDERE	53
495	KAMAN	40
496	KANDIRA	41
497	KANGAL	58
498	KAPAKLI	59
499	KARABAĞLAR	35
500	KARABURUN	35
501	KARACABEY	16
502	KARACASU	9
503	KARAÇOBAN	25
504	KARAHALLI	64
505	KARAİSALI	1
506	KARAKEÇİLİ	71
507	KARAKOÇAN	23
508	KARAKOYUNLU	76
509	KARAKÖPRÜ	63
510	KARAMANLI	15
511	KARAMÜRSEL	41
512	KARAPINAR	42
513	KARAPÜRÇEK	54
514	KARASU	54
515	KARATAŞ	1
516	KARATAY	42
517	KARAYAZI	25
518	KARESİ	10
519	KARGI	19
520	KARKAMIŞ	27
521	KARLIOVA	12
522	KARPUZLU	9
523	KARŞIYAKA	35
524	KARTAL	34
525	KARTEPE	41
526	KAŞ	7
527	KAVAK	55
528	KAVAKLIDERE	48
529	KAYAPINAR	21
530	KAYNARCA	54
531	KAYNAŞLI	81
532	KAZIMKARABEKİR	70
533	KEBAN	23
534	KEÇİBORLU	32
535	KEÇİÖREN	6
536	KELES	16
537	KELKİT	29
538	KEMAH	24
539	KEMALİYE	24
540	KEMALPAŞA	35
541	KEMER	7
542	KEMER	15
543	KEPEZ	7
544	KEPSUT	10
545	KESKİN	71
546	KESTEL	16
547	KEŞAN	22
548	KEŞAP	28
549	KIBRISCIK	14
550	KINIK	35
551	KIRIKHAN	31
552	KIRKAĞAÇ	45
553	KIZILCAHAMAM	6
554	KIZILIRMAK	18
555	KIZILÖREN	3
556	KIZILTEPE	47
557	KİĞI	12
558	KİLİMLİ	67
559	KİRAZ	35
560	KOCAALİ	54
561	KOCAKÖY	21
562	KOCASİNAN	38
563	KOÇARLI	9
564	KOFÇAZ	39
565	KONAK	35
566	KONYAALTI	7
567	KORGAN	52
568	KORGUN	18
569	KORKUT	49
570	KORKUTELİ	7
571	KOVANCILAR	23
572	KOYULHİSAR	58
573	KOZAKLI	50
574	KOZAN	1
575	KOZLU	67
576	KOZLUK	72
577	KÖPRÜBAŞI	45
578	KÖPRÜBAŞI	61
579	KÖPRÜKÖY	25
580	KÖRFEZ	41
581	KÖSE	29
582	KÖŞK	9
583	KÖYCEĞİZ	48
584	KULA	45
585	KULP	21
586	KULU	42
587	KULUNCAK	44
588	KUMLU	31
589	KUMLUCA	7
590	KUMRU	52
591	KURŞUNLU	18
592	KURTALAN	56
593	KURUCAŞİLE	74
594	KUŞADASI	9
595	KUYUCAK	9
596	KÜÇÜKÇEKMECE	34
597	KÜRE	37
598	KÜRTÜN	29
599	LAÇİN	19
600	LADİK	55
601	LALAPAŞA	22
602	LAPSEKİ	17
603	LİCE	21
604	LÜLEBURGAZ	39
605	MAÇKA	61
606	MADEN	23
607	MAHMUDİYE	26
608	MALAZGİRT	49
609	MALKARA	59
610	MALTEPE	34
611	MAMAK	6
612	MANAVGAT	7
613	MANYAS	10
614	MARMARA	10
615	MARMARAEREĞLİSİ	59
616	MARMARİS	48
617	MAZGİRT	62
618	MAZIDAĞI	47
619	MECİTÖZÜ	19
620	MELİKGAZİ	38
621	MENDERES	35
622	MENEMEN	35
623	MENGEN	14
624	MENTEŞE	48
625	MERAM	42
626	MERİÇ	22
627	MERKEZ	2
628	MERKEZ	3
629	MERKEZ	4
630	MERKEZ	5
631	MERKEZ	8
632	MERKEZ	11
633	MERKEZ	12
634	MERKEZ	13
635	MERKEZ	14
636	MERKEZ	15
637	MERKEZ	17
638	MERKEZ	18
639	MERKEZ	19
640	MERKEZ	22
641	MERKEZ	23
642	MERKEZ	24
643	MERKEZ	28
644	MERKEZ	29
645	MERKEZ	30
646	MERKEZ	32
647	MERKEZ	36
648	MERKEZ	37
649	MERKEZ	39
650	MERKEZ	40
651	MERKEZ	43
652	MERKEZ	49
653	MERKEZ	50
654	MERKEZ	51
655	MERKEZ	53
656	MERKEZ	56
657	MERKEZ	57
658	MERKEZ	58
659	MERKEZ	60
660	MERKEZ	62
661	MERKEZ	64
662	MERKEZ	66
663	MERKEZ	67
664	MERKEZ	68
665	MERKEZ	69
666	MERKEZ	70
667	MERKEZ	71
668	MERKEZ	72
669	MERKEZ	73
670	MERKEZ	74
671	MERKEZ	75
672	MERKEZ	76
673	MERKEZ	77
674	MERKEZ	78
675	MERKEZ	79
676	MERKEZ	80
677	MERKEZ	81
678	MERKEZEFENDİ	20
679	MERZİFON	5
680	MESUDİYE	52
681	MEZİTLİ	33
682	MİDYAT	47
683	MİHALGAZİ	26
684	MİHALIÇÇIK	26
685	MİLAS	48
686	MUCUR	40
687	MUDANYA	16
688	MUDURNU	14
689	MURADİYE	65
690	MURATLI	59
691	MURATPAŞA	7
692	MURGUL	8
693	MUSABEYLİ	79
694	MUSTAFAKEMALPAŞA	16
695	MUT	33
696	MUTKİ	13
697	NALLIHAN	6
698	NARLIDERE	35
699	NARMAN	25
700	NAZIMİYE	62
701	NAZİLLİ	9
702	NİKSAR	60
703	NİLÜFER	16
704	NİZİP	27
705	NURDAĞI	27
706	NURHAK	46
707	NUSAYBİN	47
708	ODUNPAZARI	26
709	OF	61
710	OĞUZELİ	27
711	OĞUZLAR	19
712	OLTU	25
713	OLUR	25
714	ONİKİŞUBAT	46
715	ORHANELİ	16
716	ORHANGAZİ	16
717	ORTA	18
718	ORTACA	48
719	ORTAHİSAR	61
720	ORTAKÖY	19
721	ORTAKÖY	68
722	OSMANCIK	19
723	OSMANELİ	11
724	OSMANGAZİ	16
725	OTLUKBELİ	24
726	OVACIK	62
727	OVACIK	78
728	ÖDEMİŞ	35
729	ÖMERLİ	47
730	ÖZALP	65
731	ÖZVATAN	38
732	PALANDÖKEN	25
733	PALU	23
734	PAMUKKALE	20
735	PAMUKOVA	54
736	PASİNLER	25
737	PATNOS	4
738	PAYAS	31
739	PAZAR	53
740	PAZAR	60
741	PAZARCIK	46
742	PAZARLAR	43
743	PAZARYERİ	11
744	PAZARYOLU	25
745	PEHLİVANKÖY	39
746	PENDİK	34
747	PERŞEMBE	52
748	PERTEK	62
749	PERVARİ	56
750	PINARBAŞI	37
751	PINARBAŞI	38
752	PINARHİSAR	39
753	PİRAZİZ	28
754	POLATELİ	79
755	POLATLI	6
756	POSOF	75
757	POZANTI	1
758	PURSAKLAR	6
759	PÜLÜMÜR	62
760	PÜTÜRGE	44
761	REFAHİYE	24
762	REŞADİYE	60
763	REYHANLI	31
764	SAFRANBOLU	78
765	SAİMBEYLİ	1
766	SALIPAZARI	55
767	SALİHLİ	45
768	SAMANDAĞ	31
769	SAMSAT	2
770	SANCAKTEPE	34
771	SANDIKLI	3
772	SAPANCA	54
773	SARAY	59
774	SARAY	65
775	SARAYDÜZÜ	57
776	SARAYKENT	66
777	SARAYKÖY	20
778	SARAYÖNÜ	42
779	SARICAKAYA	26
780	SARIÇAM	1
781	SARIGÖL	45
782	SARIKAMIŞ	36
783	SARIKAYA	66
784	SARIOĞLAN	38
785	SARIVELİLER	70
786	SARIYAHŞİ	68
787	SARIYER	34
788	SARIZ	38
789	SARUHANLI	45
790	SASON	72
791	SAVAŞTEPE	10
792	SAVUR	47
793	SEBEN	14
794	SEFERİHİSAR	35
795	SELÇUK	35
796	SELÇUKLU	42
797	SELENDİ	45
798	SELİM	36
799	SENİRKENT	32
800	SERDİVAN	54
801	SERİK	7
802	SERİNHİSAR	20
803	SEYDİKEMER	48
804	SEYDİLER	37
805	SEYDİŞEHİR	42
806	SEYHAN	1
807	SEYİTGAZİ	26
808	SINDIRGI	10
809	SİLİFKE	33
810	SİLİVRİ	34
811	SİLOPİ	73
812	SİLVAN	21
813	SİMAV	43
814	SİNANPAŞA	3
815	SİNCAN	6
816	SİNCİK	2
817	SİVASLI	64
818	SİVEREK	63
819	SİVRİCE	23
820	SİVRİHİSAR	26
821	SOLHAN	12
822	SOMA	45
823	SORGUN	66
824	SÖĞÜT	11
825	SÖĞÜTLÜ	54
826	SÖKE	9
827	SULAKYURT	71
828	SULTANBEYLİ	34
829	SULTANDAĞI	3
830	SULTANGAZİ	34
831	SULTANHİSAR	9
832	SULUOVA	5
833	SULUSARAY	60
834	SUMBAS	80
835	SUNGURLU	19
836	SUR	21
837	SURUÇ	63
838	SUSURLUK	10
839	SUSUZ	36
840	SUŞEHRİ	58
841	SÜLEYMANPAŞA	59
842	SÜLOĞLU	22
843	SÜRMENE	61
844	SÜTÇÜLER	32
845	ŞABANÖZÜ	18
846	ŞAHİNBEY	27
847	ŞALPAZARI	61
848	ŞAPHANE	43
849	ŞARKIŞLA	58
850	ŞARKİKARAAĞAÇ	32
851	ŞARKÖY	59
852	ŞAVŞAT	8
853	ŞEBİNKARAHİSAR	28
854	ŞEFAATLİ	66
855	ŞEHİTKAMİL	27
856	ŞEHZADELER	45
857	ŞEMDİNLİ	30
858	ŞENKAYA	25
859	ŞENPAZAR	37
860	ŞEREFLİKOÇHİSAR	6
861	ŞİLE	34
862	ŞİRAN	29
863	ŞİRVAN	56
864	ŞİŞLİ	34
865	ŞUHUT	3
866	TALAS	38
867	TARAKLI	54
868	TARSUS	33
869	TAŞKENT	42
870	TAŞKÖPRÜ	37
871	TAŞLIÇAY	4
872	TAŞOVA	5
873	TATVAN	13
874	TAVAS	20
875	TAVŞANLI	43
876	TEFENNİ	15
877	TEKKEKÖY	55
878	TEKMAN	25
879	TEPEBAŞI	26
880	TERCAN	24
881	TERMAL	77
882	TERME	55
883	TİLLO	56
884	TİRE	35
885	TİREBOLU	28
886	TOMARZA	38
887	TONYA	61
888	TOPRAKKALE	80
889	TORBALI	35
890	TOROSLAR	33
891	TORTUM	25
892	TORUL	29
893	TOSYA	37
894	TUFANBEYLİ	1
895	TURGUTLU	45
896	TURHAL	60
897	TUŞBA	65
898	TUT	2
899	TUTAK	4
900	TUZLA	34
901	TUZLUCA	76
902	TUZLUKÇU	42
903	TÜRKELİ	57
904	TÜRKOĞLU	46
905	UĞURLUDAĞ	19
906	ULA	48
907	ULAŞ	58
908	ULUBEY	52
909	ULUBEY	64
910	ULUBORLU	32
911	ULUDERE	73
912	ULUKIŞLA	51
913	ULUS	74
914	URLA	35
915	UZUNDERE	25
916	UZUNKÖPRÜ	22
917	ÜMRANİYE	34
918	ÜNYE	52
919	ÜRGÜP	50
920	ÜSKÜDAR	34
921	ÜZÜMLÜ	24
922	VAKFIKEBİR	61
923	VARTO	49
924	VEZİRKÖPRÜ	55
925	VİRANŞEHİR	63
926	VİZE	39
927	YAĞLIDERE	28
928	YAHŞİHAN	71
929	YAHYALI	38
930	YAKAKENT	55
931	YAKUTİYE	25
932	YALIHÜYÜK	42
933	YALVAÇ	32
934	YAPRAKLI	18
935	YATAĞAN	48
936	YAVUZELİ	27
937	YAYLADAĞI	31
938	YAYLADERE	12
939	YAZIHAN	44
940	YEDİSU	12
941	YENİCE	17
942	YENİCE	78
943	YENİÇAĞA	14
944	YENİFAKILI	66
945	YENİMAHALLE	6
946	YENİPAZAR	9
947	YENİPAZAR	11
948	YENİŞARBADEMLİ	32
949	YENİŞEHİR	16
950	YENİŞEHİR	21
951	YENİŞEHİR	33
952	YERKÖY	66
953	YEŞİLHİSAR	38
954	YEŞİLLİ	47
955	YEŞİLOVA	15
956	YEŞİLYURT	44
957	YEŞİLYURT	60
958	YIĞILCA	81
959	YILDIRIM	16
960	YILDIZELİ	58
961	YOMRA	61
962	YUMURTALIK	1
963	YUNAK	42
964	YUNUSEMRE	45
965	YUSUFELİ	8
966	YÜKSEKOVA	30
967	YÜREĞİR	1
968	ZARA	58
969	ZEYTİNBURNU	34
970	ZİLE	60
1001	MERKEZ	1
1006	MERKEZ	6
1007	MERKEZ	7
1009	MERKEZ	9
1010	MERKEZ	10
1016	MERKEZ	16
1020	MERKEZ	20
1021	MERKEZ	21
1025	MERKEZ	25
1026	MERKEZ	26
1027	MERKEZ	27
1031	MERKEZ	31
1033	MERKEZ	33
1034	MERKEZ	34
1035	MERKEZ	35
1038	MERKEZ	38
1041	MERKEZ	41
1042	MERKEZ	42
1043	MERKEZ	43
1044	MERKEZ	44
1045	MERKEZ	45
1046	MERKEZ	46
1047	MERKEZ	47
1048	MERKEZ	48
1052	MERKEZ	52
1054	MERKEZ	54
1055	MERKEZ	55
1059	MERKEZ	59
1061	MERKEZ	61
1063	MERKEZ	63
1065	MERKEZ	65
1071	MERKEZ	71
\.


--
-- TOC entry 5240 (class 0 OID 25748)
-- Dependencies: 257
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
19	2025-08-09 19:17:57.609271+03	1	ekonaz	3		4	9
20	2025-08-09 19:25:48.428536+03	10	ekonaz	2	[{"changed": {"fields": ["First name", "Last name", "Staff status", "Superuser status", "Groups", "User permissions"]}}]	4	9
21	2025-08-27 22:44:27.645049+03	10	ekonaz	2	[{"changed": {"fields": ["User permissions"]}}]	4	9
22	2025-08-27 22:44:39.943875+03	9	a	2	[{"changed": {"fields": ["User permissions"]}}]	4	9
23	2025-08-28 20:27:35.173752+03	9	a	2	[{"changed": {"fields": ["User permissions"]}}]	4	9
24	2025-08-28 21:11:21.268816+03	10	ekonaz	2	[{"changed": {"fields": ["User permissions"]}}]	4	9
25	2025-08-28 22:04:23.034965+03	9	a	2	[{"changed": {"fields": ["User permissions"]}}]	4	9
26	2025-08-29 15:08:11.528422+03	9	a	2	[{"changed": {"fields": ["User permissions"]}}]	4	9
27	2025-08-29 15:09:09.061249+03	9	a	2	[{"changed": {"fields": ["User permissions"]}}]	4	9
28	2025-08-29 15:09:19.076693+03	10	ekonaz	2	[{"changed": {"fields": ["User permissions"]}}]	4	9
29	2025-08-29 15:28:36.208628+03	11	test	2	[{"changed": {"fields": ["User permissions"]}}]	4	9
\.


--
-- TOC entry 5226 (class 0 OID 25648)
-- Dependencies: 243
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	core	city
8	core	district
9	core	firm
10	core	language
11	core	media
12	core	mediatype
13	core	nace
14	core	path
15	core	taxoffice
16	core	user
17	core	userfirm
18	core	usergroup
19	core	authgroup
20	core	authgrouppermissions
21	core	authpermission
22	core	authuser
23	core	authusergroups
24	core	authuseruserpermissions
25	core	blood
26	core	department
27	core	djangoadminlog
28	core	djangocontenttype
29	core	djangomigrations
30	core	djangosession
31	core	education
32	core	personnel
33	carbon	emissionfactor
34	carbon	coefficienttype
35	carbon	inputcategory
36	carbon	inputdata
37	carbon	report
\.


--
-- TOC entry 5224 (class 0 OID 25640)
-- Dependencies: 241
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
69	contenttypes	0001_initial	2025-08-08 23:14:51.857096+03
70	auth	0001_initial	2025-08-08 23:14:51.865981+03
71	admin	0001_initial	2025-08-08 23:14:51.865981+03
72	admin	0002_logentry_remove_auto_add	2025-08-08 23:14:51.865981+03
73	admin	0003_logentry_add_action_flag_choices	2025-08-08 23:14:51.865981+03
74	contenttypes	0002_remove_content_type_name	2025-08-08 23:14:51.865981+03
75	auth	0002_alter_permission_name_max_length	2025-08-08 23:14:51.869776+03
76	auth	0003_alter_user_email_max_length	2025-08-08 23:14:51.869776+03
77	auth	0004_alter_user_username_opts	2025-08-08 23:14:51.869776+03
78	auth	0005_alter_user_last_login_null	2025-08-08 23:14:51.869776+03
79	auth	0006_require_contenttypes_0002	2025-08-08 23:14:51.869776+03
80	auth	0007_alter_validators_add_error_messages	2025-08-08 23:14:51.874296+03
81	auth	0008_alter_user_username_max_length	2025-08-08 23:14:51.875815+03
82	auth	0009_alter_user_last_name_max_length	2025-08-08 23:14:51.876608+03
83	auth	0010_alter_group_name_max_length	2025-08-08 23:14:51.876608+03
84	auth	0011_update_proxy_permissions	2025-08-08 23:14:51.876608+03
85	auth	0012_alter_user_first_name_max_length	2025-08-08 23:14:51.878693+03
86	core	0001_initial	2025-08-08 23:14:51.878693+03
87	sessions	0001_initial	2025-08-08 23:14:51.878693+03
88	carbon	0001_initial	2025-08-27 17:28:32.864128+03
89	carbon	0002_coefficienttype_inputcategory_and_more	2025-08-27 17:28:32.924436+03
90	carbon	0003_alter_emissionfactor_type	2025-08-27 17:30:59.585254+03
91	carbon	0004_alter_coefficienttype_options_and_more	2025-08-27 20:17:59.946751+03
92	carbon	0005_alter_emissionfactor_options	2025-08-28 20:12:03.722386+03
\.


--
-- TOC entry 5241 (class 0 OID 25776)
-- Dependencies: 258
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: mydbuser
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
cgujftek4k3tp4sm4jlvo4wruqisfzom	.eJxVjMsOwiAURP-FtSHyBpfu-w3kci9K1UBS2pXx36VJF5rMas6ZebMI21ri1vMSZ2IXJtjpt0uAz1x3QA-o98ax1XWZE98VftDOp0b5dT3cv4MCvYw1CCN8tsGlkBKM2KAyGufOOAih9tYoLxVI0uIGQmkyJsmMypD2IbDPF-R2N6E:1udRH6:N7G5D0kwJorj34F5c2rroCnIHy7i_cYv169aOo0yK-k	2025-08-03 13:28:08.367264+03
py67f9crma7nk01shu37lg72c5sasy9t	.eJxVjMsOwiAURP-FtSHyBpfu-w3kci9K1UBS2pXx36VJF5rMas6ZebMI21ri1vMSZ2IXJtjpt0uAz1x3QA-o98ax1XWZE98VftDOp0b5dT3cv4MCvYw1CCN8tsGlkBKM2KAyGufOOAih9tYoLxVI0uIGQmkyJsmMypD2IbDPF-R2N6E:1uhjqs:9LoeRn5V25FDLlwL4OH8cHWm8p5BxUF9VLWX1R43-Ww	2026-08-01 10:06:50.336713+03
376l9a118ur83wr63vioiuv81aync234	.eJxVjMsOwiAURP-FtSHyBpfu-w3kci9K1UBS2pXx36VJF5rMas6ZebMI21ri1vMSZ2IXJtjpt0uAz1x3QA-o98ax1XWZE98VftDOp0b5dT3cv4MCvYw1CCN8tsGlkBKM2KAyGufOOAih9tYoLxVI0uIGQmkyJsmMypD2IbDPF-R2N6E:1uhjs0:Ltuj0wkAoOgVTuiMbivLZppWRLYSlClgdw20OtovQGk	2026-08-01 10:08:00.956517+03
a5ru6dgo0567l50i4vybeftb9tlisvvr	.eJxVjEEOwiAQRe_C2hCcgba4dN8zNAMzSNVAUtqV8e7apAvd_vfef6mJtjVPW5NlmlldlFen3y1QfEjZAd-p3KqOtazLHPSu6IM2PVaW5_Vw_w4ytfytI9I5CGNMYMk6w-DROOygMx5dnwIMhoJNlhgHFAjkIyKARGcZqFfvD-I-N7k:1useYE:lOak0yaD4u88FGYmqtghHFDOxCYpWx-_ML8HFGxibKk	2026-08-31 12:40:42.656614+03
\.


--
-- TOC entry 5249 (class 0 OID 33874)
-- Dependencies: 266
-- Data for Name: education_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.education_ (id, name_) FROM stdin;
1	Genel
2	Okuryazar
3	İlkokul
4	Ortaokul
5	Lise
6	Önlisans
7	Lisans
8	Yükseklisans
9	Doktora
\.


--
-- TOC entry 5204 (class 0 OID 25472)
-- Dependencies: 221
-- Data for Name: firm_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.firm_ (id, name_, city_id, district_id, tax_office_id, nace_id, create_, delete_, address_, telephone_, fax_, email_, type_firm, tax_, web_, sgk_sicil, payment_, ceo_name, ceo_email, ceo_cell, active_, logo_media) FROM stdin;
3	Nalçacı Holding	42	625	632	654	2025-07-10 00:00:00	\N	Nalçacı Caddesi	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	t	logo_firm/Screenshot_2025-06-18_103404.png
5	Ekonaz Ortak Sağlık Güvenlik Birimi San. Tic. Ltd. Şti.	42	516	630	628	2014-04-16 00:00:00	\N	FEVZİ ÇAKMAK MAH. KENİTRA CAD. 26/O KARATAY / KONYA	+905323957913	\N	ekonaz.muhasebe@gmail.com	OSGB	3300497959	www.ekonazcevre.com.tr	\N	\N	Ali BOZDEMİR	ekonaz.muhasebe@gmail.com	+905323957913	t	logo_firm/ekonaz.png
4	Ağaç LTD	34	143	13	609	2023-06-21 00:00:00	\N	71. cadde	2164555	\N	\N	ŞTİ	\N	\N	\N	TL	\N	\N	\N	t	logo_firm/Screenshot_2025-06-18_104003.png
\.


--
-- TOC entry 5206 (class 0 OID 25479)
-- Dependencies: 223
-- Data for Name: language_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.language_ (id, name_, short_) FROM stdin;
1	Türkçe	tr
2	İngilizce	en
\.


--
-- TOC entry 5208 (class 0 OID 25485)
-- Dependencies: 225
-- Data for Name: media_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.media_ (id, create_, media_type_id, path_id, name_, delete_, active_) FROM stdin;
\.


--
-- TOC entry 5210 (class 0 OID 25490)
-- Dependencies: 227
-- Data for Name: media_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.media_type (id, name_) FROM stdin;
\.


--
-- TOC entry 5212 (class 0 OID 25494)
-- Dependencies: 229
-- Data for Name: nace_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.nace_ (id, name_, code_, description_) FROM stdin;
1	İkinci el eşya ticareti	47.79.04	Kullanılmış mobilya, elektrikli ve elektronik ev eşyası perakende ticareti
2	İkinci el eşya ticareti	47.79.90	Diğer ikinci el eşya perakende ticareti (ikinci el motorlu kara taşıtları ve motosiklet parçaları hariç)
3	İkinci el eşya ticareti	47.92.00	Uzmanlaşmış perakende ticaret için aracılık hizmeti faaliyetleri
4	İkinci el eşya ticareti	77.22.99	Başka yerde sınıflandırılmamış diğer kişisel ve ev eşyalarının kiralanması ve operasyonel leasingi (müzik aleti, giyim eşyası, mücevher vb. ile video kasetler, büro mobilyaları, eğlence ve spor ekipmanları hariç)
5	Kerestecilik	02.40.01	Ormanda ağaçların kesilmesi, dallarından temizlenmesi, soyulması vb. destekleyici faaliyetler
6	Kerestecilik	02.40.02	Ormanda kesilmiş ve temizlenmiş ağaçların taşınması, istiflenmesi ve yüklenmesi faaliyetleri
7	Kerestecilik	16.11.01	Kereste imalatı (ağaçların biçilmesi, planyalanması, rendelenmesi ve şekillendirilmesi faaliyetleri)
8	Kerestecilik	16.12.00	Ahşabın işlenmesi ve bitirilmesi (bir ücret veya sözleşmeye dayalı olarak gerçekleştirilen)
9	Kerestecilik	46.13.02	Kereste ve kereste ürünlerinin toptan satışı ile ilgili aracıların faaliyetleri
10	Kerestecilik	46.83.02	Ağacın ilk işlenmesinden elde edilen ürünlerin toptan ticareti
11	Kerestecilik	46.83.12	İşlenmemiş ağaç (tomruk-ham haldeki) toptan ticareti (orman ağaçları, endüstriyel odunlar vb.)
12	Kerestecilik	47.52.10	Ağacın ilk işlenmesinden elde edilen ürünlerin perakende ticareti (kereste, ağaç talaşı ve yongası, kontrplak, yonga ve lifli levhalar (mdf, sunta vb.), parke, ahşap varil, fıçı ve diğer muhafazalar, vb.)
13	Marangozluk	16.11.02	Ahşap demir yolu veya tramvay traversi imalatı
14	Marangozluk	16.11.03	Ağaç yünü, ağaç unu, ağaç talaşı, ağaç yonga imalatı
15	Marangozluk	16.11.04	Ahşap döşemelerin ve yer döşemelerinin imalatı (birleştirilebilir parkeler hariç)
16	Marangozluk	16.21.01	Ahşap, bambu ve diğer odunsu malzemelerden kaplamalık plaka, levha, vb. imalatı (yaprak halde) (preslenmemiş)
17	Marangozluk	16.21.02	Sıkıştırılmış lif, tahta ve tabakalardan kontrplak, MDF, sunta, OSB, CLT vb. levha imalatı
18	Marangozluk	16.22.01	Birleştirilmiş parke yer döşemelerinin imalatı
19	Marangozluk	16.23.99	Başka yerde sınıflandırılmamış diğer inşaat doğrama ve marangozluk ürünleri imalatı
20	Marangozluk	16.24.02	Palet, kutu palet ve diğer ahşap yükleme tablaları imalatı
21	Marangozluk	16.24.90	Diğer ahşap konteyner imalatı
22	Marangozluk	16.25.00	Ahşap kapı ve pencere imalatı
23	Marangozluk	16.27.00	Ahşap ürünlerin bitirilmesi
24	Marangozluk	16.28.01	Ahşap mutfak ve sofra eşyası imalatı (kaşık, kepçe, spatula, bardak, havan, havan eli, tepsi vb.)
25	Marangozluk	16.28.02	Ahşap çerçeve ve ahşaptan diğer eşyaların imalatı (panolar, tuval için çerçeveler, ip vb. için makaralar, arı kovanları, köpek kulübeleri dahil)
26	Marangozluk	16.28.03	Ahşaptan iş aletleri, alet gövdeleri, alet sapları, süpürge veya fırça gövdeleri ile sapları, ayakkabı kalıpları, ahşap mandal, elbise ve şapka askıları imalatı
27	Marangozluk	16.28.04	Hasır veya diğer örme malzemesinden (kamış, saz, saman vb.) eşyaların imalatı ile sepet türü ve hasır işi eşyaların imalatı
28	Marangozluk	16.28.05	Sedef kakma ahşap işleri, kakma ile süslü ahşap eşyalar, mücevher için veya çatal-kaşık takımı ve benzeri eşyalar için ahşap kutular, ahşap biblo, heykel ve diğer süslerin imalatı
29	Marangozluk	16.28.06	Doğal mantarın işlenmesi, aglomera mantar imalatı ile bunlardan eşyaların imalatı
30	Marangozluk	16.28.99	Başka yerde sınıflandırılmamış diğer ağaç ürünleri imalatı; mantardan, saz, saman ve benzeri örme malzemelerinden yapılmış ürünlerin imalatı
31	Marangozluk	25.63.03	Ahşap ve diğer malzemelerden kalıp ve döküm modeli imalatı (kek ve ayakkabı kalıpları hariç)
32	Marangozluk	32.99.07	Şemsiyeler, güneş şemsiyeleri, baston ve koltuklu baston, koltuk değneği vb. imalatı (parçaları dahil)
33	Marangozluk	32.99.11	Mantar can simitlerinin imalatı
34	Marangozluk	32.99.16	Yazı veya çizim tahtaları imalatı
35	Marangozluk	46.49.05	Hasır eşyalar, mantar eşyalar ve diğer ahşap ürünlerin toptan ticareti (ip vb. için makaralar dahil)
36	Marangozluk	46.49.25	Arı kovanı toptan ticareti
37	Marangozluk	46.83.14	Masif, lamine ve laminant parke toptan ticareti
38	Marangozluk	46.83.20	Ahşap kapı, pencere ve bunların kasaları ile kapı eşiklerinin toptan ticareti
39	Marangozluk	47.52.17	Ahşap kapı, pencere ve bunların kasaları ile kapı eşiklerinin perakende ticareti
40	Marangozluk	47.52.22	Masif, lamine ve laminant parke perakende ticareti
41	Marangozluk	47.55.04	Ahşap, mantar ve hasır eşyaların perakende ticareti (ahşap sofra ve mutfak eşyaları hariç)
42	Mobilya boyacılığı	31.00.06	Mobilyaların boyanması, verniklenmesi, cilalanması vb. tamamlayıcı işlerin yapılması
43	Mobilya döşemeciliği	31.00.05	Yatak ve yatak desteklerinin imalatı (kauçuk şişme yatak ve su yatağı hariç)
44	Mobilya döşemeciliği	31.00.08	Sandalyelerin, koltukların vb. döşenmesi gibi tamamlayıcı işlerin yapılması (büro ve ev mobilyalarının yeniden kaplanması hariç)
45	Mobilya döşemeciliği	95.24.01	Mobilyaların ve ev döşemelerinin onarım ve bakımı (halı ve kilim onarımı hariç)
46	Mobilya imalatı	31.00.01	Yatak odası, yemek odası, mutfak mobilyası, banyo dolabı, genç ve çocuk odası takımı, gardırop, vestiyer, vb. imalatı (gömme dolap, masa, zigon, vb. dahil)
47	Mobilya imalatı	31.00.02	Büro, okul, ibadethane, otel, lokanta, sinema, tiyatro vb. kapalı alanlar için mobilya imalatı (iskelet imalatı dahil; taş, beton, seramikten olanlar hariç)
48	Mobilya imalatı	31.00.03	Sandalye, koltuk, kanepe, oturma takımı, çekyat, divan, markiz, vb. imalatı (iskelet imalatı dahil; plastik olanlar ile bürolarda ve park ve bahçelerde kullanılanlar hariç)
506	Dericilik	15.11.13	Deri ve kösele esaslı terkip ile elde edilen levha, yaprak, şerit deri ve kösele imalatı
49	Mobilya imalatı	31.00.04	Mağazalar için tezgah, banko, vitrin, raf, çekmeceli dolap vb. özel mobilya imalatı (laboratuvarlar ve teknik bürolar için olanlar hariç)
50	Mobilya imalatı	31.00.07	Park ve bahçelerde kullanılan bank, masa, tabure, sandalye, koltuk, vb. mobilyaların imalatı (plastik olanlar hariç)
51	Mobilya imalatı	31.00.90	Diğer mobilyaların imalatı
52	Mobilya imalatı	43.32.01	Hazır mutfaklar, mutfak tezgahları, gömme dolaplar, iç merdivenler ile ince tahta, lambri ve benzerlerinin montajı işleri
53	Mobilya ticareti	46.15.01	Mobilyaların toptan satışı ile ilgili aracıların faaliyetleri
54	Mobilya ticareti	46.47.01	Mobilya ve mobilya aksesuarları toptan ticareti (yatak dahil)
55	Mobilya ticareti	46.47.04	Büro mobilyalarının toptan ticareti
56	Mobilya ticareti	47.55.03	Ev mobilyalarının ve aksesuarlarının perakende ticareti (baza, somya, karyola dahil; hasır ve sepetçi söğüdü gibi malzemelerden olanlar hariç)
57	Mobilya ticareti	47.55.06	Büro mobilyaları ve aksesuarlarının perakende ticareti
58	Mobilya ticareti	47.55.07	Bahçe mobilyalarının perakende ticareti
59	Mobilya ticareti	47.55.08	Yatak perakende ticareti
60	Mobilya ticareti	77.33.02	Büro mobilyalarının kiralanması ve leasingi (büro sandalyesi ve masasının kiralanması dahil) (finansal leasing hariç)
61	Yakacak imalatı, ticareti	02.20.01	Endüstriyel ve yakacak odun üretimi (geleneksel yöntemlerle odun kömürü üretimi dahil)
62	Yakacak imalatı, ticareti	16.26.00	Bitkisel biyokütleden katı yakıt imalatı
63	Yakacak imalatı, ticareti	19.20.12	Turba, linyit ve taş kömürü briketleri imalatı (kömür tozundan basınçla elde edilen yakıt)
64	Yakacak imalatı, ticareti	46.81.03	Katı yakıtlar ve bunlarla ilgili ürünlerin toptan ticareti
65	Yakacak imalatı, ticareti	47.78.02	Kömür ve yakacak odun perakende ticareti
66	Yakacak imalatı, ticareti	47.78.31	Mağaza, tezgah, pazar yeri dışında müşterinin istediği yere ulaştırılarak yapılan doğrudan yakıt satışı (kalorifer yakıtı, yakacak odun, vb.)
67	Ajans, organizasyon faaliyetleri	74.99.01	Sanatçı, sporcu, şovmen, manken ve diğerleri için ajansların ve menajerlerin faaliyetleri
68	Ajans, organizasyon faaliyetleri	77.39.99	Başka yerde sınıflandırılmamış diğer makine ve ekipmanların sürücüsüz kiralanması ve leasingi ile maddi malların kiralanması ve operasyonel leasingi
69	Ajans, organizasyon faaliyetleri	78.10.04	Oyuncu seçme ajansları ve bürolarının faaliyetleri
70	Ajans, organizasyon faaliyetleri	79.90.99	Başka yerde sınıflandırılmamış diğer rezervasyon hizmetleri ve ilgili faaliyetler (turizm tanıtım faaliyetleri, vb.)
71	Ajans, organizasyon faaliyetleri	82.30.02	Kongre ve ticari gösteri organizasyonu
72	Ajans, organizasyon faaliyetleri	82.40.01	Spor, müzik, tiyatro ve diğer eğlence etkinlikleri için yer ayırma (rezervasyon) ve bilet satılması faaliyeti
73	Ajans, organizasyon faaliyetleri	90.20.01	Bağımsız aktör, aktrist ve dublörlerin faaliyetleri
74	Ajans, organizasyon faaliyetleri	90.39.90	Sanat ve gösteri sanatlarına yönelik diğer destek faaliyetleri (sanat ve gösteri sanatlarına yönelik yönetmenlerin ve yapımcıların faaliyetleri hariç)
75	Ajans, organizasyon faaliyetleri	93.19.02	Spor etkinlikleri yapımcılarının faaliyetleri ile bu etkinliklerin kendi tesisleri olmayan kuruluşlar tarafından düzenlenmesi faaliyetleri (spor kulüpleri tarafından yapılanlar hariç)
76	Ajans, organizasyon faaliyetleri	93.29.12	Sanatsal olmayan etkinliklerin organizasyonuyla ilgili görsel-işitsel ekipmanların ve özel efektlerin teknik planlanması, temini, kurulumu ve işletilmesi
77	Düğün salonu işletmeciliği	93.29.02	Düğün, balo ve kokteyl salonlarının işletilmesi
78	Düğün salonu işletmeciliği	96.99.14	Nikah salonlarının hizmetleri
79	Eğlence yerleri işletmeciliği	59.14.02	Sinema filmi gösterim faaliyetleri
80	Eğlence yerleri işletmeciliği	90.20.04	Sirklerin faaliyetleri
81	Eğlence yerleri işletmeciliği	93.21.01	Eğlence parkları ve tema parklarının faaliyetleri (bağımsız sağlayıcılar tarafından mekanik at ve arabaların, oyunların ve gösterilerin işletilmesi hariç)
82	Eğlence yerleri işletmeciliği	93.29.01	Plaj alanlarının işletilmesi (bu tesislerin bütünleyici bir parçası olan soyunma odası, dolap, sandalye, kano, deniz motosikleti vb. kiralanması dahil)
83	Eğlence yerleri işletmeciliği	93.29.10	Dinlence (rekreasyon) parklarının faaliyetleri (konaklamalı olanlar ile eğlence parkları ve tema parklarının işletilmesi hariç)
84	Eğlence yerleri işletmeciliği	93.29.99	Başka yerde sınıflandırılmamış diğer eğlence ve dinlence (rekreasyon) faaliyetleri
85	Gazinoculuk	56.30.04	Bar, meyhane ve birahanelerde içecek sunum faaliyetleri (alkollü-alkolsüz)
86	Gazinoculuk	56.30.05	Gazino, gece kulübü, taverna, diskotek, kokteyl salonları, vb. yerlerde içecek sunum faaliyetleri (alkollü-alkolsüz)
87	Kahvehanecilik, kıraathanecilik	56.30.02	Çay ocakları, kıraathaneler, kahvehaneler, kafeler (içecek ağırlıklı hizmet veren), meyve suyu salonları ve çay bahçelerinde içecek sunum faaliyeti
88	Kahvehanecilik, kıraathanecilik	56.30.90	Seyyar içecek satanlar ile diğer içecek sunum faaliyetleri (Trenlerde ve gemilerde işletilen barların faaliyetleri (alkollü-alkolsüz) dahil)
89	Lokal işletmeciliği	56.30.03	Lokallerde içecek sunum faaliyeti (alkollü-alkolsüz)
90	Otel, pansiyon, yurt işletmeciliği	55.10.02	Otel vb. konaklama yerlerinin faaliyetleri (günlük temizlik ve yatak yapma hizmeti sağlanan yerlerin faaliyetleri) (kendi müşterilerine restoran hizmeti vermeyenler ile devre mülkler hariç)
91	Otel, pansiyon, yurt işletmeciliği	55.10.05	Otel vb. konaklama yerlerinin faaliyetleri (günlük temizlik ve yatak yapma hizmeti sağlanan yerlerin faaliyetleri) (kendi müşterilerine restoran hizmeti verenler ile devre mülkler hariç)
92	Otel, pansiyon, yurt işletmeciliği	55.20.01	Tatil ve diğer kısa süreli konaklama faaliyetleri (günlük temizlik ve yatak yapma hizmeti sağlanan oda veya süit konaklama faaliyetleri hariç)
93	Otel, pansiyon, yurt işletmeciliği	55.20.03	Kendine ait veya kiralanmış mobilyalı evlerde bir aydan daha kısa süreli olarak konaklama faaliyetleri
94	Otel, pansiyon, yurt işletmeciliği	55.20.04	Tatil amaçlı pansiyonların faaliyetleri
95	Otel, pansiyon, yurt işletmeciliği	55.30.36	Kamp alanları ve karavan parkları
96	Otel, pansiyon, yurt işletmeciliği	55.90.01	Öğrenci ve işçi yurtları, pansiyonlar ve odası kiralanan evlerde yapılan konaklama faaliyetleri (tatil amaçlı olanlar hariç)
522	Dokumacılık	13.20.19	Doğal ipekten kumaş (doğal ipekten dokuma tül kumaş dahil) imalatı
97	Otel, pansiyon, yurt işletmeciliği	55.90.90	Diğer konaklama yerlerinin faaliyetleri (başka bir birim tarafından işletildiğinde yataklı vagonlar vb. dahil; misafirhaneler, öğretmen evi vb. hariç)
98	Otel, pansiyon, yurt işletmeciliği	91.22.00	Tarihi alan ve anıt faaliyetleri (tarihi alanların ve yapıların işletilmesi, korunması dahil)
99	Oyun salonu, internet kafe işletmeciliği	61.90.05	İnternet kafelerin faaliyetleri
100	Oyun salonu, internet kafe işletmeciliği	93.29.03	Oyun makinelerinin işletilmesi
101	Oyun salonu, internet kafe işletmeciliği	93.29.08	Bilardo salonlarının faaliyetleri
102	Oyun salonu, internet kafe işletmeciliği	93.29.11	Elektronik spor (e-spor) oyun merkezlerinin faaliyetleri
103	Ses, sahne sanatçılığı	90.20.02	Bağımsız müzisyen, ses sanatçısı, konuşmacı, sunucu vb.lerin faaliyetleri (müzik grupları dahil)
104	Ses, sahne sanatçılığı	90.20.03	Canlı tiyatro, opera, bale, müzikal, konser vb. yapımların sahneye konulması faaliyetleri (illüzyon gösterileri, kukla gösterileri ve kumpanyalar dahil)
105	Ses, sahne sanatçılığı	90.20.99	Başka yerde sınıflandırılmamış diğer gösteri sanatları
106	Şans oyunları bayiliği	92.00.01	Müşterek bahis faaliyetleri (at yarışı, köpek yarışı, futbol ve diğer spor yarışmaları konusunda bahis hizmetleri)
107	Şans oyunları bayiliği	92.00.02	Loto vb. sayısal şans oyunlarına ilişkin faaliyetler (piyango biletlerinin satışı dahil)
108	Asansör, yürüyen merdiven kurulumu, bakımı, onarımı	43.24.01	Asansörlerin, yürüyen merdivenlerin, yürüyen yolların, otomatik ve döner kapıların onarım ve bakımı dahil kurulum işleri
109	Beyaz eşya onarımı	95.22.01	Evde kullanılan elektrikli cihazların onarım ve bakımı
110	Beyaz eşya ticareti	46.43.01	Beyaz eşya toptan ticareti
111	Beyaz eşya ticareti	47.54.01	Beyaz eşya ve elektrikli küçük ev aleti perakende ticareti (radyo, televizyon ve fotoğrafçılık ürünleri hariç)
112	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	18.20.03	Yazılımların çoğaltılması hizmetleri (CD, kaset vb. ortamlardaki bilgisayar yazılımlarının ve verilerin asıl (master) kopyalarından çoğaltılması)
113	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	58.21.01	Video oyunlarının yayımlanması
114	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	58.29.01	Diğer yazılım programlarının yayımlanması
115	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	60.39.00	Diğer içerik dağıtım faaliyetleri
116	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	62.10.00	Bilgisayar programlama faaliyetleri
117	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	62.20.00	Bilgisayar danışmanlığı ve bilgisayar birimleri (sistemleri) yönetimi faaliyetleri (siber güvenlik danışmanlığı dahil)
118	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	62.90.01	Bilgisayarları felaketten kurtarma ve veri kurtarma faaliyetleri
119	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	62.90.99	Başka yerde sınıflandırılmamış diğer bilgi teknolojisi ve bilgisayar hizmet faaliyetleri
120	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	63.10.00	Bilgi işlem altyapısı, veri işleme, barındırma ve ilgili faaliyetler
121	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	63.91.02	Web arama portalı faaliyetleri
122	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	95.10.01	Bilgisayarların ve bilgisayar çevre birimlerinin onarımı (ATM'ler ve pos cihazları dahil)
123	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	95.10.03	Bilgisayarların ve bilgisayar çevre birimlerinin yenilenmesi hizmeti faaliyetleri (dizüstü bilgisayarlar, masaüstü bilgisayarlar, modemler, oyun konsolları)
124	Bilgisayar kurulumu, onarımı, programlama, veri kurtarma	95.10.04	İletişim araç ve gereçlerinin yenilenmesi hizmeti faaliyetleri (cep telefonları, akıllı telefonlar)
125	Elektrik makineleri imalatı, kurulumu, onarımı	27.11.01	Elektrik motoru, jeneratör ve transformatörlerin imalatı (aksam ve parçaları hariç)
126	Elektrik makineleri imalatı, kurulumu, onarımı	27.11.03	Elektrik motoru, jeneratör ve transformatörlerin aksam ve parçalarının imalatı
127	Elektrik makineleri imalatı, kurulumu, onarımı	27.90.05	Elektrikli kaynak ve lehim teçhizatı (lehim havyaları, ark kaynak makineleri, endüksiyon kaynak makineleri vb.) ile metallerin veya sinterlenmiş metal karbürlerin sıcak spreylenmesi için elektrikli makine ve cihazlarının imalatı
128	Elektrik makineleri imalatı, kurulumu, onarımı	33.14.01	Güç transformatörleri, dağıtım transformatörleri ve özel transformatörlerin onarım ve bakımı (elektrik dağıtım ve kontrol cihazları dahil)
129	Elektrik makineleri imalatı, kurulumu, onarımı	33.14.02	Elektrik motorları, jeneratörler ve motor jeneratör setlerinin onarım ve bakımı (bobinlerin tekrar sarımı dahil)
130	Elektrik makineleri imalatı, kurulumu, onarımı	33.20.51	Elektrikli ekipmanların kurulum hizmetleri (yollar, vb. için elektrikli sinyalizasyon ekipmanları hariç))
131	Elektrik malzemeleri imalatı, ticareti	23.43.01	Seramik yalıtkanların (izolatörlerin) ve yalıtkan bağlantı parçalarının imalatı
132	Elektrik malzemeleri imalatı, ticareti	27.12.01	Elektrik dağıtım ve kontrol cihazları imalatı
133	Elektrik malzemeleri imalatı, ticareti	27.12.02	Elektrik dağıtım ve kontrol cihazlarının aksam ve parçalarının imalatı
134	Elektrik malzemeleri imalatı, ticareti	27.33.00	Kablolamada kullanılan gereçlerin imalatı
135	Elektrik malzemeleri imalatı, ticareti	27.40.02	Hava ve motorlu kara taşıtları için monoblok far üniteleri, kara, hava ve deniz taşıtları için elektrikli aydınlatma donanımları veya görsel sinyalizasyon ekipmanları imalatı (polis araçları, ambulans vb. araçların dış ikaz lambaları dahil)
136	Elektrik malzemeleri imalatı, ticareti	27.40.03	Avize, aplik ve diğer elektrikli aydınlatma armatürleri, sahne, fotoğraf veya sinema stüdyoları için projektörler ve spot ışıkları, elektrikli masa lambaları, çalışma lambaları, abajur vb. lambaların imalatı (süsleme için ışıklandırma setleri dahil)
137	Elektrik malzemeleri imalatı, ticareti	27.40.04	Sokak aydınlatma donanımlarının imalatı (trafik ışıkları hariç)
138	Elektrik malzemeleri imalatı, ticareti	27.40.05	Pil, akümülatör veya manyeto ile çalışan portatif elektrik lambaları ve elektriksiz lambalar ile el feneri, gaz ve lüks lambası vb. aydınlatma armatürlerinin imalatı (taşıtlar için olanlar hariç)
139	Elektrik malzemeleri imalatı, ticareti	27.40.99	Başka yerde sınıflandırılmamış aydınlatma ekipmanları imalatı
140	Elektrik malzemeleri imalatı, ticareti	27.90.99	Başka yerde sınıflandırılmamış diğer elektrikli ekipmanların imalatı
141	Elektrik malzemeleri imalatı, ticareti	29.31.05	Motorlu kara taşıtları ve motosikletler için elektrikli sinyalizasyon donanımları, kornalar, sirenler, cam silecekleri, buğu önleyiciler, elektrikli cam/kapı sistemleri, voltaj regülatörleri vb. elektrikli ekipmanların imalatı
142	Elektrik malzemeleri imalatı, ticareti	46.47.03	Aydınlatma ekipmanlarının toptan ticareti
143	Elektrik malzemeleri imalatı, ticareti	46.64.03	Rüzgar türbinleri, kondansatörler, elektrik yalıtkanları (izolatör), AC/AD/DC motorlar, jeneratörler, yalıtılmış bobin telleri vb. elektrikli makine, cihaz ve aletlerin toptan ticareti
144	Elektrik malzemeleri imalatı, ticareti	46.64.09	Akümülatör, batarya, pil ve bunların parçalarının toptan ticareti (evlerde, motosikletlerde ve motorlu kara taşıtlarında kullanılanlar hariç)
145	Elektrik malzemeleri imalatı, ticareti	46.64.15	Elektrik malzemeleri toptan ticareti (evde kullanılan pil ve bataryalar dahil)
146	Elektrik malzemeleri imalatı, ticareti	47.54.03	Evde kullanım amaçlı elektrik tesisat malzemesi perakende ticareti
147	Elektrik malzemeleri imalatı, ticareti	47.55.02	Aydınlatma teçhizatı perakende ticareti (elektrik malzemeleri hariç)
148	Elektrik sistemleri imalatı, kurulumu, onarımı	33.14.90	Diğer profesyonel elektrikli ekipmanların onarım ve bakımı
149	Elektrik sistemleri imalatı, kurulumu, onarımı	33.20.53	Endüstriyel işlem kontrol ekipmanlarının kurulum hizmetleri (otomasyon destekliler dahil)
150	Elektrik tesisatçılığı	35.11.00	Yenilenemeyen kaynaklardan elektrik üretimi
151	Elektrik tesisatçılığı	35.12.00	Yenilenebilir kaynaklardan elektrik üretimi
152	Elektrik tesisatçılığı	43.21.01	Bina ve bina dışı yapıların (ulaşım için aydınlatma ve sinyalizasyon sistemleri hariç) elektrik tesisatı, kablolu televizyon ve bilgisayar ağı tesisatı ile konut tipi antenler (uydu antenleri dahil), elektrikli güneş enerjisi kollektörleri, elektrik sayaçları, elektrikli araçlar için elektrikli şarj cihazları tesisatının kurulumu, duvar dibi ısıtma sistemleri, yangın ve hırsızlık alarm sistemleri vb. kurulumu
153	Elektrikli ev aletleri imalatı, onarımı	27.51.02	Ev tipi elektrikli su ısıtıcıları (depolu su ısıtıcıları, anında su ısıtıcıları, şofben, termosifon dahil), elektrikli ısıtma cihazları (elektrikli soba, radyatör, vb.) ve elektrikli toprak ısıtma cihazlarının imalatı
154	Elektrikli ev aletleri imalatı, onarımı	27.51.04	Mutfakta kullanılan elektrikli küçük ev aletlerinin imalatı (çay veya kahve makinesi, semaver, ızgara, kızartma cihazı, ekmek kızartma makinesi, mutfak robotu, mikser, blender, meyve sıkacağı, et kıyma makinesi, tost makinesi, fritöz vb.)
155	Elektrikli ev aletleri imalatı, onarımı	27.51.05	Elektrikli diğer küçük ev aletleri (elektrotermik el kurutma makinesi, elektrikli ütü, havlu dispenseri, hava nemlendirici) ile elektrikli battaniyelerin imalatı
156	Elektrikli ev aletleri imalatı, onarımı	27.51.07	Elektrikli ev aletleri aksam ve parçalarının imalatı
157	Elektrikli ev aletleri imalatı, onarımı	27.51.08	Ev tipi buzdolabı, dondurucu, çamaşır makinesi, çamaşır kurutma makinesi, bulaşık makinesi, vantilatör, aspiratör, fan, aspiratörlü davlumbaz, fırın, ocak, mikrodalga fırın, elektrikli pişirme sacı vb. imalatı
158	Elektrikli ev aletleri imalatı, onarımı	27.51.99	Başka yerde sınıflandırılmamış diğer elektrikli ev aletlerinin imalatı
159	Elektrikli ev aletleri imalatı, onarımı	95.29.99	Başka yerde sınıflandırılmamış diğer kişisel ve ev eşyalarının onarım ve bakımı
160	Elektrikli ev aletleri ticareti	46.43.90	Diğer elektrikli ev aletleri toptan ticareti
161	Elektrikli ev aletleri ticareti	47.54.99	Başka yerde sınıflandırılmamış elektrikli ev aletleri perakende ticareti (radyo, TV ve fotoğrafçılık ürünleri hariç)
162	Elektronik ürün imalatı, onarımı	26.11.04	Diyotların, transistörlerin, diyakların, triyaklar, tristör, rezistans, ledler, kristal, röle, mikro anahtar, sabit veya ayarlanabilir direnç ve kondansatörler ile elektronik entegre devrelerin imalatı
163	Elektronik ürün imalatı, onarımı	26.11.06	Çıplak baskılı devre kartlarının imalatı
164	Elektronik ürün imalatı, onarımı	26.11.99	Başka yerde sınıflandırılmamış diğer elektronik bileşenlerin imalatı
165	Elektronik ürün imalatı, onarımı	26.12.01	Yüklü elektronik kart imalatı (yüklü baskılı devre kartları, ses, görüntü, denetleyici, ağ ve modem kartları ile akıllı kartlar vb.)
166	Elektronik ürün imalatı, onarımı	26.30.03	Kızıl ötesi (enfraruj) sinyal kullanan iletişim cihazlarının imalatı (örn: uzaktan kumanda cihazları)
167	Elektronik ürün imalatı, onarımı	26.30.05	Alıcı ve verici antenlerin imalatı (harici, teleskopik, çubuk, uydu, çanak ve hava ve deniz taşıtlarının antenleri)
168	Elektronik ürün imalatı, onarımı	26.40.10	Mikrofon, hoparlör ve kulaklıklar ile elektrikli ses yükselteçlerinin (amplifikatörler) imalatı
169	Elektronik ürün imalatı, onarımı	26.40.99	Başka yerde sınıflandırılmamış tüketici elektroniği ürünlerinin imalatı
170	Elektronik ürün imalatı, onarımı	26.51.03	Elektrik miktarını (volt, akım vb.) ölçmek ve kontrol etmek için kullanılan alet ve cihazların imalatı (avometre, voltmetre, osiloskop ile diğer voltaj, akım, direnç veya elektrik gücünü ölçüm veya kontrol için olanlar) (elektrik sayaçları hariç)
171	Elektronik ürün imalatı, onarımı	26.51.04	Hız ve mesafe ölçümünde kullanılan alet ve cihazların imalatı (taşıt hız göstergesi, takometre, taksimetre vb.)
172	Elektronik ürün imalatı, onarımı	26.51.05	Isı ve sıcaklık ölçümünde kullanılan alet ve cihazların imalatı (termometre, termostat, pirometre vb.)
173	Elektronik ürün imalatı, onarımı	26.51.06	Işık, ışın ve renk ölçümünde kullanılan alet ve cihazların imalatı (polarimetre, kolorimetre, refraktometre vb.)
174	Elektronik ürün imalatı, onarımı	26.51.07	Meteorolojide kullanılan alet ve cihazların imalatı
175	Elektronik ürün imalatı, onarımı	26.51.08	Yön bulma pusulaları ile diğer seyrüsefer alet ve cihazlarının, radar ve sonar cihazlarının imalatı (hava, kara ve deniz taşımacılığında kullanılanlar dahil)
523	Dokumacılık	13.20.20	Keten, rami, kenevir, jüt elyafları ile diğer bitkisel tekstil elyaflarından dokuma kumaş (bitkisel elyaftan dokuma tül kumaş dahil) imalatı (pamuk hariç)
176	Elektronik ürün imalatı, onarımı	26.51.09	Hava, sıvı ve gazların akış, seviye, basınç veya diğer değişkenlerini ölçme ve kontrol etme için kullanılan aletlerin imalatı (hidrometre, debimetre, barometre, higrometre vb.)
177	Elektronik ürün imalatı, onarımı	26.51.11	Teçhizatlı çizim masaları ve makineleri ile diğer çizim, işaretleme veya matematiksel hesaplama aletlerinin imalatı (pergel takımı, pantograf, resim, çizim, hesap yapmaya mahsus elektrikli/elektronik çiziciler vb. dahil)
178	Elektronik ürün imalatı, onarımı	26.51.12	Laboratuvar, kuyumculuk vb. yerlerde kullanılan hassas tartıların imalatı
179	Elektronik ürün imalatı, onarımı	26.51.13	Sanayide kullanılan işlem kontrol amaçlı teçhizatların imalatı
180	Elektronik ürün imalatı, onarımı	26.51.99	Başka yerde sınıflandırılmamış ölçme, test ve seyrüsefer amaçlı alet ve cihazların imalatı (hidrolik veya pnömatik otomatik ayar veya kontrol aletleri ile milometreler, pedometreler, stroboskoplar, monostatlar, kumpaslar, spektrometreler dahil)
181	Elektronik ürün imalatı, onarımı	28.23.00	Büro makine ve ekipmanları imalatı (bilgisayarlar ve çevre birimleri hariç)
182	Elektronik ürün imalatı, onarımı	28.29.08	Tartı aletleri ve baskül imalatı (ev ve dükkanlarda kullanılan terazi ve kantarlar, sürekli ölçüm için tartılar, taşıt baskülleri (köprü tipi basküller) vb.) (kuyumculukta ve laboratuvarlarda kullanılan hassas tartılar hariç)
183	Elektronik ürün imalatı, onarımı	33.12.07	Tartı aletlerinin onarım ve bakımı
184	Elektronik ürün imalatı, onarımı	33.12.18	Büro ve muhasebe makinelerinin onarım ve bakımı (daktilo, yazar kasa, fotokopi makineleri, hesap makineleri, vb.)
185	Elektronik ürün imalatı, onarımı	33.13.01	Ölçme, test ve seyrüsefer alet ve cihazlarının onarım ve bakımı
186	Elektronik ürün imalatı, onarımı	33.13.02	Işınlama, elektromedikal ve elektroterapi ekipmanlarının onarım ve bakımı
187	Elektronik ürün imalatı, onarımı	33.13.05	Yüklü elektronik devrelerin/kartların bakımı ve onarımı
188	Elektronik ürün imalatı, onarımı	33.13.90	Diğer profesyonel elektronik ekipmanların onarım ve bakımı
189	Elektronik ürün imalatı, onarımı	35.14.02	Elektrik sayaçlarının bakım ve onarımı
190	Elektronik ürün imalatı, onarımı	35.15.01	Elektrikli araçlar ve elektronik cihazlar için şarj istasyonlarının işletilmesi
191	Elektronik ürün imalatı, onarımı	35.22.02	Gaz sayaçlarının bakım ve onarımı
192	Elektronik ürün imalatı, onarımı	36.00.03	Su sayaçlarının bakım ve onarımı
193	Elektronik ürün imalatı, onarımı	95.21.01	Tüketici elektroniği ürünlerinin onarım ve bakımı
194	Elektronik ürün ticareti	46.14.01	Bilgisayar, yazılım, elektronik ve telekomünikasyon donanımlarının ve diğer büro ekipmanlarının toptan satışı ile ilgili aracıların faaliyetleri
195	Elektronik ürün ticareti	46.15.03	Radyo, televizyon ve video cihazlarının toptan satışı ile ilgili aracıların faaliyetleri
196	Elektronik ürün ticareti	46.43.09	Radyo, televizyon, video ve DVD cihazlarının toptan ticareti (antenler ile arabalar için radyo ve TV ekipmanları dahil)
197	Elektronik ürün ticareti	46.50.01	Bilgisayar, bilgisayar çevre birimleri ve yazılımlarının toptan ticareti (bilgisayar donanımları, pos cihazları, ATM cihazları vb. dahil)
198	Elektronik ürün ticareti	46.50.03	Elektronik cihaz ve parçalarının toptan ticareti (elektronik valfler, tüpler, yarı iletken cihazlar, mikroçipler, entegre devreler, baskılı devreler, vb.) (seyrüsefer cihazları hariç)
199	Elektronik ürün ticareti	46.50.90	Diğer bilgi ve iletişim teknolojisi ekipmanlarının toptan ticareti
200	Elektronik ürün ticareti	46.64.13	Sanayi, ticaret, seyrüsefer ve diğer hizmetlerde kullanılmak üzere başka yerde sınıflandırılmamış diğer makinelere ait parçaların toptan ticareti (motorlu kara taşıtları için olanlar hariç)
201	Elektronik ürün ticareti	47.40.01	Bilgisayarların, çevre donanımlarının ve yazılımların perakende ticareti
202	Elektronik ürün ticareti	47.40.03	Ses ve görüntü cihazlarının ve bunların parçalarının perakende ticareti
203	Elektronik ürün ticareti	77.33.01	Büro makine ve ekipmanlarının operatörsüz olarak kiralanması ve leasingi (finansal leasing hariç)
204	Elektronik ürün ticareti	77.33.03	Bilgisayar ve çevre birimlerinin operatörsüz olarak kiralanması ve leasingi (finansal leasing hariç)
205	E-ticaret	47.91.14	Radyo, TV, posta yoluyla veya internet üzerinden yapılan perakende ticaret
206	Güvenlik sistemleri hizmetleri	26.30.09	Hırsız ve yangın alarm sistemleri ve kapı konuşma sistemlerinin (diyafon) (görüntülü olanlar dahil) imalatı (motorlu kara taşıtları için alarm sistemleri hariç)
207	Güvenlik sistemleri hizmetleri	26.51.01	Hırsız ve yangın alarm sistemleri imalatı (bir kontrol istasyonuna sinyal gönderenler) (motorlu kara taşıtları için olanlar hariç)
208	Güvenlik sistemleri hizmetleri	46.43.08	Hırsız ve yangın alarmları ile benzeri cihazların toptan ticareti (evlerde kullanım amaçlı)
209	Güvenlik sistemleri hizmetleri	80.09.99	Başka yerde sınıflandırılmamış güvenlik faaliyetleri
210	Kayıtlı medyaların imalatı, kiralanması, ticareti	18.20.02	Ses ve görüntü kayıtlarının çoğaltılması hizmetleri (CD'lerin, DVD'lerin, kasetlerin ve benzerlerinin asıl (master) kopyalarından çoğaltılması)
211	Kayıtlı medyaların imalatı, kiralanması, ticareti	26.70.20	Boş manyetik ses ve görüntü kaset bantlarının imalatı (plak dahil)
212	Kayıtlı medyaların imalatı, kiralanması, ticareti	26.70.21	Manyetik şeritli kartların imalatı (boş telefon kartı dahil)
213	Kayıtlı medyaların imalatı, kiralanması, ticareti	26.70.99	Başka yerde sınıflandırılmamış manyetik ve optik ortamların imalatı
214	Kayıtlı medyaların imalatı, kiralanması, ticareti	47.69.02	Müzik ve video kayıtlarının perakende ticareti
215	Kayıtlı medyaların imalatı, kiralanması, ticareti	77.22.01	Video kasetlerinin, plakların ve disklerin kiralanması ve operasyonel leasingi
216	Kayıtlı medyaların imalatı, kiralanması, ticareti	77.39.07	Ticari radyo, televizyon ve telekomünikasyon ekipmanları ile sinema filmi yapım ekipmanlarının operatörsüz olarak kiralanması veya operasyonel leasingi
217	Telekomünikasyon cihazları onarımı	42.22.05	Telekomünikasyon şebeke ve ağlarının bakım ve onarımı
218	Telekomünikasyon cihazları onarımı	95.10.02	İletişim araç ve gereçlerinin onarımı (kablosuz telefonlar, telsizler, cep telefonları, çağrı cihazları, ticari kameralar vb.)
219	Telekomünikasyon cihazları ticareti	46.50.02	Telekomünikasyon ekipman ve parçalarının toptan ticareti (telefon ve iletişim ekipmanları dahil)
220	Telekomünikasyon cihazları ticareti	47.40.02	Telekomünikasyon teçhizatının perakende ticareti
221	Telekomünikasyon cihazları ticareti	61.20.04	Telekomünikasyon ürünlerinin yeniden satışı ve telekomünikasyon için aracılık hizmeti faaliyetleri
222	Aktar ürünleri imalatı, ticareti	10.83.01	Çay ürünleri imalatı (siyah çay, yeşil çay ve poşet çay ile çay ekstre, esans ve konsantreleri)
223	Aktar ürünleri imalatı, ticareti	10.83.02	Kahve ürünleri imalatı (çekilmiş kahve, çözünebilir kahve ile kahve ekstre, esans ve konsantreleri)
224	Aktar ürünleri imalatı, ticareti	10.83.03	Bitkisel çayların imalatı (nane, yaban otu, papatya, ıhlamur, kuşburnu vb. çaylar)
225	Aktar ürünleri imalatı, ticareti	10.83.04	Kahve içeren ve kahve yerine geçebilecek ürünlerin imalatı (şeker, süt vb. karıştırılmış ürünler dahil)
226	Aktar ürünleri imalatı, ticareti	10.84.01	Baharat imalatı (karabiber, kırmızı toz/pul biber, hardal unu, tarçın, yenibahar, damla sakızı, baharat karışımları vb.) (işlenmiş)
227	Aktar ürünleri imalatı, ticareti	46.37.01	Çay toptan ticareti
228	Aktar ürünleri imalatı, ticareti	46.37.02	Kahve, kakao ve baharat toptan ticareti
229	Aktar ürünleri imalatı, ticareti	46.37.03	İçecek amaçlı kullanılan aromatik bitkilerin toptan ticareti
230	Aktar ürünleri imalatı, ticareti	47.27.04	Çay, kahve, kakao ve baharat perakende ticareti (bitki çayları dahil)
231	Arıcılık	01.48.01	Arıcılık, bal ve bal mumu üretilmesi (arı sütü dahil)
232	Bakkallık, bayilik, büfecilik	11.07.03	İçme suyu üretimi (şişelenmiş, gazsız, tatlandırılmamış ve aromalandırılmamış)
233	Bakkallık, bayilik, büfecilik	35.30.22	Soğutulmuş hava ve soğutulmuş su üretim ve dağıtımı (buz üretimi dahil)
234	Bakkallık, bayilik, büfecilik	46.17.01	Gıda maddelerinin toptan satışı ile ilgili aracıların faaliyetleri (aracı üretici birlikleri dahil, içecekler ile yaş sebze ve meyve hariç)
235	Bakkallık, bayilik, büfecilik	46.34.03	Su toptan ticareti (su istasyonları dahil, şebeke suyu hariç)
236	Bakkallık, bayilik, büfecilik	46.36.03	Şeker toptan ticareti
237	Bakkallık, bayilik, büfecilik	46.38.03	Gıda tuzu (sofra tuzu) toptan ticareti
238	Bakkallık, bayilik, büfecilik	46.38.04	Un, nişasta, makarna, şehriye vb. ürünler ile hazır gıdaların toptan ticareti
239	Bakkallık, bayilik, büfecilik	46.38.05	Hazır homojenize gıda ile diyetetik gıda ürünleri toptan ticareti
240	Bakkallık, bayilik, büfecilik	46.38.99	Başka yerde sınıflandırılmamış diğer gıda ürünlerinin toptan ticareti
241	Bakkallık, bayilik, büfecilik	46.39.03	Uzmanlaşmamış gıda, içecek ve tütün toptan ticareti
242	Bakkallık, bayilik, büfecilik	47.11.01	Bakkal ve marketlerde yapılan perakende ticaret (gıda, içecek veya tütün ağırlıklı perakende ticaret)
243	Bakkallık, bayilik, büfecilik	47.11.05	Büfelerde gıda, alkollü ve alkolsüz içecek veya tütün ağırlıklı perakende ticaret
244	Bakkallık, bayilik, büfecilik	47.11.99	Başka yerde sınıflandırılmamış gıda, içecek veya tütün ağırlıklı perakende ticaret (tanzim satış ve gıda tüketim kooperatifleri dahil)
245	Bakkallık, bayilik, büfecilik	47.21.02	İşlenmiş ve korunmuş meyve ve sebzelerin perakende ticareti (turşular ile dondurulmuş, salamura edilmiş, konserve ve kurutulmuş sebze ve meyveler vb. dahil, baklagil, zeytin ve kuru yemiş hariç)
246	Bakkallık, bayilik, büfecilik	47.25.01	Alkollü ve alkolsüz içeceklerin perakende ticareti
247	Bakkallık, bayilik, büfecilik	47.25.03	İçme suyu perakende ticareti (şebeke suyu hariç)
248	Bakkallık, bayilik, büfecilik	47.26.01	Tütün ve tütün ürünleri perakende ticareti
249	Bakkallık, bayilik, büfecilik	47.26.02	Pipo, nargile, sigara ağızlığı, vb. perakende ticareti
250	Bakkallık, bayilik, büfecilik	47.27.03	Toz, kesme ve kristal şeker perakende ticareti
251	Bakkallık, bayilik, büfecilik	47.27.08	Homojenize gıda müstahzarları ve diyetetik ürünlerin perakende ticareti (glüten içermeyen gıda maddeleri, sodyum içermeyen tuzlar vb. ile besin yönünden zenginleştirilmiş sporcu gıdaları vb.)
252	Bakkallık, bayilik, büfecilik	47.27.99	Başka yerde sınıflandırılmamış diğer gıda ürünlerinin perakende ticareti
253	Bakkallık, bayilik, büfecilik	47.62.03	Gazete ve dergilerin perakende ticareti
254	Bakkallık, bayilik, büfecilik	56.11.12	Oturacak yeri olmayan fast-food (hamburger, sandviç, tost vb.) satış yerleri (büfeler dahil), al götür tesisleri (içli pide ve lahmacun fırınları hariç) ve benzerleri tarafından sağlanan diğer yemek hazırlama ve sunum faaliyetleri
255	Balıkçılık	03.11.01	Deniz ve kıyı sularında yapılan balıkçılık (gırgır balıkçılığı, dalyancılık dahil)
256	Balıkçılık	03.11.02	Deniz kabuklularının (midye, ıstakoz vb.), yumuşakçaların, diğer deniz canlıları ve ürünlerinin toplanması (sedef, doğal inci, sünger, mercan, deniz yosunu, vb.)
257	Balıkçılık	03.12.01	Tatlı su balıklçılığı
258	Balıkçılık	03.21.01	Denizde yapılan balık yetiştiriciliği
259	Balıkçılık	03.21.02	Denizde yapılan diğer su ürünleri yetiştiriciliği
260	Balıkçılık	03.22.01	Tatlı sularda yapılan balık yetiştiriciliği
261	Balıkçılık	03.22.02	Tatlısu ürünleri yetiştiriciliği (balık hariç)
262	Balıkçılık	10.20.03	Balıkların, kabuklu deniz hayvanlarının ve yumuşakçaların işlenmesi ve saklanması
263	Balıkçılık	10.20.04	Balık, kabuklu deniz hayvanı ve yumuşakça ürünlerinin üretimi
264	Balıkçılık	10.20.05	Balık unları, kaba unları ve peletlerinin üretilmesi (insan tüketimi için)
265	Balıkçılık	10.20.07	Pişirilmemiş balık yemekleri imalatı (mayalanmış balık, balık hamuru, balık köftesi vb.)
266	Balıkçılık	10.20.08	Balıkların, kabukluların, yumuşakçaların veya diğer su omurgasızlarının unları, kaba unları ve peletlerinin üretimi (insan tüketimine uygun olmayan) ile bunların diğer yenilemeyen ürünlerinin üretimi
267	Balıkçılık	46.32.05	Balık, kabuklular, yumuşakçalar ve diğer deniz ürünleri toptan ticareti
268	Balıkçılık	47.23.01	Balık, kabuklu hayvanlar ve yumuşakçaların perakende ticareti
269	Besicilik, celeplik	01.41.31	Sütü sağılan büyükbaş hayvan yetiştiriciliği (sütü için inek ve manda yetiştiriciliği)
270	Besicilik, celeplik	01.42.09	Diğer sığır ve manda yetiştiriciliği (sütü için yetiştirilenler hariç)
271	Besicilik, celeplik	01.43.01	At ve at benzeri diğer hayvan yetiştiriciliği (eşek, katır veya bardo vb.)
272	Besicilik, celeplik	01.44.01	Deve ve devegillerin yetiştiriciliği
273	Besicilik, celeplik	01.45.01	Koyun ve keçi (davar) yetiştiriciliği (işlenmemiş süt, kıl, tiftik, yapağı, yün vb. üretimi dahil)
274	Besicilik, celeplik	01.48.02	İpekböceği yetiştiriciliği ve koza üretimi
275	Besicilik, celeplik	01.62.01	Hayvan üretimini destekleyici olarak sürülerin güdülmesi, başkalarına ait hayvanların beslenmesi, kümeslerin temizlenmesi, kırkma, sağma, barınak sağlama, nalbantlık vb. faaliyetler
276	Besicilik, celeplik	13.10.08	İpeğin kozadan ayrılması ve sarılması
277	Besicilik, celeplik	46.23.01	Canlı hayvanların toptan ticareti (kümes hayvanları hariç)
278	Besicilik, celeplik	46.24.01	Ham deri, post ve kürklü deri toptan ticareti
279	Besicilik, celeplik	46.46.04	Hayvan sağlığı ile ilgili ilaçların toptan ticareti (serum, aşı, vb.)
280	Besicilik, celeplik	47.73.02	Veterinerlik ürünlerinin perakende ticareti
281	Besicilik, celeplik	47.76.04	Canlı büyükbaş ve küçükbaş hayvanların perakende ticareti (ev hayvanları hariç)
282	Bitkisel ürünlerle ilgili faaliyetler	01.13.21	Mantar ve yer mantarları (domalan) yetiştirilmesi
283	Bitkisel ürünlerle ilgili faaliyetler	01.30.03	Dikim için sebze fidesi, meyve fidanı vb. yetiştirilmesi
284	Bitkisel ürünlerle ilgili faaliyetler	01.30.90	Dikim için çiçek ve diğer bitkilerin yetiştirilmesi (dekoratif amaçlarla bitki ve çim yetiştirilmesi dahil, sebze fidesi, meyve fidanı hariç)
285	Bitkisel ürünlerle ilgili faaliyetler	01.61.03	Bitkisel üretimi destekleyici tarımsal amaçlı sulama faaliyetleri
286	Bitkisel ürünlerle ilgili faaliyetler	01.61.04	Bitkisel üretimi destekleyici ilaçlama ve zirai mücadele faaliyetleri (zararlı otların imhası dahil, hava yoluyla yapılanlar hariç)
287	Bitkisel ürünlerle ilgili faaliyetler	01.61.06	Hava yoluyla yapılan bitkisel üretimi destekleyici gübreleme, ilaçlama ve zirai mücadele faaliyetleri (zararlı otların imhası dahil)
288	Bitkisel ürünlerle ilgili faaliyetler	01.63.01	Hasat sonrası diğer ürünlerin ayıklanması ve temizlenmesi ile ilgili faaliyetler (pamuğun çırçırlanması ve nişastalı kök ürünleri hariç)
289	Bitkisel ürünlerle ilgili faaliyetler	01.63.02	Sert kabuklu ürünlerin kabuklarının kırılması ve temizlenmesi ile ilgili faaliyetler
290	Bitkisel ürünlerle ilgili faaliyetler	01.63.03	Haşhaş vb. ürünlerin sürtme, ezme ve temizlenmesi ile ilgili faaliyetler
291	Bitkisel ürünlerle ilgili faaliyetler	01.63.04	Mısır vb. ürünlerin tanelenmesi ve temizlenmesi ile ilgili faaliyetler
292	Bitkisel ürünlerle ilgili faaliyetler	01.63.05	Tütünün sınıflandırılması, balyalanması vb. hizmetler
293	Bitkisel ürünlerle ilgili faaliyetler	01.63.06	Nişastalı kök ürünlerinin ayıklanması ve temizlenmesi (patates vb.)
294	Bitkisel ürünlerle ilgili faaliyetler	01.63.07	Çırçırlama faaliyeti
295	Bitkisel ürünlerle ilgili faaliyetler	01.63.90	Hasat sonrası bitkisel ürünler ile ilgili diğer faaliyetler
296	Bitkisel ürünlerle ilgili faaliyetler	02.10.01	Baltalık olarak işletilen ormanların yetiştirilmesi (kağıtlık ve yakacak odun üretimine yönelik olanlar dahil)
297	Bitkisel ürünlerle ilgili faaliyetler	02.10.02	Orman yetiştirmek için fidan ve tohum üretimi
298	Bitkisel ürünlerle ilgili faaliyetler	02.30.01	Tabii olarak yetişen odun dışı orman ürünlerinin toplanması
299	Bitkisel ürünlerle ilgili faaliyetler	02.40.03	Ormanda silvikültürel hizmet faaliyetleri (seyreltilmesi, budanması, repikaj vb.)
300	Bitkisel ürünlerle ilgili faaliyetler	10.31.01	Patatesin işlenmesi ve saklanması (dondurulmuş, kurutulmuş, suyu çıkartılmış, ezilmiş patates imalatı) (soyulması dahil)
301	Bitkisel ürünlerle ilgili faaliyetler	12.00.04	Tütün ürünleri imalatı
302	Bitkisel ürünlerle ilgili faaliyetler	46.11.01	Çiçeklerin, bitkilerin, diğer tarımsal hammaddelerin, tekstil hammaddelerinin ve yarı mamul malların bir ücret veya sözleşmeye dayalı olarak toptan satışını yapan aracılar
303	Bitkisel ürünlerle ilgili faaliyetler	46.21.06	Pamuk toptan ticareti
304	Bitkisel ürünlerle ilgili faaliyetler	46.21.99	Başka yerde sınıflandırılmamış diğer tarımsal ham maddelerin toptan ticareti
305	Börekçilik	56.11.07	Börekçilerin faaliyetleri (imalatçıların faaliyetleri ile seyyar olanlar hariç)
306	Çeşitli gıdaların imalatı	10.31.02	Patates cipsi, patates çerezi, patates unu ve kaba unlarının imalatı
307	Çeşitli gıdaların imalatı	10.39.01	Sebze ve meyve konservesi imalatı (salça, domates püresi dahil, patatesten olanlar hariç)
507	Dericilik	15.11.14	İşlenmiş derinin başka işlemlere tabi tutulmaksızın yalnızca tamburda ütülenmesi ve kurutulması
308	Çeşitli gıdaların imalatı	10.39.02	Kavrulmuş, tuzlanmış vb. şekilde işlem görmüş sert kabuklu yemişler ile bu meyvelerin püre ve ezmelerinin imalatı (pişirilerek yapılanlar)
309	Çeşitli gıdaların imalatı	10.39.03	Meyve ve sebzelerden jöle, pekmez, marmelat, reçel vb. imalatı (pestil imalatı dahil)
310	Çeşitli gıdaların imalatı	10.39.04	Tuzlu su, sirke, sirkeli su, yağ veya diğer koruyucu çözeltilerle korunarak saklanan sebze ve meyvelerin imalatı (turşu, salamura yaprak, sofralık zeytin vb. dahil)
311	Çeşitli gıdaların imalatı	10.39.05	Dondurulmuş veya kurutulmuş meyve ve sebzelerin imalatı
312	Çeşitli gıdaların imalatı	10.39.07	Susamın işlenmesi ve tahin imalatı
313	Çeşitli gıdaların imalatı	10.81.01	Şeker kamışından, pancardan, palmiyeden, akça ağaçtan şeker (sakkaroz) ve şeker ürünleri imalatı veya bunların rafine edilmesi (sıvı şeker ve melas üretimi dahil)
314	Çeşitli gıdaların imalatı	10.84.02	Sirke ve sirke ikamelerinin imalatı
315	Çeşitli gıdaların imalatı	10.84.03	Sos imalatı (soya sosu, ketçap, mayonez, hardal sosu, çemen, mango sosu vb.) (baharat, sirke ve salça hariç)
316	Çeşitli gıdaların imalatı	10.84.05	Gıda tuzu imalatı
317	Çeşitli gıdaların imalatı	10.85.01	Hazır yemek imalatı (vakumla paketlenmiş veya korunmuş olanlar) (lokanta ve catering hizmetleri hariç)
318	Çeşitli gıdaların imalatı	10.86.04	Homojenize gıda müstahzarları ve diyetetik gıdaların imalatı
319	Çeşitli gıdaların imalatı	10.89.01	Hazır çorba (geleneksel ve yöresel olarak imal edilenler dahil) ile hazır et suyu, balık suyu, tavuk suyu ve konsantrelerinin imalatı
320	Çeşitli gıdaların imalatı	10.89.02	Maya ve kabartma tozu imalatı (bira mayası dahil)
321	Çeşitli gıdaların imalatı	10.89.04	Suni bal, karamela, kabuksuz yumurta, yumurta albümini vb. imalatı
322	Çeşitli gıdaların imalatı	10.89.05	Bitki özsu ve ekstreleri ile peptik maddeler, müsilaj ve kıvam arttırıcı maddelerin imalatı (kola konsantresi, malt özü, meyan balı dahil)
323	Çeşitli gıdaların imalatı	10.89.99	Başka yerde sınıflandırılmamış çeşitli gıda ürünleri imalatı (çabuk bozulan hazır gıdalar, peynir fondüleri, renklendirilmiş/tatlandırılmış şeker şurupları vb. dahil)
324	Değirmencilik, zahirecilik	10.61.01	Kahvaltılık tahıl ürünleri ile diğer taneli tahıl ürünlerinin imalatı
325	Değirmencilik, zahirecilik	10.61.02	Tahılların öğütülmesi ve un imalatı
326	Değirmencilik, zahirecilik	10.61.05	Pirinç, pirinç ezmesi ve pirinç unu imalatı (çeltik fabrikası ve ürünleri dahil)
327	Değirmencilik, zahirecilik	10.61.06	İrmik imalatı
328	Değirmencilik, zahirecilik	10.61.07	Ön pişirme yapılmış veya başka şekilde hazırlanmış tane halde hububat imalatı (bulgur dahil, mısır hariç)
329	Değirmencilik, zahirecilik	10.61.08	Sebzelerin ve baklagillerin öğütülmesi ve sebze unu ile ezmelerinin imalatı (karışımları ile hazır karıştırılmış sebze unları dahil) (pişirilerek yapılanlar hariç)
330	Değirmencilik, zahirecilik	10.61.90	Dövülmüş diğer tahıl ürünlerinin imalatı (bulgur ve irmik hariç)
331	Değirmencilik, zahirecilik	10.62.01	Nişasta imalatı (buğday, pirinç, patates, mısır, manyok vb. ürünlerden)
332	Değirmencilik, zahirecilik	10.62.04	Yaş mısırın öğütülmesi
333	Değirmencilik, zahirecilik	10.62.05	Glüten imalatı
334	Değirmencilik, zahirecilik	10.73.03	Makarna, şehriye, kuskus ve benzeri mamullerin imalatı (doldurulmuş veya dondurulmuş olanlar dahil)
335	Değirmencilik, zahirecilik	46.21.02	Tahıl toptan ticareti (buğday, arpa, çavdar, yulaf, mısır, çeltik vb.)
336	Değirmencilik, zahirecilik	46.21.03	Yağlı tohum ve yağlı meyvelerin toptan ticareti
337	Değirmencilik, zahirecilik	46.31.08	Kuru bakliyat ürünleri toptan ticareti (fasulye, mercimek, nohut, vb.)
338	Değirmencilik, zahirecilik	47.21.04	Kuru bakliyat ürünleri perakende ticareti (fasulye, mercimek, nohut, vb.)
339	Değirmencilik, zahirecilik	47.27.06	Hububat, un ve zahire ürünleri perakende ticareti (bulgur, pirinç, mısır, vb.)
340	Dondurmacılık	10.52.01	Dondurma imalatı (sade, sebzeli, meyveli vb.)
341	Dondurmacılık	10.52.02	Şerbetli diğer yenilebilen buzlu gıdaların imalatı
342	Dondurmacılık	46.36.04	Dondurma ve diğer yenilebilir buzların toptan ticareti
343	Dondurmacılık	47.27.02	Dondurma, aromalı yenilebilir buzlar vb. perakende ticareti (pastanelerde verilen hizmetler hariç)
344	Dondurmacılık	56.11.10	Dondurmacıların faaliyetleri (imalatçıların faaliyetleri ile seyyar olanlar hariç)
345	Evcil hayvan bakımı, ticareti	01.48.03	Evcil hayvanların yetiştirilmesi ve üretilmesi (balık hariç) (kedi, köpek, kuşlar, hamsterler vb.)
346	Evcil hayvan bakımı, ticareti	10.91.01	Çiftlik hayvanları için hazır yem imalatı
347	Evcil hayvan bakımı, ticareti	10.92.01	Ev hayvanları için hazır gıda imalatı (kedi ve köpek mamaları, kuş ve balık yemleri vb.)
348	Evcil hayvan bakımı, ticareti	46.21.01	Hayvan yemi toptan ticareti
349	Evcil hayvan bakımı, ticareti	46.38.02	Ev hayvanları için yemlerin veya yiyeceklerin toptan ticareti (çiftlik hayvanları için olanlar hariç)
350	Evcil hayvan bakımı, ticareti	47.76.01	Ev hayvanları, bunların mama ve gıdaları ile eşyalarının perakende ticareti
351	Evcil hayvan bakımı, ticareti	96.99.04	Ev hayvanları ve terk edilmiş hayvanlar için bakım hizmetleri
352	Fırıncılık	10.61.09	Fırıncılık ürünlerinin imalatında kullanılan hamur ve un karışımlarının imalatı (sebze un karışımları hariç)
353	Fırıncılık	10.71.02	Ekmek imalatı (sade pide dahil)
354	Fırıncılık	10.71.04	Simit imalatı
355	Fırıncılık	46.36.02	Fırıncılık mamullerinin toptan ticareti
356	Fırıncılık	47.24.01	Ekmek, pasta ve unlu mamullerin perakende ticareti
357	Fırıncılık	56.11.04	Oturacak yeri olmayan içli pide ve lahmacun fırınlarının faaliyetleri (al götür tesisi olarak hizmet verenler)
505	Dericilik	15.11.11	Kürklü derinin ve postların kazınarak temizlenmesi, kırkılması, tüylerinin yolunması ve ağartılması (postlu derilerin terbiyesi dahil)
358	Gübre, zirai ilaç imalatı, ticareti	20.15.01	Fosfatlı veya potasyumlu gübreler, iki (azot ve fosfor veya fosfor ve potasyum) veya üç besin maddesi (azot, fosfor ve potasyum) içeren gübreler, sodyum nitrat ile diğer kimyasal ve mineral gübrelerin imalatı
359	Gübre, zirai ilaç imalatı, ticareti	20.15.02	Bileşik azotlu ürünlerin imalatı (gübreler hariç)
360	Gübre, zirai ilaç imalatı, ticareti	20.20.13	Çimlenmeyi önleyici ve bitki gelişimini düzenleyici ürün imalatı
361	Gübre, zirai ilaç imalatı, ticareti	20.20.90	Diğer zirai kimyasal ürünlerin imalatı (gübre ve azotlu bileşik imalatı hariç)
362	Gübre, zirai ilaç imalatı, ticareti	46.85.02	Suni gübrelerin toptan ticareti (gübre mineralleri, gübre ve azot bileşikleri ve turba ile amonyum sülfat, amonyum nitrat, sodyum nitrat, potasyum nitrat vb. dahil, nitrik asit, sülfonitrik asit ve amonyak hariç)
363	Gübre, zirai ilaç imalatı, ticareti	46.85.03	Zirai kimyasal ürünlerin toptan ticareti (haşere ilaçları, yabancı ot ilaçları, dezenfektanlar, mantar ilaçları, çimlenmeyi önleyici ürünler, bitki gelişimini düzenleyiciler ve diğer zirai kimyasal ürünler)
364	Gübre, zirai ilaç imalatı, ticareti	46.85.04	Hayvansal veya bitkisel gübrelerin toptan ticareti (kapalı alanda yapılan ticaret)
365	Gübre, zirai ilaç imalatı, ticareti	46.85.05	Hayvansal veya bitkisel gübrelerin toptan ticareti (açık alanda yapılan ticaret)
366	Gübre, zirai ilaç imalatı, ticareti	47.76.03	Gübre ve zirai kimyasal ürünlerin perakende ticareti
367	Kantincilik	56.22.01	Kantinlerin faaliyetleri
368	Kasaplık	10.11.01	Etin işlenmesi ve saklanması (mezbahacılık) (kümes hayvanlarının eti hariç)
369	Kasaplık	10.12.01	Kümes hayvanları etlerinin üretimi (taze veya dondurulmuş) (yenilebilir sakatatları dahil)
370	Kasaplık	10.12.02	Kümes hayvanlarının kesilmesi, temizlenmesi veya paketlenmesi işi ile uğraşan mezbahaların faaliyetleri
371	Kasaplık	10.13.01	Et ve kümes hayvanları etlerinden üretilen pişmemiş köfte vb. ürünlerin imalatı
372	Kasaplık	10.13.02	Et ve kümes hayvanları etlerinden üretilen sosis, salam, sucuk, pastırma, kavurma et, konserve et, salamura et, jambon vb. tuzlanmış, kurutulmuş veya tütsülenmiş ürünlerin imalatı (yemek olanlar hariç)
373	Kasaplık	10.13.03	Et ve sakatat unları imalatı (et ve kümes hayvanları etlerinden üretilen)
374	Kasaplık	10.13.04	Sığır, koyun, keçi vb. hayvanların sakatat ve yağlarından yenilebilir ürünlerin imalatı
375	Kasaplık	32.99.99	Başka yerde sınıflandırılmamış diğer imalatlar (bağırsak (ipek böceği guddesi hariç), kursak ve mesaneden mamul eşyalar dahil, tıbbi amaçlı steril olanlar hariç)
376	Kasaplık	46.32.01	Kümes hayvanları ve av hayvanları etlerinin toptan ticareti
377	Kasaplık	46.32.02	Et toptan ticareti (av hayvanları ve kümes hayvanları etleri hariç)
378	Kasaplık	46.32.03	Yenilebilir sakatat (ciğer, işkembe, böbrek, taşlık vb.) toptan ticareti
379	Kasaplık	46.32.04	Et ürünlerinin toptan ticareti (salam, sosis, sucuk, pastırma vb.)
380	Kasaplık	47.22.02	Et ürünleri perakende ticareti (sosis, salam, sucuk, pastırma vb.)
381	Kasaplık	47.22.05	Et perakende ticareti
382	Kasaplık	47.22.06	Sakatat perakende ticareti
383	Kuruyemiş imalatı, ticareti	10.39.06	Leblebi imalatı ile kavrulmuş çekirdek, yerfıstığı vb. üretimi (sert kabuklular hariç)
384	Kuruyemiş imalatı, ticareti	46.31.01	Fındık, antep fıstığı, yer fıstığı ve ceviz toptan ticareti (kavrulmuş olanlar hariç)
385	Kuruyemiş imalatı, ticareti	46.31.09	Kavrulmuş veya işlenmiş kuru yemiş toptan ticareti (leblebi, kavrulmuş fındık, fıstık, çekirdek vb.)
386	Kuruyemiş imalatı, ticareti	46.31.10	Kuru üzüm toptan ticareti
387	Kuruyemiş imalatı, ticareti	46.31.11	Kuru incir toptan ticareti
388	Kuruyemiş imalatı, ticareti	46.31.12	Kuru kayısı toptan ticareti
389	Kuruyemiş imalatı, ticareti	47.21.05	Kuru yemiş perakende ticareti
390	Lokantacılık	56.11.01	Genel lokanta ve restoranların (içkili ve içkisiz) faaliyetleri
391	Lokantacılık	56.11.02	Çorbacıların ve işkembecilerin faaliyetleri (imalatçıların faaliyetleri ile seyyar olanlar hariç)
392	Lokantacılık	56.11.03	Döner, ciğer, kokoreç, köfte ve kebapçıların faaliyeti (garson servisi sunanlar ile self servis sunanlar dahil; imalatçıların ve al götür tesislerin faaliyetleri ile seyyar olanlar hariç)
393	Lokantacılık	56.11.05	Pizzacıların faaliyeti (garson servisi sunanlar ile self servis sunanlar dahil; imalatçıların ve al götür tesislerin faaliyetleri ile seyyar olanlar hariç)
394	Lokantacılık	56.11.06	Mantıcı ve gözlemecilerin faaliyeti (garson servisi sunanlar ile self servis sunanlar dahil; imalatçıların ve al götür tesislerinin faaliyetleri ile seyyar olanlar hariç)
395	Lokantacılık	56.11.09	Yiyecek ağırlıklı hizmet veren kafe ve kafeteryaların faaliyetleri
396	Lokantacılık	56.11.11	Oturacak yeri olan fast-food (hamburger, sandviç, tost vb.) satış yerleri (büfeler dahil) tarafından sağlanan yemek hazırlama ve sunum faaliyetleri
397	Lokantacılık	56.11.13	Lahmacun ve pidecilik (içli pide (kıymalı, peynirli vb.)) faaliyeti (garson servisi sunanlar ile self servis sunanlar dahil; imalatçıların ve al götür tesislerin faaliyetleri ile seyyar olanlar hariç)
398	Lokantacılık	56.11.90	Diğer lokantaların faaliyetleri
399	Lokantacılık	56.21.01	Özel günlerde dışarıya yemek hizmeti sunan işletmelerin faaliyetleri
400	Lokantacılık	56.22.02	Hava yolu şirketleri ve diğer ulaştırma şirketleri için sözleşmeye bağlı düzenlemelere dayalı olarak yiyecek hazırlanması ve temini hizmetleri
401	Lokantacılık	56.22.90	Dışarıya yemek sunan diğer işletmelerin faaliyetleri (spor, fabrika, işyeri, üniversite vb. mensupları için tabldot servisi vb. dahil; özel günlerde hizmet verenler hariç)
402	Manavlık	47.21.01	Taze sebze ve meyve perakende ticareti (manav ürünleri ile kültür mantarı dahil)
403	Meşrubat imalatı, ticareti	10.32.01	Katkısız sebze ve meyve suları imalatı
404	Meşrubat imalatı, ticareti	10.32.02	Konsantre meyve ve sebze suyu imalatı
405	Meşrubat imalatı, ticareti	10.51.04	Süt temelli hafif içeceklerin imalatı (kefir, salep vb.)
406	Meşrubat imalatı, ticareti	11.01.01	Damıtılmış alkollü içeceklerin imalatı (viski, brendi, cin, likör, rakı, votka, kanyak vb.)
407	Meşrubat imalatı, ticareti	11.01.03	Etil alkol üretimi (doğal özellikleri değiştirilmemiş/tağyir edilmemiş, alkol derecesi <%80)
408	Meşrubat imalatı, ticareti	11.02.01	Üzümden şarap, köpüklü şarap, şampanya vb. imalatı
409	Meşrubat imalatı, ticareti	11.02.02	Üzüm şırası imalatı
410	Meşrubat imalatı, ticareti	11.03.01	Elma şarabı ve diğer fermente meyve içeceklerinin imalatı
411	Meşrubat imalatı, ticareti	11.04.02	Diğer damıtılmamış fermente içeceklerin imalatı (vermut ve benzeri içkiler dahil)
412	Meşrubat imalatı, ticareti	11.05.01	Bira imalatı
413	Meşrubat imalatı, ticareti	11.06.01	Malt imalatı
414	Meşrubat imalatı, ticareti	11.07.01	Doğal veya suni maden sularının üretimi (tatlandırılmış ve aromalandırılmış olanlar dahil)
415	Meşrubat imalatı, ticareti	11.07.04	Boza imalatı
416	Meşrubat imalatı, ticareti	11.07.90	Diğer alkolsüz içeceklerin imalatı (içme suyu ve maden suları ile boza imalatı hariç)
417	Meşrubat imalatı, ticareti	46.17.04	İçeceklerin toptan satışı ile ilgili aracıların faaliyetleri
418	Meşrubat imalatı, ticareti	46.34.02	Meyve ve sebze suları, maden suyu, meşrubat ve diğer alkolsüz içeceklerin toptan ticareti (su hariç)
419	Pastanecilik, tatlıcılık	10.71.01	Taze pastane ürünleri imalatı (yaş pasta, kuru pasta, poğaça, kek, börek, pay, turta, waffles vb.)
420	Pastanecilik, tatlıcılık	10.71.03	Hamur tatlıları imalatı (tatlandırılmış kadayıf, lokma tatlısı, baklava vb.)
421	Pastanecilik, tatlıcılık	10.72.01	Peksimet, bisküvi, gofret, dondurma külahı, kağıt helva vb. ürünlerin imalatı (çikolata kaplı olanlar dahil)
422	Pastanecilik, tatlıcılık	10.72.02	Tatlı veya tuzlu hafif dayanıklı fırın ve pastane ürünlerinin imalatı (kurabiyeler, krakerler, galeta, gevrek halkalar vb.)
423	Pastanecilik, tatlıcılık	56.11.08	Pastanelerin ve tatlıcıların (sütlü, şerbetli vb.) faaliyeti (garson servisi sunanlar ile self servis sunanlar dahil; imalatçıların ve al götür tesislerin faaliyetleri ile seyyar olanlar hariç)
424	Pastanecilik, tatlıcılık	56.30.08	Boza, şalgam ve sahlep sunum faaliyeti
425	Şarküteri ürünleri imalatı, ticareti	10.12.03	Kümes hayvanlarının yağlarının sofra yağına çevrilmesi
426	Şarküteri ürünleri imalatı, ticareti	10.41.01	Ayçiçek yağı imalatı
427	Şarküteri ürünleri imalatı, ticareti	10.41.02	Bitkisel sıvı yağ (yenilebilen) imalatı (soya, susam, haşhaş, pamuk, fındık, kolza, hardal vb. yağlar) (zeytin yağı, ayçiçeği yağı ve mısır yağı hariç)
428	Şarküteri ürünleri imalatı, ticareti	10.41.03	Beziryağı imalatı
429	Şarküteri ürünleri imalatı, ticareti	10.41.05	Prina yağı imalatı (diğer küspelerden elde edilen yağlar dahil) (mısır yağı hariç)
430	Şarküteri ürünleri imalatı, ticareti	10.41.06	Kakao yağı, badem yağı, kekik yağı, defne yağı, hurma çekirdeği veya babassu yağı, keten tohumu yağı, Hint yağı, tung yağı ve diğer benzer yağların imalatı (bezir yağı hariç)
431	Şarküteri ürünleri imalatı, ticareti	10.41.07	Zeytinyağı imalatı (saf, sızma, rafine)
432	Şarküteri ürünleri imalatı, ticareti	10.41.10	Balık ve deniz memelilerinden yağ elde edilmesi
433	Şarküteri ürünleri imalatı, ticareti	10.42.01	Margarin ve benzeri yenilebilir katı yağların imalatı
434	Şarküteri ürünleri imalatı, ticareti	10.51.01	Süt imalatı, işlenmiş (pastörize edilmiş, sterilize edilmiş, homojenleştirilmiş ve/veya yüksek ısıdan geçirilmiş) (katı veya toz halde süt hariç)
435	Şarküteri ürünleri imalatı, ticareti	10.51.02	Peynir, lor ve çökelek imalatı
436	Şarküteri ürünleri imalatı, ticareti	10.51.03	Süt tozu, peynir özü (kazein), süt şekeri (laktoz) ve peynir altı suyu (kesilmiş sütün suyu) imalatı (katı veya toz halde süt, krema dahil)
437	Şarküteri ürünleri imalatı, ticareti	10.51.90	Sütten yapılan diğer ürünlerin imalatı
438	Şarküteri ürünleri imalatı, ticareti	10.62.06	Mısır yağı imalatı
439	Şarküteri ürünleri imalatı, ticareti	46.31.05	Zeytin (işlenmiş) toptan ticareti
440	Şarküteri ürünleri imalatı, ticareti	46.33.01	Süt ürünleri toptan ticareti (işlenmiş süt, süt tozu, yoğurt, peynir, kaymak, tereyağı vb.)
441	Şarküteri ürünleri imalatı, ticareti	46.33.02	Yumurta ve yumurta ürünleri toptan ticareti
442	Şarküteri ürünleri imalatı, ticareti	46.33.03	Hayvan veya bitkisel kaynaklı yenilebilir sıvı ve katı yağların toptan ticareti (tereyağı hariç)
443	Şarküteri ürünleri imalatı, ticareti	47.21.03	Zeytin perakende ticareti
444	Şarküteri ürünleri imalatı, ticareti	47.27.01	Süt ve süt ürünleri perakende ticareti (dondurma perakende ticareti hariç)
445	Şarküteri ürünleri imalatı, ticareti	47.27.05	Katı ve sıvı yağların perakende ticareti (yemeklik yağ dahil)
446	Şarküteri ürünleri imalatı, ticareti	47.27.07	Yumurta perakende ticareti
447	Şekercilik, çikolatacılık	10.81.03	Akçaağaç şurubu imalatı
448	Şekercilik, çikolatacılık	10.82.01	Çikolata ve kakao içeren şekerlemelerin imalatı (beyaz çikolata ve sürülerek yenebilen kakaolu ürünler hariç)
449	Şekercilik, çikolatacılık	10.82.02	Şekerlemelerin ve şeker pastillerinin imalatı (bonbon şekeri vb.) (kakaolu şekerlemeler hariç)
450	Şekercilik, çikolatacılık	10.82.03	Sürülerek yenebilen kakaolu ürünlerin imalatı
451	Şekercilik, çikolatacılık	10.82.04	Lokum, pişmaniye, helva, karamel, koz helva, fondan, beyaz çikolata vb. imalatı (tahin helvası dahil)
452	Şekercilik, çikolatacılık	10.82.05	Ciklet imalatı (sakız)
453	Şekercilik, çikolatacılık	10.82.06	Sert kabuklu yemiş, meyve, meyve kabuğu ve diğer bitki parçalarından şekerleme imalatı (meyan kökü hülasaları dahil)
454	Şekercilik, çikolatacılık	10.82.07	Kakao tozu, kakao ezmesi/hamuru ve kakao yağı imalatı
455	Şekercilik, çikolatacılık	46.36.01	Çikolata ve şekerleme toptan ticareti (helva, lokum, akide şekeri, bonbon şekeri vb. dahil)
456	Şekercilik, çikolatacılık	47.24.02	Çikolata ve şekerleme perakende ticareti
457	Tavukçuluk	01.47.01	Kümes hayvanlarının yetiştirilmesi (tavuk, hindi, ördek, kaz ve beç tavuğu vb.)
458	Tavukçuluk	01.47.02	Kuluçkahanelerin faaliyetleri
459	Tavukçuluk	01.47.03	Kümes hayvanlarından yumurta üretilmesi
460	Tavukçuluk	01.48.99	Başka yerde sınıflandırılmamış diğer hayvan yetiştiriciliği
461	Tavukçuluk	10.12.04	Kuş tüyü ve ince kuş tüyü imalatı (derileri dahil)
462	Tavukçuluk	46.11.02	Canlı hayvanların bir ücret veya sözleşmeye dayalı olarak toptan satışını yapan aracılar
463	Tavukçuluk	46.23.02	Canlı kümes hayvanları toptan ticareti
464	Tavukçuluk	47.76.05	Canlı kümes hayvanlarının perakende ticareti
465	Yaş sebze, meyve ticareti	10.39.99	Başka yerde sınıflandırılmamış meyve ve sebzelerin başka yöntemlerle işlenmesi ve saklanması (kesilmiş ve paketlenmiş olanlar dahil)
466	Yaş sebze, meyve ticareti	46.17.02	Yaş sebze ve meyvelerin toptan satışı ile ilgili aracıların faaliyetleri (kabzımallık ve aracı üretici birlikleri dahil)
467	Yaş sebze, meyve ticareti	46.31.02	Taze incir ve üzüm toptan ticareti
468	Yaş sebze, meyve ticareti	46.31.03	Narenciye toptan ticareti
469	Yaş sebze, meyve ticareti	46.31.04	Diğer taze meyve sebze toptan ticareti (patates dahil)
470	Yaş sebze, meyve ticareti	46.31.06	Kültür mantarı toptan ticareti
471	Yaş sebze, meyve ticareti	46.31.90	Diğer işlenmiş veya korunmuş sebze ve meyve toptan ticareti (reçel, pekmez, pestil, salamura veya turşusu yapılmış olanlar dahil) (fındık, incir, üzüm, narenciye, zeytin, kültür mantarı ve kuru yemiş hariç)
524	Dokumacılık	13.20.21	Havlı, şönil, havlu, pelüş, tırtıl ve benzeri ilmeği kesilmemiş dokuma kumaşlar ile tafting kumaş imalatı
472	Yufkacılık, kadayıfçılık	10.72.03	Tatlandırılmamış dayanıklı hamur tatlıları imalatı (pişirilmiş olsun olmasın tatlandırılmamış kadayıf, baklava vb.) (yufka imalatı dahil)
473	Ayakkabıcılık	15.20.06	Ayakkabı ve terliklerin kauçuk parçalarının imalatı
474	Ayakkabıcılık	15.20.07	Ayakkabı ve terliklerin plastik parçalarının imalatı
475	Ayakkabıcılık	15.20.15	Deriden ayakkabı, mes, bot, çizme, postal, terlik, vb. imalatı (ortopedik ayakkabı ve kayak ayakkabısı hariç)
476	Ayakkabıcılık	15.20.17	Plastik veya kauçuktan ayakkabı, bot, çizme, postal, terlik, vb. imalatı (ortopedik ayakkabı ve kayak ayakkabısı hariç)
477	Ayakkabıcılık	15.20.18	Tekstilden ve diğer malzemelerden ayakkabı, mes, bot, çizme, postal, terlik, vb. imalatı (tamamıyla tekstilden olanlar ile ortopedik ayakkabı ve kayak ayakkabısı hariç)
478	Ayakkabıcılık	15.20.19	Ayakkabı ve terliklerin deri parçalarının imalatı ile sayacılık faaliyetleri
479	Ayakkabıcılık	46.42.02	Ayakkabı toptan ticareti (spor ayakkabıları hariç)
480	Ayakkabıcılık	46.42.08	Ayakkabı malzemeleri toptan ticareti
481	Ayakkabıcılık	47.63.07	Spor ayakkabısı perakende ticareti (kayak botları dahil)
482	Ayakkabıcılık	47.72.01	Ayakkabı, terlik vb. perakende ticareti (kavafiye dahil; spor ayakkabıları ile tamamı tekstilden olanlar hariç)
483	Ayakkabıcılık	47.72.06	Ayakkabı parçaları perakende ticareti (deri, ayakkabı sayası, topuk, topuk yastığı, ayakkabı bağları vb.)
484	Ayakkabıcılık	95.23.01	Ayakkabı ve deri eşyaların onarım ve bakımı (deri giyim eşyası hariç)
485	Ayakkabıcılık	96.99.11	Ayakkabı boyama hizmetleri
486	Çamaşırhane, kuru temizleme, ütücülük hizmetleri	96.10.01	Giyim eşyası ve diğer tekstil ürünlerini ütüleme hizmetleri
487	Çamaşırhane, kuru temizleme, ütücülük hizmetleri	96.10.02	Çamaşırhane hizmetleri
488	Çamaşırhane, kuru temizleme, ütücülük hizmetleri	96.10.03	Kuru temizleme hizmetleri
489	Deri aksesuar imalatı, ticareti	15.12.07	Deri, kösele, karma deri ve diğer malzemelerden bavul ve çanta, deriden sigaralık, deri ayakkabı bağı, kişisel bakım, dikiş vb. amaçlı seyahat seti vb. ürünlerin imalatı
490	Deri aksesuar imalatı, ticareti	15.12.08	Deriden veya diğer malzemelerden saraçlık ve koşum takımı imalatı (kamçı, semer, eyer, tasma kayışı, heybe vb.)
491	Deri aksesuar imalatı, ticareti	15.12.09	Deri saat kayışı imalatı
492	Deri aksesuar imalatı, ticareti	46.16.02	Deri eşyalar ve seyahat aksesuarlarının bir ücret veya sözleşmeye dayalı olarak toptan satışını yapan aracılar
493	Deri aksesuar imalatı, ticareti	46.49.01	Deri eşyalar ve seyahat aksesuarları toptan ticareti
494	Deri aksesuar imalatı, ticareti	47.72.02	Bavul, el çantası ve diğer seyahat aksesuarlarının perakende ticareti (deriden, deri bileşimlerinden, plastik levhadan, tekstil malzemesinden, vulkanize (ebonit) elyaf veya mukavvadan)
495	Deri aksesuar imalatı, ticareti	47.72.05	Saraciye ürünleri ve koşum takımı perakende ticareti (eyer, semer, vb.)
496	Deri aksesuar imalatı, ticareti	47.72.90	Deriden veya deri bileşimlerinden diğer ürünlerin perakende ticareti (deri veya deri bileşimli giyim eşyası hariç)
497	Deri giyim eşyası imalatı, onarımı	14.24.01	Deri giyim eşyası imalatı (deri ayakkabı hariç)
498	Deri giyim eşyası imalatı, onarımı	14.24.02	Kürklü deriden giyim eşyası, giysi aksesuarları ve diğer eşyaların imalatı (kürkten şapka ve başlık hariç)
499	Deri giyim eşyası imalatı, onarımı	95.29.07	Deri ve deri bileşimli giyim eşyaları ile kürk giyim eşyalarının onarımı
500	Deri giyim eşyası ticareti	46.16.01	Deri giyim eşyası, kürk ve ayakkabının bir ücret veya sözleşmeye dayalı olarak toptan satışını yapan aracılar
501	Deri giyim eşyası ticareti	46.42.04	Kürk ve deriden giyim eşyalarının toptan ticareti
502	Deri giyim eşyası ticareti	47.71.03	Kürklü deriden giyim eşyalarının perakende ticareti (işlenmiş kürklü deriler dahil)
503	Deri giyim eşyası ticareti	47.71.07	Deri veya deri bileşimli giyim eşyası perakende ticareti
504	Dericilik	15.11.10	Deri ve kürklü deri imalatı (kürkün ve derinin tabaklanması, sepilenmesi, boyanması, cilalanması ve işlenmesi)(işlenmiş derinin başka işlemlere tabi tutulmaksızın yalnızca tamburda ütülenmesi ve kurutulması hariç)
508	Dericilik	15.12.99	Deriden veya deri bileşimlerinden başka yerde sınıflandırılmamış diğer ürünlerin imalatı (makinelerde veya mekanik cihazlarda kullanılan veya diğer teknik kullanımlar için ürünler dahil)
509	Dericilik	46.24.02	Tabaklanmış deri, güderi ve kösele toptan ticareti
510	Dokumacılık	13.10.03	Doğal pamuk elyafının imalatı (kardelenmesi, taraklanması vb.)
511	Dokumacılık	13.10.05	Doğal yün ve tiftik elyafının imalatı (kardelenmesi, taraklanması, yün yağının giderilmesi, karbonize edilmesi ve yapağının boyanması vb.)
512	Dokumacılık	13.10.06	Doğal jüt, keten ve diğer bitkisel tekstil elyaflarının imalatı (kardelenmesi, taraklanması vb.) (pamuk hariç)
513	Dokumacılık	13.10.09	Sentetik veya suni devamsız elyafın kardelenmesi ve taraklanması
514	Dokumacılık	13.10.10	Doğal ipeğin bükülmesi ve iplik haline getirilmesi
515	Dokumacılık	13.10.12	Pamuk elyafının bükülmesi ve iplik haline getirilmesi
516	Dokumacılık	13.10.13	Yün ve tiftik elyafının bükülmesi ve iplik haline getirilmesi
517	Dokumacılık	13.10.14	Jüt, keten ve diğer bitkisel tekstil elyaflarının bükülmesi ve iplik haline getirilmesi (pamuk hariç)
518	Dokumacılık	13.10.15	Suni ve sentetik elyafların bükülmesi ve iplik haline getirilmesi (filament ipliği ve suni ipek elyafı imalatı hariç)
519	Dokumacılık	13.20.14	Kot kumaşı imalatı
520	Dokumacılık	13.20.16	Pamuklu dokuma kumaş imalatı
521	Dokumacılık	13.20.17	Doğal kıl ve yünden dokuma kumaş imalatı
525	Dokumacılık	13.20.22	Suni ve sentetik filamentlerden ve devamsız elyaflardan dokuma kumaş imalatı
526	Dokumacılık	13.20.23	Dokuma yoluyla imitasyon kürk kumaş imalatı
527	Dokumacılık	13.91.01	Örgü ve tığ işi kumaşların imalatı (penye ve havlı kumaşlar ile raschel veya benzeri makineler ile örülen tül kumaş, perdelik kumaş vb. örgü veya tığ ile örülmüş kumaşlar dahil)
528	Dokumacılık	13.91.02	Örme yoluyla imitasyon kürk kumaşı imalatı
529	Dokumacılık	13.92.04	Tekstilden yer bezi, bulaşık bezi, toz bezi vb. temizlik bezleri imalatı
530	Dokumacılık	13.92.06	Tekstilden çuval, torba, çanta ve benzerlerinin imalatı
531	Dokumacılık	13.92.09	Bayrak, sancak ve flama imalatı
532	Dokumacılık	13.92.11	Branda, tente, stor (güneşlik), yelken, çadır ve kamp malzemeleri imalatı (şişme yataklar dahil)
533	Dokumacılık	13.94.02	Ağ ve ağ ürünleri imalatı, sicim, kınnap, halat veya urgandan (balık ağı, yük boşaltma ağları, vb.)
534	Dokumacılık	13.94.03	Sicim, urgan, halat, kordon ve benzerleri imalatı (kauçuk veya plastik emdirilmiş, kaplanmış olanlar dahil)
535	Dokumacılık	13.95.01	Dokusuz kumaş ve dokusuz kumaştan yapılan ürünlerin imalatı (giyim eşyası hariç)
536	Dokumacılık	13.96.01	Dokunabilir ipliklerden metalize iplik ve metalize iplik ile bunlardan dokuma kumaş imalatı (giyim ve döşemecilikte kullanılan)
537	Dokumacılık	13.96.03	Dar dokuma kumaşların imalatı (etiket, arma ve diğer benzeri eşyalar hariç)
538	Dokumacılık	13.96.05	Teknik kullanım amaçlı tekstil ürünleri ve eşyaları imalatı (fitil, lüks lambası gömleği, tekstil malzemesinden hortumlar, taşıma veya konveyör bantları, elek bezi ve süzgeç bezi dahil)
539	Dokumacılık	13.96.06	Kord bezi imalatı
540	Dokumacılık	13.96.08	Kaplanmış veya emdirilmiş tekstil kumaşlarının imalatı (cilt kapağı için mensucat, mühendis muşambası, tiyatro dekorları, tuval vb. dahil)
541	Dokumacılık	13.96.09	Cam elyafından kumaş imalatı
542	Dokumacılık	13.96.12	Tekstilden örtü ve kılıf imalatı (araba, makine, mobilya vb. için)
543	Dokumacılık	17.24.03	Tekstil duvar kaplamalarının imalatı
544	Dokumacılık	20.60.01	Kardelenmemiş ve taranmamış suni ve sentetik elyaf imalatı
545	Dokumacılık	20.60.02	Sentetik filament ipliği ve sentetik monofilamentlerin, şeritlerin ve benzerlerinin imalatı (poliamidden ve polyesterden yüksek mukavemetli filament iplikler dahil) (bükülü, katlı ve tekstürize olanlar hariç)
546	Dokumacılık	22.12.09	Kauçuk kaplanmış, emdirilmiş, sıvanmış ve lamine edilmiş tekstil kumaşlarının imalatı, ana bileşeni kauçuk olanlar (kord bezi hariç)
547	Dokumacılık	33.19.01	Tentelerin, kamp ekipmanlarının, çuvalların ve balıkçılık ağları gibi diğer hazır tekstil malzemelerinin onarımı
548	Dokumacılık	46.41.03	Kumaş toptan ticareti (manifatura ürünleri dahil)
549	Dokumacılık	46.41.90	Diğer tekstil ürünleri toptan ticareti
550	Dokumacılık	47.51.03	Kumaş perakende ticareti
551	Dokumacılık	47.78.30	Tekstilden çuval, torba, vb. perakende ticareti (eşya paketleme amacıyla kullanılanlar)
552	Ev tekstil ürünleri imalatı, ticareti	13.92.01	Yatak örtü takımları, yatak çarşafları, yastık kılıfları, masa örtüsü ile tuvalet ve mutfakta kullanılan örtülerin imalatı (el ve yüz havluları dahil)
553	Ev tekstil ürünleri imalatı, ticareti	13.92.02	Yorgan, kuştüyü yorgan, minder, puf, yastık, halı yastık, uyku tulumu ve benzerlerinin imalatı
554	Ev tekstil ürünleri imalatı, ticareti	13.92.03	Perdelerin ve iç storların, perde veya yatak saçaklarının, farbelalarının ve malzemelerinin imalatı (gipür, hazır tül perde ve kalın perdeler dahil)
555	Ev tekstil ürünleri imalatı, ticareti	13.92.05	Battaniye imalatı
556	Ev tekstil ürünleri imalatı, ticareti	13.99.02	Oya, dantel ve nakış imalatı (kapitone ürünleri dahil) ile tül ve diğer ağ kumaşların (dokuma, örgü (triko) veya tığ işi (kroşe) olanlar hariç) imalatı
557	Ev tekstil ürünleri imalatı, ticareti	13.99.04	Tekstil kırpıntısı imalatı (yatak, yorgan, yastık, şilte ve benzeri doldurmak için)
558	Ev tekstil ürünleri imalatı, ticareti	46.16.04	Tekstil ürünlerinin bir ücret veya sözleşmeye dayalı olarak toptan satışını yapan aracılar (iplik, kumaş, ev tekstili, perde vb. ürünler) (giyim eşyaları hariç)
559	Ev tekstil ürünleri imalatı, ticareti	46.41.01	Evde kullanılan tekstil takımları, perdeler ve çeşitli tekstil malzemesinden ev eşyaları toptan ticareti
560	Ev tekstil ürünleri imalatı, ticareti	47.51.05	Evde kullanılan tekstil takımları ve çeşitli tekstil malzemesinden ev eşyaları perakende ticareti
561	Ev tekstil ürünleri imalatı, ticareti	47.53.01	Perde, iç stor, perde veya yatak saçağı ve farbelası perakende ticareti
562	Halı yıkama hizmetleri	96.10.04	Halı ve kilim yıkama hizmetleri
563	Halıcılık, kilimcilik	13.93.01	Halı (duvar halısı dahil) ve kilim imalatı (paspas, yolluk ve benzeri tekstil yer kaplamaları dahil)
564	Halıcılık, kilimcilik	13.93.02	Halı, kilim vb. için çözgücülük, halı oymacılığı vb. faaliyetler
565	Halıcılık, kilimcilik	46.47.02	Halı, kilim, vb. yer kaplamaları toptan ticareti
566	Halıcılık, kilimcilik	47.53.02	Halı, kilim ve diğer tekstil yer döşemeleri perakende ticareti (keçeden olanlar dahil)
567	İkinci el tekstil ürünleri ticareti	47.79.06	Kullanılmış giysiler ve aksesuarlarının perakende ticareti
568	Konfeksiyonculuk	14.10.01	Giyim eşyası imalatı (örgü veya tığ işi kumaştan olanlar) (spor ve bebek giysileri hariç)
569	Konfeksiyonculuk	14.10.02	Bebek giyim eşyası imalatı (örgü veya tığ işi kumaştan)
570	Konfeksiyonculuk	14.10.03	Spor ve antrenman giysileri, kayak kıyafetleri, yüzme kıyafetleri vb. imalatı (örgü veya tığ işi kumaştan olanlar)
571	Konfeksiyonculuk	14.10.04	Çorap imalatı (örme ve tığ işi olan külotlu çorap, tayt çorap, kısa kadın çorabı, erkek çorabı, patik ve diğer çoraplar)
572	Konfeksiyonculuk	14.21.01	Dış giyim eşyası imalatı (örgü veya tığ işi olanlar hariç) (spor ve bebek giysileri hariç)
573	Konfeksiyonculuk	14.21.02	Bebek dış giyim eşyası imalatı (örgü veya tığ işi kumaştan olanlar hariç)
574	Konfeksiyonculuk	14.21.03	Gelinlik imalatı
575	Konfeksiyonculuk	14.22.01	Atlet, fanila, külot, slip, iç etek, kombinezon, jüp, jüpon, sütyen, korse vb. iç çamaşırı imalatı (örgü veya tığ işi kumaştan olanlar hariç)
576	Konfeksiyonculuk	14.22.02	Gecelik, sabahlık, pijama, bornoz ve ropdöşambır imalatı (örgü veya tığ işi kumaştan olanlar hariç)
577	Konfeksiyonculuk	14.22.03	Bebek iç giyim eşyalarının imalatı (örgü veya tığ işi kumaştan olanlar hariç)
578	Konfeksiyonculuk	14.22.04	Çorap bağları, jartiyer, pantolon askıları vb. iç giyim eşyalarının imalatı (her tür kumaştan)
579	Konfeksiyonculuk	14.23.00	İş giysisi imalatı (dikişsiz plastik olanlar ile ateşe dayanıklı ve koruyucu güvenlik kıyafetleri hariç)
580	Konfeksiyonculuk	14.29.01	Giyim eşyası imalatı (keçeden veya diğer dokusuz kumaştan ya da emdirilmiş veya kaplanmış tekstil kumaşından olanlar)
581	Konfeksiyonculuk	14.29.02	Spor ve antrenman giysileri, kayak kıyafetleri, yüzme kıyafetleri vb. imalatı (örgü veya tığ işi kumaştan olanlar hariç)
582	Konfeksiyonculuk	14.29.03	Yazma, tülbent, eşarp, vb. imalatı (her tür kumaştan)
583	Konfeksiyonculuk	14.29.05	Şapka, kep, başlık, kasket ve el manşonları ile bunların parçalarının imalatı (kürkten şapka ve başlıklar dahil)
584	Konfeksiyonculuk	32.99.10	Ateşe dayanıklı ve koruyucu güvenlik kıyafetleri ve başlıkları ile diğer güvenlik ürünlerinin imalatı (solunum ekipmanları ve gaz maskeleri hariç)
585	Konfeksiyonculuk	46.16.03	Giyim eşyalarının bir ücret veya sözleşmeye dayalı olarak toptan satışını yapan aracılar (deri giyim eşyaları hariç)
586	Konfeksiyonculuk	46.42.01	Bebek giysileri, sporcu giysileri ve diğer giyim eşyalarının toptan ticareti
587	Konfeksiyonculuk	46.42.05	Dış giyim eşyalarının toptan ticareti (iş giysileri ile triko olanlar dahil, kürk ve deriden olanlar hariç)
588	Konfeksiyonculuk	47.55.10	Bebek arabaları, pusetleri, bebek yürüteçleri, bebek taşıyıları, bebek oto koltukları gibi bebek ekipmanlarının perakende ticareti
589	Konfeksiyonculuk	47.71.01	Bebek ve çocuk giyim eşyası perakende ticareti
590	Konfeksiyonculuk	47.71.04	Diğer dış giyim perakende satışı (palto, kaban, anorak, takım elbise, ceket, pantolon, şort (tekstil kumaşından veya örgü ve tığ işi))
591	Konfeksiyonculuk	47.71.08	Süveter, kazak, hırka, yelek ve benzeri eşyaların perakende ticareti
592	Konfeksiyonculuk	47.71.09	İş giysisi perakende ticareti
593	Konfeksiyonculuk	47.71.11	Spor giysisi perakende ticareti
594	Konfeksiyonculuk	47.71.12	Gelinlik perakende ticareti
595	Konfeksiyonculuk	47.71.99	Belirli bir mala tahsis edilmiş mağazalarda başka yerde sınıflandırılmamış giyim eşyası perakende ticareti (plastikten, vulkanize kauçuktan, kağıttan, dokusuz kumaştan ya da emdirilmiş veya kaplanmış tekstil kumaşından giysiler)
596	Konfeksiyonculuk	77.22.02	Gelinlik, kostüm, tekstil, giyim eşyası, ayakkabı ve mücevherlerin kiralanması ve operasyonel leasingi
597	Tasarım faaliyetleri	74.14.00	Diğer uzmanlaşmış tasarım faaliyetleri (endüstriyel ürün ve moda tasarım, iç tasarım ve grafik tasarım faaliyetleri hariç)
598	Tekstil baskıcılığı, boyacılığı	13.30.01	Kumaş ve tekstil ürünlerini ağartma ve boyama hizmetleri (giyim eşyası dahil)
599	Tekstil baskıcılığı, boyacılığı	13.30.02	Tekstil elyaf ve ipliklerini ağartma ve boyama hizmetleri (kasarlama dahil)
600	Tekstil baskıcılığı, boyacılığı	13.30.03	Kumaş ve tekstil ürünlerine baskı yapılması hizmetleri (giyim eşyası dahil, emprime baskı dahil, transfer baskı hariç)
601	Tekstil baskıcılığı, boyacılığı	13.30.04	Kumaş ve tekstil ürünlerine ilişkin diğer bitirme hizmetleri (apreleme, pliseleme, sanforlama, vb. dahil)
602	Tekstil baskıcılığı, boyacılığı	13.30.05	Kumaş ve tekstil ürünlerine transfer baskı yapılması hizmetleri
603	Tekstil baskıcılığı, boyacılığı	96.10.90	Diğer tekstil temizleme hizmetleri ile giyim eşyası ve diğer tekstil ürünlerini boyama ve renklendirme hizmetleri (imalat aşamasında yapılanlar hariç)
604	Terzilik	14.10.05	Sahne ve gösteri elbiseleri imalatı, dokuma, örgü (triko) ve tığ işi (kroşe), vb. kumaştan olanlar
605	Terzilik	14.21.04	Siparişe göre ölçü alınarak dış giyim eşyası imalatı, dokuma, örgü (triko) ve tığ işi (kroşe), vb. kumaştan olanlar (terzilerin faaliyetleri) (giyim eşyası tamiri ile gömlek imalatı hariç)
606	Terzilik	95.29.02	Giyim eşyası ve ev tekstil ürünlerinin onarımı ve tadilatı (deri giyim eşyaları hariç)
607	Tuhafiye imalatı, ticareti	13.96.02	Tekstil malzemelerinden parça halinde kordonlar; işleme yapılmamış şeritçi eşyası ve benzeri süs eşyalarının imalatı
608	Tuhafiye imalatı, ticareti	13.96.04	Tekstil malzemelerinden dokuma etiket, rozet, arma ve diğer benzeri eşyaların imalatı
609	Tuhafiye imalatı, ticareti	13.96.07	Tekstille kaplanmış kauçuk iplik veya kordon ile kauçuk veya plastikle kaplanmış veya emdirilmiş tekstilden iplik veya şeritler ve bunlardan yapılmış mensucat imalatı
610	Tuhafiye imalatı, ticareti	13.99.03	Keçe, basınçlı hassas giysi dokumaları, tekstilden ayakkabı bağı, pudra ponponu vb. imalatı
611	Tuhafiye imalatı, ticareti	13.99.06	Gipe iplik ve şeritlerin, şönil ipliklerin, şenet ipliklerin imalatı (metalize olanlar ile gipe lastikler hariç)
612	Tuhafiye imalatı, ticareti	14.29.04	Eldiven, kemer, şal, papyon, kravat, saç fileleri, kumaş mendil, atkı, fular vb. giysi aksesuarları imalatı (kürklü deriden olanlar hariç)
613	Tuhafiye imalatı, ticareti	15.12.11	Kumaş ve diğer malzemelerden saat kayışı imalatı (metal olanlar hariç)
614	Tuhafiye imalatı, ticareti	32.99.02	Kot vb. baskı düğmeleri, çıtçıtlar, düğmeler, fermuarlar vb. imalatı (düğme formları ve fermuar parçaları dahil)
615	Tuhafiye imalatı, ticareti	46.21.07	Yün ve tiftik toptan ticareti
616	Tuhafiye imalatı, ticareti	46.41.02	Tuhafiye ürünleri toptan ticareti
617	Tuhafiye imalatı, ticareti	46.41.04	İplik toptan ticareti (tuhafiye ürünleri ile dikiş ipliği hariç)
618	Tuhafiye imalatı, ticareti	46.42.03	Çorap ve giysi aksesuarlarının toptan ticareti
619	Tuhafiye imalatı, ticareti	46.42.06	İç giyim eşyalarının toptan ticareti
620	Tuhafiye imalatı, ticareti	46.86.04	Tekstil elyafı toptan ticareti
621	Tuhafiye imalatı, ticareti	47.51.02	Tuhafiye ürünleri perakende ticareti
622	Tuhafiye imalatı, ticareti	47.51.04	Halı, goblen veya nakış yapımı için temel materyallerin perakende ticareti
623	Tuhafiye imalatı, ticareti	47.51.90	Diğer tekstil ürünleri perakende ticareti
624	Tuhafiye imalatı, ticareti	47.71.02	Giysi aksesuarları perakende ticareti (eldiven, kravat, şapka, eşarp, şal, mendil, kemer, pantolon askısı, şemsiye, baston, vb.)
625	Tuhafiye imalatı, ticareti	47.71.05	İç giyim ve çorap perakende ticareti
626	Tuhafiye imalatı, ticareti	47.78.16	Yün, tiftik vb. perakende ticareti
627	Arzuhalcilik, danışmanlık, bilgi hizmetleri	63.92.00	Diğer bilgi hizmeti faaliyetleri
628	Arzuhalcilik, danışmanlık, bilgi hizmetleri	70.20.01	İşletme ve diğer idari danışmanlık faaliyetleri
629	Arzuhalcilik, danışmanlık, bilgi hizmetleri	70.20.02	İnsan kaynakları yönetim danışmanlığı faaliyetleri
630	Arzuhalcilik, danışmanlık, bilgi hizmetleri	73.20.03	Piyasa ve kamuoyu araştırma faaliyetleri
631	Arzuhalcilik, danışmanlık, bilgi hizmetleri	74.99.03	İşyeri komisyonculuğu faaliyetleri (küçük ve orta ölçekli işletmelerin alım ve satımının düzenlenmesi vb.)
632	Arzuhalcilik, danışmanlık, bilgi hizmetleri	78.10.01	İş bulma acentelerinin faaliyetleri (işe girecek kişilerin seçimi ve yerleştirilmesi faaliyetleri dahil)
633	Arzuhalcilik, danışmanlık, bilgi hizmetleri	78.20.02	Geçici iş bulma acenteleri ile diğer insan kaynaklarının sağlanması faaliyetleri
634	Arzuhalcilik, danışmanlık, bilgi hizmetleri	82.10.01	Büro yönetimi ve destek faaliyetleri (sanal ofis, hazır ofis ve paylaşımlı ofis hariç)
635	Arzuhalcilik, danışmanlık, bilgi hizmetleri	82.10.02	Sanal ofis, hazır ofis ve paylaşımlı ofis yönetimi ve destek faaliyetleri
636	Arzuhalcilik, danışmanlık, bilgi hizmetleri	82.20.01	Çağrı merkezlerinin faaliyetleri
637	Arzuhalcilik, danışmanlık, bilgi hizmetleri	82.99.99	Başka yerde sınıflandırılmamış diğer işletme destek hizmeti faaliyetleri
638	Arzuhalcilik, danışmanlık, bilgi hizmetleri	96.99.08	Arzuhalcilerin faaliyetleri
639	Arzuhalcilik, danışmanlık, bilgi hizmetleri	96.99.13	Şecere bulma faaliyetleri
640	Basın, yayım, iletişim	58.11.01	Kitap yayımı (broşür, risale, ansiklopedi vb. dahil; çocuk kitaplarının, ders kitaplarının ve yardımcı ders kitaplarının yayımlanması hariç)
641	Basın, yayım, iletişim	58.11.03	Çocuk kitaplarının yayımlanması
642	Basın, yayım, iletişim	58.11.04	Ders kitaplarının ve yardımcı ders kitaplarının yayımlanması (sözlük, atlas, grafikler, haritalar vb. dahil)
643	Basın, yayım, iletişim	58.12.00	Gazetelerin yayımlanması (haftada en az dört kez yayımlananlar) (reklam gazeteleri dahil)
644	Basın, yayım, iletişim	58.13.02	Eğitime destek amaçlı dergi ve süreli yayınların yayımlanması (haftada dörtten az yayımlananlar)
645	Basın, yayım, iletişim	58.13.03	Bilimsel, teknik, kültürel vb. dergi ve süreli yayınların yayımlanması (haftada dörtten az yayımlananlar)
646	Basın, yayım, iletişim	58.13.90	Diğer dergi ve süreli yayınların yayımlanması (haftada dörtten az yayımlananlar) (çizgi roman, magazin dergileri vb.)
647	Basın, yayım, iletişim	59.12.01	Sinema filmi, video ve televizyon programları çekim sonrası faaliyetleri
648	Basın, yayım, iletişim	59.20.01	Müzik yayıncılığı faaliyetleri (basılı müzik notaları, elektronik formdaki müzikal besteler, müzikal ses diskleri, indirilebilir müzikler vb.)
649	Basın, yayım, iletişim	59.20.02	Ses kayıt ve canlı kayıt faaliyetleri (seslerin, sözlerin ve müziğin ses kayıt stüdyosunun özel teknik ekipmanları kullanılarak kaydedilmesi ile konferans, seminer, konser vb. canlı etkinliklerde yapılan kayıt hizmetleri vb.)
650	Basın, yayım, iletişim	59.20.06	Radyo programı yapımcılık faaliyetleri
651	Basın, yayım, iletişim	60.10.09	Radyo yayıncılığı ve ses dağıtım faaliyetleri
652	Basın, yayım, iletişim	60.20.00	Televizyon programcılığı, yayıncılığı ve video dağıtım faaliyetleri
653	Basın, yayım, iletişim	74.20.28	Bağımsız foto muhabirlerinin faaliyetleri
654	Bireysel sanatkârlık faaliyetleri	58.11.02	Bağımsız yazarlar tarafından kendi ürettikleri içeriklerin yayımlanması faaliyetleri
655	Bireysel sanatkârlık faaliyetleri	90.11.00	Edebiyat eseri oluşturma ve müzikal kompozisyon faaliyetleri
656	Bireysel sanatkârlık faaliyetleri	90.12.00	Görsel sanatlar yaratıcılık faaliyetleri
657	Bireysel sanatkârlık faaliyetleri	90.13.00	Diğer sanatsal yaratıcılık faaliyetleri
658	Çeşitli malların ticareti	46.19.01	Uzmanlaşmamış toptan ticaret ile ilgili aracıların faaliyetleri
659	Çeşitli malların ticareti	46.42.07	Şemsiye toptan ticareti (güneş ve bahçe şemsiyeleri hariç)
660	Çeşitli malların ticareti	46.49.99	Başka yerde sınıflandırılmamış diğer ev eşyaları ve ev gereçlerinin toptan ticareti
661	Çeşitli malların ticareti	46.86.99	Başka yerde sınıflandırılmamış ara ürün (tarım hariç) toptan ticareti
662	Çeşitli malların ticareti	46.90.01	Uzmanlaşmamış toptan ticaret (bir başka ülkeyle yapılan toptan ticaret hariç)
663	Çeşitli malların ticareti	46.90.04	Başka ülkeyle yapılan uzmanlaşmamış toptan ticaret
664	Çeşitli malların ticareti	47.12.01	Uzmanlaşmamış diğer perakende ticaret (gıda, içecek ve tütün ağırlıklı olmayan)
665	Çeşitli malların ticareti	47.55.99	Başka yerde sınıflandırılmamış diğer ev eşyalarının perakende ticareti
666	Çeşitli malların ticareti	47.78.99	Başka yerde sınıflandırılmamış diğer yeni malların perakende ticareti
667	Çeşitli malların ticareti	96.99.10	Jeton ile çalışan kişisel hizmet makinelerinin işletilmesi faaliyetleri (jetonlu makinelerle vesikalık fotoğraf, emanet dolapları, tartı, tansiyon ölçümü vb. hizmetler dahil; oyun ve kumar makineleri ile çamaşırhane hizmetleri hariç)
668	Çiçekçilik	01.19.02	Çiçek yetiştirilmesi (lale, kasımpatı, zambak, gül vb. ile bunların tohumları)
669	Çiçekçilik	46.21.08	Tohum (yağlı tohumlar hariç) toptan ticareti
670	Çiçekçilik	46.22.01	Çiçeklerin ve bitkilerin toptan ticareti
671	Çiçekçilik	47.76.02	Çiçek, bitki ve tohum perakende ticareti
672	Çiçekçilik	47.78.26	Yapma çiçek, yaprak ve meyveler ile mum perakende ticareti
673	Fatura tahsilat bürosu işletmeciliği	82.91.00	Tahsilat ve kredi kayıt bürolarının faaliyetleri
674	Fotoğrafçılık	46.43.10	Fotoğrafçılıkla ilgili ürünlerin toptan ticareti
675	Fotoğrafçılık	47.78.22	Fotoğrafçılık malzemeleri ve aletlerinin perakende ticareti
676	Fotoğrafçılık	74.20.22	Tüketicilere yönelik fotoğrafçılık faaliyetleri (pasaport, okul, düğün vb. için vesikalık ve portre fotoğrafçılığı vb.)
677	Fotoğrafçılık	74.20.25	Hava ve su altı fotoğrafçılığı faaliyetleri
678	Fotoğrafçılık	74.20.26	Reklamcılık ile ilgili fotoğrafçılık faaliyetleri (reklam görselleri, broşür, gazete ilanı, katalog vb. için ticari ürünlerin, moda kıyafetlerinin, makinelerin, binaların, kişilerin vb.nin fotoğraflarının çekilmesi)
679	Fotoğrafçılık	74.20.27	Etkinlik fotoğrafçılığı ve etkinliklerin videoya çekilmesi faaliyetleri (düğün, mezuniyet, konferans, resepsiyon, moda gösterileri, spor ve diğer ilgi çekici olayların fotoğraflanması veya videoya çekilmesi)
680	Fotoğrafçılık	74.20.29	Fotoğraf işleme faaliyetleri
681	Fotoğrafçılık	74.20.90	Diğer fotoğrafçılık faaliyetleri (fotomikrografi, mikrofilm hizmetleri, fotoğrafların restorasyonu ve rötuşlama vb.)
682	Fotokopicilik, tez yazımı	18.12.08	Fotokopi çekme faaliyetleri
683	Hediyelik eşya imalatı, ticareti	23.15.04	Küçük cam eşya imalatı (biblo, vb. süs eşyası, boncuklar, imitasyon inciler/taşlar, imitasyon mücevherler, vb. dahil)
684	Hediyelik eşya imalatı, ticareti	23.41.02	Seramik ve porselenden heykelcik, vazo, biblo, vb. süs eşyası imalatı (oyuncaklar hariç)
685	Hediyelik eşya imalatı, ticareti	23.70.02	Doğal taşlardan, mermerden, su mermerinden, travertenden, kayağantaşından süs eşyası imalatı (lületaşı, kehribar ve benzerlerinden olanlar dahil)
686	Hediyelik eşya imalatı, ticareti	32.13.01	İmitasyon (taklit) takılar ve ilgili eşyaların imalatı
687	Hediyelik eşya imalatı, ticareti	32.99.15	Suni balmumu ile suni mumların ve müstahzar mumların imalatı
688	Hediyelik eşya imalatı, ticareti	32.99.18	Fildişi, kemik, boynuz, sedef gibi hayvansal malzemelerden oyma eşyaların imalatı
689	Hediyelik eşya imalatı, ticareti	46.49.12	Hediyelik eşya toptan ticareti (pipo, tespih, bakır süs eşyaları, imitasyon takılar dahil)
690	Hediyelik eşya imalatı, ticareti	47.78.04	Hediyelik eşyaların, el işi ürünlerin ve imitasyon takıların perakende ticareti (sanat eserleri hariç)
691	Kağıt, kağıt ürünleri imalatı, ticareti	17.11.08	Kağıt hamuru imalatı
692	Kağıt, kağıt ürünleri imalatı, ticareti	17.12.07	Kağıt ve mukavva imalatı
693	Kağıt, kağıt ürünleri imalatı, ticareti	17.21.10	Bürolarda, dükkanlarda ve benzeri yerlerde kullanılan kağıt veya mukavvadan dosya veya evrak tasnif kutuları, mektup kutuları ve benzeri eşyaların imalatı
694	Kağıt, kağıt ürünleri imalatı, ticareti	17.21.11	Kağıt ve kartondan torba ve çanta imalatı
695	Kağıt, kağıt ürünleri imalatı, ticareti	17.21.12	Kağıt veya mukavvadan koli, kutu ve benzeri muhafazaların imalatı
696	Kağıt, kağıt ürünleri imalatı, ticareti	17.21.13	Oluklu kağıt ve mukavva imalatı
697	Kağıt, kağıt ürünleri imalatı, ticareti	17.22.03	Kağıt veya mukavvadan tepsi, tabak, kase, bardak ve benzerlerinin imalatı
698	Kağıt, kağıt ürünleri imalatı, ticareti	17.23.04	Kullanıma hazır karbon kağıdı, kendinden kopyalı kağıt ve diğer kopyalama veya transfer kağıtları, mumlu teksir kağıdı, kağıttan ofset tabakalar ile tutkallı veya yapışkanlı kağıtların imalatı
699	Kağıt, kağıt ürünleri imalatı, ticareti	17.23.06	Kağıt veya mukavvadan ana niteliği bilgi içermeyen eğitim ve ticari kırtasiye malzemeleri imalatı (ajandalar, defterler, sicil defterleri, muhasebe defterleri, ciltler, kayıt formları ve diğer benzeri kırtasiye ürünleri)
700	Kağıt, kağıt ürünleri imalatı, ticareti	17.23.07	Kağıt veya mukavvadan dosya, portföy dosya, klasör ve benzerlerinin imalatı
701	Kağıt, kağıt ürünleri imalatı, ticareti	17.23.08	Kullanıma hazır basım ve yazım kağıdı ile bilgisayar çıktısı için kullanılacak kağıt ve benzerlerinin imalatı
702	Kağıt, kağıt ürünleri imalatı, ticareti	17.23.09	Baskısız zarf, mektup kartı, yazışma kartı ve benzerlerinin imalatı
703	Kağıt, kağıt ürünleri imalatı, ticareti	17.25.01	Kağıt veya mukavvadan etiketlerin imalatı
704	Kağıt, kağıt ürünleri imalatı, ticareti	17.25.02	Sigara kağıdı, kağıt ve mukavvadan bobin, makara, masura, yumurta viyolü ve benzeri kağıt, mukavva veya kağıt hamurundan destekler ile kağıttan hediyelik ve süs eşyaları imalatı
705	Kağıt, kağıt ürünleri imalatı, ticareti	17.25.03	Filtre kağıdı, kartonları ve mukavvaları, kağıt hamurundan filtre edici blok ve levhalar ile kalıplanmış ya da sıkıştırılmış eşyaların imalatı (kağıt veya karton esaslı contalar ve rondelalar dahil)
706	Kağıt, kağıt ürünleri imalatı, ticareti	17.25.99	Başka yerde sınıflandırılmamış kağıt ve mukavvadan diğer ürünlerin imalatı
707	Kağıt, kağıt ürünleri imalatı, ticareti	46.18.04	Kağıt ve karton (mukavva) ile ilgili belirli ürünlerin toptan satışı ile ilgili aracıların faaliyetleri
708	Kağıt, kağıt ürünleri imalatı, ticareti	46.86.03	Dökme halde kağıt ve mukavva toptan ticareti
709	Kauçuk, plastik ürünlerin imalatı, ticareti	15.12.10	Plastik veya kauçuk saat kayışı imalatı
710	Kauçuk, plastik ürünlerin imalatı, ticareti	19.20.17	Vazelin, parafin mumu, petrol mumu, petrol koku, petrol bitümeni ve diğer petrol ürünlerinin imalatı
711	Kauçuk, plastik ürünlerin imalatı, ticareti	20.17.01	Birincil formda sentetik kauçuk imalatı
712	Kauçuk, plastik ürünlerin imalatı, ticareti	22.12.01	Kauçuktan tüp, boru ve hortumların imalatı (vulkanize kauçuktan)
713	Kauçuk, plastik ürünlerin imalatı, ticareti	22.12.02	Kauçuktan silgi, rondela, conta, tekne veya iskele usturmaçaları, gözenekli vulkanize kauçuktan teknik işlerde kullanılan diğer eşyalar ile demiryolu, kara yolu taşıtları ve diğer araçlar için kalıplanmış parçaların imalatı
714	Kauçuk, plastik ürünlerin imalatı, ticareti	22.12.03	Kauçuktan konveyör bantları ve taşıma kayışlarının imalatı
715	Kauçuk, plastik ürünlerin imalatı, ticareti	22.12.04	Vulkanize edilmiş (kükürtle sertleştirilmiş) kauçuk imalatı (ip, kordon, levha, tabaka, şerit, çubuk ve profil halinde)
716	Kauçuk, plastik ürünlerin imalatı, ticareti	22.12.05	Rejenere kauçuk imalatı, birincil formda veya levha, tabaka veya şerit halinde
717	Kauçuk, plastik ürünlerin imalatı, ticareti	22.12.06	Kauçuktan paket lastiği, tütün kesesi, cam silecekleri, tarih ıstampaları için karakterler, tapalar, lavabo pompaları, şişeler için tıpa ve halkalar ile sert kauçuktan diğer çeşitli eşyaların imalatı
718	Kauçuk, plastik ürünlerin imalatı, ticareti	22.12.07	Kauçuktan yer döşemeleri ve paspasların imalatı
719	Kauçuk, plastik ürünlerin imalatı, ticareti	22.12.10	Kauçuktan süpürgelerin ve fırçaların imalatı
720	Kauçuk, plastik ürünlerin imalatı, ticareti	22.12.11	Kauçuktan giyim eşyası ve giysi aksesuarlarının imalatı (giysiler, eldivenler vb.)
721	Kauçuk, plastik ürünlerin imalatı, ticareti	22.21.03	Plastikten mamul halde tüp, boru, hortum ve bunların bağlantı elemanlarının imalatı
722	Kauçuk, plastik ürünlerin imalatı, ticareti	22.21.04	Plastikten yarı mamul halde profil, çubuk, tabaka, levha, blok, film, folyo, şerit, vb. imalatı
723	Kauçuk, plastik ürünlerin imalatı, ticareti	22.22.43	Plastik ambalaj malzemeleri imalatı
724	Kauçuk, plastik ürünlerin imalatı, ticareti	22.24.02	Plastikten depo, tank, fıçı ve benzeri kapların imalatı
725	Kauçuk, plastik ürünlerin imalatı, ticareti	22.24.03	Plastikten merdiven, merdiven korkuluğu, panjur, güneşlik, jaluzi, stor, vb. eşya ile bunların parçalarının imalatı
726	Kauçuk, plastik ürünlerin imalatı, ticareti	22.26.01	Plastikten sofra, mutfak, banyoda kullanılan eşya (silikon kek kalıbı, leğen, tas, kova vb.) ve diğer ev eşyası imalatı
727	Kauçuk, plastik ürünlerin imalatı, ticareti	22.26.02	Plastikten mandal, askı, sünger, sabunluk, tarak, bigudi, toka, saç firketesi, boncuk, biblo, heykelcik ve diğer eşyalar ile mamul haldeki kendinden yapışkanlı levha, şerit vb. ürünlerin imalatı
728	Kauçuk, plastik ürünlerin imalatı, ticareti	22.26.03	Makine, mobilya, kaporta, el aletleri ve benzerlerinin plastikten bağlantı parçaları, plastikten taşıyıcı bantların ve konveyör bantlarının imalatı
729	Kauçuk, plastik ürünlerin imalatı, ticareti	22.26.04	Plastikten büro ve okul malzemelerinin imalatı
730	Kauçuk, plastik ürünlerin imalatı, ticareti	22.26.05	Plastik başlık (koruma amaçlı olanlar hariç), izolasyon bağlantı parçaları ile lambaların, aydınlatma ekipmanlarının, ışıklı tabelaların, vb.nin başka yerde sınıflandırılmamış plastik kısımlarının imalatı
731	Kauçuk, plastik ürünlerin imalatı, ticareti	22.26.06	Plastikten dikişsiz giyim eşyası ve giysi aksesuarlarının imalatı (eldiven dahil)
732	Kauçuk, plastik ürünlerin imalatı, ticareti	22.26.99	Başka yerde sınıflandırılmamış diğer plastik ürünlerin imalatı
733	Kauçuk, plastik ürünlerin imalatı, ticareti	30.11.05	Yüzen rıhtımlar, dubalar, batardolar, koferdamlar, yüzen iskeleler, şamandıralar, yüzen tanklar, mavnalar, salapuryalar, yüzen vinçler, eğlence amaçlı olmayan şişme botlar vb. imalatı
734	Kauçuk, plastik ürünlerin imalatı, ticareti	31.00.09	Plastikten bank, masa, tabure, sandalye vb. mobilyaların imalatı
735	Kauçuk, plastik ürünlerin imalatı, ticareti	32.91.01	Ev veya büro temizliği için olan süpürge ve fırçaların imalatı (elektrikli olanlar hariç)
736	Kauçuk, plastik ürünlerin imalatı, ticareti	32.91.99	Başka yerde sınıflandırılmamış diğer süpürge ve fırçaların imalatı (elektrikli olanlar hariç)
737	Kauçuk, plastik ürünlerin imalatı, ticareti	32.99.01	Terzi mankeni, el kalbur ve eleği, yapma çiçek, meyve ve bitkiler, şaka ve sihirbazlık benzeri eşya, koku püskürtücüleri ve mekanizmaları, tabut vb. eşyaların imalatı (gelin çiçeği dahil)
738	Kauçuk, plastik ürünlerin imalatı, ticareti	46.49.17	Plastik sofra, mutfak ve diğer ev eşyası ile tuvalet eşyası toptan ticareti
739	Kauçuk, plastik ürünlerin imalatı, ticareti	46.86.01	Birincil formdaki plastik ve kauçuk toptan ticareti
740	Kauçuk, plastik ürünlerin imalatı, ticareti	46.86.02	Sanayide kullanım amaçlı plastik poşet, çanta, torba, çuval, vb. ambalaj malzemelerinin toptan ticareti
741	Kırtasiye imalatı, ticareti	20.59.05	Yazım ve çizim mürekkepleri ve diğer mürekkeplerin imalatı (matbaa mürekkebi imalatı hariç)
742	Kırtasiye imalatı, ticareti	25.99.04	Adi metalden büro malzemeleri imalatı (dosya kutuları, kaşeler, zımba telleri, kağıt ataçları vb.)
743	Kırtasiye imalatı, ticareti	32.99.04	Mekanik olsun veya olmasın her çeşit dolma kalem, tükenmez ve kurşun kalem ile boya kalemi, pastel boya imalatı (kalem ucu ve kurşun kalem içleri dahil)
744	Kırtasiye imalatı, ticareti	32.99.08	Tarih verme, damga, mühür veya numara verme kaşeleri, numaratör, elle çalışan basım aletleri, kabartma etiketleri, el baskı setleri, hazır daktilo şeritleri ve ıstampaların imalatı
745	Kırtasiye imalatı, ticareti	46.49.03	Kırtasiye ürünleri toptan ticareti
746	Kırtasiye imalatı, ticareti	46.49.24	Resim, fotoğraf vb. için çerçeve toptan ticareti
747	Kırtasiye imalatı, ticareti	47.62.01	Kırtasiye ürünlerinin perakende ticareti
748	Kırtasiye imalatı, ticareti	47.78.08	Büro makine ve ekipmanlarının perakende ticareti (hesaplama makineleri, daktilolar, fotokopi makineleri, tarama ve faks cihazları, çizim masaları vb.)
749	Kitapçılık	46.49.11	Kitap, dergi ve gazete toptan ticareti
750	Kitapçılık	47.61.00	Kitap perakende ticareti
751	Kitapçılık	47.79.03	İkinci el kitapların perakende ticareti (sahafların faaliyetleri)
752	Kreş işletmeciliği	85.10.02	Özel öğretim kurumları tarafından verilen okul öncesi eğitim faaliyeti (okula yönelik eğitim verilmeyen gündüz bakım (kreş) faaliyetleri hariç)
753	Kreş işletmeciliği	88.91.01	Çocuk gündüz bakım (kreş) faaliyetleri (engelli çocuklar için olanlar ile bebek bakıcılığı dahil; okul öncesi eğitim faaliyetleri ile çocuk kulüpleri (6 yaş ve üzeri çocuklar için) hariç)
754	Kurs işletmeciliği	85.32.15	Ticari sertifika veren havacılık, yelkencilik, gemicilik vb. kursların faaliyetleri
755	Kurs işletmeciliği	85.32.16	Ticari taşıt kullanma belgesi veren sürücü kurslarının faaliyetleri
756	Kurs işletmeciliği	85.32.90	Mesleki amaçlı eğitim veren diğer kursların faaliyetleri (özel öğretim kurumları tarafından verilen fiziksel veya zihinsel engellilere yönelik teknik ve mesleki ortaöğretim (ortaokul/lise) faaliyetleri ile çıraklık eğitimi faaliyetleri dahil)
757	Kurs işletmeciliği	85.51.03	Spor ve eğlence (rekreasyon) eğitimi (fitness merkezleri tarafından sağlanan eğitimler ile temel, orta ve yükseköğretim düzeyinde verilen eğitim hariç)
758	Kurs işletmeciliği	85.52.05	Kültürel eğitim (bale, dans, müzik, fotoğraf, halk oyunu, resim, drama, vb. eğitimi dahil, temel, orta ve yükseköğretim düzeyinde verilen eğitim hariç)
759	Kurs işletmeciliği	85.53.01	Sürücü kursu faaliyetleri (ticari sertifika veren sürücülük, havacılık, yelkencilik, gemicilik eğitimi hariç)
760	Kurs işletmeciliği	85.59.03	Bilgisayar, yazılım, veritabanı, vb. eğitimi veren kursların faaliyetleri (temel, orta ve yükseköğretim düzeyinde verilen eğitim hariç)
761	Kurs işletmeciliği	85.59.05	Orta öğretime, yüksek öğretime, kamu personeli vb. sınavlara yönelik kurs ve etüt merkezlerinin faaliyetleri
762	Kurs işletmeciliği	85.59.06	Biçki, dikiş, nakış, halıcılık, güzellik, berberlik, kuaförlük kurslarının faaliyetleri
763	Kurs işletmeciliği	85.59.09	Dil ve konuşma becerileri eğitimi veren kursların faaliyetleri (temel, orta ve yükseköğretim düzeyinde verilen eğitim hariç)
764	Kurs işletmeciliği	85.59.10	Mankenlik, modelistlik, stilistlik kurslarının faaliyetleri
765	Kurs işletmeciliği	85.59.12	Muhasebe eğitimi kurslarının faaliyeti
766	Kurs işletmeciliği	85.59.15	Akademik özel ders verme faaliyeti (temel, orta ve yükseköğretim düzeyinde bire bir eğitim)
767	Kurs işletmeciliği	85.59.16	Çocuk kulüplerinin faaliyetleri (6 yaş ve üzeri çocuklar için)
768	Kurs işletmeciliği	85.59.99	Başka yerde sınıflandırılmamış diğer eğitim kursu faaliyetleri (cankurtaranlık, hayatta kalma, topluluğa konuşma, hızlı okuma vb. eğitimi dahil; yetişkin okuma yazma programları ile temel, orta ve yükseköğretim düzeyinde verilen eğitim hariç)
769	Kurs işletmeciliği	85.69.00	Eğitimi destekleyici faaliyetler (eğitim rehberlik, danışmanlık (yurt dışı eğitim danışmanlığı dahil), test değerlendirme, öğrenci değişim programlarının organizasyonu, yaprak test ve soru bankası hazırlama gibi eğitimi destekleyen öğrenim dışı faaliyetler)
770	Matbaacılık	13.30.06	Serigrafi faaliyetleri
771	Matbaacılık	18.11.01	Gazetelerin basımı (haftada dört veya daha fazla yayınlananlar)
772	Matbaacılık	18.12.01	Çıkartma, takvim, ticari katalog, tanıtım broşürü, poster, satış bülteni, kartpostal, davetiye ve tebrik kartları, yıllık, rehber, resim, çizim ve boyama kitapları, çizgi roman vb. basım hizmetleri
773	Matbaacılık	18.12.02	Gazetelerin, dergilerin ve süreli yayınların basım hizmetleri (haftada dört kereden daha az yayınlananlar)
774	Matbaacılık	18.12.03	Ansiklopedi, sözlük, kitap, kitapçık, müzik eserleri ve müzik el yazmaları, atlas, harita vb. basım hizmetleri
775	Matbaacılık	18.12.04	Röprodüksiyon basımı (bir sanat eserinin aslını bozmadan basılması)
776	Matbaacılık	18.12.06	Posta pulu, damga pulu, matbu belgeler, tapu senetleri, akıllı kart, çek defterleri, kağıt para ve diğer değerli kağıtların ve benzerlerinin basım hizmetleri
777	Matbaacılık	18.12.07	Plastik, cam, metal, ağaç ve seramik üstüne baskı hizmetleri
778	Matbaacılık	18.13.01	Basımda kullanmak üzere baskı klişeleri ya da silindirleri ile diğer basım unsurlarının üretilmesi (klişecilik vb.) ile mizanpaj, dizgi, tabaka yapım hizmetleri, gravür baskı için silindirlerin kazınması veya asitle aşındırılması vb. hizmetler
779	Matbaacılık	18.13.02	Basım öncesi bilgisayar destekli hizmetler (bilgisayar destekli sayfa tasarımı ile saydam, asetat, reprografik sunum araçları ve diğer sayısal sunum ortamları, taslaklar, planlar vb. baskı ürünlerinin tasarlanması) (masa üstü yayımcılık dahil)
780	Matbaacılık	18.14.01	Ciltçilik ve ilgili hizmetler (katlama, birleştirme, dikme, yapıştırma, kesme, kapak takma gibi işlemler ile damgalama, Braille alfabesi kopyalama vb. hizmetler)
781	Matbaacılık	58.19.99	Başka yerde sınıflandırılmamış diğer yayımcılık faaliyetleri (fotoğraf, kartpostal, tebrik kartları vb. ile katalog, poster, reklam materyali vb.)
782	Müzik aletleri imalatı, onarımı, ticareti	32.20.21	Elektronik müzik aletleri veya klavyeli çalgıların imalatı (elektrik gücüyle ses üreten veya sesi güçlendirilen enstrümanlar) (dijital piyano, sintizayzır, elektrogitar, vb.)
783	Müzik aletleri imalatı, onarımı, ticareti	32.20.23	Ağızları huni gibi genişleyen neviden olan boru esaslı müzik aletleri ile diğer üflemeli müzik aletlerinin imalatı (saksafon, flüt, trombon, borazan, vb.)
784	Müzik aletleri imalatı, onarımı, ticareti	32.20.24	Vurmalı çalgıların imalatı (trampet, davul, ksilofon, zil, kas vs.)
785	Müzik aletleri imalatı, onarımı, ticareti	32.20.25	Piyanolar ve diğer klavyeli yaylı/telli çalgıların imalatı
786	Müzik aletleri imalatı, onarımı, ticareti	32.20.26	Borulu ve klavyeli orglar, armonyumlar, akordiyonlar, ağız mızıkaları (armonikalar), tulum vb. çalgıların imalatı
787	Müzik aletleri imalatı, onarımı, ticareti	32.20.27	Müzik kutuları, orkestriyonlar, laternalar, çıngıraklar vb. imalatı
788	Müzik aletleri imalatı, onarımı, ticareti	32.20.28	Metronomlar, akort çatalları (diyapazonlar) ve akort düdükleri, müzik kutuları için mekanizmalar, müzik aleti telleri ile müzik aletlerinin parça ve aksesuarlarının imalatı
789	Müzik aletleri imalatı, onarımı, ticareti	32.20.90	Diğer yaylı/telli müzik aletlerinin imalatı (saz, gitar, keman, vb.)
790	Müzik aletleri imalatı, onarımı, ticareti	32.20.99	Başka yerde sınıflandırılmamış diğer müzik aletlerinin imalatı
791	Müzik aletleri imalatı, onarımı, ticareti	46.49.06	Müzik aletleri toptan ticareti
792	Müzik aletleri imalatı, onarımı, ticareti	47.69.01	Müzik aletleri ve müzik partisyonu (nota kağıdı) perakende ticareti
793	Müzik aletleri imalatı, onarımı, ticareti	77.22.03	Müzik aletlerinin kiralanması ve operasyonel leasingi
794	Müzik aletleri imalatı, onarımı, ticareti	95.29.06	Müzik aletlerinin onarım ve bakımı (piyano akordu dahil, tarihi müzik aletleri hariç)
795	Oyuncak imalatı, ticareti	32.40.03	Yap boz, puzzle ve benzeri ürünlerin imalatı (lego vb. dahil)
796	Oyuncak imalatı, ticareti	32.40.04	İçi doldurulmuş oyuncak bebeklerin ve oyuncak hayvanların imalatı
797	Oyuncak imalatı, ticareti	32.40.05	Oyuncak bebek, kukla ve hayvanlar ile bunların giysi, parça ve aksesuarlarının imalatı (içi doldurulmuş olanlar hariç)
798	Oyuncak imalatı, ticareti	32.40.09	Oyun tahtaları (satranç, dama, dart, tavla tahtaları, okey istekası, go vb.) ve tabu, monopol vb. oyunların imalatı
1000	Demir, çelik eşya imalatı, ticareti	43.24.03	Parmaklık ve korkuluk tesisatı işleri (metal yangın merdivenlerinin kurulumu dahil)
799	Oyuncak imalatı, ticareti	32.40.10	Tekerlekli oyuncaklar, oyuncak bebek arabaları, oyuncak trenler ve diğer küçültülmüş boyutlu modeller/maketler veya inşaat oyun takımları, yarış setleri imalatı (motorlu olanlar, pres döküm oyuncaklar ve plastik diğer oyuncaklar dahil)
800	Oyuncak imalatı, ticareti	32.40.99	Başka yerde sınıflandırılmamış diğer oyun ve oyuncakların imalatı
801	Oyuncak imalatı, ticareti	46.18.01	Oyun ve oyuncak, spor malzemesi, bisiklet, kitap, gazete, dergi, kırtasiye ürünleri, müzik aleti, saat ve mücevher ile fotoğrafçılıkla ilgili ve optik aletlerin toptan satışı ile ilgili aracıların faaliyetleri
802	Oyuncak imalatı, ticareti	46.49.04	Oyun ve oyuncak toptan ticareti
803	Oyuncak imalatı, ticareti	47.64.08	Oyunlar ve oyuncakların perakende ticareti
804	Reklamcılık, tabelacılık	25.99.14	Adi metallerden işaret levhaları ve tabelalar ile rakamlar, harfler ve diğer sembollerin imalatı (oto plakaları dahil, ışıklı olanlar hariç)
805	Reklamcılık, tabelacılık	27.40.06	Işıklı tabela, ışıklı reklam panosu ve benzerlerinin imalatı
806	Reklamcılık, tabelacılık	27.90.06	Sıvı kristal cihazlı (LCD) veya ışık yayan diyotlu (LED) gösterge panelleri ile bys. elektrikli sesli veya görsel sinyalizasyon cihazlarının imalatı (elektronik sayı levhası (skorbord) dahil)
807	Reklamcılık, tabelacılık	73.11.01	Reklam ajanslarının faaliyetleri (kullanılacak medyanın seçimi, reklamın tasarımı, sözlerin yazılması, reklam filmleri için senaryonun yazımı, satış noktalarında reklam ürünlerinin gösterimi ve sunumu vb.)
808	Reklamcılık, tabelacılık	74.12.00	Grafik tasarım ve görsel iletişim faaliyetleri
809	Sanat eseri, antika ticareti	47.69.03	Sanat eserlerinin perakende ticareti (antika eşyalar hariç)
810	Sanat eseri, antika ticareti	47.79.01	Antika perakende ticareti
811	Sanat eseri, antika ticareti	90.31.00	Sanat tesislerinin ve alanlarının (mekanlarının) işletilmesi
812	Sanat eseri, antika ticareti	91.30.00	Kültürel mirasın konservasyonu, restorasyonu ve diğer destek faaliyetleri (müzeler ve özel koleksiyonlar dahil
813	Tercümanlık	74.30.12	Tercüme ve sözlü tercüme faaliyetleri (işaret dili dahil)
814	Züccaciye imalatı, ticareti	23.13.01	Camdan şişe, kavanoz ve diğer muhafaza kapları, bardaklar, termos ve diğer vakumlu kapların camdan yapılmış iç yüzeyleri ile camdan sofra ve mutfak eşyaları imalatı (ampuller hariç)
815	Züccaciye imalatı, ticareti	23.13.02	Tuvalet, banyo, büro, iç dekorasyon, vb. amaçlarla kullanılan cam ve kristal eşya imalatı (camdan biblo, boncuk vb. küçük cam eşyalar hariç)
816	Züccaciye imalatı, ticareti	23.41.01	Seramik veya porselenden sofra takımları (tabak, bardak, fincan, vb.) ve diğer ev ve tuvalet eşyasının imalatı (çiniden olanlar ve sıhhi ürünler hariç)
817	Züccaciye imalatı, ticareti	23.41.03	Çiniden sofra takımı, ev, tuvalet ve süs eşyası imalatı (çinicilik) (çini dekoru dahil)
818	Züccaciye imalatı, ticareti	23.41.04	Topraktan güveç, çanak, çömlek, küp, vazo, vb. eşyalar ile topraktan heykel vb. süs ve dekoratif eşya imalatı (porselen ve çiniden olanlar ile malların ambalajlanması ve taşınması için olanlar hariç)
819	Züccaciye imalatı, ticareti	23.45.01	Tarımsal amaçlı olanlar ile malların taşınması ya da ambalajlanması için kullanılan seramik ürünlerin imalatı
820	Züccaciye imalatı, ticareti	23.45.99	Başka yerde sınıflandırılmamış yapı işlerinde kullanılmayan diğer seramik eşyaların imalatı (dekoratif amaçlı olmayan seramik saksılar dahil)
821	Züccaciye imalatı, ticareti	46.15.90	Diğer ev eşyalarının toptan satışı ile ilgili aracıların faaliyetleri
822	Züccaciye imalatı, ticareti	46.44.01	Porselen ve cam eşyalar ile toprak ve seramikten yapılan ürünlerin toptan ticareti
823	Züccaciye imalatı, ticareti	46.49.07	Çatal-bıçak takımı ve diğer kesici aletler ile metal sofra ve mutfak eşyalarının toptan ticareti (bakır mutfak eşyaları dahil)
824	Züccaciye imalatı, ticareti	47.55.01	Elektriksiz ev aletleri, sofra ve mutfak eşyaları ile züccaciye ürünlerinin perakende ticareti (plastikten olanlar hariç)
825	Züccaciye imalatı, ticareti	47.55.05	Plastikten sofra, mutfak, tuvalet ve diğer ev eşyalarının perakende ticareti
826	Alternatif tedavi merkezi işletmeciliği	86.95.00	Fizyoterapi hizmetleri (tıp doktorları dışında yetkili kişilerce sağlanan fizyoterapi, ergoterapi vb. alanlardaki hizmetler) (hastane dışı)
827	Alternatif tedavi merkezi işletmeciliği	86.96.00	Geleneksel, tamamlayıcı ve alternatif tıp faaliyetleri
828	Alternatif tedavi merkezi işletmeciliği	86.99.99	Başka yerde sınıflandırılmamış diğer insan sağlığı faaliyetleri (kan merkezleri ile kan, sperm ve organ bankalarının faaliyetleri hariç)
829	Cenaze hizmetleri	96.30.01	Cenaze işleri ile ilgili faaliyetler (cenaze yıkama yerlerinin işletilmesi, cenazenin nakli, yıkama hizmetleri, defin hizmetleri vb.)
830	Diş laboratuvarlarının faaliyetleri	32.50.03	Diş laboratuvarlarının faaliyetleri (protez diş, metal kuron, vb. imalatı)
831	Diş laboratuvarlarının faaliyetleri	32.50.06	Dişçi çimentosu, dişçilik mumları, dolgu maddesi, kemik tedavisinde kullanılan çimento, jel preparat, steril adhezyon bariyeri, dikiş malzemesi (katgüt hariç), doku yapıştırıcısı, laminarya, emilebilir hemostatik, vb. imalatı
832	Dövme salonu işletmeciliği	96.99.99	Başka yerde sınıflandırılmamış diğer hizmet faaliyetleri (dövme ve piercing hizmetleri vb.)
833	Erkek berberliği	96.21.02	Erkekler için kuaför ve berber işletmelerinin faaliyetleri
834	Genel temizlik, haşere kontrol faaliyetleri	81.21.01	Binaların genel temizliği (uzmanlaşmış temizlik faaliyetleri hariç)
835	Genel temizlik, haşere kontrol faaliyetleri	81.22.03	Nesne veya binaların (ameliyathaneler vb.) sterilizasyonu faaliyetleri
836	Genel temizlik, haşere kontrol faaliyetleri	81.22.04	Yapıların dış cepheleri için buharlı temizleme, kum püskürtme vb. uzmanlaşmış inşaat faaliyetleri
837	Genel temizlik, haşere kontrol faaliyetleri	81.22.05	Yeni binaların inşaat sonrası temizliği
838	Genel temizlik, haşere kontrol faaliyetleri	81.22.99	Başka yerde sınıflandırılmamış diğer bina ve endüstriyel temizlik faaliyetleri (sterilizasyon faaliyetleri hariç)
839	Genel temizlik, haşere kontrol faaliyetleri	81.23.01	Böceklerin, kemirgenlerin ve diğer zararlıların imhası ve haşere kontrol faaliyetleri (tarımsal zararlılarla mücadele hariç)
840	Genel temizlik, haşere kontrol faaliyetleri	81.23.99	Başka yerde sınıflandırılmamış diğer temizlik faaliyetleri (oto yıkama hariç)
841	Güzellik salonu işletmeciliği	96.22.01	Güzellik salonlarının faaliyetleri (cilt bakımı, kaş alma, ağda, manikür, pedikür, makyaj, kalıcı makyaj vb.nin bir arada sunulduğu salonlar) (sağlık bakım hizmetleri hariç)
842	Güzellik salonu işletmeciliği	96.22.02	Sadece manikür ve pedikür hizmeti sunan salonların faaliyetleri
843	Güzellik salonu işletmeciliği	96.22.03	Sadece ağdacılık hizmeti sunan salonların faaliyetleri
844	Hasta bakıcılığı	86.94.01	Ebe, sağlık memuru, sünnetçi, iğneci, pansumancı vb.leri tarafından verilen hizmetler (tıp doktorları dışında yetkili kişilerce sağlanan gebelik süresince ve doğum sonrası izleme ve tıbbi işlemleri kapsayan aile planlaması hizmetleri dahil) (hastane dışı)
845	Hasta bakıcılığı	86.94.02	Hemşirelik hizmetleri (evdeki hastalar için bakım, koruma, anne bakımı, çocuk sağlığı ve hemşirelik bakımı alanındaki benzeri hizmetler dahil; hemşireli yatılı bakım tesislerinin faaliyetleri ile tıp doktorlarının hizmetleri hariç) (hastane dışı)
846	Hasta bakıcılığı	87.10.01	Hemşireli yatılı bakım faaliyetleri (hemşireli bakım evlerinin, hemşireli huzur evlerinin faaliyetleri dahil; sadece asgari düzeyde hemşire bakımı sağlanan yaşlı evlerinin, yetimhanelerin, yurtların faaliyetleri ile evlerde sağlanan hizmetler hariç)
847	Hasta bakıcılığı	87.20.02	Zihinsel rahatsızlığı veya madde kullanımı teşhisi olan kişilere yönelik yatılı bakım faaliyetleri (hastanelerin faaliyetleri ile yatılı sosyal hizmet faaliyetleri hariç)
848	Hasta bakıcılığı	87.30.02	Yaşlılara ve bedensel engellilere yönelik yatılı bakım faaliyetleri (destekli yaşam tesisleri, hemşire bakımı olmayan huzurevleri ve asgari düzeyde hemşire bakımı olan evlerin faaliyetleri dahil, yaşlılar için hemşire bakımlı evlerin faaliyetleri hariç)
849	Hasta bakıcılığı	88.10.02	Yaşlılar ve bedensel engelliler için barınacak yer sağlanmaksızın verilen sosyal hizmetler (yatılı bakım faaliyetleri ile engelli çocuklara yönelik gündüz bakım (kreş) faaliyetleri hariç)
850	Hasta bakıcılığı	88.99.07	Barınacak yer sağlanmaksızın mesleki rehabilitasyon hizmetleri (bedensel engelliler için rehabilitasyon hizmetleri hariç)
851	Hasta bakıcılığı	88.99.09	Barınacak yer sağlanmaksızın çocuk ve gençlere yönelik rehabilitasyon hizmetleri (zihinsel engelliler için olanlar dahil, bedensel engellilere yönelik olanlar hariç)
852	Hasta bakıcılığı	96.99.01	Eskort ve refakat hizmetleri (güvenlik hizmetleri hariç)
853	Kadın kuaförlüğü	96.21.01	Kadınlar için kuaför işletmelerinin faaliyetleri
854	Kaplıca, hamam işletmeciliği	96.23.01	Hamam, sauna, vb. yerlerin faaliyetleri
855	Kaplıca, hamam işletmeciliği	96.23.02	Zayıflama salonu, masaj salonu, solaryum vb. yerlerin işletilmesi faaliyetleri (form tutma salonlarının ve diyetisyenlerin faaliyetleri hariç)
856	Kaplıca, hamam işletmeciliği	96.23.03	Kaplıca, ılıca, içmeler, spa merkezleri, vb. yerlerin faaliyetleri (konaklama hizmetleri hariç)
857	Kozmetik imalatı, ticareti	20.42.01	Ağız veya diş bakım ürünleri imalatı (diş macunu, vb. ile takma dişleri ağızda sabit tutmaya yarayan macun ve tozlar ile diş temizleme iplikleri dahil)
858	Kozmetik imalatı, ticareti	20.42.02	Kolonya imalatı
859	Kozmetik imalatı, ticareti	20.42.03	Parfüm ve koku verici diğer sıvı ürün, manikür/pedikür müstahzarı, güneş koruyucu ürünler, dudak ve göz makyajı ürünü, banyo tuzu, kozmetik veya kişisel bakım amaçlı pudra, sabun ve organik yüzey aktif müstahzarı, deodorant, vb. imalatı (kolonya hariç)
860	Kozmetik imalatı, ticareti	20.42.04	Şampuan, saç kremi, saç spreyi, jöle, saç düzleştirme ve perma ürünleri, saç losyonları, saç boyaları, vb. imalatı
861	Kozmetik imalatı, ticareti	20.59.19	Uçucu yağların imalatı
862	Kozmetik imalatı, ticareti	32.91.03	Diş fırçaları, saç fırçaları, tıraş fırçaları ve kişisel bakım için kullanılan diğer fırçalar ile resim fırçaları, yazı fırçaları ve kozmetik fırçaların imalatı
863	Kozmetik imalatı, ticareti	32.99.06	Peruk, takma saç, takma sakal, takma kaş vb. imalatı
864	Kozmetik imalatı, ticareti	46.18.02	Kozmetik, parfüm ve bakım ürünleri ile temizlik malzemesinin toptan satışı ile ilgili aracıların faaliyetleri
865	Kozmetik imalatı, ticareti	46.45.01	Parfüm, kozmetik ürünleri ve kolonya toptan ticareti (ıtriyat dahil)
866	Kozmetik imalatı, ticareti	46.49.22	Tıraş bıçakları, usturalar ve jiletlerin toptan ticareti
867	Kozmetik imalatı, ticareti	47.75.01	Kozmetik ve kişisel bakım malzemelerinin perakende ticareti
868	Optik ürünlerin imalatı, ticareti	26.70.11	Objektif merceği, levha ve tabaka halinde polarizan madde, renk filtresi, optik mercek, prizma, ayna ve diğer optik elemanlar ile dürbün, optik mikroskop, optik teleskop ve diğer astronomik aletler ile bunların aksam ve parçalarının imalatı
869	Optik ürünlerin imalatı, ticareti	32.50.04	Gözlükler ve lensler ile parçalarının imalatı
870	Optik ürünlerin imalatı, ticareti	33.13.03	Profesyonel optik aletlerin ve fotoğrafçılık ekipmanlarının onarım ve bakımı (tüketici elektronik ürünlerinin onarımı hariç)
871	Optik ürünlerin imalatı, ticareti	46.43.11	Optik ürünlerin toptan ticareti
872	Optik ürünlerin imalatı, ticareti	47.74.02	Gözlük, kontak lens, gözlük camı vb. perakende ticareti
873	Optik ürünlerin imalatı, ticareti	47.78.07	Optik ve hassas aletlerin perakende ticareti (mikroskop, dürbün ve pusula dahil; gözlük camı, fotoğrafik ürünler hariç)
874	Spor malzemeleri imalatı, ticareti	13.96.10	Can yeleği ve can kurtaran simidi imalatı
875	Spor malzemeleri imalatı, ticareti	13.96.11	Paraşüt (yönlendirilebilen paraşütler dahil) ve rotoşüt ile bunların parçalarının imalatı
876	Spor malzemeleri imalatı, ticareti	32.30.17	Kar kayakları, kayak ayakkabıları, kayak botları, kayak batonları, buz patenleri ve tekerlekli patenler ile su kayağı araçları, sörf tahtaları, rüzgar sörfleri vb. ekipmanlar ile bunların parçalarının imalatı (kaykaylar dahil)
877	Spor malzemeleri imalatı, ticareti	32.30.18	Jimnastik ve atletizm eşyaları ile form tutma salonlarına ait eşya ve ekipmanların imalatı (atlama beygiri, dambıl ve halterler, kürek çekme ve bisiklete binme aletleri, ciritler, çekiçler; boks çalışma topları, boks veya güreş için ringler vb.)
878	Spor malzemeleri imalatı, ticareti	32.30.19	Spor amaçlı dağcılık, avcılık veya balıkçılık eşyalarının imalatı (kasklar, olta kamışları, olta iğneleri ve kancaları, otomatik olta makaraları, el kepçeleri, kelebek ağları, yapma balıklar, sinekler gibi suni yemler, kurşunlar, yapma kuşlar vb.)
879	Spor malzemeleri imalatı, ticareti	32.30.20	Spor veya açık hava oyunları için diğer eşyaların imalatı (boks eldiveni, spor eldiveni, yaylar, beyzbol ve golf sopaları ile top ve diğer eşyaları, tenis masası, raket, ağ ve topları, tozluklar, bacak koruyucular, şişme ve diğer havuzlar vb.)
880	Spor malzemeleri imalatı, ticareti	32.30.21	Top imalatı (beyzbol, futbol, basketbol ve voleybol için)
881	Spor malzemeleri imalatı, ticareti	46.49.02	Spor malzemesi toptan ticareti
882	Spor malzemeleri imalatı, ticareti	46.49.09	Sportif amaçlı avcılık ve balıkçılık malzemeleri toptan ticareti (tabanca, av tüfeği ve balık ağları hariç)
883	Spor malzemeleri imalatı, ticareti	47.63.03	Kamp malzemeleri perakende ticareti
884	Spor malzemeleri imalatı, ticareti	47.63.05	Jimnastik ve atletizm eşya ve ekipmanları ile form tutma merkezlerine ait eşya ve ekipmanların perakende ticareti (halter, yürüme bantları, vb.)
885	Spor malzemeleri imalatı, ticareti	47.63.08	Avcılık ve balıkçılık teçhizatı ve malzemeleri ile silah ve mühimmat perakende ticareti
886	Spor malzemeleri imalatı, ticareti	47.63.90	Uzmanlaşmış diğer spor malzemelerinin perakende ticareti
887	Spor malzemeleri imalatı, ticareti	77.21.02	Bisikletlerin kiralanması ve leasingi (elektrikli bisikletler dahil) (finansal leasing hariç)
888	Spor malzemeleri imalatı, ticareti	77.21.04	Eğlence ve spor amaçlı sandal, tekne, kano, yelkenli vb.nin mürettebatsız olarak kiralanması ve leasingi (finansal leasing hariç)
889	Spor malzemeleri imalatı, ticareti	77.21.90	Diğer eğlence ve spor eşyalarının kiralanması ve leasingi (finansal leasing hariç)
890	Spor malzemeleri imalatı, ticareti	77.39.03	Motosiklet, karavan ve kamp gereçlerinin operatörsüz olarak kiralanması veya leasingi (finansal leasing hariç)
891	Spor malzemeleri imalatı, ticareti	95.29.03	Spor araç ve gereçleri ile kamp malzemelerinin bakımı ve onarımı
892	Spor tesisi işletmeciliği	93.11.01	Spor tesislerinin işletilmesi (hipodromların işletilmesi hariç)
893	Spor tesisi işletmeciliği	93.13.01	Fitness merkezlerinin faaliyetleri (yoga, pilates, tai chi stüdyolarının faaliyetleri vb. dahil)
894	Spor tesisi işletmeciliği	93.19.03	Spor ve eğlence amaçlı sporlara ilişkin destek faaliyetleri
895	Spor tesisi işletmeciliği	93.19.99	Başka yerde sınıflandırılmamış diğer spor amaçlı faaliyetler
896	Temizlik malzemeleri imalatı, ticareti	17.22.02	Kağıt hamurundan, kağıttan, selüloz vatkadan veya selüloz lifli ağlardan tuvalet kağıdı, kağıt mendil, temizlik veya yüz temizleme için kağıt mendil ve havlular ile masa örtüsü ve peçetelerin imalatı
897	Temizlik malzemeleri imalatı, ticareti	17.22.04	Kağıt hamurundan, kağıttan, selüloz vatkadan veya selüloz lifli ağlardan hijyenik havlu ve tamponlar, kadın bağı, pedler, bebek bezleri vb. hijyenik ürünler ile giyim eşyası ve giysi aksesuarlarının imalatı
898	Temizlik malzemeleri imalatı, ticareti	20.13.04	Karbonatların imalatı (sodyum, kalsiyum ve diğerleri) (çamaşır sodası dahil)
899	Temizlik malzemeleri imalatı, ticareti	20.20.11	Böcek ilacı, kemirgen ilacı, küf ve mantar ilacı, yabancı otla mücadele ilacı imalatı
900	Temizlik malzemeleri imalatı, ticareti	20.20.15	Dezenfektan imalatı (tarımsal ve diğer kullanımlar için) (hijyenik maddeler, bakteriostatlar ve sterilize ediciler dahil) (doğal dezenfektanlar hariç)
901	Temizlik malzemeleri imalatı, ticareti	20.20.16	Doğal dezenfektan imalatı
902	Temizlik malzemeleri imalatı, ticareti	20.41.01	Kapalı alanlar için kokulu müstahzarlar ve koku gidericiler ile suni mumların imalatı (kişisel kullanım için olanlar hariç)
903	Temizlik malzemeleri imalatı, ticareti	20.41.04	Sabun, yıkama ve temizleme müstahzarları (deterjanlar) ile sabun olarak kullanılan müstahzarlar imalatı (kişisel bakım için olanlar ile ovalama toz ve kremleri hariç)
904	Temizlik malzemeleri imalatı, ticareti	20.41.06	Cila, krem ve ovalama krem ve tozlarının imalatı (ayakkabı, mobilya, yer döşemesi, kaporta, cam, metal vb. için)
905	Temizlik malzemeleri imalatı, ticareti	46.44.02	Temizlik malzemesi toptan ticareti (kişisel temizlik sabunları hariç)
906	Temizlik malzemeleri imalatı, ticareti	46.44.04	Cila ve krem (ayakkabı, mobilya, yer döşemesi, kaporta, cam veya metal için) toptan ticareti
907	Temizlik malzemeleri imalatı, ticareti	46.45.02	Sabun toptan ticareti (kişisel temizlik için)
908	Temizlik malzemeleri imalatı, ticareti	46.49.08	Tuvalet kağıdı, peçete, kağıt havlu ile kağıt tepsi, tabak, bardak, çocuk bezi vb. toptan ticareti (plastikten olanlar hariç)
909	Temizlik malzemeleri imalatı, ticareti	47.55.11	Kağıt veya mukavvadan tuvalet kağıdı, kağıt mendil, kağıt havlular, kağıt masa örtüsü ve peçeteler ile kağıt veya mukavvadan tepsi, tabak, kase, bardak ve benzerlerinin perakende ticareti
910	Temizlik malzemeleri imalatı, ticareti	47.78.15	Temizlik malzemesi perakende ticareti (Arap sabunu, deterjan, yumuşatıcılar, şampuanlar vb. dahil; kişisel hijyen için olanlar hariç)
911	Tıbbi malzemelerin imalatı, ticareti	20.59.07	Laboratuvar için hazır kültür ortamları, model hamurları, kompozit diyagnostik reaktifler veya laboratuvar reaktifleri imalatı
912	Tıbbi malzemelerin imalatı, ticareti	21.20.02	Yapışkanlı bandajlar, katkütler ve benzeri tıbbi malzemelerin üretimi (steril cerrahi katgütler, eczacılık maddeleri ile birlikte kullanılan tamponlar, hidrofil pamuk, gazlı bez, sargı bezi vb.)
913	Tıbbi malzemelerin imalatı, ticareti	22.12.08	Kauçuktan hijyenik ve eczacılık ürünlerinin imalatı (prezervatifler, emzikler, hijyenik eldivenler vb. dahil)
914	Tıbbi malzemelerin imalatı, ticareti	26.60.01	Işınlama, elektro medikal ve elektro terapi ile ilgili cihazların imalatı
915	Tıbbi malzemelerin imalatı, ticareti	32.50.02	Tıpta, cerrahide ve dişçilikte kullanılan protezler, ortopedik cihazlar ve aksesuarların imalatı
916	Tıbbi malzemelerin imalatı, ticareti	32.50.07	Tıpta, cerrahide, dişçilikte veya veterinerlikte kullanılan şırınga, iğne, katater, kanül ve benzerlerinin imalatı
917	Tıbbi malzemelerin imalatı, ticareti	32.50.14	Tıpta, cerrahide ve dişçilikte kullanılan araç-gereç ve cihazların imalatı (ortopedik cihazlar hariç)
918	Tıbbi malzemelerin imalatı, ticareti	32.50.15	Terapatik alet ve cihazların imalatı (suni solunum veya terapatik solunum cihazları hariç)
919	Tıbbi malzemelerin imalatı, ticareti	32.50.90	Tıbbi ve dişçilik ile ilgili diğer araç ve gereçlerin imalatı
920	Tıbbi malzemelerin imalatı, ticareti	32.99.09	Koruyucu amaçlı solunum ekipmanları ve gaz maskelerinin imalatı (tedavi edici olanlar hariç)
921	Tıbbi malzemelerin imalatı, ticareti	46.18.03	Tıbbi ürünlerin, araç ve malzemelerin toptan satışı ile ilgili aracıların faaliyetleri
922	Tıbbi malzemelerin imalatı, ticareti	46.46.01	Cerrahi, tıbbi ve ortopedik alet ve cihazların toptan ticareti
923	Tıbbi malzemelerin imalatı, ticareti	46.46.03	Dişçilikte kullanılan alet ve cihazların toptan ticareti (protezler, bağlantı parçaları dahil)
924	Tıbbi malzemelerin imalatı, ticareti	47.74.01	Tıbbi ve ortopedik ürünlerin perakende ticareti
925	Tuvalet işletmeciliği	96.99.07	Genel tuvaletlerin işletilmesi faaliyeti
926	Alüminyum ürün imalatı	24.42.16	Alüminyum folyo imalatı (alaşımdan olanlar dahil)
927	Alüminyum ürün imalatı	24.42.18	Alüminyum sac, levha, tabaka, şerit imalatı (alaşımdan olanlar dahil)
928	Alüminyum ürün imalatı	24.42.21	Alüminyum bar, çubuk, tel ve profil, tüp, boru ve bağlantı parçaları imalatı (alaşımdan olanlar dahil)
929	Alüminyum ürün imalatı	25.12.04	Alüminyum kapı, pencere, bunların kasaları, kapı eşiği, panjur, vb. imalatı
930	Alüminyum ürün imalatı	25.92.03	Kapasitesi 300 lt.yi geçmeyen alüminyum varil fıçı, kova vb. imalatı (diş macunu, krem gibi kapaklı tüpler ve katlanabilir kutular ile aerosol kutuları dahil)
931	Alüminyum ürün imalatı	25.99.01	Demir, çelik ve alüminyumdan sofra ve mutfak eşyalarının imalatı (tencere, tava, çaydanlık, cezve, yemek kapları, bulaşık telleri vb.) (teflon, emaye vb. ile kaplanmışlar dahil, bakırdan olanlar hariç)
932	At arabası imalatı, onarımı	30.99.02	Hayvanlar tarafından çekilen araçların imalatı (at, eşek arabası, fayton, vb.)
933	At arabası imalatı, onarımı	33.17.99	Başka yerde sınıflandırılmamış diğer ulaşım ekipmanlarının onarım ve bakımı
934	Bakırcılık	24.44.01	Bakır, bakır matı, bakır tozu, semente bakır, bakır anotu ile bakır ve bakır alaşımlarının imalatı
935	Bakırcılık	24.44.03	Bakır sac, tabaka, levha, şerit, folyo imalatı (alaşımdan olanlar dahil)
936	Bakırcılık	24.44.04	Bakırın çekilmesi ve haddelenmesi ile tüp, boru, bunların bağlantı elemanları, bar, çubuk, tel ve profil imalatı (alaşımdan olanlar dahil)
937	Bakırcılık	25.99.06	Bakırdan sofra ve mutfak eşyası imalatı (cezve, tencere, çanak, tabak, ibrik vb.)
938	Bakırcılık	25.99.18	Bakırdan yapılan biblolar, çerçeveler, aynalar ve diğer süsleme eşyaları ile süsleme işleri (mutfak eşyaları hariç)
939	Bakırcılık	47.55.13	Bakır eşya, bakır sofra ve mutfak eşyası perakende ticareti
940	Çilingirlik	25.62.04	Kilit ve menteşe imalatı
941	Çilingirlik	80.09.01	Çilingirlik hizmetleri
942	Çilingirlik	95.29.04	Anahtar çoğaltma hizmetleri
943	Demir, çelik eşya imalatı, ticareti	24.10.02	Çelikten açık profil imalatı (sıcak haddeleme, sıcak çekme veya kalıptan çekme işlemlerinden daha ileri işlem görmemiş)
944	Demir, çelik eşya imalatı, ticareti	24.10.03	Demir ve çelikten sıcak veya soğuk çekilmiş yassı hadde ürünleri imalatı (demir veya çelik alaşımlı levha, şerit, sac, teneke sac, vb. dahil)
945	Demir, çelik eşya imalatı, ticareti	24.10.05	Sıcak haddelenmiş demir veya çelikten bar ve çubukların üretilmesi (inşaat demiri dahil)
946	Demir, çelik eşya imalatı, ticareti	24.10.06	Demir veya çelik granül ve demir tozu üretilmesi
947	Demir, çelik eşya imalatı, ticareti	24.10.07	Demir ya da çelik hurdaların yeniden eritilmesi
948	Demir, çelik eşya imalatı, ticareti	24.10.08	Demir cevherinin doğrudan indirgenmesiyle elde edilen demirli ürünler ve diğer sünger demir ürünlerinin imalatı ile elektroliz veya diğer kimyasal yöntemlerle istisnai saflıkta demir üretilmesi
949	Demir, çelik eşya imalatı, ticareti	24.10.09	Çelikten demir yolu ve tramvay yolu yapım malzemesi (birleştirilmemiş raylar ile ray donanımı, aksamı, vb.) ile levha kazıkları (palplanş) ve kaynaklı açık profil imalatı
950	Demir, çelik eşya imalatı, ticareti	24.10.10	Pik demir ve manganezli dökme demir (aynalı demir/spiegeleisen) üretimi (külçe, blok, veya diğer birincil formlarda)
951	Demir, çelik eşya imalatı, ticareti	24.10.12	Ferro alaşımların imalatı (ferro manganez, ferro silisyum, ferro siliko manganez, ferro krom ve diğerleri)
952	Demir, çelik eşya imalatı, ticareti	24.20.09	Çelikten/demirden yapılmış tüp, boru, içi boş profiller ve ilgili bağlantı parçalarının imalatı (sıcak çekilmiş veya sıcak haddelenmiş)
953	Demir, çelik eşya imalatı, ticareti	24.20.10	Çelikten/demirden yapılmış tüp, boru, içi boş profiller ve ilgili bağlantı parçalarının imalatı (soğuk çekilmiş veya soğuk haddelenmiş)
954	Demir, çelik eşya imalatı, ticareti	24.31.01	Barların soğuk çekilmesi
955	Demir, çelik eşya imalatı, ticareti	24.32.01	Dar şeritlerin soğuk haddelenmesi
956	Demir, çelik eşya imalatı, ticareti	24.33.01	Soğuk şekillendirme veya katlama
957	Demir, çelik eşya imalatı, ticareti	24.34.01	Tellerin soğuk çekilmesi
958	Demir, çelik eşya imalatı, ticareti	24.43.04	Kalay bar, çubuk, profil, tel, vb. imalatı (alaşımdan olanlar dahil)
959	Demir, çelik eşya imalatı, ticareti	24.43.07	Çinko bar, çubuk, profil, tel vb. imalatı (alaşımdan olanlar dahil)
960	Demir, çelik eşya imalatı, ticareti	24.45.06	Nikel matları, nikel oksit sinterleri ve diğer ara ürünleri ile nikel bar, çubuk, profil, tel, levha, şerit, folyo, tüp, boru ve bağlantı parçaları imalatı
961	Demir, çelik eşya imalatı, ticareti	24.51.13	Demir döküm
962	Demir, çelik eşya imalatı, ticareti	25.11.06	İnşaat ve inşaatın parçaları için metal çatı ya da iskeletlerin imalatı (kuleler, direkler, destekler, köprüler vb.) (kepenk ve yangın merdiveni ile prefabrik yapılar hariç)
963	Demir, çelik eşya imalatı, ticareti	25.11.07	Metalden kepenk ve yangın merdiveni imalatı
964	Demir, çelik eşya imalatı, ticareti	25.11.08	Metalden prefabrik yapı imalatı
965	Demir, çelik eşya imalatı, ticareti	25.12.05	Çelik kapı, pencere, bunların kasaları, kapı eşiği, panjur, vb. imalatı
966	Demir, çelik eşya imalatı, ticareti	25.12.06	Demir kapı, pencere, bunların kasaları, kapı eşiği, panjur, vb. imalatı (bahçe kapıları dahil)
967	Demir, çelik eşya imalatı, ticareti	25.21.10	Merkezi ısıtma radyatörleri imalatı (elektrikli radyatörler ile döküm olanlar hariç)
968	Demir, çelik eşya imalatı, ticareti	25.21.11	Merkezi ısıtma kazanları (boyler) imalatı (kombi, kat kaloriferi ve diğer merkezi ısıtma kazanları,) (buhar jeneratörleri ve kızgın su üreten kazanlar hariç)
969	Demir, çelik eşya imalatı, ticareti	25.21.13	Buhar üretim kazanları (buhar jeneratörü), kızgın su kazanları (boyler), denizcilik veya enerji kazanları ile bunların parçaları ile kazanlar (boylerler) için yardımcı üniteler ve buhar veya diğer buhar güç üniteleri için kondansatör imalatı
970	Demir, çelik eşya imalatı, ticareti	25.22.01	Metalden rezervuarlar, tanklar, fıçılar ve benzeri kapasitesi > 300 litre olan konteynerlerin imalatı (sıkıştırılmış veya sıvılaştırılmış gazlar için olanlar ile mekanik veya termal ekipmanlı olanlar hariç)
971	Demir, çelik eşya imalatı, ticareti	25.22.02	Sıkıştırılmış veya sıvılaştırılmış gaz için kullanılan metal konteynerlerin imalatı
972	Demir, çelik eşya imalatı, ticareti	25.30.03	Tabanca, revolver (altıpatlar), av tüfeği, havalı tabanca, cop, vb. askeri amaçlı olmayan ateşli silahlar ve benzeri aletlerin ve bunların parçalarının imalatı
973	Demir, çelik eşya imalatı, ticareti	25.61.04	Kaşık, çatal, kepçe, kevgir, servis spatulası, şeker maşası ve benzeri mutfak gereçleri, sofra takımları, çatal bıçak takımları imalatı (balık bıçakları, kahvaltı ve meyve bıçakları dahil fakat, sofra bıçakları hariç)
974	Demir, çelik eşya imalatı, ticareti	25.61.05	Tıraş bıçakları, usturalar ile jiletler ve tıraş makinelerinin bıçaklarının imalatı
975	Demir, çelik eşya imalatı, ticareti	25.61.06	Sofra bıçakları (balık bıçakları, kahvaltı ve meyve bıçakları hariç), budama bıçakları, sustalı bıçaklar, satır,balta vb. bıçaklar (makineler için olanlar hariç) ile terzi makasları, vb. makaslar ve bunların ağızlarının imalatı
976	Demir, çelik eşya imalatı, ticareti	25.61.07	Manikür veya pedikür setleri ve aletleri, kağıt bıçakları, mektup açacakları, kalemtıraşlar ve bunların bıçakları, kırma, yarma ve kıyma bıçakları, saç kesme ve hayvan kırkma makine ve aletleri ile benzeri elektriksiz kesici aletlerin imalatı
977	Demir, çelik eşya imalatı, ticareti	25.61.08	Kılıç, pala, kasatura, mızrak, süngü, avcı bıçağı ve benzeri silahlar ile bunların parçalarının imalatı
978	Demir, çelik eşya imalatı, ticareti	25.63.04	El aletleri, takım tezgahı uçları, testere ağızları, mengeneler, kıskaçlar, sıkıştırma anahtarları vb. imalatı (makineler veya mekanik cihazlar için değiştirilebilen uçlar dahil)
979	Demir, çelik eşya imalatı, ticareti	25.91.01	Çelik varil ve benzer muhafazaların imalatı
980	Demir, çelik eşya imalatı, ticareti	25.92.01	Demir veya çelikten yiyecek, içecek ve diğer ürünler için kapasitesi < 50 litre olan kutuların imalatı (lehim veya kıvrılarak kapatılanlar) (tenekeden olanlar dahil)
981	Demir, çelik eşya imalatı, ticareti	25.92.02	Adi metalden dişli kapaklar (şişe kapağı vb.) ve tıpalar ile tıkaçlar ve kapakların imalatı
982	Demir, çelik eşya imalatı, ticareti	25.93.01	Metalden zincirler (mafsallı bağlantı zinciri hariç) ve parçaları ile yay ve yay yaprakları, kaplanmış veya nüveli teller, çubuklar, tüpler, levhalar ve elektrotların imalatı (elektrik işlerinde kullanılanlar ile elektrik yalıtımı olanlar hariç)
983	Demir, çelik eşya imalatı, ticareti	25.93.02	İğne, çengelli iğne, çuvaldız, örgü şişi, tığ, raptiye, çivi, vb. imalatı
984	Demir, çelik eşya imalatı, ticareti	25.93.03	Telden yapılan diğer ürünlerin imalatı (örgülü tel, örme şerit,örme halat, taşıma askısı, dikenli tel (elektrik yalıtımı olanlar hariç) ve demir, çelik veya bakır tellerden mensucat, ızgara, ağ, kafeslik ve çitler)
985	Demir, çelik eşya imalatı, ticareti	25.94.01	Yivsiz bağlantı malzemeleri imalatı, demir, çelik veya bakırdan (rondelalar, perçinler, perçin çivileri, kamalı pimler, kopilyalar vb. ürünler)
986	Demir, çelik eşya imalatı, ticareti	25.94.02	Yivli bağlantı malzemeleri imalatı, demir, çelik veya bakırdan (vidalar, cıvatalar, somunlar vb. yivli ürünler)
987	Demir, çelik eşya imalatı, ticareti	25.99.03	Zırhlı veya güçlendirilmiş kasalar, kasa daireleri, kilitli para kasaları, zırhlı kapılar vb. imalatı (adi metalden)
988	Demir, çelik eşya imalatı, ticareti	25.99.05	Adi metalden tokalar, klipsli çanta sapları, kemer tokaları, kancalar, halkalar, kuş gözü halkalar ve benzerleri (giysi, ayakkabı, tente, el çantası, seyahat eşyası veya diğer hazır eşya için kullanılan türde) ile adi metallerden boru şeklinde veya çatallı perçinler; boncuklar vb. imalatı
989	Demir, çelik eşya imalatı, ticareti	25.99.15	Kurşun tüp, boru ve bunların bağlantı parçaları ile kurşun bar, çubuk, profil, tel vb. imalatı (alaşımdan olanlar dahil)
990	Demir, çelik eşya imalatı, ticareti	25.99.21	Metalden elektriksiz hazneli döner bacaların, havalandırma kanallarının vb. imalatı
991	Demir, çelik eşya imalatı, ticareti	25.99.99	Başka yerde sınıflandırılmamış diğer fabrikasyon metal ürünlerin imalatı
992	Demir, çelik eşya imalatı, ticareti	28.29.07	Metal tabakalardan contaların ve mekanik salmastraların imalatı (diğer malzemelerle birleştirilmiş metal tabakalardan veya iki ya da daha fazla metal tabakasından yapılmış olanlar)
993	Demir, çelik eşya imalatı, ticareti	29.20.03	Konteyner imalatı (bir veya daha fazla taşıma şekline göre özel olarak tasarlanmış olanlar)
994	Demir, çelik eşya imalatı, ticareti	32.50.05	Tıbbi, cerrahi, dişçilik veya veterinerlikle ilgili mobilyaların, berber koltukları ve benzeri sandalyeler ile bunların parçalarının imalatı (X ışını masa ve koltukları hariç)
995	Demir, çelik eşya imalatı, ticareti	33.11.01	Metal boru ve boru hatları ile pompa istasyonlarının onarım ve bakımı
996	Demir, çelik eşya imalatı, ticareti	33.11.02	Ateşli silahların ve savaş gereçlerinin onarım ve bakımı (spor ve eğlence amaçlı silahların onarımı dahil)
997	Demir, çelik eşya imalatı, ticareti	33.11.03	Buhar kazanları veya buhar jeneratörlerinin onarım ve bakımı
998	Demir, çelik eşya imalatı, ticareti	33.11.04	Merkezi ısıtma sıcak su kazanları (boyler) ve radyatörlerin onarım ve bakımı
999	Demir, çelik eşya imalatı, ticareti	33.11.10	Metal tankların, rezervuarların ve muhafaza kaplarının (konteynerler dahil) onarımı
1001	Demir, çelik eşya imalatı, ticareti	43.32.02	Herhangi bir malzemeden yapılan kapı ve pencere kasaları, kapılar (zırhlı kapılar dahil, otomatik ve döner kapılar hariç), pencereler, kepenkler, panjurlar, garaj kapıları ve benzerlerinin montajı
1002	Demir, çelik eşya imalatı, ticareti	43.42.01	Yapısal çelik bileşenlerin kurulması işleri (bina inşaatları için)
1003	Demir, çelik eşya imalatı, ticareti	43.50.01	Yapısal çelik bileşenlerin kurulması işleri (bina dışı inşaatları için)
1004	Demir, çelik eşya imalatı, ticareti	46.64.10	Silah ve mühimmat toptan ticareti
1005	Demir, çelik eşya imalatı, ticareti	46.64.14	Zırhlı veya güçlendirilmiş kasalar ve kutular ile kasa daireleri için zırhlı veya güçlendirilmiş kapılar ve kilitli kutular ile para veya evrak kutuları, vb. (adi metalden) toptan ticareti
1006	Demir, çelik eşya imalatı, ticareti	46.82.04	Demir/çelikten haddelenmiş/soğuk çekilmiş yassı ürünlerin toptan ticareti
1007	Demir, çelik eşya imalatı, ticareti	46.83.13	Metalden kapı, pencere ve bunların kasaları ile kapı eşiklerinin toptan ticareti
1008	Demir, çelik eşya imalatı, ticareti	46.84.04	Demir veya çelikten dikenli tel, bakır veya alüminyumdan örgülü tel, kablo, örme şerit ve benzerleri (elektrik yalıtımı olanlar hariç), demir, çelik veya bakır tellerden mensucat, ızgara, ağ, kafeslik ve çit toptan ticareti
1009	Demir, çelik eşya imalatı, ticareti	47.52.05	Metalden kapı, pencere ve bunların kasaları ile kapı eşiklerinin perakende ticareti
1010	Demir, çelik eşya imalatı, ticareti	47.52.13	Demirden/çelikten bar ve çubukların, profillerin, tüp ve boruların perakende ticareti
1011	Demir, çelik eşya imalatı, ticareti	47.52.15	Demirden veya çelikten merkezi ısıtma radyatörleri, merkezi ısıtma kazanları (kombiler dahil) ile bunların parçalarının perakende ticareti (buhar jeneratörleri ve kızgın su üreten kazanlar hariç)
1012	Demir, çelik eşya imalatı, ticareti	47.69.99	Başka yerde sınıflandırılmamış diğer kültür ve eğlence (rekreasyon) ürünlerinin perakende ticareti
1013	Deniz taşıtları imalatı, onarımı, ticareti	25.99.08	Metalden gemi ve tekne pervaneleri ve bunların aksamları ile çıpalar, filika demirleri vb. imalatı
1014	Deniz taşıtları imalatı, onarımı, ticareti	30.11.07	Gemiler ve yüzer yapılar için iç bölmelerin imalatı
1015	Deniz taşıtları imalatı, onarımı, ticareti	30.12.01	Jet ski vb. kişisel su araçlarının imalatı
1016	Deniz taşıtları imalatı, onarımı, ticareti	30.12.03	Şişirilebilir motorlu/motorsuz botların imalatı (eğlence ve spor amaçlı olanlar)
1017	Deniz taşıtları imalatı, onarımı, ticareti	30.12.04	Eğlence ve sportif amaçlı motorlu/motorsuz yelkenlilerin, motorlu tekne ve yatların, sandalların, kayıkların, kanoların, eğlence amaçlı hover kraftların ve benzer araçların imalatı (polyester tekneler dahil)
1018	Deniz taşıtları imalatı, onarımı, ticareti	33.15.00	Sivil gemilerin ve teknelerin onarım ve bakımı (yüzen yapılar, sandal, kayık, vb. bakım ve onarımı ile bunların kalafatlanması dahil)
1019	Deniz taşıtları imalatı, onarımı, ticareti	33.19.02	Halatlar, gemi çarmık ve halatları ile yelken bezleri ve bez astarlı muşambaların onarımı
1020	Deniz taşıtları imalatı, onarımı, ticareti	46.49.26	Spor ve eğlence amaçlı teknelerin, kayıkların ve kanoların toptan ticareti
1021	Deniz taşıtları imalatı, onarımı, ticareti	47.63.02	Motorlu taşıtlar dışındaki eğlence ve spor amaçlı taşıtların perakende ticareti (tekne, yelkenli, kano, kayık, bot, balon,vb. ile deniz taşıtları için dıştan takmalı motorlar dahil)
1022	Dökümcülük	24.45.01	Maden cevherlerinden ya da oksitlerden işlenmemiş krom, manganez, nikel, tungsten, molibden, tantalum, kobalt, bizmut, titanyum, zirkonyum, berilyum, germanyum vb. imalatı (alaşımları dahil)(atık ve hurdalardan dahil)
1023	Dökümcülük	24.45.02	Krom, manganez, tungsten, molibden, tantalum, kobalt, bizmut, titanyum, zirkonyum, berilyum, germanyum vb. diğer demir dışı metallerden yapılan ürünlerin imalatı (sermetler ve diğer ara ürünler dahil, nikelden olanlar hariç)
1024	Dökümcülük	24.52.20	Çelik dökümü
1025	Dökümcülük	24.53.01	Hafif metallerin dökümü
1026	Dökümcülük	24.54.02	Değerli metallerin dökümü
1027	Dökümcülük	24.54.90	Demir dışı diğer metallerin dökümü (değerli metallerin dökümü hariç)
1028	Dökümcülük	25.63.01	Metalden kalıp ve döküm modeli imalatı (kek ve ayakkabı kalıpları hariç)
1029	Dökümcülük	25.63.02	Plastikten kalıp ve döküm modeli imalatı (kek ve ayakkabı kalıpları hariç)
1030	Dökümcülük	25.99.12	Kalıba dökülerek yapılan zil, çan, gong vb. eşyalar ile adi metallerden kalıba dökülerek yapılan biblo, heykelcik ve diğer süs eşyası imalatı (bisiklet zilleri dahil ancak bakırdan olanlar ile mutfak eşyaları hariç)
1031	Ev aletleri imalatı, onarımı, ticareti	27.52.05	Elektriksiz yemek pişirme cihazlarının imalatı (gaz yakıtlı set üstü ocaklar, gaz veya sıvı yakıtlı fırınlar ve ocaklar vb.)
1032	Ev aletleri imalatı, onarımı, ticareti	27.52.06	Elektriksiz ev aletlerinin aksam ve parçalarının imalatı
1033	Ev aletleri imalatı, onarımı, ticareti	47.55.09	Elektriksiz fırın ve ocaklar ile hava ve su ısıtıcılarının perakende ticareti
1034	Ev aletleri imalatı, onarımı, ticareti	95.22.02	Ev ve bahçe gereçlerinin bakım ve onarımı
1035	Hurdacılık	38.11.01	Tehlikesiz atıkların toplanması (çöpler, geri dönüştürülebilir maddeler, tekstil atıkları, vb.) (inşaat ve yıkım atıkları, çalı, çırpı, moloz gibi enkazlar hariç)
1036	Hurdacılık	38.11.03	Tehlikesiz atık transfer istasyonlarının işletilmesi
1037	Hurdacılık	38.12.01	Tehlikeli atıkların toplanması
1038	Hurdacılık	38.21.02	Gemi ve yüzer yapıların hurdalarının materyallerinin geri kazanımı amacıyla parçalara ayrılması (sökülmesi)
1039	Hurdacılık	38.21.03	Hurdaların geri kazanım amacıyla parçalara ayrılması (otomobil, bilgisayar, televizyon vb. donanımlar) (gemiler ve yüzer yapılar ile satmak için kullanılabilir parçalar oluşturmak amacıyla sökme hariç)
1040	Hurdacılık	38.21.04	Tasnif edilmiş metal atıklar, hurdalar ve diğer parçaların genellikle mekanik veya kimyasal değişim işlemleri ile geri kazanılması
1041	Hurdacılık	38.21.05	Tasnif edilmiş metal dışı atıklar, hurdalar ve diğer parçaların genellikle mekanik veya kimyasal değişim işlemleri ile geri kazanılması (plastik atıkların kimyasal işlemlerle geri kazanılması hariç)
1042	Hurdacılık	38.22.00	Enerji geri kazanımı
1043	Hurdacılık	38.23.00	Diğer atık geri kazanımı
1044	Hurdacılık	38.31.00	Enerji geri kazanımı olmaksızın atıkların yakılması
1045	Hurdacılık	38.32.03	Tehlikesiz atıkların düzenli veya kalıcı olarak depolanması
1046	Hurdacılık	38.32.04	Tehlikeli atıkların düzenli veya kalıcı olarak depolanması (radyoaktif atıklar hariç)
1047	Hurdacılık	38.33.00	Diğer atıkların bertarafı
1048	Hurdacılık	46.87.01	Atık ve hurda toptan ticareti (metal olanlar) (kağıt, cam, plastik vb. ikincil hammaddeler hariç)
1049	Hurdacılık	46.87.02	Atık ve hurda toptan ticareti (kağıt, cam, plastik vb. olanlar) (metal olanlar hariç)
1050	İklimlendirme, soğutma sistemi imalatı, kurulumu, onarımı	28.21.10	Güneşle (güneş kolektörleri), buharla ve yağla ısıtma sistemleri ile benzeri ocak ve ısınma donanımları gibi elektriksiz ev tipi ısıtma, soğutma, havalandırma donanımlarının imalatı
1051	İklimlendirme, soğutma sistemi imalatı, kurulumu, onarımı	28.25.01	Sanayi tipi soğutucu ve dondurucu donanımları ile ısı pompalarının imalatı (camekanlı, tezgahlı veya mobilya tipi soğutucular, kondenserleri ısı değiştiricisi fonksiyonu gören kompresörlü üniteler vb.)
1052	İklimlendirme, soğutma sistemi imalatı, kurulumu, onarımı	28.25.02	Sanayi tipi fan ve vantilatörlerin imalatı (çatı havalandırma pervaneleri dahil)
1053	İklimlendirme, soğutma sistemi imalatı, kurulumu, onarımı	28.25.03	İklimlendirme cihazlarının (klimalar) imalatı (motorlu taşıtlarda kullanılanlar hariç)
1054	İklimlendirme, soğutma sistemi imalatı, kurulumu, onarımı	29.32.24	Motorlu kara taşıtları için iklimlendirme cihazlarının (klimalar) imalatı
1055	İklimlendirme, soğutma sistemi imalatı, kurulumu, onarımı	33.12.06	Sanayi tipi soğutma ve havalandırma ekipmanlarının onarım ve bakımı
1056	İklimlendirme, soğutma sistemi imalatı, kurulumu, onarımı	33.20.45	Sanayi tipi ısıtma, iklimlendirme ve soğutma cihaz ve ekipmanlarının kurulumu
1057	İklimlendirme, soğutma sistemi imalatı, kurulumu, onarımı	35.30.21	Buhar ve sıcak su üretimi, toplanması ve dağıtımı
1058	İklimlendirme, soğutma sistemi imalatı, kurulumu, onarımı	43.22.06	Bina veya diğer inşaat projelerinde ısıtma, havalandırma, soğutma ve iklimlendirme sistemlerinin onarım ve bakımı
1059	İklimlendirme, soğutma sistemi imalatı, kurulumu, onarımı	43.22.07	Bina veya diğer inşaat projelerinde ısıtma, havalandırma, soğutma ve iklimlendirme sistemlerinin kurulumu
1060	Kalaycılık, kaplamacılık	24.43.01	Kurşun tabaka, levha, şerit, folyo, kurşun tozu ve pulu imalatı (alaşımdan olanlar dahil)
1061	Kalaycılık, kaplamacılık	24.43.02	Kurşun imalatı (işlenmemiş)
1062	Kalaycılık, kaplamacılık	24.43.05	Kalay imalatı (işlenmemiş halde)
1063	Kalaycılık, kaplamacılık	24.43.06	Çinko imalatı (işlenmemiş halde)
1064	Kalaycılık, kaplamacılık	24.43.08	Çinko sac, tabaka, levha, şerit, folyo, çinko tozları, vb. imalatı (alaşımdan olanlar dahil)
1065	Kalaycılık, kaplamacılık	25.51.01	Metallerin nikel ile kaplanması (nikelajcılık) faaliyeti
1066	Kalaycılık, kaplamacılık	25.51.02	Metallerin kalay ile kaplanması (kalaycılık) faaliyeti
1067	Kalaycılık, kaplamacılık	25.51.09	Metallerin diğer malzemelerle kaplanması (ısıl işlem hariç)
1068	Kalaycılık, kaplamacılık	25.52.00	Metallerin ısıl işlemi
1069	Karoser imalatı, kaportacılık	29.20.01	Treyler (römork), yarı treyler (yarı römork) ve mekanik hareket ettirici tertibatı bulunmayan diğer araçların parçalarının imalatı (bu araçların karoserleri, kasaları, aksları ve diğer parçaları)
1070	Karoser imalatı, kaportacılık	29.20.02	Motorlu kara taşıtları için karoser, kabin, kupa, dorse ve damper imalatı (otomobil, kamyon, kamyonet, otobüs, minibüs, traktör, damperli kamyon ve özel amaçlı motorlu kara taşıtlarının karoserleri)
1071	Karoser imalatı, kaportacılık	29.20.04	Treyler (römork) ve yarı treyler (yarı römork) imalatı, römorklar için şasi imalatı (karavan tipinde olanlar ve tarımsal amaçlı olanlar hariç)
1072	Karoser imalatı, kaportacılık	29.20.05	Karavan tipinde treyler (römork) ve yarı treyler (yarı römork) imalatı - ev olarak veya kamp için kullanılanlar
1073	Karoser imalatı, kaportacılık	29.20.06	Motorlu kara taşıtlarının modifiye edilmesi ve karoser hizmetleri
1074	Karoser imalatı, kaportacılık	30.99.99	Başka yerde sınıflandırılmamış diğer ulaşım ekipmanlarının imalatı
1075	Karoser imalatı, kaportacılık	33.12.30	Tarımsal amaçlı kullanılan römorkların onarım ve bakımı
1076	Karoser imalatı, kaportacılık	95.31.04	Motorlu kara taşıtlarının karoser ve kaporta onarımı vb. faaliyetleri
1077	Kuyumculuk	08.99.03	Kıymetli ve yarı kıymetli taşların ocakçılığı (kehribar, Oltu taşı, lüle taşı ve elmas hariç)
1078	Kuyumculuk	24.41.16	İşlenmemiş, yarı işlenmiş, toz halde altın imalatı ile gümüş veya adi metallerin altınla preslenerek kaplanması (Mücevher ve benzeri eşyaların imalatı hariç)
1079	Kuyumculuk	24.41.17	İşlenmemiş, yarı işlenmiş, toz halde gümüş imalatı ile adi metallerin gümüşle preslenerek kaplanması (Mücevher ve benzeri eşyaların imalatı hariç)
1080	Kuyumculuk	24.41.18	İşlenmemiş, yarı işlenmiş, toz halde platin imalatı ile altın, gümüş veya adi metallerin platinle preslenerek kaplanması (paladyum, rodyum, osmiyum ve rutenyum imalatı ile platin katalizör imalatı dahil) (Mücevher ve benzeri eşyaların imalatı hariç)
1081	Kuyumculuk	24.41.19	Değerli metal alaşımlarının imalatı (Mücevher ve benzeri eşyaların imalatı hariç)
1082	Kuyumculuk	32.12.01	Değerli metallerden takı ve mücevherlerin imalatı (değerli metallerle baskı, yapıştırma vb. yöntemlerle giydirilmiş adi metallerden olanlar dahil)
1083	Kuyumculuk	32.12.04	İnci ve değerli doğal taşların işlenmesi ve değerli taşlardan takı ve mücevher ile bunların parçalarının imalatı (sentetik veya yeniden oluşturulmuş olanlar dahil)
1084	Kuyumculuk	32.12.90	Mücevher ve benzeri diğer eşyaların imalatı
1085	Kuyumculuk	32.99.03	Pipo, sigara ağızlıkları, Oltu veya lüle taşından tespih vb. imalatı
1086	Kuyumculuk	46.48.01	Mücevher ve takı toptan ticareti (altın, gümüş, vb. olanlar) (imitasyon olanlar hariç)
1087	Kuyumculuk	46.82.02	Değerli metal cevherleri ve konsantrelerinin toptan ticareti (altın, gümüş, platin vb.)
1088	Kuyumculuk	47.77.01	Altın ve diğer değerli metallerden takı, eşya ve mücevherat perakende ticareti (kuyumculuk ürünleri perakende ticareti dahil, gümüşten olanlar hariç)
1089	Kuyumculuk	47.77.02	Gümüş takı, eşya ve mücevherat perakende ticareti (gümüşçü ürünleri perakende ticareti)
1090	Kuyumculuk	47.77.05	Doğal inciden veya kültür incisinden ürünler ile değerli ya da yarı değerli taşlardan yapılan ürünlerin perakende ticareti (pırlanta, yakut, zümrüt, safir vb.den yapılan ürünler)
1091	Kuyumculuk	95.25.02	Mücevherlerin onarımı
1092	Makine kurulumu, onarımı	27.90.01	Elektro kaplama makinelerinin imalatı (galvanoplasti, elektro kaplama, elektroliz veya elektroforez için)
1093	Makine kurulumu, onarımı	28.11.08	Türbin ve türbin parçalarının imalatı (rüzgar, gaz, su ve buhar türbinleri ile su çarkları ve bunların parçaları) (hava taşıtları için turbo jetler veya turbo pervaneler hariç)
1094	Makine kurulumu, onarımı	28.11.09	Deniz taşıtlarında, demir yolu taşıtlarında ve sanayide kullanılan kıvılcım ateşlemeli veya sıkıştırma ateşlemeli içten yanmalı motorların ve bunların parçalarının imalatı (hava taşıtı, motorlu kara taşıtı ve motosiklet motorları hariç)
1095	Makine kurulumu, onarımı	28.11.10	İçten yanmalı motorlar, dizel motorlar vb.de kullanılan pistonlar, silindirler ve silindir blokları, silindir başları, silindir gömlekleri, emme ve egzos subapları, segmanlar, hareket kolları, karbüratörler, yakıt memeleri vb.nin imalatı  (hava taşıtı, motorlu kara taşıtı ve motosiklet motorları hariç)
1096	Makine kurulumu, onarımı	28.12.05	Akışkan gücü ile çalışan ekipmanların ve bunların parçalarının imalatı (hidrolik ve pnömatik motorlar, hidrolik pompalar, hidrolik ve pnömatik valfler, hidrolik sistemler ve bunların parçaları)
1097	Makine kurulumu, onarımı	28.13.01	Hava veya vakum pompaları ile hava veya diğer gaz kompresörlerinin imalatı (el ve ayakla çalışan hava pompaları ile motorlu taşıtlar için olanlar hariç)
1098	Makine kurulumu, onarımı	28.13.02	Sıvı pompaları ve sıvı elevatörleri imalatı (yakıt, yağlama, soğutma ve diğer amaçlar için) (deplasmanlı ve santrifüjlü pompalar ile benzinliklerde kullanılan akaryakıt pompaları dahil) (tulumba dahil, içten yanmalı motorlar için olanlar hariç)
1099	Makine kurulumu, onarımı	28.13.03	El ve ayakla çalışan hava pompalarının imalatı
1100	Makine kurulumu, onarımı	28.15.01	Rulmanlar ve mekanik güç aktarma donanımları imalatı
1101	Makine kurulumu, onarımı	28.15.02	Debriyajlar (kavramalar), mil (şaft) kaplinler ve üniversal mafsalların imalatı (motorlu kara taşıtlarında kullanılan debriyajlar hariç)
1102	Makine kurulumu, onarımı	28.15.03	Dişliler/dişli takımları, bilyeli ve makaralı vidalar, şanzımanlar, vites kutuları ve diğer hız değiştiricilerin imalatı (motorlu kara taşıtlarında kullanılan vites kutuları ve diferansiyelleri hariç)
1103	Makine kurulumu, onarımı	28.15.04	Volanlar ve kasnaklar ile mafsallı bağlantı zincirleri ve güç aktarım zincirlerinin imalatı
1104	Makine kurulumu, onarımı	28.21.07	Elektrikli veya elektriksiz laboratuar ocakları, döküm ocakları vb. endüstriyel ocak ve fırınlarının imalatı (çöp yakma fırınları ile elektrikli ekmek ve unlu mamul fırınları dahil)
1105	Makine kurulumu, onarımı	28.21.99	Başka yerde sınıflandırılmamış diğer fırın ve ocakların (sanayi ocakları) imalatı (ocak brülörleri (ateşleyicileri), endüksiyon veya dielektrik ısıtma ekipmanları, mekanik kömür taşıyıcıları, mekanik ızgaralar, mekanik kül boşaltıcıları ve benzeri cihazların imalatı, vb.)
1106	Makine kurulumu, onarımı	28.22.10	El veya motor gücü ile çalışan kaldırma, taşıma, yükleme ya da boşaltma makinelerinin imalatı
1107	Makine kurulumu, onarımı	28.22.11	Asansör, yürüyen merdiven ve yürüyen yolların imalatı (yeraltında kullanılanlar hariç)
1108	Makine kurulumu, onarımı	28.24.01	Motorlu veya pnömatik (hava basınçlı) el aletlerinin imalatı
1109	Makine kurulumu, onarımı	28.29.04	Sıvılar için filtreleme veya arıtma makine ve cihazlarının imalatı (suyun filtre edilmesi/arıtılmasına mahsus cihazlar dahil)
1110	Makine kurulumu, onarımı	28.29.10	Yangın söndürücüler, püskürtme tabancaları, buhar veya kum püskürtme makineleri vb. sıvı ve tozları atan, dağıtan ya da püskürten mekanik cihazların imalatı
1111	Makine kurulumu, onarımı	28.29.90	Diğer genel amaçlı makinelerin imalatı
1112	Makine kurulumu, onarımı	28.30.08	Tarımsal amaçlı römork veya yarı römork imalatı
1113	Makine kurulumu, onarımı	28.30.09	Yumurta, meyve ve diğer tarımsal ürünlerin temizlenmesi, tasnif edilmesi veya derecelendirilmesi için kullanılan makine ve ekipmanların imalatı
1114	Makine kurulumu, onarımı	28.30.11	Kümes hayvanı makineleri, arıcılık makineleri ve hayvan yemi hazırlama makinelerinin ve donanımlarının imalatı (kuluçka makineleri dahil)
1115	Makine kurulumu, onarımı	28.30.12	Çim biçme makinelerinin imalatı (traktörlere monte edilen kesici barlar dahil)
1116	Makine kurulumu, onarımı	28.30.13	Hasat ve harman makinelerinin imalatı (biçer döver, saman yapma makinesi, ot ve saman balyalama makinesi, kök ve yumru hasat makinesi, vb.)
1117	Makine kurulumu, onarımı	28.30.14	Pulluk, saban, tırmık, diskaro, skarifikatör, kültivatör, çapa makinesi, mibzer, fide ve fidan dikim makinesi vb. toprağın hazırlanmasında, ekiminde, dikiminde kullanılan aletler ile gübreleme makinelerinin imalatı
1118	Makine kurulumu, onarımı	28.30.15	Süt sağma makinelerinin imalatı
1119	Makine kurulumu, onarımı	28.30.16	Tarım ve bahçecilikte kullanılan hava, sıvı veya toz atma, dağıtma, püskürtme ve iklimlendirme makinelerinin imalatı (sulama cihazları, pülverizatörler, zirai mücadelede kullanılan portatif sıvı ve toz püskürtücüler, don pervaneleri vb.)
1120	Makine kurulumu, onarımı	28.30.90	Ormancılığa özgü makineler ile tarla bahçe bakımına mahsus diğer makine ve cihazların imalatı
1121	Makine kurulumu, onarımı	28.41.01	Takım tezgahları (metal işlemek için lazer ve benzerleriyle çalışanlar) ile metal ve benzerlerini işlemek için işleme merkezlerinin imalatı
1122	Makine kurulumu, onarımı	28.41.03	Metal tornalama, delme, frezeleme ve planyalama takım tezgahlarının imalatı
1123	Makine kurulumu, onarımı	28.41.07	Metal işleyen takım tezgahlarının parça ve aksesuarlarının imalatı (alet tutacakları ve kendinden açılan pafta kafaları, iş tutacakları, ayırıcı kafalar ve takım tezgahları için diğer özel aksesuarlar hariç)
1124	Makine kurulumu, onarımı	28.41.90	Metal işlemek için kullanılan diğer takım tezgahlarının imalatı
1125	Makine kurulumu, onarımı	28.42.01	Ahşap, mantar, kemik, sert kauçuk, sert plastik veya benzeri sert malzemeleri işlemek için olan takım tezgahı ile bunların parçalarının imalatı (transfer, testere, planya, freze, taşlama, zımparalama, parlatma, bükme, delme, dilimleme, pres, vb.)
1126	Makine kurulumu, onarımı	28.42.02	Takım tezgahları ve el aletleri için takım tutucuları ve kendinden açılan pafta kafaları, işlenecek parça tutucuları, bölme başlıkları ve diğer özel ek parçalar, dingiller, yüksükler ve rakorlar ile fikstürlerin imalatı
1127	Makine kurulumu, onarımı	28.42.03	Taş, seramik, beton veya benzeri mineral malzemeleri işlemek veya camı soğuk işlemek için olan takım tezgahı ile bunların parçalarının imalatı (testere, taşlama, parlatma, vb.)
1128	Makine kurulumu, onarımı	28.42.99	Başka yerde sınıflandırılmamış diğer takım tezgahlarının imalatı
1129	Makine kurulumu, onarımı	28.91.01	Konvertörler (metalürji), külçe kalıpları (ingot kalıpları), döküm kepçeleri, döküm makineleri, vb. sıcak metallerin işlenmesi için kullanılan makine ve teçhizatın imalatı
1130	Makine kurulumu, onarımı	28.91.02	Sıcak ve soğuk metal haddeleme makinesi ve metal boru imaline özgü hadde makinesi ile hadde ve metalürji makineleri için silindir ve diğer parçaların imalatı
1131	Makine kurulumu, onarımı	28.92.01	Beton ve harç karıştırıcılarının imalatı (mikserler dahil, beton karıştırıcılı (mikserli) kamyonlar hariç)
1132	Makine kurulumu, onarımı	28.92.03	Taş, toprak, cevher, alçı, çimento ve diğer mineral maddeleri tasnif etme, eleme, ayırma, yıkama, ezme, öğütme, karıştırma, yoğurma vb. işlemden geçirme için kullanılan makinelerin imalatı (beton ve harç karıştırıcılar (mikserler) hariç)
1133	Makine kurulumu, onarımı	28.92.05	Kömür veya kaya kesicileri (havözler), tünel ve kuyu açma makineleri ile delme ve sondaj makinelerinin imalatı (yer altı veya yer üstü)
1134	Makine kurulumu, onarımı	28.92.11	Delme, sondaj, hafriyat ve kazı makinesi parçalarının, vinç ve hareketli kaldırma kafeslerinin ve toprak, taş ve benzeri maddeleri tasnifleme, öğütme, karıştırma veya diğer işlerde kullanılan makine parçalarının imalatı (buldozer bıçakları dahil)
1135	Makine kurulumu, onarımı	28.93.02	Şarap, meyve suyu ve benzeri içeceklerin imalatında kullanılan makinelerin imalatı (presler, eziciler ve benzeri makineler)
1136	Makine kurulumu, onarımı	28.93.03	Süt ürünleri makinelerinin ve santrifüjlü krema ayırıcılarının imalatı
1137	Makine kurulumu, onarımı	28.93.04	Tütünün hazırlanmasında ve işlenmesinde kullanılan makinelerin imalatı (tütün yapraklarını damarlarından ayıran makineler ile enfiye, sigara, puro, pipo tütünü veya çiğneme tütünleri imalinde kullanılan makineler)
1138	Makine kurulumu, onarımı	28.93.06	Değirmencilik sanayiinde, hububat veya kurutulmuş sebzelerin işlenmesi veya öğütülmesi için kullanılan makinelerin imalatı
1139	Makine kurulumu, onarımı	28.93.07	Ekmek ve diğer unlu mamuller için elektrikli olmayan fırınların imalatı (gaz, sıvı ve katı yakıtlı olanlar)
1140	Makine kurulumu, onarımı	28.93.08	Ev tipi olmayan pişirme veya ısıtma cihazlarının imalatı (ev tipi olmayan filtreli kahve makineleri vb. dahil)
1141	Makine kurulumu, onarımı	28.93.09	Tarımsal ürünler için kurutucuların imalatı (kahve, kuruyemiş vb. için kavurma makine ve cihazları dahil)
1142	Makine kurulumu, onarımı	28.93.10	Tohumların, tanelerin veya kuru baklagillerin temizlenmesi, tasnif edilmesi veya derecelendirilmesi için kullanılan makinelerin imalatı (tarımsal selektörler dahil)
1143	Makine kurulumu, onarımı	28.93.99	Gıda ve içeceklerin endüstriyel olarak hazırlanması veya imalatı için başka yerde sınıflandırılmamış makinelerin imalatı
1144	Makine kurulumu, onarımı	28.94.01	Post, deri ve köselelerin işlenmesi ile ayakkabı ve diğer deri eşyaların üretimi veya tamiri için kullanılan makinelerin imalatı
1145	Makine kurulumu, onarımı	28.94.02	Sanayi tipi çamaşır makinesi, kuru temizleme makinesi, çamaşır kurutma makinesi, ütü makinesi ve pres ütü imalatı
1146	Makine kurulumu, onarımı	28.94.03	Sanayi ve ev tipi dikiş makinelerinin imalatı (dikiş makinelerinin iğneleri, mobilyaları, tabanları, kapakları vb. parçaları dahil)
1147	Makine kurulumu, onarımı	28.94.04	Suni ve sentetik tekstil malzemesinin ekstrüzyonu, çekilmesi, tekstüre edilmesi veya kesilmesi için kullanılan makineler ile doğal tekstil elyafı hazırlama makineleri ve dokuma makinelerinin imalatı (çırçır makinesi, taraklama makinesi vb. dahil)
1148	Makine kurulumu, onarımı	28.94.05	Tekstil ipliği ve kumaşını yıkama, ağartma, boyama, apreleme, temizleme, sıkma, sarma, emprenye etme, bitirme, kesme, surfile ve benzerleri için makineler ile keçe imalatında ve bitirilmesinde kullanılan makinelerin imalatı
1149	Makine kurulumu, onarımı	28.94.06	Tekstil büküm makineleri ile katlama, bükme, bobine sarma veya çile yapma makinelerinin imalatı
1150	Makine kurulumu, onarımı	28.94.08	Tekstil amaçlı makinelerle kullanılan yardımcı makinelerin ve tekstil baskı makinelerinin imalatı (ratiyerler, jakardlar, vb.) (ofset baskı makineleri, tipografik, fleksografik, gravür baskı makineleri hariç)
1151	Makine kurulumu, onarımı	28.94.09	Tekstil, giyim eşyası ve deri üretiminde kullanılan makinelerin parçalarının imalatı (dikiş makinelerinde kullanılanlar hariç)
1152	Makine kurulumu, onarımı	28.95.01	Kağıt ve mukavva üretiminde kullanılan makinelerin imalatı
1153	Makine kurulumu, onarımı	28.96.01	Plastik ve kauçuk makinelerinin imalatı
1154	Makine kurulumu, onarımı	28.99.01	Basım ve ciltleme makineleri ile basıma yardımcı makinelerin ve bunların parçalarının imalatı (ofset baskı makinesi, tipografik baskı makinesi, dizgi makinesi, baskı kalıpları için makineler, ciltleme makinesi vb.) (büro tipi baskı makinesi hariç)
1155	Makine kurulumu, onarımı	28.99.05	Otomatik bovling salonu donanımlarının, dönme dolap, atlı karınca, salıncak, poligon, vb. diğer panayır alanı eğlence donanımları ile kumarhane oyun masalarının imalatı
1156	Makine kurulumu, onarımı	28.99.08	Sicim ve halat makinelerinin imalatı
1157	Makine kurulumu, onarımı	28.99.99	Başka yerde sınıflandırılmamış diğer özel amaçlı makinelerin imalatı
1158	Makine kurulumu, onarımı	32.40.02	Bozuk para veya jetonla çalışan oyun makineleri ile bilardo için kullanılan eşya ve aksesuarların imalatı (rulet vb. oyun makineleri ile bilardo masa ve istekaları, isteka dayanakları, bilardo topları, tebeşirleri, toplu veya sürgülü puan sayaçları vb.)
1159	Makine kurulumu, onarımı	32.40.06	Lunapark, masa ve salon oyunları için gereçlerin imalatı
1160	Makine kurulumu, onarımı	33.11.99	Başka yerde sınıflandırılmamış metal ürünlerin onarım ve bakımı (balık kafesleri hariç)
1161	Makine kurulumu, onarımı	33.12.02	Tarım ve ormancılık makinelerinin onarım ve bakımı (traktörlerin bakım ve onarımı hariç)
1162	Makine kurulumu, onarımı	33.12.03	Motor ve türbinlerin onarım ve bakımı (hidrolik, rüzgar, gaz, su, buhar türbinleri) (gemi ve tekne motorları, motorlu kara taşıtı ve motosiklet motorları hariç)
1163	Makine kurulumu, onarımı	33.12.04	Sanayi fırınlarının, ocaklarının ve ocak brülörlerinin onarım ve bakımı
1164	Makine kurulumu, onarımı	33.12.05	Kaldırma ve taşıma ekipmanlarının onarım ve bakımı
1165	Makine kurulumu, onarımı	33.12.08	Madencilik, inşaat, petrol ve gaz sahalarında kullanılan makinelerin onarım ve bakımı
1166	Makine kurulumu, onarımı	33.12.10	Akışkan gücü ile çalışan ekipmanlar, pompalar, kompresörler ile valflerin ve vanaların onarım ve bakımı (akaryakıt pompalarının tamiri dahil)
1167	Makine kurulumu, onarımı	33.12.11	Metal işleme makinelerinin ve takım tezgahlarının onarım ve bakımı (CNC olanlar dahil)
1168	Makine kurulumu, onarımı	33.12.12	Motorlu veya pnömatik (hava basınçlı) el aletlerinin onarımı (yuvarlak/vargel/zincir testere, matkap, pnömatik veya motorlu metal kesme makası, darbeli cıvata anahtarı vb.)
1169	Makine kurulumu, onarımı	33.12.13	Elektrikli kaynak ve lehim aletlerinin onarım ve bakımı
1170	Makine kurulumu, onarımı	33.12.14	Metalürji makinelerinin onarım ve bakımı
1171	Makine kurulumu, onarımı	33.12.15	Gıda, içecek ve tütün işleme makinelerinin onarım ve bakımı
1172	Makine kurulumu, onarımı	33.12.16	Tekstil, giyim eşyası ve deri üretim makinelerinin onarım ve bakımı (triko makinelerinin onarımı dahil)
1173	Makine kurulumu, onarımı	33.12.17	Kağıt, karton ve mukavva üretiminde kullanılan makinelerin onarım ve bakımı
1174	Makine kurulumu, onarımı	33.12.19	Ağaç, mantar, taş, sert kauçuk veya benzeri sert malzemeleri işlemede kullanılan takım tezgahlarının onarım ve bakımı (CNC olanlar dahil)
1175	Makine kurulumu, onarımı	33.12.21	Sıvılar için filtreleme ya da temizleme makineleri ve aparatlarının onarım ve bakımı
1176	Makine kurulumu, onarımı	33.12.27	Kesici aletler ile el aletlerinin onarım ve bakımı (matbaa giyotini, şerit testere, el testeresi, çapa, orak vb. bileyleme ve çarkçılık dahil) (motorlu ve pnömatik olanlar hariç)
1177	Makine kurulumu, onarımı	33.12.28	Plastik ve kauçuk imalatında ve işlenmesinde kullanılan makinelerin onarım ve bakımı
1178	Makine kurulumu, onarımı	33.12.29	Endüstriyel rulmanların, dişlilerin, dişli takımlarının ve tahrik tertibatı elemanlarının onarım ve bakımı
1179	Makine kurulumu, onarımı	33.12.99	Başka yerde sınıflandırılmamış diğer makinelerin onarım ve bakımı (motorlu kara taşıtları, gemiler, tekneler ve uçaklar hariç)
1180	Makine kurulumu, onarımı	33.19.99	Başka yerde sınıflandırılmamış diğer ekipmanların onarımı (ahşap konteyner, gemi fıçı ve varilleri, madeni para ile çalışan oyun makineleri, değirmentaşı, bileme taşı vs.)
1181	Makine kurulumu, onarımı	33.20.36	Metallerin işlenmesinde, kesilmesinde ve şekillendirilmesinde kullanılan makinelerin kurulum hizmetleri
1182	Makine kurulumu, onarımı	33.20.46	Genel amaçlı makinelerin kurulum hizmetleri
1183	Makine kurulumu, onarımı	33.20.52	Fabrikasyon metal ürünlerin kurulum hizmetleri (buhar jeneratörlerinin kurulum hizmetleri ve sanayi tesislerindeki metal boru sistemlerinin kurulumu dahil, merkezi ısıtma sıcak su kazanları (boylerleri) ile makine ve ekipmanlar hariç)
1184	Makine kurulumu, onarımı	33.20.90	Diğer sanayi makine ve ekipmanlarının kurulumu
1185	Makine, yedek parça ticareti	46.14.02	Tarımsal ekipmalar ile makine ve sanayi ekipmanlarının toptan satışı ile ilgili aracıların faaliyetleri
1186	Makine, yedek parça ticareti	46.43.12	Konutlarda, bürolarda ve mağazalarda kullanılan klimaların (iklimlendirme ekipmanlarının) toptan ticareti (sanayi tipi olanlar hariç)
1187	Makine, yedek parça ticareti	46.61.02	Tarım, hayvancılık ve ormancılık makine ve ekipmanları ile aksam ve parçalarının toptan ticareti
1188	Makine, yedek parça ticareti	46.61.03	Çim biçme ve bahçe makine ve ekipmanları ile aksam ve parçalarının toptan ticareti
1189	Makine, yedek parça ticareti	46.62.01	Ağaç işleme takım tezgahları ve parçalarının toptan ticareti (parça tutucuları dahil)
1190	Makine, yedek parça ticareti	46.62.02	Metal işleme takım tezgahlarının ve parçalarının toptan ticareti (parça tutucuları dahil)
1191	Makine, yedek parça ticareti	46.64.05	Tekstil endüstrisi makineleri ile dikiş ve örgü makineleri ve parçalarının toptan ticareti (ev tipi olanlar hariç)
1192	Makine, yedek parça ticareti	46.64.06	Kompresör ve parçalarının toptan ticareti (soğutma, hava ve diğer amaçlar için)
1193	Makine, yedek parça ticareti	46.64.11	İş güvenliği amaçlı kişisel koruyucu donanımların toptan ticareti
1194	Makine, yedek parça ticareti	46.64.12	Yangın söndürücüler, püskürtme tabancaları, buhar veya kum püskürtme makineleri ile benzeri mekanik cihazların toptan ticareti (tarımsal amaçlı kullanılanlar ile taşıtlar için yangın söndürücüler hariç)
1195	Makine, yedek parça ticareti	46.64.16	Makine ve ekipmanlarla ilgili aksam ve parçaların toptan ticareti (motorlu kara taşıtları için olanlar hariç)
1196	Makine, yedek parça ticareti	46.64.99	Başka yerde sınıflandırılmamış diğer makine ve ekipmanların toptan ticareti
1197	Makine, yedek parça ticareti	46.84.03	Demirden veya çelikten merkezi ısıtma radyatörleri, merkezi ısıtma kazanları (kombiler dahil) ile bunların parçalarının toptan ticareti (buhar jeneratörleri ve kızgın su üreten kazanlar hariç)
1198	Makine, yedek parça ticareti	47.52.23	Yangın söndürücüler ve ekipmanlarının perakende ticareti (arabalar için olanlar ve yüksek basınçlı olanlar hariç)
1199	Makine, yedek parça ticareti	77.31.01	Tarımsal makine ve ekipmanların operatörsüz olarak kiralanması ve operasyonel leasingi (çim biçme makineleri hariç)
1200	Motosiklet, bisiklet imalatı, onarımı	30.91.02	Motosiklet parça ve aksesuarları imalatı (motosikletler için pistonlar, piston segmanları, karbüratörler dahil)
1201	Motosiklet, bisiklet imalatı, onarımı	30.92.01	Bisiklet imalatı (yardımcı elektrikli motoru bulunan bisiklet dahil) (çocuklar için plastik bisikletler hariç)
1202	Motosiklet, bisiklet imalatı, onarımı	30.92.02	Bisiklet parça ve aksesuarlarının imalatı (jantlar, gidonlar, iskelet, çatallar, pedal fren göbekleri/poyraları, göbek/poyra frenleri, krank dişlileri, pedallar ve serbest dişlilerin parçaları, vb.)
1203	Motosiklet, bisiklet imalatı, onarımı	30.92.05	Bebek arabaları, pusetler ve bunların parçalarının imalatı
1204	Motosiklet, bisiklet imalatı, onarımı	30.99.01	Mekanik hareket ettirici tertibatı bulunmayan araçların imalatı (alışveriş arabaları, sanayi el arabaları, işportacı arabaları, bagaj arabaları, elle çekilen golf arabaları, hasta nakli için arabalar, kızaklar dahil)
1205	Motosiklet, bisiklet imalatı, onarımı	95.29.05	Bisiklet onarımı
1206	Motosiklet, bisiklet imalatı, onarımı	95.32.00	Motosikletlerin onarım ve bakımı
1207	Motosiklet, bisiklet ticareti	46.18.09	Motosikletler, motorlu bisikletler ve bunların parça ve aksesuarlarının toptan satışı ile ilgili aracıların faaliyetleri
1208	Motosiklet, bisiklet ticareti	46.73.25	Motosikletler ve motorlu bisikletlerin parça ve aksesuarlarının toptan ticareti
1209	Motosiklet, bisiklet ticareti	47.63.04	Bisiklet perakende ticareti
1210	Motosiklet, bisiklet ticareti	47.83.01	Motosikletler ve motorlu bisikletlerin perakende ticareti
1211	Motosiklet, bisiklet ticareti	47.83.02	Motosikletler ve motorlu bisikletlerin parça ve aksesuarlarının perakende ticareti
1212	Oto bakım servisçiliği	33.12.09	Tarım ve ormancılıkta kullanılan motokültörler ve traktörlerin onarım ve bakımı
1213	Oto bakım servisçiliği	71.20.12	Entegre mekanik ve elektrik sistemleri konusunda teknik test ve analiz faaliyetleri
1214	Oto bakım servisçiliği	95.31.01	Motorlu kara taşıtlarının genel onarım ve bakımı faaliyetleri
1215	Oto boyacılık	95.31.05	Motorlu kara taşıtlarının boyanması faaliyetleri
1216	Oto döşemecilik	29.32.22	Motorlu kara taşıtları için koltuk imalatı
1217	Oto döşemecilik	30.11.06	Gemiler ve yüzer yapılar için oturulacak yerlerin imalatı
1218	Oto döşemecilik	95.31.07	Motorlu kara taşıtların koltuk ve döşemelerinin onarım ve bakımı faaliyetleri
1219	Oto elektrikçilik	95.31.06	Motorlu kara taşıtlarının elektrik sistemlerinin onarım faaliyetleri
1220	Oto lastik onarımı	22.11.19	Lastik tekerleklerinin yeniden işlenmesi ve sırt geçirilmesi (lastiğin kaplanması)
1221	Oto lastik onarımı	95.31.02	Motorlu kara taşıtlarının lastik onarımı faaliyetleri
1222	Oto lastik ticareti	46.72.13	Motorlu kara taşıtı lastiklerinin ve jantlarının toptan ticareti (motosiklet lastik ve jantları hariç)
1223	Oto lastik ticareti	47.82.04	Motorlu kara taşıtı lastiklerinin ve jantlarının perakende ticareti (motosiklet parça ve aksesuarları hariç)
1224	Oto LPG montajı	95.31.08	Motorlu kara taşıtlarına yakıt sistemi (benzin, dizel, LPG, CNG, LNG vb.) montajı ve bakımı hizmetleri
1225	Oto yedek parça imalatı	28.29.18	İçten yanmalı motorlar için yağ filtresi, yakıt filtresi, hava filtresi, gres nipelleri, yağ keçesi ve benzerlerinin imalatı
1226	Oto yedek parça imalatı	29.31.90	Motorlu kara taşıtları için diğer elektrik ve elektronik donanımların imalatı (oto alarm sistemlerinin imalatı dahil)
1227	Oto yedek parça imalatı	29.32.20	Motorlu kara taşıtları için vites kutusu, debriyaj, fren, aks, amortisör gibi çeşitli parça ve aksesuarların imalatı
1228	Oto yedek parça imalatı	29.32.21	Motorlu kara taşıtları için karoser, kabin ve kupalara ait parça ve aksesuarların imalatı
1229	Oto yedek parça imalatı	30.92.03	Engelli araçlarının imalatı (motorlu, motorsuz, akülü, şarjlı, vb.)
1230	Oto yedek parça imalatı	30.92.04	Engelli araçlarının parça ve aksesuarlarının imalatı
1231	Oto yedek parça ticareti	46.18.08	Motorlu kara taşıtlarının parça ve aksesuarlarının toptan satışı ile ilgili aracıların faaliyetleri
1232	Oto yedek parça ticareti	46.72.12	Motorlu kara taşıtlarının parçalarının toptan ticareti (cam, lastik ve jantlar ile motosiklet parçaları hariç)
1233	Oto yedek parça ticareti	46.72.14	Motorlu kara taşıtlarının aksesuarlarının toptan ticareti (motosiklet aksesuarları hariç)
1234	Oto yedek parça ticareti	47.30.02	Motorlu kara taşıtları için yağlama ve soğutma ürünlerinin perakende ticareti
1235	Oto yedek parça ticareti	47.82.05	Motorlu kara taşıtı camlarının perakende ticareti (motosiklet parça ve aksesuarları hariç)
1236	Oto yedek parça ticareti	47.82.06	Motorlu kara taşıtlarının ikinci el (kullanılmış) parçalarının perakende ticareti (motosiklet parça ve aksesuarları hariç)
1237	Oto yedek parça ticareti	47.82.07	Motorlu kara taşıtlarının aksesuarlarının perakende ticareti (motosiklet parça ve aksesuarları hariç)
1238	Oto yedek parça ticareti	47.82.08	Motorlu kara taşıtlarının akülerinin perakende ticareti
1239	Oto yedek parça ticareti	47.82.90	Motorlu kara taşıtlarının diğer parça ve aksesuarlarının perakende ticareti
1240	Oto yıkama, yağlama	95.31.03	Motorlu kara taşıtlarının yağlama, yıkama, cilalama vb. faaliyetlerİ
1241	Saatçilik	23.15.08	Duvar saati, kol saati veya gözlük için camlar (bombeli, kavisli, içi oyuk vb. şekilde fakat, optik açıdan işlenmemiş) ile bu tür camların imalatı için kullanılan içi boş küre ve bunların parçalarının imalatı
1242	Saatçilik	26.52.03	Devam kayıt cihazları, zaman kayıt cihazları, parkmetreler; duvar ve kol saati makineli zaman ayarlı anahtarların imalatı (vardiya saati vb.)
1243	Saatçilik	26.52.04	Kol, masa, duvar ve cep saatlerinin, bunların makinelerinin, kasalarının ve diğer parçalarının imalatı (kronometreler ve taşıtlar için gösterge panellerinde bulunan saatler ve benzeri tipteki saatler dahil)
1244	Saatçilik	46.48.02	Saat toptan ticareti
1245	Saatçilik	47.77.03	Saat (kol, masa, duvar vb. saatler ile kronometreler) perakende ticareti
1246	Saatçilik	95.25.01	Saatlerin onarımı (kronometreler dahil, devam kayıt cihazları hariç)
1247	Saatçilik	95.25.03	Saatlerin yenilenmesi hizmeti faaliyetleri (telefon özelliği olmayan akıllı saatler)
1248	Soba, banyo kazanı, şofben imalatı, onarımı, ticareti	27.52.02	Elektriksiz ev tipi gaz, sıvı veya katı yakıtlı soba, kuzine, ızgara, şömine, mangal, semaver, su ısıtıcısı (termosifon, şofben vb.) vb. aletlerin imalatı
1249	Soba, banyo kazanı, şofben imalatı, onarımı, ticareti	95.22.03	Termosifon, şofben, banyo kazanı vb. onarım ve bakımı (merkezi ısıtma kazanlarının (boylerler) onarımı hariç)
1250	Tenekecilik	25.99.13	Metalden çatı olukları, çatı kaplamaları vb. imalatı
1251	Tenekecilik	43.41.00	Çatı işleri
1252	Tornacılık	25.40.04	Metallerin dövülmesi, preslenmesi, baskılanması ve damgalanması
1253	Tornacılık	25.40.05	Toz metalürjisi
1254	Tornacılık	25.53.01	Metallerin makinede işlenmesi (torna tesfiye işleri, metal parçaları delme, tornalama, frezeleme, rendeleme, parlatma, oluk açma, perdahlama, birleştirme, kaynak yapma, çapak alma, kumlama, vb. faaliyetler)
1255	Tornacılık	25.53.02	CNC oksijen, CNC plazma, CNC su jeti vb. makinelerinin kullanılması yoluyla metallerin kesilmesi veya üzerlerinin yazılması
1256	Tornacılık	25.53.03	Lazer ışınlarının kullanılması yoluyla metallerin kesilmesi veya üzerlerinin yazılması
1257	Tornacılık	28.14.01	Sanayi musluk, valf ve vanaları, sıhhi tesisat ve ısıtmada kullanılan musluk ve vanalar ile doğalgaz vanaları, dökme olanlar
1258	Tornacılık	28.14.02	Sanayi musluk, valf ve vanaları, sıhhi tesisat ve ısıtmada kullanılan musluk ve vanalar ile doğalgaz vanaları, dökme olanlar hariç
1259	Tüp gaz bayiliği	47.78.10	Evlerde kullanılan tüpgaz perakende ticareti
1260	Pazarda ayakkabı, tekstil ürünleri ticareti	47.51.06	Tezgahlar ve pazar yerleri vasıtasıyla tuhafiye, manifatura ve mefruşat ürünleri perakende ticareti (seyyar satıcılar hariç)
1261	Pazarda ayakkabı, tekstil ürünleri ticareti	47.71.13	Tezgahlar ve pazar yerleri vasıtasıyla iç giyim eşyası, dış giyim eşyası, çorap, giysi aksesuarı ve ayakkabı perakende ticareti (seyyar satıcılar hariç)
1262	Pazarda bitki, hayvan, su ürünleri ticareti	47.23.02	Tezgahlar ve pazar yerleri vasıtasıyla balık ve diğer su ürünleri perakende ticareti (seyyar satıcılar hariç)
1263	Pazarda bitki, hayvan, su ürünleri ticareti	47.76.06	Tezgahlar ve pazar yerleri vasıtasıyla çiçek, bitki ve bitki tohumu (çiçek toprağı ve saksıları dahil) perakende ticareti (seyyar satıcılar hariç)
1264	Pazarda bitki, hayvan, su ürünleri ticareti	47.76.07	Tezgahlar ve pazar yerleri vasıtasıyla canlı büyük ve küçükbaş hayvan, canlı kümes hayvanı, ev hayvanı ve yemlerinin perakende ticareti (seyyar satıcılar hariç)
1265	Pazarda çeşitli malların ticareti	47.12.03	Tezgahlar ve pazar yerleri vasıtasıyla bys. diğer malların perakende ticareti (seyyar satıcılar hariç)
1266	Pazarda çeşitli malların ticareti	47.52.24	Tezgahlar ve pazar yerleri vasıtasıyla mutfak eşyaları ile banyo ve tuvalette kullanılan eşyaların perakende ticareti (seyyar satıcılar hariç)
1267	Pazarda çeşitli malların ticareti	47.52.25	Tezgahlar ve pazar yerleri vasıtasıyla elektrikli alet, cihaz ve elektrik malzemeleri, el aletleri ile hırdavat perakende ticareti (seyyar satıcılar hariç)
1268	Pazarda çeşitli malların ticareti	47.53.04	Tezgahlar ve pazar yerleri vasıtasıyla halı, kilim, vb. perakende ticareti (seyyar satıcılar hariç)
1269	Pazarda çeşitli malların ticareti	47.55.12	Tezgahlar ve pazar yerleri vasıtasıyla ev ve büro mobilyaları (ağaç, metal, vb.) perakende ticareti (seyyar satıcılar hariç)
1270	Pazarda çeşitli malların ticareti	47.64.09	Tezgahlar ve pazar yerleri vasıtasıyla imitasyon takı, süs eşyası, oyun, oyuncak, turistik ve hediyelik eşya perakende ticareti (seyyar satıcılar hariç)
1271	Pazarda çeşitli malların ticareti	47.75.02	Tezgahlar ve pazar yerleri vasıtasıyla kişisel bakım ve kozmetik ürünleri ile temizlik ürünleri perakende ticareti (seyyar satıcılar hariç)
1272	Pazarda sebze, meyve ticareti	47.21.06	Tezgahlar ve pazar yerleri vasıtasıyla sebze ve meyve (taze veya işlenmiş) (zeytin dahil) perakende ticareti (seyyar satıcılar hariç)
1273	Pazarda yiyecek, içecek ticareti	47.11.03	Tezgahlar ve pazar yerleri vasıtasıyla diğer gıda ürünleri (bal, un, tahıl, pirinç, bakliyat vb. dahil) perakende ticareti (seyyar satıcılar hariç)
1274	Pazarda yiyecek, içecek ticareti	47.22.07	Tezgahlar ve pazar yerleri vasıtasıyla şarküteri ürünleri, süt ve süt ürünleri ile yumurta perakende ticareti (seyyar satıcılar hariç)
1275	Pazarda yiyecek, içecek ticareti	47.24.03	Tezgahlar ve pazar yerleri vasıtasıyla fırın ürünleri perakende ticareti (seyyar satıcılar hariç)
1276	Pazarda yiyecek, içecek ticareti	47.24.04	Tezgahlar ve pazar yerleri vasıtasıyla şekerleme perakende ticareti (seyyar satıcılar hariç)
1277	Pazarda yiyecek, içecek ticareti	47.27.09	Tezgahlar ve pazar yerleri vasıtasıyla yenilebilir katı ve sıvı yağ (tereyağı hariç) perakende ticareti (seyyar satıcılar hariç)
1278	Pazarda yiyecek, içecek ticareti	47.27.10	Tezgahlar ve pazar yerleri vasıtasıyla çay, kahve, kakao, baharat perakende ticareti (seyyar satıcılar hariç)
1279	Seyyar satıcılık	47.11.04	Seyyar olarak ve motorlu araçlarla gıda ürünleri ve içeceklerin (alkollü içecekler hariç) perakende ticareti
1280	Seyyar satıcılık	47.11.06	Mağaza, tezgah, pazar yeri dışında yapılan perakende ticaret (ev ev dolaşarak veya komisyoncular tarafından perakende olarak yapılanlar)
1281	Seyyar satıcılık	47.12.02	Seyyar olarak ve motorlu araçlarla diğer malların perakende ticareti
1282	Seyyar satıcılık	47.51.07	Seyyar olarak ve motorlu araçlarla tekstil, giyim eşyası ve ayakkabı perakende ticareti
1283	Seyyar satıcılık	56.12.00	Seyyar yemek hizmeti faaliyetleri
1284	Akaryakıt ticareti	20.51.24	Sıvı biyoyakıt imalatı
1285	Akaryakıt ticareti	46.81.01	Sıvı yakıtlar ve bunlarla ilgili ürünlerin toptan ticareti
1286	Akaryakıt ticareti	47.30.01	Motorlu kara taşıtı ve motosiklet yakıtının perakende ticareti
1287	Akaryakıt ticareti	47.78.09	Evlerde kullanılan fuel oil perakende ticareti
1288	Durak, otopark işletmeciliği	52.21.07	Otopark ve garaj işletmeciliği (bisiklet parkları ve karavanların kışın saklanması dahil)
1289	Durak, otopark işletmeciliği	52.21.09	Kara yolu yolcu taşımacılığına yönelik otobüs terminal hizmetleri
1290	Durak, otopark işletmeciliği	52.21.10	Kara yolu yolcu taşımacılığına yönelik otobüs, minibüs ve taksi duraklarının işletilmesi (otobüs terminal hizmetleri hariç)
1291	Durak, otopark işletmeciliği	52.21.90	Kara taşımacılığını destekleyici diğer hizmetler (kamyon terminal işletmeciliği dahil)
1292	Durak, otopark işletmeciliği	96.99.05	Kendi hesabına çalışan valelerin hizmetleri
1293	Faytonculuk	49.39.00	Başka yerde sınıflandırılmamış kara taşımacılığı ile yapılan diğer yolcu taşımacılığı
1294	İş makinesi işletmeciliği	01.61.02	Bitkisel üretimi destekleyici mahsulün hasat ve harmanlanması, biçilmesi, balyalanması, biçerdöver işletilmesi vb. faaliyetler
1295	İş makinesi işletmeciliği	37.00.01	Kanalizasyon (kanalizasyon atıklarının uzaklaştırılması ve arıtılması, kanalizasyon sistemlerinin ve atık su arıtma tesislerinin işletimi, foseptik çukurların ve havuzların boşaltılması ve temizlenmesi, seyyar tuvalet faaliyetleri vb.)
1296	İş makinesi işletmeciliği	43.99.04	Vinç ve benzeri diğer inşaat ekipmanlarının operatörü ile birlikte kiralanması (özel bir inşaat çeşidinde yer almayan)
1297	İş makinesi işletmeciliği	77.32.01	Bina ve bina dışı inşaatlarda kullanılan makine ve ekipmanların operatörsüz olarak kiralanması ve operasyonel leasingi (kurma/sökme hariç)
1298	Kara yolu ile yük taşımacılığı	49.41.01	Kara yolu ile şehir içi yük taşımacılığı (gıda, sıvı, kuru yük vb.) (gaz ve petrol ürünleri hariç)
1299	Kara yolu ile yük taşımacılığı	49.41.02	Kara yolu ile şehirler arası yük taşımacılığı (gıda, sıvı, kuru yük, vb.) (gaz ve petrol ürünleri hariç)
1300	Kara yolu ile yük taşımacılığı	49.41.03	Kara yolu ile uluslararası yük taşımacılığı (gıda, sıvı, kuru yük, vb.) (gaz ve petrol ürünleri hariç)
1301	Kara yolu ile yük taşımacılığı	49.41.05	Kara yolu ile canlı hayvan taşımacılığı (çiftlik hayvanları, kümes hayvanları, vahşi hayvanlar vb.)
1302	Kara yolu ile yük taşımacılığı	49.41.06	Sürücüsü ile birlikte kamyon, beton mikseri ve diğer motorlu yük taşıma araçlarının kiralanması
1303	Kara yolu ile yük taşımacılığı	49.41.08	Kara yolu ile şehir içi yük taşımacılığı (gaz ve petrol ürünleri, kimyasal ürünler vb.)
1304	Kara yolu ile yük taşımacılığı	49.41.09	Kara yolu ile şehirler arası yük taşımacılığı (gaz ve petrol ürünleri, kimyasal ürünler vb.)
1305	Kara yolu ile yük taşımacılığı	49.41.10	Kara yolu ile uluslararası yük taşımacılığı (gaz ve petrol ürünleri, kimyasal ürünler vb.)
1306	Kara yolu ile yük taşımacılığı	49.41.90	Kara yolu ile diğer yük taşımacılığı
1307	Kara yolu ile yük taşımacılığı	49.42.01	Ev ve iş yerlerine verilen taşımacılık hizmetleri
1308	Minibüsçülük	49.31.06	Minibüs ve dolmuş ile yapılan şehir içi ve banliyö yolcu taşımacılığı (belirlenmiş güzergahlarda)
1309	Minibüsçülük	49.31.90	Kara yoluyla tarifeli diğer yolcu taşımacılığı
1310	Nakliyat komisyonculuğu	52.26.03	Kara yolu yük nakliyat acentelerinin faaliyetleri
1311	Nakliyat komisyonculuğu	52.31.02	Kara yolu yük nakliyat komisyoncularının faaliyetleri
1312	Oto galericilik, oto kiralama	47.81.14	Otomobillerin ve hafif motorlu kara taşıtlarının perakende ticareti (elektrikli olanlar ile ambulans ve minibüs benzeri motorlu yolcu taşıtları dahil)
1313	Oto galericilik, oto kiralama	47.81.90	Diğer motorlu kara taşıtlarının perakende ticareti (kamyonlar, çekiciler, römorklar, yarı römorklar, kamp araçları vb., elektrikli olanlar dahil)
1314	Oto galericilik, oto kiralama	49.32.04	Kara yoluyla tarifesiz yolcu taşımacılığı
1315	Oto galericilik, oto kiralama	49.33.02	Sürücüsü ile birlikte diğer özel araç kiralama faaliyeti
1316	Oto galericilik, oto kiralama	77.11.01	Motorlu hafif kara taşıtlarının ve arabaların sürücüsüz olarak kiralanması ve operasyonel leasingi (motosiklet ve motokaravan için olanlar hariç)
1317	Oto galericilik, oto kiralama	77.12.01	Motorlu ağır kara taşıtlarının sürücüsüz olarak kiralanması ve operasyonel leasingi (ağırlığı 3.5 tondan daha fazla olanlar) (motokaravan için olanlar hariç)
1318	Oto kurtarıcılık	52.21.04	Kara yolu taşımacılığı ile ilgili özel ve ticari araçlar için çekme ve yol yardımı faaliyetleri
1319	Otobüsçülük	49.31.04	Halk otobüsü/otobüs ile yapılan şehir içi ve banliyö yolcu taşımacılığı
1320	Otobüsçülük	49.31.07	Kara yolu (otobüs, vb.) ile uluslararası yolcu taşımacılığı
1321	Otobüsçülük	49.31.08	Şehirler arası tarifeli kara yolu yolcu taşımacılığı
1322	Özel ambulans işletmeciliği	86.92.00	Ambulansla hasta taşıma
1323	Servis aracı işletmeciliği	49.31.09	Şehir içi, banliyö ve kırsal alanlarda kara yolu ile personel, öğrenci, vb. grup taşımacılığı (şehir içi personel ve okul servisleri, vb.)
1324	Servis aracı işletmeciliği	49.31.10	Kara yolu şehir içi ve şehirler arası havaalanı servisleri ile yolcu taşımacılığı
1325	Su yolu taşımacılığı	50.10.12	Deniz ve kıyı sularında yolcu gemilerinin ve teknelerinin mürettebatıyla birlikte kiralanması (gezinti tekneleri dahil)
1326	Su yolu taşımacılığı	50.10.13	Kıyı sularında yolcuların feribotlarla, kruvaziyer gemilerle ve teknelerle taşınması (deniz otobüsleri işletmeciliği dahil; uluslararası denizler ile göl ve nehirlerde yapılanlar hariç)
1327	Su yolu taşımacılığı	50.10.14	Deniz ve kıyı sularında yat işletmeciliği
1328	Su yolu taşımacılığı	50.10.15	Deniz ve kıyı sularında gezi veya tur bot ve teknelerinin işletilmesi (yat işletmeciliği hariç)
1329	Su yolu taşımacılığı	50.10.90	Deniz ve kıyı sularında diğer yolcu taşımacılığı (deniz taksi vb. dahil)
1330	Su yolu taşımacılığı	50.30.08	İç sularda yolcu taşımacılığı (nehir, kanal ve göllerde yapılanlar, vb.) (gezinti amaçlı olanlar dahil)
1331	Su yolu taşımacılığı	50.30.09	İç sularda yolcu taşıma gemilerinin ve teknelerinin mürettebatıyla birlikte kiralanması
1332	Su yolu taşımacılığı	50.40.05	İç sularda yük taşımacılığı (nehir, kanal ve göllerde yapılanlar, vb.)
1333	Su yolu taşımacılığı	50.40.07	İç sularda yük taşıma gemi ve teknelerinin mürettebatıyla birlikte kiralanması hizmetleri (nehir, kanal ve göllerde, vb.)
1334	Su yolu taşımacılığı	50.40.08	İç sularda çekme ve itme hizmetleri (römorkaj) (mavnaların, şamandıraların vb.nin taşınması) (nehir, kanal, göl vb.)
1335	Su yolu taşımacılığı	52.22.90	Su taşımacılığını destekleyici diğer hizmetler (Su yolu taşımacılığını destekleyici olarak deniz feneri, fener dubası, fener gemisi, şamandıra, kanal işaretleri vb. seyir yardımcıları ile verilen hizmet faaliyetleri dahil)
1336	Su yolu taşımacılığı	77.34.01	Su yolu taşımacılığı ekipmanlarının operatörsüz olarak kiralanması ve operasyonel leasingi (yolcu ve yük taşımacılığı için ticari tekne ve gemiler dahil, gezinti tekneleri hariç)
1337	Taksicilik	49.33.01	Taksi ile yolcu taşımacılığı
1338	Trafik müşavirliği, iş takipçiliği	82.99.04	Trafik müşavirliği
1339	Trafik müşavirliği, iş takipçiliği	82.99.08	İş takipçiliği faaliyeti
1340	Yük taşımacılığını destekleyici faaliyetler	52.10.02	Frigorifik depolama ve antrepoculuk faaliyetleri (bozulabilir gıda ürünleri dahil dondurulmuş veya soğutulmuş mallar için depolama)
1341	Yük taşımacılığını destekleyici faaliyetler	52.10.03	Hububat depolama ve antrepoculuk faaliyetleri (hububat silolarının işletilmesi vb.)
1342	Yük taşımacılığını destekleyici faaliyetler	52.10.05	Dökme sıvı depolama ve antrepoculuk faaliyetleri (yağ, şarap vb. dahil; petrol, petrol ürünleri, kimyasallar, gaz vb. hariç)
1343	Yük taşımacılığını destekleyici faaliyetler	52.10.90	Diğer depolama ve antrepoculuk faaliyetleri (frigorifik depolar ile hububat, kimyasallar, dökme sıvı ve gaz depolama faaliyetleri hariç)
1344	Yük taşımacılığını destekleyici faaliyetler	52.21.06	Kara taşımacılığına yönelik emanet büroları işletmeciliği (demir yollarında yapılanlar dahil)
1345	Yük taşımacılığını destekleyici faaliyetler	52.24.08	Su yolu taşımacılığıyla ilgili kargo ve bagaj yükleme boşaltma (elleçleme) hizmetleri
1346	Yük taşımacılığını destekleyici faaliyetler	52.24.10	Kara yolu taşımacılığıyla ilgili kargo yükleme boşaltma (elleçleme) hizmetleri
1347	Yük taşımacılığını destekleyici faaliyetler	52.24.11	Demir yolu taşımacılığıyla ilgili kargo yükleme boşaltma (elleçleme) hizmetleri
1348	Yük taşımacılığını destekleyici faaliyetler	52.25.99	Başke yerde sınıflandırılmamış taşımacılığı destekleyici diğer faaliyetler (grup sevkiyatının organizasyonu, malların taşınması sırasında korunması için geçici olarak kasalara vb. yerleştirilmesi, yüklerin birleştirilmesi, gruplanması ve parçalara ayırılması, vb. dahil)
1349	Yük taşımacılığını destekleyici faaliyetler	52.26.99	Başka yerde sınıflandırılmamış taşımacılığa yönelik diğer destekleyici faaliyetler
1350	Yük taşımacılığını destekleyici faaliyetler	53.20.08	Gıda dağıtım faaliyetleri
1351	Yük taşımacılığını destekleyici faaliyetler	53.20.09	Kurye faaliyetleri (kara, deniz ve hava yolu ile yapılanlar dahil; evrensel hizmet yükümlülüğü altında postacılık ile gıda dağıtım faaliyetleri hariç)
1352	Yük taşımacılığını destekleyici faaliyetler	53.20.10	Paket ve koli gibi kargoların toplanması, sınıflandırılması, taşınması ve dağıtımı faaliyetleri (dökme yükler ve evrensel hizmet yükümlülüğü altında postacılık faaliyetleri hariç)
1353	Yük taşımacılığını destekleyici faaliyetler	69.10.10	Yediemin faaliyetleri
1354	Yük taşımacılığını destekleyici faaliyetler	73.11.03	Reklam araç ve eşantiyonların dağıtımı ve teslimi faaliyetleri
1355	Yük taşımacılığını destekleyici faaliyetler	82.92.01	Tehlikesiz ürünleri paketleme faaliyetleri
1356	Yük taşımacılığını destekleyici faaliyetler	82.92.05	Tehlikeli ürünleri paketleme faaliyetleri
1357	Yük taşımacılığını destekleyici faaliyetler	96.99.02	Hamallık hizmetleri
1358	Boya, kimyasal ürünlerin imalatı	20.11.01	Sanayi gazları imalatı
1359	Boya, kimyasal ürünlerin imalatı	20.12.01	Boya maddeleri ve pigment imalatı (birincil formda veya konsantre olarak herhangi bir kaynaktan) (hazır boyalar hariç)
1360	Boya, kimyasal ürünlerin imalatı	20.12.02	Tabaklama ekstreleri, bitkisel kökenli; tanenler ve tuzları, eterleri, esterleri ve diğer türevleri; bitkisel veya hayvansal kökenli renklendirme maddelerinin imalatı
1361	Boya, kimyasal ürünlerin imalatı	20.13.02	Metalik halojenler, hipokloritler, kloratlar ve perkloratların imalatı (çamaşır suyu dahil)
1362	Boya, kimyasal ürünlerin imalatı	20.13.03	Sülfidler (sülfürler), sülfatlar, fosfinatlar, fosfonatlar, fosfatlar ve nitratların imalatı (şap dahil)
1363	Boya, kimyasal ürünlerin imalatı	20.13.90	Diğer metal tuzları ve temel inorganik kimyasalların imalatı
1364	Boya, kimyasal ürünlerin imalatı	20.13.99	Başka yerde sınıflandırılmamış kimyasal elementler, inorganik asitler ve bileşiklerin imalatı
1365	Boya, kimyasal ürünlerin imalatı	20.14.00	Diğer organik temel kimyasalların imalatı
1366	Boya, kimyasal ürünlerin imalatı	20.16.01	Birincil formda poliamitler, üre reçineleri, melamin reçineleri, vb. plastik hammaddelerin imalatı
1367	Boya, kimyasal ürünlerin imalatı	20.16.02	Birincil formda alkid reçine, polyester reçine, epoksi reçine, poliasetal, polikarbonat ile diğer polieter ve polyester imalatı
1368	Boya, kimyasal ürünlerin imalatı	20.16.03	Birincil formda polimerlerin imalatı (etilen, propilen, stiren, vinil klorür, vinil asetat, vinil esterleri, akrilik vb. polimerleri ile sertleştirilmiş proteinler, doğal kauçuğun kimyasal türevleri dahil)
1369	Boya, kimyasal ürünlerin imalatı	20.16.04	Birincil formda silikon ve polimer esaslı iyon değiştiricileri imalatı
1370	Boya, kimyasal ürünlerin imalatı	20.16.05	Birincil formda diğer amino reçineler, fenolik reçineler, poliüretanlar, politerpenler, polisülfürler, selüloz ve kimyasal türevleri ile diğer petrol reçineleri imalatı
1371	Boya, kimyasal ürünlerin imalatı	20.30.11	Boya ve vernikler, akrilik ve vinil polimer esaslı olanların (sulu ortamda dağılanlar, çözülenler ve çözeltiler) imalatı
1372	Boya, kimyasal ürünlerin imalatı	20.30.12	Macun imalatı (dolgu, cam, sıvama için olanlar ile üstübeç, vb. dahil)
1373	Boya, kimyasal ürünlerin imalatı	20.30.15	Hazır boya pigmentleri, matlaştırıcılar (opaklaştırıcı) ve renklendiriciler, camlaştırılabilir emay ve sırlar, astarlar, cam firit, sıvı cilalar ve benzerlerin imalatı
1374	Boya, kimyasal ürünlerin imalatı	20.30.16	Boya müstahzarları hazır kurutucu maddelerinin imalatı
1375	Boya, kimyasal ürünlerin imalatı	20.30.17	Elektrostatik toz boya imalatı
1376	Boya, kimyasal ürünlerin imalatı	20.30.90	Diğer boya, vernik ve ilgili ürünlerin imalatı (renk ayarlayıcılar, matbaa mürekkepleri, solventler, incelticiler (tiner))
1377	Boya, kimyasal ürünlerin imalatı	20.59.01	Fotoğrafik levha ve filmlerin (hassaslaştırılmış, ışığa maruz kalmamış olanlar), anında baskılanan filmlerin, fotoğrafçılıkta kullanılan kimyasal müstahzarların ve karışımsız (saf) ürünlerin imalatı
1378	Boya, kimyasal ürünlerin imalatı	20.59.02	Tutkal imalatı
1379	Boya, kimyasal ürünlerin imalatı	20.59.04	Yağlama müstahzarları (hidrolik fren sıvıları dahil), vuruntu önleyici müstahzarlar ile katkı maddeleri ve antifrizlerin imalatı
1380	Boya, kimyasal ürünlerin imalatı	20.59.08	Elektronikte kullanılan macun kıvamında (dope edilmiş) olan kimyasal elementler ile bileşiklerin imalatı
1381	Boya, kimyasal ürünlerin imalatı	20.59.09	Bitirme (apreleme dahil) maddeleri, boya hammaddesi ve benzeri ürünlerin sabitlenmesini veya boyayıcılığını hızlandıran boya taşıyıcı maddelerin imalatı
1382	Boya, kimyasal ürünlerin imalatı	20.59.10	Dekapaj (temizleme) müstahzarları, eritkenler, hazır vulkanizasyon hızlandırıcı maddeler, kauçuk veya plastikler için plastikleştirici bileşikler ve stabilizatörler, diğer katalitik müstahzarların imalatı
1383	Boya, kimyasal ürünlerin imalatı	20.59.12	Kimyasal olarak değiştirilmiş veya yenilemeyen hayvansal veya bitkisel katı ve sıvı yağlar ve yağ karışımlarının imalatı (linoksin, teknik ve sanayi amaçlı bitkisel sabit sıvı yağlar, sanayide kullanılan sıvı yağlar, vb.)
1384	Boya, kimyasal ürünlerin imalatı	20.59.15	Yangın söndürücü müstahzarları ve dolum malzemeleri imalatı
1385	Boya, kimyasal ürünlerin imalatı	20.59.17	Patlayıcı diğer maddelerin imalatı (itici tozların imalatı hariç)
1386	Boya, kimyasal ürünlerin imalatı	20.59.20	Barut vb. itici tozların imalatı
1387	Boya, kimyasal ürünlerin imalatı	20.59.99	Başka yerde sınıflandırılmamış diğer kimyasal ürünlerin imalatı (vakum tüpleri için emiciler, pirolinyitler, kazan taşı önleyici bileşikler, yağ emülsiyonlaştırıcıları, dökümhanelerde kullanılan yardımcı kimyasal ürünler ve hazır bağlayıcılar, vb.)
1388	Boya, kimyasal ürünlerin imalatı	32.99.17	Sigara çakmakları ve diğer çakmaklar ile çabuk tutuşan (piroforik) alaşımların imalatı (çakmaklar için kap hacmi ≤ 300cm3 sıvı veya sıvılaştırılmış gaz yakıtları dahil)
1389	Boya, kimyasal ürünlerin ticareti	46.83.04	Boya, vernik ve lak toptan ticareti
1390	Boya, kimyasal ürünlerin ticareti	46.85.01	Endüstriyel kimyasalların toptan ticareti (anilin, matbaa mürekkebi, kimyasal yapıştırıcı, havai fişek, boyama maddeleri, sentetik reçine, metil alkol, parafin, esans ve tatlandırıcı, soda, sanayi tuzu, parafin, nitrik asit, amonyak, sanayi gazları vb.)
1391	Boya, kimyasal ürünlerin ticareti	47.52.03	Boya, vernik, lak, solvent vb. ürünlerin perakende ticareti
1392	Camcılık	23.11.01	Düz cam imalatı (telli, buzlu cam, renkli veya boyalı düz cam dahil) (dökülmüş, haddelenmiş, çekilmiş, üflenmiş, float, yüzeyi parlatılmış veya cilalanmış ancak başka şekilde işlenmemiş olanlar)
1393	Camcılık	23.12.01	Cam ayna imalatı
1394	Camcılık	23.12.03	Çok katlı yalıtım camları imalatı
1395	Camcılık	23.12.04	Levha veya tabaka halinde işlenmiş cam imalatı (kavislendirilmiş, kenarları işlenmiş, gravür yapılmış, delinmiş, emaylanmış/sırlanmış veya başka bir şekilde işlenmiş, fakat çerçevelenmemiş veya monte edilmemiş olanlar) (optik camlar dahil)
1396	Camcılık	23.14.01	Cam elyafı imalatı (cam yünü ve bunlardan yapılmış dokuma dışı ürünler dahil)
1397	Camcılık	23.15.01	Laboratuvar, hijyen veya eczacılık ile ilgili cam eşyalar ile cam ampullerin (serum ampulleri) imalatı (ambalajlama ve taşımada kullanılanlar hariç)
1398	Camcılık	23.15.02	Lamba ve aydınlatma teçhizatının, ışıklı işaretlerin, isim tabelalarının vb.nin cam parçalarının imalatı (cam tabelaların imalatı dahil)
1399	Camcılık	23.15.05	Vitray cam imalatı
1400	Camcılık	23.15.06	Camdan elektrik izolasyon malzemesi imalatı
1401	Camcılık	23.15.07	Cam zarflar (açık) ve bunların cam parçalarının imalatı (elektrik ampulleri, elektrik lambaları, katot ışınlı tüpler vb. için kullanılan)
1402	Camcılık	23.15.99	Başka yerde sınıflandırılmamış diğer cam ürünlerin imalatı ve işlenmesi (düz camdan yapılmış akvaryumların imalatı dahil)
1403	Camcılık	43.34.02	Cam takma işleri
1404	Camcılık	46.83.03	Düz cam toptan ticareti
1405	Camcılık	47.52.04	Düz cam perakende ticareti
1406	Çevre düzenleme, peyzaj faaliyetleri	81.30.06	Çevre düzenlemesi ve bakımı faaliyetleri
1407	Emlakçılık	68.31.01	Gayrimenkul faaliyetleri için aracılık hizmeti faaliyetleri
1408	Emlakçılık	68.32.01	Gayrimenkul değerleme (eskpertiz) , danışmanlık ve emanet aracılarının (escrow) faaliyetleri
1409	Emlakçılık	68.32.02	Bir ücret veya sözleşmeye dayalı olarak yapılan diğer gayrimenkul yönetimi faaliyetleri (apartman yöneticiliği hariç)
1410	Emlakçılık	68.32.03	Bir ücret veya sözleşmeye dayalı olarak yapılan kira toplama faaliyetleri
1411	Emlakçılık	68.32.04	Bir ücret veya sözleşmeye dayalı olarak yapılan apartman yöneticiliği
1412	Emlakçılık	81.10.01	Tesis bünyesindeki kombine destek hizmetleri
1413	Hırdavatçılık	46.15.02	Hırdavatçı (nalburiye) eşyalarının, madeni eşyaların ve el aletlerinin toptan satışı ile ilgili aracıların faaliyetleri
1414	Hırdavatçılık	46.84.01	Hırdavat (nalburiye) malzemesi ve el aletleri toptan ticareti (çivi, raptiye, vida, adi metalden kilit, menteşe, bağlantı parçası, çekiç, testere, pense, tornavida, takım tezgahı uçları, çengel, halka, perçin, vb.)
1415	Hırdavatçılık	46.84.02	Sıhhi tesisat ve ısıtma tesisatı malzemesi toptan ticareti (lavabo musluğu, vana, valf, tıkaç, t-parçaları, bağlantılar, vb.) (kombiler ve radyatörler hariç)
1416	Hırdavatçılık	46.84.05	Tarım ve ormancılık alet ve malzemeleri toptan ticareti (balta, kazma, orak, tırpan, vb. dahil, tarımsal amaçlı makine ve ekipmanlar hariç)
1417	Hırdavatçılık	47.52.02	Hırdavat (nalburiye) ve el aletleri perakende ticareti
1418	Hırdavatçılık	47.52.06	Sıhhi tesisat ve ısıtma tesisatı malzemesi perakende ticareti (kombiler ve radyatörler hariç)
1419	İnşaat malzemeleri imalatı	17.24.02	Duvar kağıdı ve benzeri duvar kaplamalarının imalatı (tekstilden olanlar hariç)
1420	İnşaat malzemeleri imalatı	20.59.18	Mikronize edilmiş ve stearik asitle kaplanmış kalsit imalatı
1421	İnşaat malzemeleri imalatı	22.24.01	Plastikten banyo küvetleri, lavabolar, klozet kapakları, oturakları ve rezervuarları ile benzeri sıhhi ürünlerin imalatı (kalıcı tesisat için kullanılan montaj ve bağlantı parçaları dahil)
1422	İnşaat malzemeleri imalatı	22.24.04	Vinil, linolyum (muşamba) gibi esnek yer kaplamaları ile plastik zemin, duvar ve tavan kaplamalarının imalatı (duvar kağıdı hariç)
1423	İnşaat malzemeleri imalatı	22.24.99	Başka yerde sınıflandırılmamış plastik inşaat malzemelerinin imalatı (plastik suni taş-mermerit imalatı hariç)
1424	İnşaat malzemeleri imalatı	23.15.03	Sıkıştırılmış veya kalıplanmış camdan döşeme blokları, tuğlalar, karolar ve diğer ürünler, kurşunlu lambalar ve benzerleri, blok, plaka veya benzer şekillerdeki gözenekli, köpüklü camların imalatı (vitray cam hariç)
1425	İnşaat malzemeleri imalatı	23.20.16	Silisli süzme topraktan (kizelgur) ısı yalıtımlı seramik ürünler ile ateşe dayanıklı briket, blok, tuğla, ateş tuğlası, vb. ateşe dayanıklı seramik yapı ürünleri imalatı
1426	İnşaat malzemeleri imalatı	23.20.17	Ateşe dayanıklı imbikler, damıtma kabı, eritme potası, vana ucu, tüp, boru, döküm potaları, mufl ocağı, püskürtme tüpleri vb. seramik ürünlerin imalatı
1427	İnşaat malzemeleri imalatı	23.20.19	Ateşe dayanıklı çimento imalatı
1428	İnşaat malzemeleri imalatı	23.20.20	Ateşe dayanıklı çamur, harç, beton vb. imalatı
1429	İnşaat malzemeleri imalatı	23.31.01	Seramik karo ve kaldırım taşları imalatı (mozaik taşı ve mozaik küpleri dahil) (ateşe dayanıklı olanlar hariç)
1430	İnşaat malzemeleri imalatı	23.32.02	Fırınlanmış, ateşe dayanıklı olmayan kil ve topraktan baca künkleri ve başlıkları, şömine ve baca boruları, oluklar ve bağlantı parçaları ile karo vb. inşaat malzemeleri imalatı (seramikten oluklar, borular ve bağlantı parçaları dahil) (tuğla ve kiremit hariç)
1431	İnşaat malzemeleri imalatı	23.32.03	Fırınlanmış, ateşe dayanıklı olmayan kil ve topraktan tuğla ve kiremit imalatı
1432	İnşaat malzemeleri imalatı	23.42.01	Seramik sıhhi ürünlerin imalatı
1433	İnşaat malzemeleri imalatı	23.44.01	Diğer teknik seramik ürünlerin imalatı (laboratuvar, kimyasal ve diğer teknik alanlarda kullanılan seramikten ürünler) (ateşe dayanıklı seramik ürünler hariç)
1434	İnşaat malzemeleri imalatı	23.52.01	Sönmemiş kireç, sönmüş kireç ve suya dayanıklı kireç imalatı
1435	İnşaat malzemeleri imalatı	23.52.02	Sönmüş alçıtaşından ya da sönmüş sülfattan alçı imalatı
1436	İnşaat malzemeleri imalatı	23.61.01	Çimentodan, betondan veya suni taştan prefabrik yapı elemanları imalatı (gazbetondan ve kireç taşından olanlar dahil)
1437	İnşaat malzemeleri imalatı	23.61.02	Çimentodan, betondan veya suni taştan karo, döşeme taşı, kiremit, tuğla, boru, vb. inşaat amaçlı ürünlerin imalatı
1438	İnşaat malzemeleri imalatı	23.62.01	İnşaat amaçlı alçı ürünlerin imalatı
1439	İnşaat malzemeleri imalatı	23.63.01	Hazır beton imalatı
1440	İnşaat malzemeleri imalatı	23.64.01	Toz harç imalatı
1441	İnşaat malzemeleri imalatı	23.65.02	Lif ve çimento karışımlı ürünlerin imalatı
1442	İnşaat malzemeleri imalatı	23.66.00	Beton, çimento ve alçıdan diğer eşyaların imalatı
1443	İnşaat malzemeleri imalatı	23.91.01	Aşındırıcı ürünlerin imalatı (değirmen taşları, bileği taşı, zımpara taşı vb.)(dokuma tekstil kumaşlarına, kağıt ve mukavvaya tutturulmuş zımparalar hariç)
1444	İnşaat malzemeleri imalatı	23.91.02	Dokuma tekstil kumaşlarına, kağıt ve mukavvaya tutturulmuş olan zımparaların imalatı
1445	İnşaat malzemeleri imalatı	23.99.01	Asfalttan ve benzeri malzemelerden yapılan ürünlerin imalatı (çatı yapımında veya su yalıtımında kullanılan bitüm esaslı keçeler dahil)
1446	İnşaat malzemeleri imalatı	23.99.02	Mineral ses/ısı izolasyon malzemelerinin imalatı (cüruf yünleri, taş yünü, madeni yünler, pul pul ayrılmış vermikulit, genleştirilmiş kil, soğuk tandiş plakası, vb. ısı ve ses yalıtım malzemeleri)
1447	İnşaat malzemeleri imalatı	23.99.05	Bitümlü karışımların imalatı (doğal veya suni taştan malzemeler ile bir bağlayıcı olarak bitüm, doğal asfalt veya ilgili maddelerin karıştırılmasıyla elde edilenler)
1448	İnşaat malzemeleri imalatı	23.99.07	Amyantlı kağıt imalatı
1449	İnşaat malzemeleri imalatı	23.99.99	Başka yerde sınıflandırılmamış metal dışı minerallerden ürünlerin imalatı
1450	İnşaat malzemeleri imalatı	25.99.02	Metalden yapılmış eviye, lavabo, küvet, duş teknesi, jakuzi (emaye olsun ya da olmasın) ve diğer sıhhi ürünlerin imalatı
1451	İnşaat malzemeleri imalatı	32.91.02	Boyama, badana, duvar kağıdı ve vernik fırçaları ile rulolarının imalatı
1452	İnşaat malzemeleri ticareti	46.13.01	İnşaat malzemesi toptan satışı ile ilgili aracıların faaliyetleri (inşaat demiri ve kerestesi hariç)
1453	İnşaat malzemeleri ticareti	46.83.01	Çimento, alçı, harç, kireç, mozaik vb. inşaat malzemeleri toptan ticareti
1454	İnşaat malzemeleri ticareti	46.83.05	Banyo küvetleri, lavabolar, eviyeler, klozet kapakları, tuvalet taşı ve rezervuarları ile seramikten karo ve fayans vb. sıhhi ürünlerin toptan ticareti
1455	İnşaat malzemeleri ticareti	46.83.08	Taş, kum, çakıl, mıcır, kil, kaolin vb. inşaat malzemeleri toptan ticareti
1456	İnşaat malzemeleri ticareti	46.83.10	Tuğla, kiremit, briket, kaldırım taşı vb. inşaat malzemeleri toptan ticareti
1457	İnşaat malzemeleri ticareti	46.83.15	İnşaatlarda izolasyon amaçlı kullanılan malzemelerin toptan ticareti
1458	İnşaat malzemeleri ticareti	46.83.17	Alçı ve alçı esaslı bileşenlerden inşaat amaçlı ürünlerin toptan ticareti
1459	İnşaat malzemeleri ticareti	46.83.18	Duvar kağıdı, tekstil duvar kaplamaları, plastikten zemin, duvar veya tavan kaplamalarının toptan ticareti
1460	İnşaat malzemeleri ticareti	46.83.19	Plastikten inşaat amaçlı tabakalar, levhalar, filmler, folyolar, şeritler ve borular ile asfalt vb. malzemeden çatı kaplama ürünlerinin toptan ticareti
1461	İnşaat malzemeleri ticareti	46.83.99	Başka yerde sınıflandırılmamış diğer inşaat malzemesi toptan ticareti
1462	İnşaat malzemeleri ticareti	47.52.01	Çimento, alçı, harç, kireç, tuğla, kiremit, briket, taş, kum, çakıl vb. inşaat malzemeleri perakende ticareti
1463	İnşaat malzemeleri ticareti	47.52.11	Banyo küveti, lavabo, klozet kapağı, tuvalet taşı ve rezervuarı ile seramikten karo ve fayans vb. sıhhi ürünlerin perakende ticareti
1464	İnşaat malzemeleri ticareti	47.52.16	Çim biçme ve bahçe ekipmanları perakende ticareti (kar küreyiciler dahil) (tarımda kullanılan el aletleri hariç)
1465	İnşaat malzemeleri ticareti	47.52.20	Alçı ve alçı esaslı bileşenlerden inşaat amaçlı ürünlerin perakende ticareti (kartonpiyer, panel, levha vb.)
1466	İnşaat malzemeleri ticareti	47.52.21	Plastikten inşaat amaçlı levhalar, folyolar, şeritler ve borular ile asfalt vb. malzemeden çatı kaplama ürünlerinin perakende ticareti (inşaat için naylon örtü, shıngle, mantolama amaçlı strafor vb. dahil)
1467	İnşaat malzemeleri ticareti	47.52.99	Başka yerde sınıflandırılmamış inşaat malzemesi perakende ticareti
1468	İnşaat malzemeleri ticareti	47.53.03	Duvar kağıdı, tekstil duvar kaplamaları, kauçuk yer döşemeleri ve paspaslar ile plastik zemin, duvar veya tavan kaplamaları perakende ticareti (linolyum gibi elastiki zemin kaplamaları, marley, vb. dahil)
1469	İnşaatçılık	08.11.04	Süsleme ve yapı taşlarının kırılması ve kabaca kesilmesi
1470	İnşaatçılık	23.70.01	Taş ve mermerin kesilmesi, şekil verilmesi ve bitirilmesi (doğal taşlardan, mermerden, su mermerinden, travertenden, kayağantaşından levha/tabaka, kurna, lavabo, karo, kaldırım taşı, yapı taşı, mezar taşı, vb. imalatı dahil, süs eşyası hariç)
1471	İnşaatçılık	38.11.02	İnşaat ve yıkım atıklarının, çalı, çırpı, moloz gibi enkazların toplanması ve kaldırılması
1472	İnşaatçılık	41.00.01	İkamet amaçlı binaların inşaatı (ahşap binaların inşaatı hariç)
1473	İnşaatçılık	41.00.02	İkamet amaçlı olmayan binaların inşaatı
1474	İnşaatçılık	41.00.03	Mevcut ikamet amaçlı olan veya ikamet amaçlı olmayan binaların yeniden düzenlenmesi veya yenilenmesi (büyük çaplı revizyon) (tarihi yapıların restorasyonu hariç)
1475	İnşaatçılık	41.00.04	İkamet amaçlı ahşap binaların inşaatı
1476	İnşaatçılık	42.11.02	Yol yüzeylerinin asfaltlanması ve onarımı, kaldırım, kasis, bisiklet yolu vb.lerin inşaatı
1477	İnşaatçılık	43.11.01	Yıkım işleri (binaların ve diğer yapıların yıkılması ve sökülmesi)
1478	İnşaatçılık	43.12.01	Zemin ve arazi hazırlama, alanın temizlenmesi ile kazı ve hafriyat işleri (madencilik için yapılanlar hariç)
1479	İnşaatçılık	43.23.01	Yalıtım tesisatı (su yalıtımı ile çatıların dış yalıtımı hariç)
1480	İnşaatçılık	43.23.02	Su yalıtımı (çatıların su yalıtımı hariç)
1481	İnşaatçılık	43.24.02	Isı, ses veya titreşim yalıtımı ile diğer inşaat tesisatı işleri (mantolama ve vakumlu temizleme sistemlerinin kurulumu dahil)
1482	İnşaatçılık	43.24.99	Başka yerde sınıflandırılmamış diğer tesisat işleri
1483	İnşaatçılık	43.31.01	Sıva işleri
1484	İnşaatçılık	43.32.03	Seyyar bölme ve metal yapı üzerine asma tavan montaj işleri ile diğer doğrama tesisatı işleri
1485	İnşaatçılık	43.33.01	Bina ve diğer yapıların içi veya dışında yer ve duvar kaplama faaliyetleri (halı, taban muşambası ve kağıt kaplama hariç)
1486	İnşaatçılık	43.33.99	Başka yerde sınıflandırılmamış diğer yer döşeme ve kaplama ile duvar kaplama işleri (halı, taban muşambası ve diğer esnek yer kaplamaları ile duvar kaplama işleri)
1487	İnşaatçılık	43.34.01	Binaların iç ve dış boyama işleri
1488	İnşaatçılık	43.34.03	Bina dışı yapıların boyama işleri
1489	İnşaatçılık	43.35.00	İnşaatlardaki diğer bütünleyici ve tamamlayıcı işler
1490	İnşaatçılık	43.42.02	Bina inşaatı için kazık çakma ve temel inşaatı işleri (forekazık çakma dahil)
1491	İnşaatçılık	43.42.03	Baca ve sanayi fırınlarının inşaatı ve kurulması (fırınlar için yanma odasına ateş tuğlası döşenmesi işleri dahil)
1492	İnşaatçılık	43.50.02	Bina dışı yapılar için kazık çakma ve temel inşaatı işleri (forekazık çakma dahil)
1493	İnşaatçılık	43.50.05	Yol yüzeylerin boyayla işaretlenmesi, yol bariyeri, trafik işaret ve levhaları vb.nin kurulumu gibi yol, tünel vb. yerlerdeki yüzey işleri
1494	İnşaatçılık	43.91.00	Duvarcılık ve tuğla, briket vb. döşeme faaliyetleri
1495	İnşaatçılık	43.99.05	İnşaatlarda beton işleri (kalıp içerisine beton dökülmesi vb.)
1496	İnşaatçılık	43.99.07	İnşaat iskelesi ve çalışma platformunu kurma ve sökme işleri
1497	İnşaatçılık	43.99.13	İnşaat demirciliği (inşaat demirinin bükülmesi ve bağlanması)
1498	İnşaatçılık	43.99.99	Başka yerde sınıflandırılmamış diğer uzmanlaşmış inşaat işleri
1499	İnşaatçılık	46.83.07	Mermer, granit, kayağan taşı, kum taşı vb. toptan ticareti (işlenmemiş veya blok halde olanlar)
1500	İnşaatçılık	46.83.09	İşlenmiş mermer, traverten, kaymaktaşı (su mermeri) ve bunlardan yapılmış ürünlerin toptan ticareti (levha halinde olanlar ile lavabo vb. sıhhi ürünler dahil)
1501	İnşaatçılık	47.52.19	İşlenmiş mermer, traverten, kaymaktaşı (su mermeri) ve bunlardan yapılmış ürünlerin perakende ticareti (levha halinde olanlar ile mermer lavabo vb. sıhhi ürünler dahil)
1502	Mermer, taş, kum ocakçılığı	08.11.01	Mermer ocakçılığı (traverten dahil)
1503	Mermer, taş, kum ocakçılığı	08.11.02	Granit ocakçılığı
1504	Mermer, taş, kum ocakçılığı	08.11.03	Yapı taşları ocakçılığı
1505	Mermer, taş, kum ocakçılığı	08.11.05	Dolomit ve kayağan taşı (arduvaz / kayraktaşı) ocakçılığı
1506	Mermer, taş, kum ocakçılığı	08.11.06	Kireçtaşı (kalker) ocakçılığı (kireçtaşının kabaca kırılması ve parçalanması dahil)
1507	Mermer, taş, kum ocakçılığı	08.11.07	Tebeşir, alçıtaşı ve anhidrit ocakçılığı (çıkarma, parçalama, pişirme işlemi dahil)
1508	Mermer, taş, kum ocakçılığı	08.12.01	Çakıl ve kum ocakçılığı (taşların kırılması ile kil ve kaolin madenciliği hariç)
1509	Mermer, taş, kum ocakçılığı	08.12.02	Çakıl taşlarının kırılması ve parçalanması
1510	Mermer, taş, kum ocakçılığı	08.91.05	Kehribar, oltu taşı ve lületaşı ocakçılığı
1511	Mermer, taş, kum ocakçılığı	08.93.01	Kaya tuzunun çıkarımı (tuzun elenmesi ve kırılması dahil) (tuzun yemeklik tuza dönüştürülmesi hariç)
1512	Mermer, taş, kum ocakçılığı	08.93.02	Deniz, göl ve kaynak tuzu üretimi (tuzun yemeklik tuza dönüştürülmesi hariç)
1513	Mermer, taş, kum ocakçılığı	08.99.04	Grafit ocakçılığı
1514	Prefabrik yapıların imalatı, kurulumu, ticareti	16.23.02	Ahşap prefabrik yapılar ve ahşap taşınabilir evlerin imalatı
1515	Prefabrik yapıların imalatı, kurulumu, ticareti	22.24.05	Plastikten prefabrik yapıların imalatı
1516	Prefabrik yapıların imalatı, kurulumu, ticareti	23.61.03	Betondan yapılmış prefabrik yapıların imalatı
1517	Prefabrik yapıların imalatı, kurulumu, ticareti	41.00.05	Prefabrik binalar için bileşenlerin alanda birleştirilmesi ve kurulması
1518	Prefabrik yapıların imalatı, kurulumu, ticareti	43.50.04	Prefabrik yüzme havuzlarının kurulumu
1519	Prefabrik yapıların imalatı, kurulumu, ticareti	43.50.06	Prefabrik yapıların montajı ve kurulması (prefabrik binalar ve yüzme havuzları hariç her çeşit prefabrik sokak düzeneklerinin (otobüs durağı, telefon kulübesi, bank vb.) kurulumu vb.)
1520	Prefabrik yapıların imalatı, kurulumu, ticareti	46.83.16	Betondan, çimentodan ve suni taştan prefabrik yapıların, yapı elemanlarının ve diğer ürünlerin toptan ticareti
1521	Prefabrik yapıların imalatı, kurulumu, ticareti	46.83.21	Plastikten prefabrik yapılar ve yapı elemanlarının toptan ticareti
1522	Prefabrik yapıların imalatı, kurulumu, ticareti	46.83.22	Ahşaptan prefabrik yapıların ve yapı elemanlarının toptan ticareti
1523	Prefabrik yapıların imalatı, kurulumu, ticareti	47.52.18	Prefabrik yapılar ve yapı elemanlarının perakende ticareti (metalden, betondan, plastikten, ahşaptan vb.)
1524	PVC ürün imalatı	22.23.08	Plastikten kapı ve pencere imalatı
1525	PVC ürün ticareti	46.83.11	Plastik kapı, pencere ve bunların kasaları ile kapı eşikleri, panjurlar, jaluziler, storlar vb. eşyaların toptan ticareti
1526	PVC ürün ticareti	47.52.09	Plastik kapı, pencere ve bunların kasaları ile kapı eşikleri, panjurlar, jaluziler, storlar ve benzeri eşyaların perakende ticareti (PVC olanlar dahil)
1527	Sıhhi tesisatçılık	43.22.03	Bina ve diğer inşaat projelerinde su ve kanalizasyon tesisatı ve onarımı
1528	Sıhhi tesisatçılık	43.22.05	Gaz tesisatı faaliyetleri (hastanelerdeki oksijen gazı temini için kurulum işleri dahil)
1529	Sondajcılık	42.21.02	Su kuyusu açma ve septik sistem kurulum faaliyetleri (kuyu, artezyen vb.)
1530	Sondajcılık	43.13.01	Test sondajı ve delme (madencilikle bağlantılı olarak gerçekleştirilen test sondajı hariç)
\.


--
-- TOC entry 5214 (class 0 OID 25500)
-- Dependencies: 231
-- Data for Name: path_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.path_ (id, name_) FROM stdin;
\.


--
-- TOC entry 5243 (class 0 OID 33832)
-- Dependencies: 260
-- Data for Name: personnel_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.personnel_ (id, name_, surname_, tckno_, address_, cell_, birthday_, driving_license, status_, education_id, department_id, children_, email_, blood_id, military_, gender_, marital_, related_personnel_id, firm_id, commencement_, termination_, delete_, picture_) FROM stdin;
3	Ali	Veli	111	Site	\N	2017-08-16 21:00:00	A	\N	6	1	1	\N	\N	t	t	f	\N	3	2025-07-10 00:00:00	\N	\N	picture_personnel/Screenshot_2025-06-18_103404.png
4	Muhittin	ARI	5748896542	741. cadde	5516487799	2002-08-09 21:00:00	B	\N	6	3	\N	\N	6	t	t	f	\N	4	\N	\N	\N	
5	Ali	BOZDEMİR	62089291120	FEVZİ ÇAKMAK MAH. KENİTRA CAD. 26/N KARATAY / KONYA	+905323957913	1982-07-10 21:00:00	\N	\N	7	\N	\N	bilgi@ekonaz.com.tr	4	t	t	t	\N	5	2004-06-18 00:00:00	\N	\N	
\.


--
-- TOC entry 5216 (class 0 OID 25504)
-- Dependencies: 233
-- Data for Name: tax_office; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tax_office (id, name_, city_id, district_id) FROM stdin;
1	ADANA İHTİSAS	1	1001
2	5 OCAK	1	1001
3	YÜREĞİR	1	1001
4	SEYHAN	1	1001
5	ZİYAPAŞA	1	1001
6	ÇUKUROVA	1	1001
7	CEYHAN	1	182
8	KOZAN	1	574
9	KARATAŞ	1	515
10	FEKE	1	347
11	KARAİSALI	1	505
12	POZANTI	1	757
13	SAİMBEYLİ	1	765
14	TUFANBEYLİ	1	894
15	YUMURTALIK	1	962
16	ALADAĞ	1	40
17	İMAMOĞLU	1	462
18	ADIYAMAN	2	627
19	KAHTA	2	490
20	BESNİ	2	137
21	ÇELİKHAN	2	223
22	GERGER	2	366
23	GÖLBAŞI	2	374
24	SAMSAT	2	769
25	SİNCİK	2	816
26	TUT	2	898
27	TINAZTEPE	3	628
28	KOCATEPE	3	628
29	DİNAR	3	280
30	BOLVADİN	3	157
31	EMİRDAĞ	3	316
32	SANDIKLI	3	771
33	ÇAY	3	212
34	DAZKIRI	3	256
35	İHSANİYE	3	457
36	SİNANPAŞA	3	814
37	SULTANDAĞI	3	829
38	ŞUHUT	3	865
39	BAŞMAKÇI	3	123
40	BAYAT	3	126
41	İSCEHİSAR	3	472
42	ÇOBANLAR	3	242
43	EVCİLER	3	339
44	HOCALAR	3	446
45	KIZILÖREN	3	555
46	AĞRI	4	629
47	DOĞUBEYAZIT	4	290
48	PATNOS	4	737
49	DİYADİN	4	282
50	ELEŞKİRT	4	312
51	HAMUR	4	421
52	TAŞLIÇAY	4	871
53	TUTAK	4	899
54	AMASYA	5	630
55	MERZİFON	5	679
56	GÜMÜŞHACIKÖY	5	398
57	TAŞOVA	5	872
58	SULUOVA	5	832
59	GÖYNÜCEK	5	389
60	HAMAMÖZÜ	5	420
61	ANADOLU İHTİSAS	6	1006
62	ANKARA İHTİSAS	6	1006
63	KAVAKLIDERE	6	1006
64	HİTİT	6	1006
65	OSTİM	6	1006
66	VERASET VE HARÇLAR	6	1006
67	MALTEPE	6	1006
68	YENİMAHALLE	6	1006
69	ÇANKAYA	6	1006
70	KIZILBEY	6	1006
71	MİTHATPAŞA	6	1006
72	ULUS	6	1006
73	YILDIRIM BEYAZIT	6	1006
74	SEĞMENLER	6	1006
75	DİKİMEVİ	6	1006
76	DOĞANBEY	6	1006
77	YEĞENBEY	6	1006
78	YAHYA GALİP	6	1006
79	MUHAMMET KARAGÜZEL	6	1006
80	GÖLBAŞI	6	1006
81	SİNCAN	6	1006
82	DIŞKAPI	6	1006
83	ETİMESGUT	6	1006
84	BAŞKENT	6	1006
85	CUMHURİYET	6	1006
86	KEÇİÖREN	6	1006
87	KAHRAMANKAZAN	6	1006
88	POLATLI	6	755
89	ŞEREFLİKOÇHİSAR	6	860
90	BEYPAZARI	6	147
91	ÇUBUK	6	1006
92	HAYMANA	6	435
93	ELMADAĞ	6	1006
94	AYAŞ	6	1006
95	BALÂ	6	1006
96	ÇAMLIDERE	6	194
97	GÜDÜL	6	393
98	KALECİK	6	1006
99	KIZILCAHAMAM	6	553
100	NALLIHAN	6	697
101	AKYURT	6	1006
102	EVREN	6	340
103	ANTALYA KURUMLAR	7	1007
104	ANTALYA İHTİSAS	7	1007
105	ÜÇKAPILAR	7	1007
106	KALEKAPI	7	1007
107	MURATPAŞA	7	1007
108	DÜDEN	7	1007
109	ALANYA	7	41
110	SERİK	7	801
111	MANAVGAT	7	612
112	ELMALI	7	314
113	KEMER	7	541
114	KUMLUCA	7	589
115	FİNİKE	7	352
116	AKSEKİ	7	30
117	GAZİPAŞA	7	356
118	GÜNDOĞMUŞ	7	400
119	KAŞ	7	526
120	KORKUTELİ	7	570
121	DEMRE	7	262
122	İBRADI	7	454
123	ARTVİN	8	631
124	HOPA	8	448
125	ARHAVİ	8	70
126	ARDANUÇ	8	67
127	BORÇKA	8	159
128	ŞAVŞAT	8	852
129	YUSUFELİ	8	965
130	MURGUL	8	692
131	EFELER	9	1009
132	GÜZELHİSAR	9	1009
133	NAZİLLİ	9	701
134	SÖKE	9	826
135	ÇİNE	9	240
136	GERMENCİK	9	367
137	KUŞADASI	9	594
138	DİDİM	9	275
139	BOZDOĞAN	9	163
140	KARACASU	9	502
141	KOÇARLI	9	563
142	KUYUCAK	9	595
143	SULTANHİSAR	9	831
144	YENİPAZAR	9	946
145	BUHARKENT	9	173
146	İNCİRLİOVA	9	465
147	KARPUZLU	9	522
148	KÖŞK	9	582
149	KARESİ	10	1010
150	KURTDERELİ	10	1010
151	AYVALIK	10	98
152	BANDIRMA	10	117
153	BURHANİYE	10	177
154	EDREMİT	10	302
155	GÖNEN	10	385
156	SUSURLUK	10	838
157	ERDEK	10	321
158	BİGADİÇ	10	151
159	SINDIRGI	10	808
160	DURSUNBEY	10	298
161	BALYA	10	115
162	HAVRAN	10	432
163	İVRİNDİ	10	477
164	KEPSUT	10	544
165	MANYAS	10	613
166	SAVAŞTEPE	10	791
167	MARMARA	10	614
168	GÖMEÇ	10	384
169	BİLECİK	11	632
170	BOZÜYÜK	11	169
171	GÖLPAZARI	11	382
172	OSMANELİ	11	723
173	PAZARYERİ	11	743
174	SÖĞÜT	11	824
175	YENİPAZAR	11	947
176	İNHİSAR	11	468
177	BİNGÖL	12	633
178	GENÇ	12	363
179	KARLIOVA	12	521
180	KİĞI	12	557
181	SOLHAN	12	821
182	ADAKLI	12	5
183	YAYLADERE	12	938
184	YEDİSU	12	940
185	BİTLİS	13	634
186	TATVAN	13	873
187	ADİLCEVAZ	13	8
188	AHLAT	13	15
189	HİZAN	13	445
190	MUTKİ	13	696
191	GÜROYMAK	13	407
192	BOLU	14	635
193	GEREDE	14	365
194	GÖYNÜK	14	390
195	KIBRISCIK	14	549
196	MENGEN	14	623
197	MUDURNU	14	688
198	SEBEN	14	793
199	DÖRTDİVAN	14	292
200	YENİÇAĞA	14	943
201	BURDUR	15	636
202	BUCAK	15	172
203	AĞLASUN	15	12
204	GÖLHİSAR	15	378
205	TEFENNİ	15	876
206	YEŞİLOVA	15	955
207	KARAMANLI	15	510
208	KEMER	15	542
209	ALTINYAYLA	15	54
210	ÇAVDIR	15	211
211	ÇELTİKÇİ	15	225
212	BURSA İHTİSAS	16	1016
213	OSMANGAZİ	16	1016
214	YILDIRIM	16	1016
215	ÇEKİRGE	16	1016
216	SETBAŞI	16	1016
217	ULUDAĞ	16	1016
218	YEŞİL	16	1016
219	NİLÜFER	16	1016
220	ERTUĞRULGAZİ	16	1016
221	GÖKDERE	16	1016
222	GEMLİK	16	1016
223	İNEGÖL	16	467
224	KARACABEY	16	501
225	MUSTAFAKEMALPAŞA	16	694
226	MUDANYA	16	1016
227	ORHANGAZİ	16	716
228	İZNİK	16	480
229	YENİŞEHİR	16	949
230	KELES	16	536
231	ORHANELİ	16	715
232	HARMANCIK	16	426
233	BÜYÜKORHAN	16	180
234	ÇANAKKALE	17	637
235	BİGA	17	150
236	ÇAN	17	198
237	GELİBOLU	17	360
238	AYVACIK	17	96
239	BAYRAMİÇ	17	131
240	BOZCAADA	17	162
241	ECEABAT	17	301
242	EZİNE	17	344
243	GÖKÇEADA	17	371
244	LAPSEKİ	17	602
245	YENİCE	17	941
246	ÇANKIRI	18	638
247	ÇERKEŞ	18	227
248	ELDİVAN	18	311
249	ILGAZ	18	452
250	KURŞUNLU	18	591
251	ORTA	18	717
252	ŞABANÖZÜ	18	845
253	YAPRAKLI	18	934
254	ATKARACALAR	18	86
255	KIZILIRMAK	18	554
256	BAYRAMÖREN	18	132
257	KORGUN	18	568
258	ÇORUM	19	639
259	SUNGURLU	19	835
260	ALACA	19	37
261	BAYAT	19	127
262	İSKİLİP	19	474
263	KARGI	19	519
264	MECİTÖZÜ	19	619
265	ORTAKÖY	19	720
266	OSMANCIK	19	722
267	BOĞAZKALE	19	155
268	UĞURLUDAĞ	19	905
269	DODURGA	19	283
270	OĞUZLAR	19	711
271	LAÇİN	19	599
272	ÇINAR	20	1020
273	GÖKPINAR	20	1020
274	SARAYLAR	20	1020
275	DENİZLİ İHTİSAS	20	1020
276	PAMUKKALE	20	1020
277	SARAYKÖY	20	777
278	ACIPAYAM	20	4
279	TAVAS	20	874
280	BULDAN	20	176
281	ÇAL	20	189
282	ÇİVRİL	20	241
283	ÇAMELİ	20	193
284	ÇARDAK	20	202
285	GÜNEY	20	401
286	KALE	20	491
287	BABADAĞ	20	101
288	BEKİLLİ	20	134
289	HONAZ	20	447
290	SERİNHİSAR	20	802
291	AKKÖY	20	734
292	BAKLAN	20	111
293	BEYAĞAÇ	20	141
294	BOZKURT	20	165
295	GÖKALP	21	1021
296	SÜLEYMAN NAZİF	21	1021
297	CAHİT SITKI TARANCI	21	1021
298	BİSMİL	21	153
299	ÇERMİK	21	229
300	ÇINAR	21	232
301	ÇÜNGÜŞ	21	248
302	DİCLE	21	274
303	ERGANİ	21	327
304	HANİ	21	424
305	HAZRO	21	438
306	KULP	21	585
307	LİCE	21	603
308	SİLVAN	21	812
309	EĞİL	21	306
310	KOCAKÖY	21	561
311	ARDA	22	640
312	KIRKPINAR	22	640
313	KEŞAN	22	547
314	UZUNKÖPRÜ	22	916
315	HAVSA	22	433
316	İPSALA	22	471
317	ENEZ	22	318
318	LALAPAŞA	22	601
319	MERİÇ	22	626
320	SÜLOĞLU	22	842
321	HARPUT	23	641
322	HAZAR	23	641
323	AĞIN	23	11
324	BASKİL	23	118
325	KARAKOÇAN	23	507
326	KEBAN	23	533
327	MADEN	23	606
328	PALU	23	733
329	SİVRİCE	23	819
330	ARICAK	23	71
331	KOVANCILAR	23	571
332	ALACAKAYA	23	38
333	FEVZİPAŞA	24	642
334	ÇAYIRLI	24	217
335	İLİÇ	24	460
336	KEMAH	24	538
337	KEMALİYE	24	539
338	REFAHİYE	24	761
339	TERCAN	24	880
340	ÜZÜMLÜ	24	921
341	OTLUKBELİ	24	725
342	AZİZİYE	25	1025
343	KAZIMKARABEKİR	25	1025
344	AŞKALE	25	82
345	ÇAT	25	205
346	HINIS	25	442
347	HORASAN	25	449
348	İSPİR	25	476
349	KARAYAZI	25	517
350	NARMAN	25	699
351	OLTU	25	712
352	OLUR	25	713
353	PASİNLER	25	736
354	ŞENKAYA	25	858
355	TEKMAN	25	878
356	TORTUM	25	891
357	KARAÇOBAN	25	503
358	UZUNDERE	25	915
359	PAZARYOLU	25	744
360	AZİZİYE (ILICA)	25	1025
361	KÖPRÜKÖY	25	579
362	ESKİŞEHİR	26	1026
363	MAHMUDİYE	26	607
364	MİHALIÇÇIK	26	684
365	SARICAKAYA	26	779
366	SEYİTGAZİ	26	807
367	ALPU	26	46
368	BEYLİKOVA	26	145
369	İNÖNÜ	26	469
370	GÜNYÜZÜ	26	405
371	HAN	26	422
372	MİHALGAZİ	26	683
373	GAZİANTEP İHTİSAS	27	1027
374	SUBURCU	27	1027
375	ŞEHİTKÂMİL	27	1027
376	ŞAHİNBEY	27	1027
377	GAZİKENT	27	1027
378	KOZANLI	27	1027
379	NİZİP	27	704
380	İSLAHİYE	27	475
381	ARABAN	27	62
382	OĞUZELİ	27	1027
383	YAVUZELİ	27	936
384	KARKAMIŞ	27	520
385	NURDAĞI	27	705
386	GİRESUN	28	643
387	BULANCAK	28	174
388	ALUCRA	28	57
389	DERELİ	28	265
390	ESPİYE	28	336
391	EYNESİL	28	341
392	GÖRELE	28	388
393	KEŞAP	28	548
394	ŞEBİNKARAHİSAR	28	853
395	TİREBOLU	28	885
396	PİRAZİZ	28	753
397	YAĞLIDERE	28	927
398	ÇANAKÇI	28	199
399	GÜCE	28	391
400	ÇAMOLUK	28	197
401	DOĞANKENT	28	285
402	GÜMÜŞHANE	29	644
403	KELKİT	29	537
404	ŞİRAN	29	862
405	TORUL	29	892
406	KÖSE	29	581
407	KÜRTÜN	29	598
408	HAKKARİ	30	645
409	YÜKSEKOVA	30	966
410	ÇUKURCA	30	245
411	ŞEMDİNLİ	30	857
412	23 TEMMUZ	31	1031
413	ANTAKYA	31	1031
414	ŞÜKRÜKANATLI	31	1031
415	SAHİL	31	473
416	AKDENİZ	31	473
417	ASIM GÜNDÜZ	31	473
418	DÖRTYOL	31	293
419	KIRIKHAN	31	551
420	REYHANLI	31	763
421	SAMANDAĞ	31	768
422	ALTINÖZÜ	31	52
423	HASSA	31	431
424	YAYLADAĞI	31	937
425	ERZİN	31	331
426	BELEN	31	135
427	KUMLU	31	588
428	DAVRAZ	32	646
429	KAYMAKKAPI	32	646
430	EĞİRDİR	32	307
431	YALVAÇ	32	933
432	ATABEY	32	83
433	GELENDOST	32	359
434	KEÇİBORLU	32	534
435	SENİRKENT	32	799
436	SÜTÇÜLER	32	844
437	ŞARKİKARAAĞAÇ	32	850
438	ULUBORLU	32	910
439	AKSU	32	32
440	GÖNEN	32	386
441	YENİŞARBADEMLİ	32	948
442	İSTİKLÂL	33	1033
443	URAY	33	1033
444	LİMAN	33	1033
445	TOROS	33	1033
446	MERSİN İHTİSAS	33	1033
447	ERDEMLİ	33	322
448	SİLİFKE	33	809
449	ANAMUR	33	59
450	KIZILMURAT	33	868
451	ŞEHİTKERİM	33	868
452	GÜLNAR	33	395
453	MUT	33	695
454	AYDINCIK	33	92
455	BOZYAZI	33	170
456	ÇAMLIYAYLA	33	196
457	BÜYÜK MÜKELLEFLER	34	1034
458	BOĞAZİÇİ KURUMLAR	34	1034
459	ANADOLU KURUMLAR	34	1034
460	MARMARA KURUMLAR	34	1034
461	HALİÇ İHTİSAS	34	1034
462	VATAN İHTİSAS	34	1034
463	ÇAMLICA İHTİSAS	34	1034
464	ALEMDAĞ	34	1034
465	BEYOĞLU	34	1034
466	HALKALI	34	1034
467	DAVUTPAŞA	34	1034
468	ESENLER	34	1034
469	FATİH	34	1034
470	KÜÇÜKKÖY	34	1034
471	MERTER	34	1034
472	SULTANBEYLİ	34	1034
473	TUZLA	34	1034
474	KOZYATAĞI	34	1034
475	MASLAK	34	1034
476	ZİNCİRLİKUYU	34	1034
477	İKİTELLİ	34	1034
478	BEŞİKTAŞ	34	1034
479	ÜMRANİYE	34	1034
480	YEDİTEPE	34	1034
481	KASIMPAŞA	34	1034
482	ERENKÖY	34	1034
483	HİSAR	34	1034
484	TUNA	34	1034
485	RIHTIM	34	1034
486	GÜNGÖREN	34	1034
487	KOCASİNAN	34	1034
488	GÜNEŞLİ	34	1034
489	KÜÇÜKYALI	34	1034
490	PENDİK	34	1034
491	BAYRAMPAŞA	34	1034
492	BEYAZIT	34	1034
493	GAZİOSMANPAŞA	34	1034
494	GÖZTEPE	34	1034
495	HOCAPAŞA	34	1034
496	KADIKÖY	34	1034
497	KOCAMUSTAFAPAŞA	34	1034
498	MECİDİYEKÖY	34	1034
499	ŞİŞLİ	34	1034
500	ÜSKÜDAR	34	1034
501	KAĞITHANE	34	1034
502	ZEYTİNBURNU	34	1034
503	BEYKOZ	34	1034
504	SARIYER	34	1034
505	BAKIRKÖY	34	1034
506	KARTAL	34	1034
507	NAKİL VASITALARI	34	1034
508	SARIGAZİ	34	1034
509	ATIŞALANI	34	1034
510	YAKACIK	34	1034
511	YENİBOSNA	34	1034
512	AVCILAR	34	1034
513	KÜÇÜKÇEKMECE	34	1034
514	BEYLİKDÜZÜ	34	1034
515	ADALAR	34	1034
516	SİLİVRİ	34	1034
517	BÜYÜKÇEKMECE	34	1034
518	ŞİLE	34	1034
519	BORNOVA	35	1035
520	ÇAKABEY	35	1035
521	KORDON	35	1035
522	HASAN TAHSİN	35	1035
523	İZMİR İHTİSAS	35	1035
524	9 EYLÜL	35	1035
525	YAMANLAR	35	1035
526	KARŞIYAKA	35	1035
527	KEMERALTI	35	1035
528	KONAK	35	1035
529	ŞİRİNYER	35	1035
530	KADİFEKALE	35	1035
531	TAŞITLAR	35	1035
532	BELKAHVE	35	1035
533	BALÇOVA	35	1035
534	GAZİEMİR	35	1035
535	EGE	35	1035
536	ÇİĞLİ	35	1035
537	BAYINDIR	35	128
538	BERGAMA	35	136
539	MENEMEN	35	1035
540	ÖDEMİŞ	35	728
541	TİRE	35	884
542	TORBALI	35	1035
543	KEMALPAŞA	35	1035
544	URLA	35	1035
545	SELÇUK	35	795
546	KINIK	35	550
547	KİRAZ	35	559
548	ÇEŞME	35	230
549	ALİAĞA	35	1035
550	MENDERES	35	1035
551	DİKİLİ	35	277
552	FOÇA	35	1035
553	KARABURUN	35	500
554	SEFERİHİSAR	35	1035
555	BEYDAĞ	35	142
556	KARS	36	647
557	ARPAÇAY	36	75
558	DİGOR	36	276
559	KAĞIZMAN	36	488
560	SARIKAMIŞ	36	782
561	SELİM	36	798
562	SUSUZ	36	839
563	AKYAKA	36	34
564	KASTAMONU	37	648
565	TOSYA	37	893
566	TAŞKÖPRÜ	37	870
567	ARAÇ	37	63
568	AZDAVAY	37	99
569	BOZKURT	37	166
570	CİDE	37	184
571	ÇATALZEYTİN	37	209
572	DADAY	37	249
573	DEVREKANİ	37	273
574	İNEBOLU	37	466
575	KÜRE	37	597
576	ABANA	37	2
577	İHSANGAZİ	37	456
578	PINARBAŞI	37	750
579	ŞENPAZAR	37	859
580	AĞLI	37	13
581	DOĞANYURT	37	289
582	HANÖNÜ	37	425
583	SEYDİLER	37	804
584	KAYSERİ İHTİSAS	38	1038
585	MİMAR SİNAN	38	1038
586	ERCİYES	38	1038
587	KALEÖNÜ	38	1038
588	GEVHER NESİBE	38	1038
589	DEVELİ	38	271
590	PINARBAŞI	38	751
591	BÜNYAN	38	178
592	FELAHİYE	38	348
593	İNCESU	38	464
594	SARIOĞLAN	38	784
595	SARIZ	38	788
596	TOMARZA	38	886
597	YAHYALI	38	929
598	YEŞİLHİSAR	38	953
599	AKKIŞLA	38	26
600	HACILAR	38	1038
601	ÖZVATAN	38	731
602	KIRKLARELİ	39	649
603	LÜLEBURGAZ	39	604
604	BABAESKİ	39	102
605	DEMİRKÖY	39	260
606	KOFÇAZ	39	564
607	PEHLİVANKÖY	39	745
608	PINARHİSAR	39	752
609	VİZE	39	926
610	KIRŞEHİR	40	650
611	KAMAN	40	495
612	ÇİÇEKDAĞI	40	234
613	MUCUR	40	686
614	AKPINAR	40	29
615	AKÇAKENT	40	20
616	BOZTEPE	40	168
617	KOCAELİ İHTİSAS	41	1041
618	TEPECİK	41	1041
619	ALEMDAR	41	1041
620	GEBZE İHTİSAS	41	1041
621	ACISU	41	1041
622	ULUÇINAR	41	1041
623	İLYASBEY	41	1041
624	GÖLCÜK	41	1041
625	KARAMÜRSEL	41	1041
626	KÖRFEZ	41	1041
627	DERİNCE	41	1041
628	KANDIRA	41	1041
629	KONYA İHTİSAS	42	1042
630	SELÇUK	42	1042
631	MEVLANA	42	1042
632	MERAM	42	1042
633	ALAADDİN	42	1042
634	AKŞEHİR	42	33
635	EREĞLİ	42	323
636	BEYŞEHİR	42	148
637	CİHANBEYLİ	42	185
638	ÇUMRA	42	247
639	SEYDİŞEHİR	42	805
640	ILGIN	42	453
641	KULU	42	586
642	KARAPINAR	42	512
643	BOZKIR	42	164
644	DOĞANHİSAR	42	284
645	HADİM	42	415
646	KADINHANI	42	484
647	SARAYÖNÜ	42	778
648	YUNAK	42	963
649	AKÖREN	42	28
650	ALTINEKİN	42	49
651	DEREBUCAK	42	264
652	HÜYÜK	42	451
653	TAŞKENT	42	869
654	EMİRGAZİ	42	317
655	GÜNEYSINIR	42	402
656	HALKAPINAR	42	419
657	TUZLUKÇU	42	902
658	AHIRLI	42	14
659	ÇELTİK	42	224
660	DERBENT	42	263
661	YALIHÜYÜK	42	932
662	30 AĞUSTOS	43	651
663	ÇİNİLİ	43	651
664	GEDİZ	43	358
665	SİMAV	43	813
666	TAVŞANLI	43	875
667	EMET	43	315
668	ALTINTAŞ	43	53
669	DOMANİÇ	43	291
670	ASLANAPA	43	81
671	DUMLUPINAR	43	296
672	HİSARCIK	43	444
673	ŞAPHANE	43	848
674	ÇAVDARHİSAR	43	210
675	PAZARLAR	43	742
676	FIRAT	44	1044
677	BEYDAĞI	44	1044
678	AKÇADAĞ	44	18
679	ARAPGİR	44	66
680	ARGUVAN	44	69
681	DARENDE	44	252
682	DOĞANŞEHİR	44	287
683	HEKİMHAN	44	439
684	PÜTÜRGE	44	760
685	YEŞİLYURT	44	956
686	BATTALGAZİ	44	125
687	DOĞANYOL	44	288
688	KALE	44	492
689	KULUNCAK	44	587
690	YAZIHAN	44	939
691	MANİSA İHTİSAS	45	1045
692	ALAYBEY	45	1045
693	MESİR	45	1045
694	AKHİSAR	45	24
695	ALAŞEHİR	45	43
696	DEMİRCİ	45	259
697	KIRKAĞAÇ	45	552
698	SALİHLİ ADİL ORAL	45	767
699	SARIGÖL	45	781
700	SARUHANLI	45	789
701	SOMA	45	822
702	TURGUTLU	45	895
703	GÖRDES	45	387
704	KULA	45	584
705	SELENDİ	45	797
706	AHMETLİ	45	16
707	GÖLMARMARA	45	380
708	KÖPRÜBAŞI	45	577
709	ASLANBEY	46	1046
710	AKSU	46	1046
711	ELBİSTAN	46	310
712	AFŞİN	46	9
713	PAZARCIK	46	741
714	ANDIRIN	46	60
715	GÖKSUN	46	373
716	TÜRKOĞLU	46	904
717	ÇAĞLAYANCERİT	46	188
718	EKİNÖZÜ	46	308
719	NURHAK	46	706
720	MARDİN	47	1047
721	KIZILTEPE	47	556
722	NUSAYBİN	47	707
723	DERİK	47	267
724	MAZIDAĞI	47	618
725	MİDYAT	47	682
726	ÖMERLİ	47	729
727	SAVUR	47	792
728	DARGEÇİT	47	253
729	YEŞİLLİ	47	954
730	MUĞLA	48	1048
731	BODRUM	48	154
732	FETHİYE	48	350
733	KÖYCEĞİZ	48	583
734	MİLAS	48	685
735	MARMARİS	48	616
736	YATAĞAN	48	935
737	DATÇA	48	255
738	ULA	48	906
739	DALAMAN	48	250
740	ORTACA	48	718
741	KAVAKLIDERE	48	528
742	SEYDİKEMER	48	803
743	MUŞ	49	652
744	BULANIK	49	175
745	MALAZGİRT	49	608
746	VARTO	49	923
747	HASKÖY	49	430
748	KORKUT	49	569
749	NEVŞEHİR	50	653
750	AVANOS	50	87
751	DERİNKUYU	50	269
752	GÜLŞEHİR	50	396
753	HACIBEKTAŞ	50	413
754	KOZAKLI	50	573
755	ÜRGÜP	50	919
756	ACIGÖL	50	3
757	NİĞDE	51	654
758	BOR	51	158
759	ÇAMARDI	51	191
760	ULUKIŞLA	51	912
761	ALTUNHİSAR	51	56
762	ÇİFTLİK	51	236
763	BOZTEPE	52	1052
764	KÖPRÜBAŞI	52	1052
765	FATSA	52	346
766	ÜNYE	52	918
767	AKKUŞ	52	27
768	AYBASTI	52	91
769	GÖLKÖY	52	379
770	KORGAN	52	567
771	KUMRU	52	590
772	MESUDİYE	52	680
773	PERŞEMBE	52	747
774	ULUBEY	52	908
775	GÜLYALI	52	397
776	GÜRGENTEPE	52	406
777	ÇAMAŞ	52	192
778	ÇATALPINAR	52	208
779	ÇAYBAŞI	52	213
780	İKİZCE	52	458
781	KABADÜZ	52	481
782	KABATAŞ	52	482
783	KAÇKAR	53	655
784	YEŞİLÇAY	53	655
785	ÇAYELİ	53	215
786	PAZAR	53	739
787	ARDEŞEN	53	68
788	ÇAMLIHEMŞİN	53	195
789	FINDIKLI	53	351
790	İKİZDERE	53	459
791	KALKANDERE	53	494
792	GÜNEYSU	53	403
793	DEREPAZARI	53	266
794	HEMŞİN	53	440
795	İYİDERE	53	478
796	GÜMRÜKÖNÜ	54	1054
797	ALİ FUAT CEBESOY	54	1054
798	SAPANCA	54	1054
799	AKYAZI	54	1054
800	GEYVE	54	370
801	HENDEK	54	1054
802	KARASU	54	514
803	KAYNARCA	54	530
804	KOCAALİ	54	560
805	PAMUKOVA	54	735
806	TARAKLI	54	867
807	KARAPÜRÇEK	54	1054
808	19 MAYIS	55	1055
809	GAZİLER	55	1055
810	ZAFER	55	1055
811	BAFRA	55	103
812	ÇARŞAMBA	55	203
813	TERME	55	882
814	HAVZA	55	434
815	ALAÇAM	55	39
816	KAVAK	55	527
817	LADİK	55	600
818	VEZİRKÖPRÜ	55	924
819	ASARCIK	55	80
820	ONDOKUZ MAYIS	55	1
821	SALIPAZARI	55	766
822	TEKKEKÖY	55	1055
823	AYVACIK	55	97
824	YAKAKENT	55	930
825	SİİRT	56	656
826	BAYKAN	56	129
827	ERUH	56	330
828	KURTALAN	56	592
829	PERVARİ	56	749
830	ŞİRVAN	56	863
831	SİNOP	57	657
832	BOYABAT	57	161
833	AYANCIK	57	89
834	DURAĞAN	57	297
835	ERFELEK	57	326
836	GERZE	57	368
837	TÜRKELİ	57	903
838	DİKMEN	57	278
839	SARAYDÜZÜ	57	775
840	KALE	58	658
841	SİTE	58	658
842	ŞARKIŞLA	58	849
843	DİVRİĞİ	58	281
844	GEMEREK	58	361
845	GÜRÜN	58	410
846	HAFİK	58	416
847	İMRANLI	58	463
848	KANGAL	58	497
849	KOYULHİSAR	58	572
850	SUŞEHRİ	58	840
851	YILDIZELİ	58	960
852	ZARA	58	968
853	AKINCILAR	58	25
854	ALTINYAYLA	58	55
855	DOĞANŞAR	58	286
856	GÖLOVA	58	381
857	ULAŞ	58	907
858	SÜLEYMANPAŞA	59	1059
859	NAMIK KEMAL	59	1059
860	ÇERKEZKÖY	59	228
861	ÇORLU	59	243
862	HAYRABOLU	59	436
863	MALKARA	59	609
864	MURATLI	59	690
865	SARAY	59	773
866	ŞARKÖY	59	851
867	MARMARA EREĞLİSİ	59	615
868	TOKAT	60	659
869	ERBAA	60	319
870	NİKSAR	60	702
871	TURHAL	60	896
872	ZİLE	60	970
873	ALMUS	60	45
874	ARTOVA	60	78
875	REŞADİYE	60	762
876	PAZAR	60	740
877	YEŞİLYURT	60	957
878	BAŞÇİFTLİK	60	120
879	SULUSARAY	60	833
880	HIZIRBEY	61	1061
881	KARADENİZ	61	1061
882	AKÇAABAT	61	17
883	OF	61	709
884	VAKFIKEBİR	61	922
885	ARAKLI	61	64
886	ARSİN	61	76
887	ÇAYKARA	61	219
888	MAÇKA	61	605
889	SÜRMENE	61	843
890	TONYA	61	887
891	YOMRA	61	961
892	BEŞİKDÜZÜ	61	138
893	ŞALPAZARI	61	847
894	ÇARŞIBAŞI	61	204
895	DERNEKPAZARI	61	270
896	DÜZKÖY	61	300
897	HAYRAT	61	437
898	KÖPRÜBAŞI	61	578
899	TUNCELİ	62	660
900	ÇEMİŞGEZEK	62	226
901	HOZAT	62	450
902	MAZGİRT	62	617
903	NAZİMİYE	62	700
904	OVACIK	62	726
905	PERTEK	62	748
906	PÜLÜMÜR	62	759
907	ŞEHİTLİK	63	1063
908	TOPÇU MEYDANI	63	1063
909	SİVEREK	63	818
910	VİRANŞEHİR	63	925
911	BİRECİK	63	152
912	AKÇAKALE	63	19
913	BOZOVA	63	167
914	HALFETİ	63	417
915	HİLVAN	63	443
916	SURUÇ	63	837
917	CEYLANPINAR	63	183
918	HARRAN	63	427
919	UŞAK	64	661
920	BANAZ	64	116
921	EŞME	64	337
922	KARAHALLI	64	504
923	ULUBEY	64	909
924	SİVASLI	64	817
925	VAN	65	1065
926	ERCİŞ	65	320
927	BAŞKALE	65	122
928	ÇATAK	65	206
929	GEVAŞ	65	369
930	GÜRPINAR	65	408
931	MURADİYE	65	689
932	ÖZALP	65	730
933	BAHÇESARAY	65	108
934	ÇALDIRAN	65	190
935	EDREMİT	65	303
936	SARAY	65	774
937	YOZGAT	66	662
938	BOĞAZLIYAN	66	156
939	SORGUN	66	823
940	YERKÖY	66	952
941	AKDAĞMADENİ	66	22
942	ÇAYIRALAN	66	216
943	ÇEKEREK	66	220
944	SARIKAYA	66	783
945	ŞEFAATLİ	66	854
946	AYDINCIK	66	93
947	ÇANDIR	66	200
948	KADIŞEHRİ	66	485
949	SARAYKENT	66	776
950	YENİFAKILI	66	944
951	UZUNMEHMET	67	663
952	KARA ELMAS	67	663
953	EREĞLİ	67	324
954	ÇAYCUMA	67	214
955	DEVREK	67	272
956	ALAPLI	67	42
957	GÖKÇEBEY	67	372
958	AKSARAY	68	664
959	AĞAÇÖREN	68	10
960	GÜZELYURT	68	412
961	ORTAKÖY	68	721
962	SARIYAHŞİ	68	786
963	ESKİL	68	334
964	GÜLAĞAÇ	68	394
965	BAYBURT	69	665
966	AYDINTEPE	69	94
967	DEMİRÖZÜ	69	261
968	KARAMAN	70	666
969	AYRANCI	70	95
970	ERMENEK	70	329
971	KAZIM KARABEKİR	70	532
972	BAŞYAYLA	70	124
973	SARIVELİLER	70	785
974	IRMAK	71	667
975	KALETEPE	71	667
976	DELİCE	71	258
977	KESKİN	71	545
978	SULAKYURT	71	827
979	BALIŞEYH	71	114
980	ÇELEBİ	71	222
981	KARAKEÇİLİ	71	506
982	BATMAN	72	668
983	BEŞİRİ	72	140
984	GERCÜŞ	72	364
985	HASANKEYF	72	429
986	KOZLUK	72	576
987	SASON	72	790
988	ŞIRNAK	73	669
989	CİZRE	73	186
990	SİLOPİ	73	811
991	BEYTÜŞŞEBAP	73	149
992	GÜÇLÜKONAK	73	392
993	İDİL	73	455
994	ULUDERE	73	911
995	BARTIN	74	670
996	AMASRA	74	58
997	KURUCAŞİLE	74	593
998	ULUS	74	913
999	ARDAHAN	75	671
1000	ÇILDIR	75	231
1001	DAMAL	75	251
1002	GÖLE	75	377
1003	HANAK	75	423
1004	POSOF	75	756
1005	IĞDIR	76	672
1006	ARALIK	76	65
1007	KARAKOYUNLU	76	508
1008	TUZLUCA	76	901
1009	YALOVA	77	673
1010	ALTINOVA	77	51
1011	ARMUTLU	77	73
1012	ÇINARCIK	77	233
1013	KARABÜK	78	674
1014	SAFRANBOLU	78	764
1015	EFLANİ	78	305
1016	ESKİPAZAR	78	335
1017	OVACIK	78	727
1018	YENİCE	78	942
1019	KİLİS	79	675
1020	OSMANİYE	80	676
1021	KADİRLİ	80	486
1022	BAHÇE	80	106
1023	DÜZİÇİ	80	299
1024	HASANBEYLİ	80	428
1025	SUMBAS	80	834
1026	TOPRAKKALE	80	888
1027	DÜZCE	81	677
1028	AKÇAKOCA	81	21
1029	YIĞILCA	81	958
1030	CUMAYERİ	81	187
1031	GÖLYAKA	81	383
1032	ÇİLİMLİ	81	239
1033	GÜMÜŞOVA	81	399
1034	KAYNAŞLI	81	531
\.


--
-- TOC entry 5218 (class 0 OID 25508)
-- Dependencies: 235
-- Data for Name: user_; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_ (id, user_group_id, language_id, name_, tckno_, certificate_number, title_, email_, password_, active_, picture, first_name, last_name, is_superuser, is_staff, last_login, date_joined, auth_user_id, logo_media) FROM stdin;
9	1	\N	a	8744561248	\N	\N	\N	\N	t	picture_user/Screenshot_2025-08-09_103333.png	Ahmet	Cemal	\N	f	\N	\N	9	\N
10	1	1	ekonaz	62089291120	\N	CEO	\N	\N	t	picture_user/ekonaz.png	Ali	Bozdemir	f	t	\N	\N	10	\N
11	2	1	Muhasebeci	476387995	\N	Eğitmen	\N	\N	t		Mehmet	Yılmaz	f	t	\N	\N	11	\N
\.


--
-- TOC entry 5220 (class 0 OID 25515)
-- Dependencies: 237
-- Data for Name: user_firm; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_firm (user_id, firm_id, create_, id) FROM stdin;
11	4	2025-08-29 14:54:18.725504	2
\.


--
-- TOC entry 5221 (class 0 OID 25519)
-- Dependencies: 238
-- Data for Name: user_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_group (id, name_, description_) FROM stdin;
1	Yönetici	Sistemin tam yetkili yöneticisi
2	Operatör	Sınırlı yetkilere sahip standart kullanıcı
\.


--
-- TOC entry 5316 (class 0 OID 0)
-- Dependencies: 246
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);


--
-- TOC entry 5317 (class 0 OID 0)
-- Dependencies: 248
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 12, true);


--
-- TOC entry 5318 (class 0 OID 0)
-- Dependencies: 244
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 153, true);


--
-- TOC entry 5319 (class 0 OID 0)
-- Dependencies: 252
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 8, true);


--
-- TOC entry 5320 (class 0 OID 0)
-- Dependencies: 250
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 11, true);


--
-- TOC entry 5321 (class 0 OID 0)
-- Dependencies: 254
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 459, true);


--
-- TOC entry 5322 (class 0 OID 0)
-- Dependencies: 261
-- Name: blood__id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blood__id_seq', 8, true);


--
-- TOC entry 5323 (class 0 OID 0)
-- Dependencies: 269
-- Name: carbon_coefficienttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.carbon_coefficienttype_id_seq', 1, true);


--
-- TOC entry 5324 (class 0 OID 0)
-- Dependencies: 267
-- Name: carbon_emissionfactor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.carbon_emissionfactor_id_seq', 3, true);


--
-- TOC entry 5325 (class 0 OID 0)
-- Dependencies: 271
-- Name: carbon_inputcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.carbon_inputcategory_id_seq', 1, false);


--
-- TOC entry 5326 (class 0 OID 0)
-- Dependencies: 273
-- Name: carbon_inputdata_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.carbon_inputdata_id_seq', 1, false);


--
-- TOC entry 5327 (class 0 OID 0)
-- Dependencies: 275
-- Name: carbon_report_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.carbon_report_id_seq', 1, false);


--
-- TOC entry 5328 (class 0 OID 0)
-- Dependencies: 218
-- Name: city_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.city_id_seq', 1, false);


--
-- TOC entry 5329 (class 0 OID 0)
-- Dependencies: 263
-- Name: department__id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.department__id_seq', 3, true);


--
-- TOC entry 5330 (class 0 OID 0)
-- Dependencies: 220
-- Name: district_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.district_id_seq', 1, false);


--
-- TOC entry 5331 (class 0 OID 0)
-- Dependencies: 256
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 29, true);


--
-- TOC entry 5332 (class 0 OID 0)
-- Dependencies: 242
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 37, true);


--
-- TOC entry 5333 (class 0 OID 0)
-- Dependencies: 240
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mydbuser
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 92, true);


--
-- TOC entry 5334 (class 0 OID 0)
-- Dependencies: 265
-- Name: education__id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.education__id_seq', 9, true);


--
-- TOC entry 5335 (class 0 OID 0)
-- Dependencies: 222
-- Name: firm_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.firm_id_seq', 5, true);


--
-- TOC entry 5336 (class 0 OID 0)
-- Dependencies: 224
-- Name: language__id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.language__id_seq', 1, false);


--
-- TOC entry 5337 (class 0 OID 0)
-- Dependencies: 226
-- Name: media_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.media_id_seq', 1, false);


--
-- TOC entry 5338 (class 0 OID 0)
-- Dependencies: 228
-- Name: media_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.media_type_id_seq', 1, false);


--
-- TOC entry 5339 (class 0 OID 0)
-- Dependencies: 230
-- Name: nace_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.nace_id_seq', 1, false);


--
-- TOC entry 5340 (class 0 OID 0)
-- Dependencies: 232
-- Name: path_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.path_id_seq', 1, false);


--
-- TOC entry 5341 (class 0 OID 0)
-- Dependencies: 259
-- Name: personnel__id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.personnel__id_seq', 5, true);


--
-- TOC entry 5342 (class 0 OID 0)
-- Dependencies: 234
-- Name: tax_office_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tax_office_id_seq', 1, false);


--
-- TOC entry 5343 (class 0 OID 0)
-- Dependencies: 236
-- Name: user__id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user__id_seq', 11, true);


--
-- TOC entry 5344 (class 0 OID 0)
-- Dependencies: 277
-- Name: user_firm_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_firm_id_seq', 2, true);


--
-- TOC entry 5345 (class 0 OID 0)
-- Dependencies: 239
-- Name: user_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_group_id_seq', 1, false);


-- Completed on 2025-09-01 12:16:31

--
-- PostgreSQL database dump complete
--

