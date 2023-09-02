---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
UNIX ^6MYYHsQ9

la signal invece di segnalare e basta segnaliamo passando la lock, 
così che chi viene risvegliato ha già la lock, e non la deve riacquisire, 
sicuramente se gli passo la lock non potrà essere scavalcato da un altro. ^eCA7dzpo

SO ^9okUCD0N

MULTIPROCESSOR ^LPBdSKDN

SCRITTORI E LETTORI ^IMHqHh61

SO MODERNI NON USANO IL BANCHIERE PERCHE:
1) Molto costoso quindi ha senso utilizzarlo solo in situazioni molto critiche.
2) Dobbiamo sapere in anticipo quello di cui ogni processo ha bisogno. ^gLkrphHI

FILOSOFI A CENA ^AGwbIvvQ

ORDINE ASSIMETRICO ^mH952EYF

ATTESA ATTIVA ^CXj6MQ8J

(FAIRNESS -> ATTESA INFINITA) ^GLbtvMY0

MONITOR ^lAZZVzmI

ALGORITMI: (QDT = QUANTO DI TEMPO)
1) FIFO -> ESEGUIAMO TASK IN ORDINE DI ARRIVO

2) SJF -> ESEGUIAMO PRIMA I TASK + VELOCI

2.1) PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE
MI FERMO ED PASSO A QUELLO, SUCCESSIVAMENTE RIPRENDO
DA DOVE MI ERO FERMATO.

2.2) NO PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE
FINISCO IL TASK CORRENTE E POI PASSO A QUELLO

3) ROUND ROBIN -> OGNI TASK ACQUISISCE LA CPU PER UN
QUANTO DI TEMPO, QUANDO SI ESAURISCE PASSO AL TASK 
SUCCESSIVO (CON PRERILASCIO) E MI METTO IN FONDO
ALLA CODA

4) MAX-MIN FAIRNESS -> ROUND ROBIN ASSEGNANDO IL
AD OGNI TASK UNA PORZIONE DI QUANTO DI TEMPO

5)MFQ -> N CODE ROUND ROBIN CON PRIORITA E QUANTO
DI TEMPO SPECIFICO, + PRIORITA IMPLICA UN QDT 
+ PICCOLO E VICEVERSA. SE SCADE IL QDT IL TASK SCENDE
 DI PRIORITA, SE RILASCIAMO IL PROCESSORE VOLONTARIAMENTE 
RIMANIAMO NELLA CODA CORRENTE E INFINE SE IL PROCESSO SI 
SOSPENDE SALE DI PRIORITA ^iAfEmFao

PRIORITY INVERSION -> SE UN TASK STA FERMO DA UN PO' LO
SCHEDULER LO SVEGLIA E GLI DA UN BOOST DI PRIORITA
(EX: UN THREAD SOSPESO CHE ATTENDE DI ESSERE SVEGLIATO
DA UN THREAD DI PRIORITA MOLTO INFERIORE) ^ahyRjWNk

MULTIPROCESSOR ^GRVkWSDo

MFQ ^4afkSfBr

AFFINITY SCHEDULING -> ASSEGNARE IL PROCESSO AL PROCESSORE + AFFINE 
(QUELLO CHE DETIENE I DATI CHE MODIFICA IL TASK DEL CASO) ^xwDxYI34


# Embedded files
ec76cc75119cb360935bc19a2dbcbb971fb6d22c: [[Pasted Image 20230826225908_117.png]]
3142bca187c4563fc2d7bf5c7afc60beb148687e: [[Pasted Image 20230826230008_133.png]]
254d8736b501d26d758cc3c205a1da5a90d3edc7: [[Pasted Image 20230826230038_157.png]]
9a251f55ddb78daaa7c5f6bc51e72f4a35cf1629: [[Pasted Image 20230826230123_191.png]]
0f32f4416cd7b3d0f13373e5fb9f14eca26eed75: [[Pasted Image 20230826230208_206.png]]
7994e852dcf8225da180fa089d61b304c277c0cb: [[Pasted Image 20230826230338_228.png]]
0219c81f373dee340b030ad957f77dbb09bf88f7: [[Pasted Image 20230826230408_243.png]]
07f4bcbdd837c51d7eee0bf24ddd020ee7eb0123: [[Pasted Image 20230826230453_252.png]]
d3e54c9e92d39f6cbbb61da9b3c8e0e5aa52852a: [[Pasted Image 20230826230538_271.png]]
10f2351f5de258d9cae77b77db77e65f76f424ad: [[Pasted Image 20230826230624_289.png]]
6cc9c91c142b06a505b2455e6227488d0d6c362e: [[Pasted Image 20230826230726_343.png]]
e8fb4d4c2ec1acc61a2ca86350e238aa91069c2e: [[Pasted Image 20230826230958_433.png]]
00b359e132da19452a54ac7aa48015df234d33d4: [[Pasted Image 20230826231043_461.png]]
db990272c305e4645301c1bcf93ebb6fe77ae827: [[Pasted Image 20230826231223_546.png]]
b53395bdc8f67fb1d13c011f2700b7f99e96e047: [[Pasted Image 20230826231415_640.png]]
f5a1ef425973e6688c1dfa441d233858ff34a01f: [[Pasted Image 20230826231445_673.png]]
0883d858fe8a24ba992d3328ebe319dacc950904: [[Pasted Image 20230826231720_770.png]]
f44b51176322ee4865adfbf8a370ceae142a6a71: [[Pasted Image 20230831120917_536.png]]
3a5ee61a851138c48ae380b0a9bfe2b5aa938470: [[Pasted Image 20230831121034_661.png]]
fb96f07b3714861e331354f76df7276eaf972850: [[Pasted Image 20230831121138_970.png]]
c43b42c27dc39c0f28774df4e371df42d98afd45: [[Pasted Image 20230831121412_004.png]]
554e0421a8b658a2e32d0696df884ead35c79327: [[Pasted Image 20230831121513_031.png]]
8f07c909db308ffadbaf2f3becda9ad52b21f9be: [[Pasted Image 20230831121729_109.png]]
c36fae0dd9b8000ae8ea7b1c47e58a5fdb0a52e9: [[Pasted Image 20230831121926_374.png]]
9ca6b0593fc14b58bfb24572f880a0f98fd19d67: [[Pasted Image 20230831122047_434.png]]
4348cdc5957c17e5ff53f72b2bd0c7ee4b05dcf1: [[Pasted Image 20230831122205_097.png]]
358d82e3c4e8ac84bd07c8ea06f27199eb3e405a: [[Pasted Image 20230831122653_088.png]]
993a144126a141df530b2b68fbbbe6af2f2d7b29: [[Pasted Image 20230831152058_682.png]]
398250e87eb98abc2d7b05f2eec7647559cc843a: [[Pasted Image 20230831161134_606.png]]
e7a4241df5ba5480e231594974736f40218851eb: [[Pasted Image 20230831164106_278.png]]
97d7103da9f6ba984e3d11ed0c363df34ec8e2c5: [[Pasted Image 20230831164352_905.png]]
510b6336c846b72d20d7878ff271f15b6048ae4c: [[Pasted Image 20230831164753_781.png]]
fd019b84cec5c412ab6a9fa2c834f857bad8d771: [[Pasted Image 20230831172125_599.png]]
2d9823f1b39bd3b7c5bd434608f5ed0ae2d4ee56: [[Pasted Image 20230831172245_927.png]]
da6d7680c1d7af21f37172b328852935e1dc2167: [[Pasted Image 20230831172619_642.png]]
8c90f6ef403f9135afb1225879bbc8f09d6b77cb: [[Pasted Image 20230831172744_247.png]]
5681d9b04b0506a8d45563628dac9abe2c2adf26: [[Pasted Image 20230831173305_502.png]]
791af62a020433b6da793fe87b4811b59bf57b2f: [[Pasted Image 20230831173526_609.png]]
a472d3cdd365d641fc5bf9a8708d07e9fe63fb63: [[Pasted Image 20230831174244_057.png]]
68edf30da2e094b55a446927660587f804d5c6a2: [[Pasted Image 20230831181444_218.png]]
2a6748c811a2c01345d0b25d9ce94538b310cd56: [[Pasted Image 20230831182514_354.png]]
ff2e7181cf1605c79a141a3a7eb4c3678d06ce0e: [[Pasted Image 20230831182726_439.png]]
ad2bcf10863fa773d7c02d6adf5153052020df6b: [[Pasted Image 20230831183502_833.png]]
01d2eac8ccd18a693f492837083d835e685f7722: [[Pasted Image 20230831184316_950.png]]
c222f552f60a20db8db6366d770f821b01b25f52: [[Pasted Image 20230831184920_375.png]]
9b7d4806704fb770b55194b4e14116bc40420a58: [[Pasted Image 20230831185256_207.png]]
10fb3d2ece95569b9e1e392ea026950be972cda3: [[Pasted Image 20230831185447_258.png]]
fbc78c7e7956823040c6b9c70ef98efe56b1a5d9: [[Pasted Image 20230831185833_240.png]]
02c082f4a8c1f23e38336113d85467391cd871c7: [[Pasted Image 20230831190126_492.png]]
4d9c1745b572ff944b6cb9aacf07d53cdb4bf87e: [[Pasted Image 20230831190315_524.png]]
24128ffed79cfea035e6f7055d9296df65c0eb0e: [[Pasted Image 20230831190401_329.png]]
8ef05b42873fee038ea7194da136ca48d44616a6: [[Pasted Image 20230831191249_124.png]]
1469ca617e5cf5b55257bc845dbeebe82fbe8b40: [[Pasted Image 20230831191801_829.png]]
e819e16ac83f11b142ee859db0a01db11de71970: [[Pasted Image 20230831192059_469.png]]
759de97f120d05765d1a49ae4a5ba6fd0203d0db: [[Pasted Image 20230831192319_052.png]]
2b77fbeabf3a56eaff0da1264eacff45118a5a5f: [[Pasted Image 20230901150955_847.png]]
ebd64853de77c0d7796a06e600c3eb568fa003c8: [[Pasted Image 20230901154212_003.png]]
3541300b2dbb9244501297335f434a757747f70a: [[Pasted image 20230628233419.png]]
a613079fedc0e3ede8bc2ebb3a84efd49a8c7d9b: [[Pasted Image 20230901160446_171.png]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.9.18",
	"elements": [
		{
			"type": "rectangle",
			"version": 76,
			"versionNonce": 1045223330,
			"isDeleted": false,
			"id": "sBS7rS0Rk4aj3-qvxtuUo",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -124.13624954223633,
			"y": -159.25635528564453,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 117,
			"height": 77,
			"seed": 701537210,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "6MYYHsQ9"
				},
				{
					"id": "Y4yrgaAqTuT1WgsVC675X",
					"type": "arrow"
				},
				{
					"id": "XhEBtzN1-ZXIp8fLwyoAw",
					"type": "arrow"
				},
				{
					"id": "h5bAaNe2fUIJNhaIFsjMt",
					"type": "arrow"
				},
				{
					"id": "GgjyNIzY13dUTdHHEKPUK",
					"type": "arrow"
				},
				{
					"id": "1zSJSVm4na2xlYGnaot8p",
					"type": "arrow"
				}
			],
			"updated": 1693583097012,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 7,
			"versionNonce": 994536318,
			"isDeleted": false,
			"id": "6MYYHsQ9",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -90.64623641967773,
			"y": -133.25635528564453,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 50.01997375488281,
			"height": 25,
			"seed": 692398758,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693583097012,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "UNIX",
			"rawText": "UNIX",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "sBS7rS0Rk4aj3-qvxtuUo",
			"originalText": "UNIX",
			"lineHeight": 1.25,
			"baseline": 18
		},
		{
			"type": "image",
			"version": 160,
			"versionNonce": 265655138,
			"isDeleted": false,
			"id": "va53xekOBDr_MIYyFVoSG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -395.8327628242197,
			"y": -727.6543438879007,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 462.6953684322521,
			"height": 391.9777357024319,
			"seed": 29630438,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Y4yrgaAqTuT1WgsVC675X",
					"type": "arrow"
				}
			],
			"updated": 1693583097012,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "ec76cc75119cb360935bc19a2dbcbb971fb6d22c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 298,
			"versionNonce": 814304190,
			"isDeleted": false,
			"id": "Y4yrgaAqTuT1WgsVC675X",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -73.27827409682934,
			"y": -160.25635528564453,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 48.255860285616535,
			"height": 169.74187588961348,
			"seed": 1301207014,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097012,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "sBS7rS0Rk4aj3-qvxtuUo",
				"gap": 1,
				"focus": 0.0516582790749671
			},
			"endBinding": {
				"elementId": "va53xekOBDr_MIYyFVoSG",
				"gap": 5.678377010210795,
				"focus": 0.05009650669428144
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-48.255860285616535,
					-169.74187588961348
				]
			]
		},
		{
			"type": "image",
			"version": 42,
			"versionNonce": 1884346146,
			"isDeleted": false,
			"id": "f3wRC-_PXpQ7-AQwQbnt3",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 204.9097503246394,
			"y": -211.76045743782288,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 658,
			"height": 288,
			"seed": 194369254,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "XhEBtzN1-ZXIp8fLwyoAw",
					"type": "arrow"
				}
			],
			"updated": 1693583097012,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "3142bca187c4563fc2d7bf5c7afc60beb148687e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 196,
			"versionNonce": 455418878,
			"isDeleted": false,
			"id": "XhEBtzN1-ZXIp8fLwyoAw",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -4.342736875819696,
			"y": -132.89485066738442,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 208.00242229119692,
			"height": 49.4149869009466,
			"seed": 1499568634,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097012,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "sBS7rS0Rk4aj3-qvxtuUo",
				"gap": 2.793512666416632,
				"focus": -0.5095624199587158
			},
			"endBinding": {
				"elementId": "f3wRC-_PXpQ7-AQwQbnt3",
				"gap": 1.2500649092621643,
				"focus": -0.2823990925598365
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					208.00242229119692,
					49.4149869009466
				]
			]
		},
		{
			"type": "image",
			"version": 68,
			"versionNonce": 1882039010,
			"isDeleted": false,
			"id": "T5fgAD3kTk9P1z8u04eIm",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 966.7951587199555,
			"y": -279.5533822288462,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 658,
			"height": 364,
			"seed": 1349502650,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "p6He2p7YYjO5MWzrYIRZ7",
					"type": "arrow"
				}
			],
			"updated": 1693583097012,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "254d8736b501d26d758cc3c205a1da5a90d3edc7",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 50,
			"versionNonce": 756806718,
			"isDeleted": false,
			"id": "p6He2p7YYjO5MWzrYIRZ7",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 862.6262455249558,
			"y": -76.93186193214507,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 98.82977371016409,
			"height": 52.86246734720959,
			"seed": 280970598,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097012,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "T5fgAD3kTk9P1z8u04eIm",
				"focus": 0.5896292326602194,
				"gap": 5.339139484835528
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					98.82977371016409,
					-52.86246734720959
				]
			]
		},
		{
			"type": "image",
			"version": 83,
			"versionNonce": 972748450,
			"isDeleted": false,
			"id": "ZB86g9lkZzi4weeFpfv-g",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -896.4049652846702,
			"y": 5.301006636998579,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 672,
			"height": 490,
			"seed": 335151290,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "h5bAaNe2fUIJNhaIFsjMt",
					"type": "arrow"
				}
			],
			"updated": 1693583097012,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "9a251f55ddb78daaa7c5f6bc51e72f4a35cf1629",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 240,
			"versionNonce": 810466430,
			"isDeleted": false,
			"id": "h5bAaNe2fUIJNhaIFsjMt",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -125.13624954223633,
			"y": -113.16191345940379,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 316.5211220804346,
			"height": 109.33131723342154,
			"seed": 1262744870,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097012,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "sBS7rS0Rk4aj3-qvxtuUo",
				"gap": 1,
				"focus": 0.22072083277473792
			},
			"endBinding": {
				"elementId": "ZB86g9lkZzi4weeFpfv-g",
				"gap": 9.131602862980856,
				"focus": -0.5902469373088
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-316.5211220804346,
					109.33131723342154
				]
			]
		},
		{
			"type": "image",
			"version": 112,
			"versionNonce": 1315426914,
			"isDeleted": false,
			"id": "tNAyGnOvaEDUz6mBNmEvC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 108.62401350009964,
			"y": 132.41318686947824,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 656.7202508655768,
			"height": 728.5191121118133,
			"seed": 1503004538,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "UErj643S4w77xbYSwwDHG",
					"type": "arrow"
				}
			],
			"updated": 1693583097012,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "0f32f4416cd7b3d0f13373e5fb9f14eca26eed75",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 111,
			"versionNonce": 176061630,
			"isDeleted": false,
			"id": "UErj643S4w77xbYSwwDHG",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -11.825233782180135,
			"y": -90.97960191012248,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 188.17789581615068,
			"height": 221.79098779103555,
			"seed": 2029828602,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "tNAyGnOvaEDUz6mBNmEvC",
				"focus": 0.07810058769936516,
				"gap": 1.6018009885651736
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					188.17789581615068,
					221.79098779103555
				]
			]
		},
		{
			"type": "image",
			"version": 115,
			"versionNonce": 1078146594,
			"isDeleted": false,
			"id": "wDknedoq9YVCUt52uP2jN",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 837.9389496133472,
			"y": 658.7196467190688,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 660,
			"height": 203,
			"seed": 1215994726,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "SnR8f7a7HlWN-CBR0rOA4",
					"type": "arrow"
				},
				{
					"id": "jEHDl82g664qFqOuNk1F_",
					"type": "arrow"
				}
			],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "7994e852dcf8225da180fa089d61b304c277c0cb",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 101,
			"versionNonce": 1095513342,
			"isDeleted": false,
			"id": "SnR8f7a7HlWN-CBR0rOA4",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 664.6834497320756,
			"y": 502.70621593779265,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 310.44578143482045,
			"height": 154.33789827834357,
			"seed": 2112702950,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "wDknedoq9YVCUt52uP2jN",
				"focus": 0.027565669222730307,
				"gap": 1.6755325029325832
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					310.44578143482045,
					154.33789827834357
				]
			]
		},
		{
			"type": "image",
			"version": 136,
			"versionNonce": 1887183330,
			"isDeleted": false,
			"id": "gAdMNrF6TTfHJ_OorfTpu",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 657.9516035432734,
			"y": 961.4221791435093,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 794.656370346375,
			"height": 352.7792674416483,
			"seed": 1466104506,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "jEHDl82g664qFqOuNk1F_",
					"type": "arrow"
				}
			],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "0219c81f373dee340b030ad957f77dbb09bf88f7",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 250,
			"versionNonce": 2117657918,
			"isDeleted": false,
			"id": "jEHDl82g664qFqOuNk1F_",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1087.8382624322999,
			"y": 862.7196467190688,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 29.885374289583524,
			"height": 94.92079006361337,
			"seed": 1629234150,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "wDknedoq9YVCUt52uP2jN",
				"focus": 0.31084116950844426,
				"gap": 1
			},
			"endBinding": {
				"elementId": "gAdMNrF6TTfHJ_OorfTpu",
				"focus": 0.2631475880924301,
				"gap": 3.7817423608270815
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					29.885374289583524,
					94.92079006361337
				]
			]
		},
		{
			"type": "image",
			"version": 31,
			"versionNonce": 1243714978,
			"isDeleted": false,
			"id": "TYibSpozxR83JulzCr2gq",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1189.7304151976948,
			"y": -655.2866748686331,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 689,
			"height": 501,
			"seed": 1066237606,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "SRutYN89Cy7CsTxR2QsfZ",
					"type": "arrow"
				},
				{
					"id": "Lu8-9N6MwXrWMGxJHorLZ",
					"type": "arrow"
				},
				{
					"id": "DSRHdBQGidfoQb2Re9b0u",
					"type": "arrow"
				},
				{
					"id": "p7iTx9QgJBrim5MtkHnDp",
					"type": "arrow"
				}
			],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "07f4bcbdd837c51d7eee0bf24ddd020ee7eb0123",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 51,
			"versionNonce": 312839550,
			"isDeleted": false,
			"id": "SRutYN89Cy7CsTxR2QsfZ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -119.38006231854638,
			"y": -154.07810217123335,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 374.7147806002122,
			"height": 129.76497934368103,
			"seed": 1743797946,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "TYibSpozxR83JulzCr2gq",
				"focus": -0.001773458029427869,
				"gap": 6.635572278936252
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-374.7147806002122,
					-129.76497934368103
				]
			]
		},
		{
			"type": "image",
			"version": 184,
			"versionNonce": 2120388962,
			"isDeleted": false,
			"id": "LJi5TYyR1uIVUVdcBegIE",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1766.4340731514585,
			"y": 7.469410670638126,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 816.7216461222489,
			"height": 391.32130670317827,
			"seed": 1965112378,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Lu8-9N6MwXrWMGxJHorLZ",
					"type": "arrow"
				}
			],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "d3e54c9e92d39f6cbbb61da9b3c8e0e5aa52852a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 262,
			"versionNonce": 2077437374,
			"isDeleted": false,
			"id": "Lu8-9N6MwXrWMGxJHorLZ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -897.2767677722567,
			"y": -147.31934686325104,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 183.41187081214355,
			"height": 153.28959810090657,
			"seed": 606278202,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "TYibSpozxR83JulzCr2gq",
				"focus": -0.39739981169669986,
				"gap": 6.967328005382058
			},
			"endBinding": {
				"elementId": "LJi5TYyR1uIVUVdcBegIE",
				"focus": 0.06456610764110014,
				"gap": 1.4991594329825944
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-183.41187081214355,
					153.28959810090657
				]
			]
		},
		{
			"type": "image",
			"version": 66,
			"versionNonce": 1083053346,
			"isDeleted": false,
			"id": "IUK1g8v-Q19uscOIIsXL5",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2067.682945188709,
			"y": -676.4501889510286,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 757.560112243259,
			"height": 521.1919024949723,
			"seed": 656567226,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "DSRHdBQGidfoQb2Re9b0u",
					"type": "arrow"
				},
				{
					"id": "zSCrpfE4e07gLrKkVemgK",
					"type": "arrow"
				},
				{
					"id": "3eun4n3-aAJhEAhmUwnN0",
					"type": "arrow"
				},
				{
					"id": "uK9TJmzNJRR_TzPSSIukX",
					"type": "arrow"
				},
				{
					"id": "T_MGw8jW6FRBxwwQCpgcf",
					"type": "arrow"
				},
				{
					"id": "8XvvbvQUSSKhTAZoLCQ1z",
					"type": "arrow"
				},
				{
					"id": "WsiIDngH3hrtqfobGpA5J",
					"type": "arrow"
				}
			],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "10f2351f5de258d9cae77b77db77e65f76f424ad",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 51,
			"versionNonce": 1726137854,
			"isDeleted": false,
			"id": "DSRHdBQGidfoQb2Re9b0u",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1191.3656450286544,
			"y": -432.5750054333075,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 118.10074338979007,
			"height": 8.748187543228482,
			"seed": 192592294,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "TYibSpozxR83JulzCr2gq",
				"focus": 0.19356650570061676,
				"gap": 1.635229830959588
			},
			"endBinding": {
				"elementId": "IUK1g8v-Q19uscOIIsXL5",
				"focus": 0.06975063237559907,
				"gap": 1
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-118.10074338979007,
					8.748187543228482
				]
			]
		},
		{
			"type": "image",
			"version": 200,
			"versionNonce": 34808034,
			"isDeleted": false,
			"id": "699tPIpCYInr6JJVPv3k0",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2987.313556116794,
			"y": -1032.0224298539656,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 735.3947640927788,
			"height": 925.7706275783354,
			"seed": 805839354,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "zSCrpfE4e07gLrKkVemgK",
					"type": "arrow"
				},
				{
					"id": "3_1p0VTkuK49tF_mJ1yfT",
					"type": "arrow"
				}
			],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "6cc9c91c142b06a505b2455e6227488d0d6c362e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 369,
			"versionNonce": 886396478,
			"isDeleted": false,
			"id": "zSCrpfE4e07gLrKkVemgK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2070.822134465089,
			"y": -624.3664292798595,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 176.476967021179,
			"height": 37.794254386157036,
			"seed": 1434779238,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097013,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "IUK1g8v-Q19uscOIIsXL5",
				"focus": 0.3807116088717874,
				"gap": 3.139189276380421
			},
			"endBinding": {
				"elementId": "699tPIpCYInr6JJVPv3k0",
				"focus": -0.31896031175910833,
				"gap": 4.619690537747147
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-176.476967021179,
					-37.794254386157036
				]
			]
		},
		{
			"type": "image",
			"version": 310,
			"versionNonce": 780186786,
			"isDeleted": false,
			"id": "FeUu2asg1lm9m8xz3xHT3",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -3842.146932099234,
			"y": -1566.0054074283198,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 676.2715008240893,
			"height": 895.6317186546879,
			"seed": 1990975910,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "_KYRAQQRGYkCbINTHerXS",
					"type": "arrow"
				},
				{
					"id": "3_1p0VTkuK49tF_mJ1yfT",
					"type": "arrow"
				}
			],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "e8fb4d4c2ec1acc61a2ca86350e238aa91069c2e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 126,
			"versionNonce": 2123095678,
			"isDeleted": false,
			"id": "3_1p0VTkuK49tF_mJ1yfT",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2988.401048877878,
			"y": -487.17693826555944,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 169.2088308342868,
			"height": 515.3348968598281,
			"seed": 22689018,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "699tPIpCYInr6JJVPv3k0",
				"focus": -0.7614163096703975,
				"gap": 1.0874927610841496
			},
			"endBinding": {
				"elementId": "FeUu2asg1lm9m8xz3xHT3",
				"focus": -0.6356859019258079,
				"gap": 8.265551562979908
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-169.2088308342868,
					-515.3348968598281
				]
			]
		},
		{
			"type": "image",
			"version": 460,
			"versionNonce": 1736822882,
			"isDeleted": false,
			"id": "O7l9TGiHjm8Xn8LpgDPZi",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -4878.0153562745145,
			"y": -1374.0285816508722,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 635.6657340516302,
			"height": 869.220561814101,
			"seed": 2048765818,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "_KYRAQQRGYkCbINTHerXS",
					"type": "arrow"
				},
				{
					"id": "_DJOjhXH9oE43iYANTcvw",
					"type": "arrow"
				}
			],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "00b359e132da19452a54ac7aa48015df234d33d4",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 888,
			"versionNonce": 415719102,
			"isDeleted": false,
			"id": "_KYRAQQRGYkCbINTHerXS",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -3845.8976859532836,
			"y": -1378.4933360745995,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 388.9660011418805,
			"height": 401.1836678440375,
			"seed": 245618746,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "FeUu2asg1lm9m8xz3xHT3",
				"focus": 0.7690123359442993,
				"gap": 3.750753854049435
			},
			"endBinding": {
				"elementId": "O7l9TGiHjm8Xn8LpgDPZi",
				"focus": 0.3903929248914648,
				"gap": 7.48593512772004
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-388.9660011418805,
					401.1836678440375
				]
			]
		},
		{
			"type": "image",
			"version": 247,
			"versionNonce": 1089565730,
			"isDeleted": false,
			"id": "QnfKJE6cEObJgV9zOxVvK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -5001.632858954919,
			"y": -400.68659450018583,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 910.9050046882388,
			"height": 1250.2905790156312,
			"seed": 1699017766,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "_DJOjhXH9oE43iYANTcvw",
					"type": "arrow"
				},
				{
					"id": "v7Bne1O5ZiIuG2FsRYwBN",
					"type": "arrow"
				}
			],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "db990272c305e4645301c1bcf93ebb6fe77ae827",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 101,
			"versionNonce": 405329662,
			"isDeleted": false,
			"id": "_DJOjhXH9oE43iYANTcvw",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -4542.6806935827635,
			"y": -500.6494473710354,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.07489841109327244,
			"height": 91.49440603160338,
			"seed": 1143259770,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "O7l9TGiHjm8Xn8LpgDPZi",
				"focus": -0.05766466159056271,
				"gap": 4.158572465735745
			},
			"endBinding": {
				"elementId": "QnfKJE6cEObJgV9zOxVvK",
				"focus": 0.008977118624650348,
				"gap": 8.468446839246326
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					0.07489841109327244,
					91.49440603160338
				]
			]
		},
		{
			"type": "image",
			"version": 160,
			"versionNonce": 2092081122,
			"isDeleted": false,
			"id": "w2EtDnH-DeHgph1kOXnDl",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -5169.108205159796,
			"y": 944.9531439695423,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1265.9078228029184,
			"height": 230.37660745861936,
			"seed": 1684670566,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "v7Bne1O5ZiIuG2FsRYwBN",
					"type": "arrow"
				}
			],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "b53395bdc8f67fb1d13c011f2700b7f99e96e047",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 64,
			"versionNonce": 1429292862,
			"isDeleted": false,
			"id": "v7Bne1O5ZiIuG2FsRYwBN",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -4541.66421892616,
			"y": 855.2724877451326,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 88.68065622440986,
			"seed": 1744605286,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "QnfKJE6cEObJgV9zOxVvK",
				"focus": -0.00991571604370669,
				"gap": 5.668503229687417
			},
			"endBinding": {
				"elementId": "w2EtDnH-DeHgph1kOXnDl",
				"focus": -0.008705096956623675,
				"gap": 1
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					0,
					88.68065622440986
				]
			]
		},
		{
			"type": "image",
			"version": 249,
			"versionNonce": 1188582306,
			"isDeleted": false,
			"id": "iDByhbB9KbdhGDikMdEaI",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1360.5751615075637,
			"y": -2238.8284083924445,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 978.3614632770926,
			"height": 1192.5301418054114,
			"seed": 1229152422,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "3eun4n3-aAJhEAhmUwnN0",
					"type": "arrow"
				}
			],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "f5a1ef425973e6688c1dfa441d233858ff34a01f",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 126,
			"versionNonce": 1883352958,
			"isDeleted": false,
			"id": "3eun4n3-aAJhEAhmUwnN0",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1510.112488841176,
			"y": -687.3876149984292,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 174.9055122576915,
			"height": 340.351451026065,
			"seed": 62842918,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "IUK1g8v-Q19uscOIIsXL5",
				"focus": 0.075731549490119,
				"gap": 10.93742604740055
			},
			"endBinding": {
				"elementId": "iDByhbB9KbdhGDikMdEaI",
				"focus": 0.1858426901586696,
				"gap": 18.559200562539047
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					174.9055122576915,
					-340.351451026065
				]
			]
		},
		{
			"type": "image",
			"version": 194,
			"versionNonce": 1905364834,
			"isDeleted": false,
			"id": "g8jCshx5JeKTDMq7tw2ru",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2479.3835925091917,
			"y": -2214.9963546260697,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1054.955124222889,
			"height": 715.7412579132783,
			"seed": 834402470,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "uK9TJmzNJRR_TzPSSIukX",
					"type": "arrow"
				}
			],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "0883d858fe8a24ba992d3328ebe319dacc950904",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 183,
			"versionNonce": 1436225470,
			"isDeleted": false,
			"id": "uK9TJmzNJRR_TzPSSIukX",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1576.6835234368773,
			"y": -680.3495313961973,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 159.4858385914804,
			"height": 816.6511387550345,
			"seed": 1093863674,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "IUK1g8v-Q19uscOIIsXL5",
				"focus": 0.3813380559972349,
				"gap": 3.8993424451687133
			},
			"endBinding": {
				"elementId": "g8jCshx5JeKTDMq7tw2ru",
				"focus": -0.24341308644891776,
				"gap": 2.2544265615595123
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-159.4858385914804,
					-816.6511387550345
				]
			]
		},
		{
			"type": "image",
			"version": 135,
			"versionNonce": 825053986,
			"isDeleted": false,
			"id": "ykCRhgVBJ0uhguyCTaq9n",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -3634.961429161362,
			"y": 5.213050339369033,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1087.025252367179,
			"height": 521.4783305274981,
			"seed": 1659590690,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "T_MGw8jW6FRBxwwQCpgcf",
					"type": "arrow"
				}
			],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "f44b51176322ee4865adfbf8a370ceae142a6a71",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 206,
			"versionNonce": 1096706046,
			"isDeleted": false,
			"id": "T_MGw8jW6FRBxwwQCpgcf",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2002.0143220799314,
			"y": -148.38566137451514,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 543.0144094098309,
			"height": 282.35782929780504,
			"seed": 1631731746,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097014,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "IUK1g8v-Q19uscOIIsXL5",
				"focus": -0.22954878216635063,
				"gap": 6.872625081541173
			},
			"endBinding": {
				"elementId": "ykCRhgVBJ0uhguyCTaq9n",
				"focus": 0.28001650654984245,
				"gap": 2.907445304420321
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-543.0144094098309,
					282.35782929780504
				]
			]
		},
		{
			"type": "image",
			"version": 93,
			"versionNonce": 1478139618,
			"isDeleted": false,
			"id": "YNI9AsMVZ5wAKhSHmNvpg",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -3889.8407648065463,
			"y": -2112.6786885454862,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1290.0502122651665,
			"height": 314.3269552727309,
			"seed": 1587064446,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "8XvvbvQUSSKhTAZoLCQ1z",
					"type": "arrow"
				},
				{
					"id": "RJqZ7Wjoti7aqN9JSyJbt",
					"type": "arrow"
				}
			],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "3a5ee61a851138c48ae380b0a9bfe2b5aa938470",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 64,
			"versionNonce": 1133295678,
			"isDeleted": false,
			"id": "8XvvbvQUSSKhTAZoLCQ1z",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1758.607777027894,
			"y": -683.0585185753255,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1261.1751691366767,
			"height": 1114.3534318344548,
			"seed": 1458064702,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "IUK1g8v-Q19uscOIIsXL5",
				"focus": 0.34540770265142223,
				"gap": 6.608329624296857
			},
			"endBinding": {
				"elementId": "YNI9AsMVZ5wAKhSHmNvpg",
				"focus": -0.05601991136611808,
				"gap": 1
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-1261.1751691366767,
					-1114.3534318344548
				]
			]
		},
		{
			"type": "image",
			"version": 78,
			"versionNonce": 317223586,
			"isDeleted": false,
			"id": "dBSRsIdamMNJ8G1P0Liyx",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -3937.9331855341165,
			"y": -2934.776204880393,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1389.2204372240187,
			"height": 698.0545668034739,
			"seed": 847494946,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "RJqZ7Wjoti7aqN9JSyJbt",
					"type": "arrow"
				}
			],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "fb96f07b3714861e331354f76df7276eaf972850",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 37,
			"versionNonce": 1141309566,
			"isDeleted": false,
			"id": "RJqZ7Wjoti7aqN9JSyJbt",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -3317.2539927976177,
			"y": -2113.1571999075804,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2.4437575259530604,
			"height": 109.69428862479481,
			"seed": 140765374,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "YNI9AsMVZ5wAKhSHmNvpg",
				"focus": -0.11711206825719163,
				"gap": 1
			},
			"endBinding": {
				"elementId": "dBSRsIdamMNJ8G1P0Liyx",
				"focus": 0.09026759584653687,
				"gap": 13.870149544543892
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					2.4437575259530604,
					-109.69428862479481
				]
			]
		},
		{
			"type": "image",
			"version": 82,
			"versionNonce": 608554594,
			"isDeleted": false,
			"id": "3vcJQTFgJj2-ftCKxvOIY",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2497.352316765954,
			"y": 500.7045924514889,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 962.1899272666799,
			"height": 805.0004837033114,
			"seed": 736505406,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "WsiIDngH3hrtqfobGpA5J",
					"type": "arrow"
				},
				{
					"id": "KcCDKWfsL7N3JCyPg3LiV",
					"type": "arrow"
				},
				{
					"id": "F8Cubuehjcl7l5eWmcc7p",
					"type": "arrow"
				}
			],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "c43b42c27dc39c0f28774df4e371df42d98afd45",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 89,
			"versionNonce": 109985982,
			"isDeleted": false,
			"id": "WsiIDngH3hrtqfobGpA5J",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1743.2091603282188,
			"y": -153.8427070413885,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 264.3183842930098,
			"height": 654.1418739751119,
			"seed": 759505762,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "IUK1g8v-Q19uscOIIsXL5",
				"focus": -0.10652075901178154,
				"gap": 1.4155794146678318
			},
			"endBinding": {
				"elementId": "3vcJQTFgJj2-ftCKxvOIY",
				"focus": -0.23934129401430543,
				"gap": 1
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-264.3183842930098,
					654.1418739751119
				]
			]
		},
		{
			"type": "image",
			"version": 120,
			"versionNonce": 553759266,
			"isDeleted": false,
			"id": "56xlTbZthQ87fJUAImcp3",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2602.4809096106696,
			"y": 1395.4244461902842,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1174.1842417998612,
			"height": 1348.5496742314363,
			"seed": 1255018786,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "KcCDKWfsL7N3JCyPg3LiV",
					"type": "arrow"
				}
			],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "554e0421a8b658a2e32d0696df884ead35c79327",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 79,
			"versionNonce": 784562430,
			"isDeleted": false,
			"id": "KcCDKWfsL7N3JCyPg3LiV",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2040.994264153353,
			"y": 1307.2593077225315,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.336857665959542,
			"height": 87.72991375297852,
			"seed": 1910927742,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "3vcJQTFgJj2-ftCKxvOIY",
				"focus": 0.018872655162410032,
				"gap": 1.5542315677312217
			},
			"endBinding": {
				"elementId": "56xlTbZthQ87fJUAImcp3",
				"focus": -0.0891168309034297,
				"gap": 1
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-3.336857665959542,
					87.72991375297852
				]
			]
		},
		{
			"type": "image",
			"version": 158,
			"versionNonce": 738926050,
			"isDeleted": false,
			"id": "tF0kj8G9vsSp1TUDqXvdi",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1346.6415848207164,
			"y": 610.4130749941123,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 927.7607904686646,
			"height": 1175.7947977164097,
			"seed": 465050942,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "F8Cubuehjcl7l5eWmcc7p",
					"type": "arrow"
				}
			],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "8f07c909db308ffadbaf2f3becda9ad52b21f9be",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 331,
			"versionNonce": 1143449918,
			"isDeleted": false,
			"id": "F8Cubuehjcl7l5eWmcc7p",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1525.3908690390806,
			"y": 745.3408289892604,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 173.55365928216565,
			"height": 90.58351181757575,
			"seed": 1704059902,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "3vcJQTFgJj2-ftCKxvOIY",
				"gap": 9.771520460193756,
				"focus": -0.6332408789444304
			},
			"endBinding": {
				"elementId": "tF0kj8G9vsSp1TUDqXvdi",
				"gap": 5.195624936198556,
				"focus": 0.14163589805206658
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					173.55365928216565,
					90.58351181757575
				]
			]
		},
		{
			"type": "image",
			"version": 180,
			"versionNonce": 846270882,
			"isDeleted": false,
			"id": "Fz_wnR2n5CPGPQHpvSUaF",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -237.04735038746998,
			"y": -2004.844102422846,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 737.0966090439234,
			"height": 1060.2496109212175,
			"seed": 1399371042,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "p7iTx9QgJBrim5MtkHnDp",
					"type": "arrow"
				},
				{
					"id": "6vQ4GRb84nCIC5cMFBzOG",
					"type": "arrow"
				}
			],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "c36fae0dd9b8000ae8ea7b1c47e58a5fdb0a52e9",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 171,
			"versionNonce": 907792766,
			"isDeleted": false,
			"id": "p7iTx9QgJBrim5MtkHnDp",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -986.7561233860558,
			"y": -664.3809442657714,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 741.3966519823098,
			"height": 326.2986121385434,
			"seed": 1401756350,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "TYibSpozxR83JulzCr2gq",
				"focus": -0.8004634821374462,
				"gap": 9.094269397138305
			},
			"endBinding": {
				"elementId": "Fz_wnR2n5CPGPQHpvSUaF",
				"focus": -0.45957765244993126,
				"gap": 8.31212101627608
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					741.3966519823098,
					-326.2986121385434
				]
			]
		},
		{
			"type": "image",
			"version": 309,
			"versionNonce": 660770146,
			"isDeleted": false,
			"id": "_RtYLDppX4FyyYn1L8gzg",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -644.3384959929308,
			"y": -2657.108385353336,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1248.4936643344327,
			"height": 306.5497836535438,
			"seed": 1828514850,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "6vQ4GRb84nCIC5cMFBzOG",
					"type": "arrow"
				}
			],
			"updated": 1693583097015,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "9ca6b0593fc14b58bfb24572f880a0f98fd19d67",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 501,
			"versionNonce": 1608577470,
			"isDeleted": false,
			"id": "6vQ4GRb84nCIC5cMFBzOG",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 97.35205296766514,
			"y": -2017.1774106323,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 147.43548682158945,
			"height": 316.63103170919067,
			"seed": 704765374,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Fz_wnR2n5CPGPQHpvSUaF",
				"focus": 0.35439196296416714,
				"gap": 12.333308209454117
			},
			"endBinding": {
				"elementId": "_RtYLDppX4FyyYn1L8gzg",
				"focus": 0.15692808860406998,
				"gap": 16.75015935830129
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-147.43548682158945,
					-316.63103170919067
				]
			]
		},
		{
			"type": "image",
			"version": 112,
			"versionNonce": 1076793634,
			"isDeleted": false,
			"id": "CO8ImJugdOyn6anM8zR2H",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 269.48269341712455,
			"y": -788.3610632638174,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 468.38872437946804,
			"height": 529.8647444542733,
			"seed": 1961026558,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "GgjyNIzY13dUTdHHEKPUK",
					"type": "arrow"
				},
				{
					"id": "akYygFE_XqcBn8xJgxBxd",
					"type": "arrow"
				},
				{
					"id": "3uphtt1sOucM0fWULkfC_",
					"type": "arrow"
				}
			],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "4348cdc5957c17e5ff53f72b2bd0c7ee4b05dcf1",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 150,
			"versionNonce": 211290622,
			"isDeleted": false,
			"id": "GgjyNIzY13dUTdHHEKPUK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -25.99710737217559,
			"y": -164.03864356608415,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 287.49559321210086,
			"height": 262.177508057453,
			"seed": 834535742,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "sBS7rS0Rk4aj3-qvxtuUo",
				"gap": 4.782288280439616,
				"focus": -0.07767092258334966
			},
			"endBinding": {
				"elementId": "CO8ImJugdOyn6anM8zR2H",
				"gap": 7.9842075771992995,
				"focus": 0.2583868084113937
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					287.49559321210086,
					-262.177508057453
				]
			]
		},
		{
			"type": "image",
			"version": 77,
			"versionNonce": 809770210,
			"isDeleted": false,
			"id": "B4v5NdLTmiJhEcI4F1zgP",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 807.0903303357484,
			"y": -1019.4202735068482,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 733.3609608706018,
			"height": 641.6908407617767,
			"seed": 876257150,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "akYygFE_XqcBn8xJgxBxd",
					"type": "arrow"
				},
				{
					"id": "DcwVG60_QCTSe0Dv3x6Nc",
					"type": "arrow"
				}
			],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "358d82e3c4e8ac84bd07c8ea06f27199eb3e405a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 91,
			"versionNonce": 2067929662,
			"isDeleted": false,
			"id": "akYygFE_XqcBn8xJgxBxd",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 743.3780459673725,
			"y": -674.6715277660704,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 59.932356457128094,
			"height": 44.912194213851535,
			"seed": 863359586,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "CO8ImJugdOyn6anM8zR2H",
				"gap": 5.506628170779777,
				"focus": 0.05924696350894226
			},
			"endBinding": {
				"elementId": "B4v5NdLTmiJhEcI4F1zgP",
				"gap": 3.7799279112475688,
				"focus": 0.5013608059485343
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					59.932356457128094,
					-44.912194213851535
				]
			]
		},
		{
			"type": "image",
			"version": 103,
			"versionNonce": 1697788066,
			"isDeleted": false,
			"id": "mAt7AGvYIFfvsPKcUf467",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1654.8837036015723,
			"y": -1460.7018360287827,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 811.2138223361724,
			"height": 1100.3429850832806,
			"seed": 105846242,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "DcwVG60_QCTSe0Dv3x6Nc",
					"type": "arrow"
				},
				{
					"id": "AokBIUPjlq71hCHX7Nhvh",
					"type": "arrow"
				},
				{
					"id": "teBx_ybotKnp_qTsB6Wwz",
					"type": "arrow"
				}
			],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "993a144126a141df530b2b68fbbbe6af2f2d7b29",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 40,
			"versionNonce": 1656758910,
			"isDeleted": false,
			"id": "DcwVG60_QCTSe0Dv3x6Nc",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1541.5520929212605,
			"y": -809.2626778482406,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 108.03524996842543,
			"height": 71.52787305260313,
			"seed": 901474174,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "B4v5NdLTmiJhEcI4F1zgP",
				"focus": 0.23564313634582154,
				"gap": 1.1008017149105171
			},
			"endBinding": {
				"elementId": "mAt7AGvYIFfvsPKcUf467",
				"focus": 0.29596446909394897,
				"gap": 5.296360711886223
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					108.03524996842543,
					-71.52787305260313
				]
			]
		},
		{
			"type": "image",
			"version": 42,
			"versionNonce": 1118293090,
			"isDeleted": false,
			"id": "J9LUTHLoLuTY6lf5UpMmA",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2708.691612788099,
			"y": -1303.167965935902,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 902.5754830369741,
			"height": 641.5455062727168,
			"seed": 1638944098,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "AokBIUPjlq71hCHX7Nhvh",
					"type": "arrow"
				}
			],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "398250e87eb98abc2d7b05f2eec7647559cc843a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 56,
			"versionNonce": 1976771262,
			"isDeleted": false,
			"id": "AokBIUPjlq71hCHX7Nhvh",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2470.201641232335,
			"y": -1174.5488585463272,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 233.04971915558372,
			"height": 40.46782433649514,
			"seed": 1432670434,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mAt7AGvYIFfvsPKcUf467",
				"focus": -0.5400596721584734,
				"gap": 4.104115294590542
			},
			"endBinding": {
				"elementId": "J9LUTHLoLuTY6lf5UpMmA",
				"focus": 0.1813351722504102,
				"gap": 5.44025240018027
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					233.04971915558372,
					40.46782433649514
				]
			]
		},
		{
			"type": "image",
			"version": 95,
			"versionNonce": 1584656418,
			"isDeleted": false,
			"id": "aVN_hPqpwdmC1DhScRYPd",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2661.049865180773,
			"y": -580.6909250342044,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1089.27357795671,
			"height": 253.616461199301,
			"seed": 375411774,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "IUr3vJTuftECa5_Xye95e",
					"type": "arrow"
				},
				{
					"id": "mP4XPhrroF2JOKyx85x-R",
					"type": "arrow"
				}
			],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "e7a4241df5ba5480e231594974736f40218851eb",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 62,
			"versionNonce": 1729895166,
			"isDeleted": false,
			"id": "IUr3vJTuftECa5_Xye95e",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3159.4907920583446,
			"y": -665.1311700734055,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 19.117038587677598,
			"height": 82.01141034261968,
			"seed": 225880290,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "aVN_hPqpwdmC1DhScRYPd",
				"focus": 0.005305884900339007,
				"gap": 2.4288346965815037
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					19.117038587677598,
					82.01141034261968
				]
			]
		},
		{
			"type": "image",
			"version": 82,
			"versionNonce": 1015389154,
			"isDeleted": false,
			"id": "mn3Rop8tMZNBX4TRgbw4s",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2773.5653388595365,
			"y": -232.51652726758067,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 848.0312773717376,
			"height": 862.3561300300439,
			"seed": 1541707134,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "mP4XPhrroF2JOKyx85x-R",
					"type": "arrow"
				}
			],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "97d7103da9f6ba984e3d11ed0c363df34ec8e2c5",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 39,
			"versionNonce": 1830554430,
			"isDeleted": false,
			"id": "mP4XPhrroF2JOKyx85x-R",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3166.089253764414,
			"y": -325.81401311986986,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 23.71472062793964,
			"height": 91.08343869032024,
			"seed": 1976261758,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097016,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "aVN_hPqpwdmC1DhScRYPd",
				"focus": 0.1262725309194586,
				"gap": 1.2604507150334996
			},
			"endBinding": {
				"elementId": "mn3Rop8tMZNBX4TRgbw4s",
				"focus": 0.19590965486709935,
				"gap": 2.214047161969006
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					23.71472062793964,
					91.08343869032024
				]
			]
		},
		{
			"type": "image",
			"version": 59,
			"versionNonce": 183226274,
			"isDeleted": false,
			"id": "btZmZUutjQbZOz7biy4eL",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1735.9074575448951,
			"y": -21.987222567001368,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 932.8740515145565,
			"height": 351.9409518893467,
			"seed": 752159906,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "teBx_ybotKnp_qTsB6Wwz",
					"type": "arrow"
				},
				{
					"id": "tOIRODLH46AHXrAISlD-K",
					"type": "arrow"
				},
				{
					"id": "9WGYd08Enxk5Miavu74wb",
					"type": "arrow"
				}
			],
			"updated": 1693583097017,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "510b6336c846b72d20d7878ff271f15b6048ae4c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 91,
			"versionNonce": 1177809790,
			"isDeleted": false,
			"id": "teBx_ybotKnp_qTsB6Wwz",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2047.7787556964938,
			"y": -355.55927610672916,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 140.99989885549098,
			"height": 329.44345364143464,
			"seed": 109516898,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693583097017,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mAt7AGvYIFfvsPKcUf467",
				"focus": 0.3903372332513652,
				"gap": 4.799574838772969
			},
			"endBinding": {
				"elementId": "btZmZUutjQbZOz7biy4eL",
				"focus": 0.11724111897381775,
				"gap": 4.128599898293146
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					140.99989885549098,
					329.44345364143464
				]
			]
		},
		{
			"id": "N4ixpycSJ-mC-P7y-wHQ9",
			"type": "image",
			"x": 1544.357541413392,
			"y": 435.24766722718164,
			"width": 728.3321894209118,
			"height": 1033.085389600871,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1478684770,
			"version": 180,
			"versionNonce": 1574275938,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "tOIRODLH46AHXrAISlD-K",
					"type": "arrow"
				},
				{
					"id": "AKcO4al7sLLMmc8z6opMG",
					"type": "arrow"
				},
				{
					"id": "cfgrdvpC9IcaqDH4mgArK",
					"type": "arrow"
				}
			],
			"updated": 1693583097017,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "fd019b84cec5c412ab6a9fa2c834f857bad8d771",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "tOIRODLH46AHXrAISlD-K",
			"type": "arrow",
			"x": 2100.127781048343,
			"y": 331.41466204654836,
			"width": 32.88578130027827,
			"height": 100.54066694964177,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 602049378,
			"version": 119,
			"versionNonce": 1017435070,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097017,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-32.88578130027827,
					100.54066694964177
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "btZmZUutjQbZOz7biy4eL",
				"focus": 0.08823017304213888,
				"gap": 1.460932724203019
			},
			"endBinding": {
				"elementId": "N4ixpycSJ-mC-P7y-wHQ9",
				"focus": -0.021222431455780764,
				"gap": 3.2923382309913904
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "_fWmRN9P-xP4yJ09hj9NM",
			"type": "image",
			"x": 2723.927785277215,
			"y": 892.0007670648413,
			"width": 973.802138863129,
			"height": 1023.4859214581867,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1697018594,
			"version": 116,
			"versionNonce": 1804717858,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "9WGYd08Enxk5Miavu74wb",
					"type": "arrow"
				}
			],
			"updated": 1693583097017,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "2d9823f1b39bd3b7c5bd434608f5ed0ae2d4ee56",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "9WGYd08Enxk5Miavu74wb",
			"type": "arrow",
			"x": 2544.630835927974,
			"y": 332.2732754341271,
			"width": 388.4293172850216,
			"height": 557.8847982804895,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 897114594,
			"version": 185,
			"versionNonce": 714058750,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097017,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					388.4293172850216,
					557.8847982804895
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "btZmZUutjQbZOz7biy4eL",
				"gap": 2.3195461117816762,
				"focus": -0.37040366191883883
			},
			"endBinding": {
				"elementId": "_fWmRN9P-xP4yJ09hj9NM",
				"gap": 1.842693350224863,
				"focus": 0.09465939329676185
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "J_rwX2Wf7G9Fsn6w2q2iQ",
			"type": "image",
			"x": 706.4904583797397,
			"y": 1683.0687010205904,
			"width": 840.4415237666474,
			"height": 541.3324225134519,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 881921406,
			"version": 140,
			"versionNonce": 1217370850,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "cfgrdvpC9IcaqDH4mgArK",
					"type": "arrow"
				},
				{
					"id": "aHYIC6pTlufm3WJZqpPse",
					"type": "arrow"
				}
			],
			"updated": 1693583097017,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "da6d7680c1d7af21f37172b328852935e1dc2167",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "Do10efRIVP1H-E0-0gN-y",
			"type": "image",
			"x": 1652.830641390917,
			"y": 1655.1702279476458,
			"width": 952.9945283562978,
			"height": 756.316483104529,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 450729022,
			"version": 136,
			"versionNonce": 2113240126,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "AKcO4al7sLLMmc8z6opMG",
					"type": "arrow"
				}
			],
			"updated": 1693583097017,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "8c90f6ef403f9135afb1225879bbc8f09d6b77cb",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "AKcO4al7sLLMmc8z6opMG",
			"type": "arrow",
			"x": 1955.3174659807387,
			"y": 1471.6647261238218,
			"width": 143.93324385208462,
			"height": 179.69550865126075,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1328546914,
			"version": 40,
			"versionNonce": 593358498,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097017,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					143.93324385208462,
					179.69550865126075
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "N4ixpycSJ-mC-P7y-wHQ9",
				"focus": 0.4751422943703951,
				"gap": 3.3316692957691885
			},
			"endBinding": {
				"elementId": "Do10efRIVP1H-E0-0gN-y",
				"focus": 0.3539577878017843,
				"gap": 3.8099931725632814
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "cfgrdvpC9IcaqDH4mgArK",
			"type": "arrow",
			"x": 1739.0012608260492,
			"y": 1472.6690912177978,
			"width": 341.35536719616744,
			"height": 202.52120766734515,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 932713598,
			"version": 50,
			"versionNonce": 1018643582,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097017,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-341.35536719616744,
					202.52120766734515
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "N4ixpycSJ-mC-P7y-wHQ9",
				"focus": -0.5737171340017109,
				"gap": 4.336034389745237
			},
			"endBinding": {
				"elementId": "J_rwX2Wf7G9Fsn6w2q2iQ",
				"focus": -0.22655417297704078,
				"gap": 7.878402135447345
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "eCA7dzpo",
			"type": "text",
			"x": 221.94641580214642,
			"y": 2462.717732430397,
			"width": 1334.339599609375,
			"height": 135,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1434402274,
			"version": 149,
			"versionNonce": 11258466,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "aHYIC6pTlufm3WJZqpPse",
					"type": "arrow"
				}
			],
			"updated": 1693583097018,
			"link": null,
			"locked": false,
			"text": "la signal invece di segnalare e basta segnaliamo passando la lock, \ncosì che chi viene risvegliato ha già la lock, e non la deve riacquisire, \nsicuramente se gli passo la lock non potrà essere scavalcato da un altro.",
			"rawText": "la signal invece di segnalare e basta segnaliamo passando la lock, \ncosì che chi viene risvegliato ha già la lock, e non la deve riacquisire, \nsicuramente se gli passo la lock non potrà essere scavalcato da un altro.",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 122,
			"containerId": null,
			"originalText": "la signal invece di segnalare e basta segnaliamo passando la lock, \ncosì che chi viene risvegliato ha già la lock, e non la deve riacquisire, \nsicuramente se gli passo la lock non potrà essere scavalcato da un altro.",
			"lineHeight": 1.25
		},
		{
			"id": "aHYIC6pTlufm3WJZqpPse",
			"type": "arrow",
			"x": 950.6175836401818,
			"y": 2238.398755728431,
			"width": 73.9796442725152,
			"height": 220.2049007749556,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1046107390,
			"version": 37,
			"versionNonce": 144049342,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097018,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-73.9796442725152,
					220.2049007749556
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "J_rwX2Wf7G9Fsn6w2q2iQ",
				"focus": 0.15740577576382148,
				"gap": 13.997632194388757
			},
			"endBinding": {
				"elementId": "eCA7dzpo",
				"focus": -0.05296480828937681,
				"gap": 4.114075927010617
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "f5_9i_uRtbWAKmkNVORBd",
			"type": "image",
			"x": 572.2914204844761,
			"y": -2000.6410486861423,
			"width": 730.0292735435199,
			"height": 750.2277119419573,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 151955746,
			"version": 121,
			"versionNonce": 2001219106,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "3uphtt1sOucM0fWULkfC_",
					"type": "arrow"
				},
				{
					"id": "i8vGygleUbwU6lzZhPaOV",
					"type": "arrow"
				}
			],
			"updated": 1693583097018,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "5681d9b04b0506a8d45563628dac9abe2c2adf26",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "3uphtt1sOucM0fWULkfC_",
			"type": "arrow",
			"x": 454.0500513667779,
			"y": -798.779070116273,
			"width": 249.42803304134566,
			"height": 445.2900539338166,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 883726178,
			"version": 195,
			"versionNonce": 590527742,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097018,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					249.42803304134566,
					-445.2900539338166
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "CO8ImJugdOyn6anM8zR2H",
				"gap": 10.418006852455505,
				"focus": -0.5329486251143168
			},
			"endBinding": {
				"elementId": "f5_9i_uRtbWAKmkNVORBd",
				"gap": 6.344212694095404,
				"focus": 0.03504447238842902
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "9okUCD0N",
			"type": "text",
			"x": 588.4730295788286,
			"y": -1148.693766143094,
			"width": 48.02398681640625,
			"height": 45,
			"angle": 5.280197117783722,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 168133986,
			"version": 176,
			"versionNonce": 1814174178,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097018,
			"link": null,
			"locked": false,
			"text": "SO",
			"rawText": "SO",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 32,
			"containerId": null,
			"originalText": "SO",
			"lineHeight": 1.25
		},
		{
			"id": "YJ56e-w7FODgCK3V0INDz",
			"type": "image",
			"x": 1427.6423595098597,
			"y": -2483.475214563668,
			"width": 633.7764193834333,
			"height": 898.1517257548084,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 130639778,
			"version": 117,
			"versionNonce": 1913548094,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "i8vGygleUbwU6lzZhPaOV",
					"type": "arrow"
				},
				{
					"id": "Zse60mBZPeijsBEl9a9Cq",
					"type": "arrow"
				}
			],
			"updated": 1693583097018,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "791af62a020433b6da793fe87b4811b59bf57b2f",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "i8vGygleUbwU6lzZhPaOV",
			"type": "arrow",
			"x": 949.5343328112874,
			"y": -2003.1387938514283,
			"width": 471.8109369339402,
			"height": 118.48235326027066,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 543442530,
			"version": 76,
			"versionNonce": 1313377698,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097018,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					89.40523022105526,
					-92.46525126470601
				],
				[
					471.8109369339402,
					-118.48235326027066
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "f5_9i_uRtbWAKmkNVORBd",
				"focus": -0.48492466514775423,
				"gap": 2.4977451652860054
			},
			"endBinding": {
				"elementId": "YJ56e-w7FODgCK3V0INDz",
				"focus": 0.23204757453468972,
				"gap": 6.297089764632005
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "LPBdSKDN",
			"type": "text",
			"x": 1050.3488722629681,
			"y": -2164.6345198361387,
			"width": 339.5158996582031,
			"height": 45,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1550156002,
			"version": 57,
			"versionNonce": 42603902,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097018,
			"link": null,
			"locked": false,
			"text": "MULTIPROCESSOR",
			"rawText": "MULTIPROCESSOR",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 32,
			"containerId": null,
			"originalText": "MULTIPROCESSOR",
			"lineHeight": 1.25
		},
		{
			"id": "EiRKym6Hjms99AEwzpnXT",
			"type": "image",
			"x": 2128.8114951883163,
			"y": -2338.959208208529,
			"width": 957.0580474805956,
			"height": 307.0875231089313,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 620500578,
			"version": 127,
			"versionNonce": 1391102306,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Zse60mBZPeijsBEl9a9Cq",
					"type": "arrow"
				}
			],
			"updated": 1693583097018,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "a472d3cdd365d641fc5bf9a8708d07e9fe63fb63",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "Zse60mBZPeijsBEl9a9Cq",
			"type": "arrow",
			"x": 2063.4796787966625,
			"y": -2076.7558585948573,
			"width": 62.025980545592574,
			"height": 45.11778070688024,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1716176610,
			"version": 79,
			"versionNonce": 233223614,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097022,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					62.025980545592574,
					-45.11778070688024
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "YJ56e-w7FODgCK3V0INDz",
				"focus": 0.2680530609269335,
				"gap": 2.0608999033694317
			},
			"endBinding": {
				"elementId": "EiRKym6Hjms99AEwzpnXT",
				"focus": 0.572030308979913,
				"gap": 3.3058358460612
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "Ni2b4gCXH7PSUYt8DC2hv",
			"type": "image",
			"x": 2222.5759747132242,
			"y": -3354.16572256615,
			"width": 729.8625748628623,
			"height": 937.4257234762784,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 51372478,
			"version": 60,
			"versionNonce": 827788578,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "u8IR1j5l0NIYkwa6boT4k",
					"type": "arrow"
				},
				{
					"id": "c7rUTrlSV7BwaxpjvJtdF",
					"type": "arrow"
				},
				{
					"id": "wykyrnYbWtddKWrJVn8Vf",
					"type": "arrow"
				}
			],
			"updated": 1693583097022,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "68edf30da2e094b55a446927660587f804d5c6a2",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "u8IR1j5l0NIYkwa6boT4k",
			"type": "arrow",
			"x": 2585.148063514718,
			"y": -2336.2780451387825,
			"width": 8.262662208670918,
			"height": 77.58364095396882,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1135725666,
			"version": 34,
			"versionNonce": 2101693950,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097022,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-8.262662208670918,
					-77.58364095396882
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "Ni2b4gCXH7PSUYt8DC2hv",
				"focus": 0.14667099028240896,
				"gap": 2.8783129971200196
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "_hMUSQMBVHG3rJp6j5SZn",
			"type": "image",
			"x": 3087.3064782702945,
			"y": -2611.7958721777595,
			"width": 767.5223851169983,
			"height": 207.35483791467294,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1078825954,
			"version": 304,
			"versionNonce": 1593645282,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "c7rUTrlSV7BwaxpjvJtdF",
					"type": "arrow"
				}
			],
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "2a6748c811a2c01345d0b25d9ce94538b310cd56",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "c7rUTrlSV7BwaxpjvJtdF",
			"type": "arrow",
			"x": 2959.1897405329482,
			"y": -2527.5462584882216,
			"width": 126.51367305395206,
			"height": 0.4086945190779261,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1683533502,
			"version": 122,
			"versionNonce": 1839652414,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					126.51367305395206,
					-0.4086945190779261
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "Ni2b4gCXH7PSUYt8DC2hv",
				"focus": 0.7642341023806035,
				"gap": 6.751190956861819
			},
			"endBinding": {
				"elementId": "_hMUSQMBVHG3rJp6j5SZn",
				"focus": 0.2009337640253602,
				"gap": 1.6030646833944502
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "dFGQEkltkEe7FW9Y8Javi",
			"type": "image",
			"x": 3234.0727403952064,
			"y": -2211.27116586203,
			"width": 968.8526382481123,
			"height": 689.6281835112288,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 173975010,
			"version": 85,
			"versionNonce": 1265347746,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Des8uDswl4Z9d0bK3f_9e",
					"type": "arrow"
				}
			],
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "ff2e7181cf1605c79a141a3a7eb4c3678d06ce0e",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "Des8uDswl4Z9d0bK3f_9e",
			"type": "arrow",
			"x": 3082.9363042590294,
			"y": -2164.3516106484817,
			"width": 149.92885412486612,
			"height": 127.10978398614498,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 59469438,
			"version": 31,
			"versionNonce": 871130750,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					149.92885412486612,
					127.10978398614498
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "dFGQEkltkEe7FW9Y8Javi",
				"focus": -0.3189046626501807,
				"gap": 1.2075820113107056
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "KEV9dhg-uE77EEzqp_yjt",
			"type": "image",
			"x": 1231.277214800669,
			"y": -3478.927860544447,
			"width": 771.4396817365322,
			"height": 828.8873176105292,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 521853602,
			"version": 113,
			"versionNonce": 475121762,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "wykyrnYbWtddKWrJVn8Vf",
					"type": "arrow"
				}
			],
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "ad2bcf10863fa773d7c02d6adf5153052020df6b",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "wykyrnYbWtddKWrJVn8Vf",
			"type": "arrow",
			"x": 2219.7814261556014,
			"y": -2797.1688318837996,
			"width": 215.12133137681826,
			"height": 185.50421936760495,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1411284798,
			"version": 30,
			"versionNonce": 1624696510,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-215.12133137681826,
					-185.50421936760495
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "Ni2b4gCXH7PSUYt8DC2hv",
				"focus": -0.5174646658994209,
				"gap": 2.7945485576226474
			},
			"endBinding": {
				"elementId": "KEV9dhg-uE77EEzqp_yjt",
				"focus": -0.3379650946268891,
				"gap": 1.9431982415820812
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "IMHqHh61",
			"type": "text",
			"x": 1370.9949968813842,
			"y": -3528.390943275007,
			"width": 451.2958984375,
			"height": 45,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1885050622,
			"version": 53,
			"versionNonce": 1769892898,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"text": "SCRITTORI E LETTORI",
			"rawText": "SCRITTORI E LETTORI",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 32,
			"containerId": null,
			"originalText": "SCRITTORI E LETTORI",
			"lineHeight": 1.25
		},
		{
			"id": "4o3EJWSb2aKipO9XBkCM8",
			"type": "image",
			"x": 3068.149068055894,
			"y": -3324.1214171669662,
			"width": 792.3966749663367,
			"height": 620.7362734262405,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1738706046,
			"version": 171,
			"versionNonce": 1158110974,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "aAXK3BkfvbyYKR7pE8DfQ",
					"type": "arrow"
				}
			],
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "01d2eac8ccd18a693f492837083d835e685f7722",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "Fr9G0zyg_eQH_nsERuJd-",
			"type": "image",
			"x": 4014.63620186357,
			"y": -3533.7971348841784,
			"width": 785.3328087117804,
			"height": 670.0260074326698,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 112630398,
			"version": 74,
			"versionNonce": 2027984866,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "aAXK3BkfvbyYKR7pE8DfQ",
					"type": "arrow"
				}
			],
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "c222f552f60a20db8db6366d770f821b01b25f52",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "aAXK3BkfvbyYKR7pE8DfQ",
			"type": "arrow",
			"x": 3863.661282613328,
			"y": -3097.9907426915306,
			"width": 149.20202379664488,
			"height": 129.87966649368673,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1227952610,
			"version": 49,
			"versionNonce": 1962856254,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					149.20202379664488,
					-129.87966649368673
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "4o3EJWSb2aKipO9XBkCM8",
				"focus": 0.40192387090200543,
				"gap": 3.1155395910968764
			},
			"endBinding": {
				"elementId": "Fr9G0zyg_eQH_nsERuJd-",
				"focus": 0.5502790181582493,
				"gap": 1.7728954535973571
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "j1SWFSNhGa3R86-A4TQOE",
			"type": "image",
			"x": 4007.300589164267,
			"y": -4084.26387107757,
			"width": 825.0138097214664,
			"height": 381.5092761717764,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1721660258,
			"version": 92,
			"versionNonce": 2055687074,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "RLUkEL1BGck52YLce3o_f",
					"type": "arrow"
				},
				{
					"id": "Vq6PYQi7MmlvOJOTPgMhc",
					"type": "arrow"
				}
			],
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "9b7d4806704fb770b55194b4e14116bc40420a58",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "RLUkEL1BGck52YLce3o_f",
			"type": "arrow",
			"x": 4414.845052385159,
			"y": -3533.034884519741,
			"width": 3.4452838438101026,
			"height": 159.9556930506842,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 632663102,
			"version": 48,
			"versionNonce": 1293825918,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					3.4452838438101026,
					-159.9556930506842
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "j1SWFSNhGa3R86-A4TQOE",
				"focus": -0.006725171725662479,
				"gap": 9.76401733536818
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "QtUn3g4CxEk_dHoTtRv9Q",
			"type": "image",
			"x": 4986.281589997467,
			"y": -4532.329141339253,
			"width": 899.9837758439571,
			"height": 383.9216504096246,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 284384994,
			"version": 103,
			"versionNonce": 1151436642,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "z5DxXU2PkkD9nL76DPdy2",
					"type": "arrow"
				}
			],
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "10fb3d2ece95569b9e1e392ea026950be972cda3",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "z5DxXU2PkkD9nL76DPdy2",
			"type": "arrow",
			"x": 4831.9915268498,
			"y": -4011.3813811403297,
			"width": 150.52397167309664,
			"height": 262.0402067845689,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 144354238,
			"version": 52,
			"versionNonce": 1973852094,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					150.52397167309664,
					-262.0402067845689
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "QtUn3g4CxEk_dHoTtRv9Q",
				"focus": 0.7412659105425456,
				"gap": 3.766091474570203
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "wfb7M3gVgnWLzy5DpEkKO",
			"type": "image",
			"x": 4994.7052582284605,
			"y": -4096.275067968423,
			"width": 895.4965348630544,
			"height": 882.7297818202003,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 550659682,
			"version": 81,
			"versionNonce": 259935010,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Vq6PYQi7MmlvOJOTPgMhc",
					"type": "arrow"
				},
				{
					"id": "8jRc7W5FuPrramsfiRcnH",
					"type": "arrow"
				},
				{
					"id": "Mg5ufHxZHpO6a_7DaZFTG",
					"type": "arrow"
				}
			],
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "fbc78c7e7956823040c6b9c70ef98efe56b1a5d9",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "Vq6PYQi7MmlvOJOTPgMhc",
			"type": "arrow",
			"x": 4838.272491630656,
			"y": -3840.3021474090365,
			"width": 145.59920212299858,
			"height": 43.405096855315605,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1070485602,
			"version": 42,
			"versionNonce": 1723396094,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097023,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					145.59920212299858,
					43.405096855315605
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "j1SWFSNhGa3R86-A4TQOE",
				"focus": -0.22804111294849966,
				"gap": 5.958092744921942
			},
			"endBinding": {
				"elementId": "wfb7M3gVgnWLzy5DpEkKO",
				"focus": 0.009180583284006713,
				"gap": 10.83356447480628
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "J3Y9HqOmAZQm7s4LGy-45",
			"type": "image",
			"x": 6015.490150055246,
			"y": -4075.2199101037045,
			"width": 850.5483394929693,
			"height": 850.5483394929693,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 386707774,
			"version": 121,
			"versionNonce": 831297250,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "8jRc7W5FuPrramsfiRcnH",
					"type": "arrow"
				},
				{
					"id": "MtfI6yVgDfCEy6W9UKGm-",
					"type": "arrow"
				},
				{
					"id": "Mg5ufHxZHpO6a_7DaZFTG",
					"type": "arrow"
				}
			],
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "02c082f4a8c1f23e38336113d85467391cd871c7",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "8jRc7W5FuPrramsfiRcnH",
			"type": "arrow",
			"x": 5891.631304462309,
			"y": -3748.487394908773,
			"width": 120.82566383193534,
			"height": 6.174816969307358,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 432251134,
			"version": 34,
			"versionNonce": 1817591870,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					120.82566383193534,
					-6.174816969307358
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "wfb7M3gVgnWLzy5DpEkKO",
				"focus": -0.15212136148470298,
				"gap": 1.4295113707935343
			},
			"endBinding": {
				"elementId": "J3Y9HqOmAZQm7s4LGy-45",
				"focus": 0.2832281037178081,
				"gap": 3.0331817610012877
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "a_tg_dSRudUDNXu3eIoxx",
			"type": "image",
			"x": 7015.997508303727,
			"y": -3805.4944185858612,
			"width": 1156.533888205735,
			"height": 468.066760256152,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 775569442,
			"version": 54,
			"versionNonce": 1532717730,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "4d9c1745b572ff944b6cb9aacf07d53cdb4bf87e",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "Gx1xNqfKce3JwJXBrzPzN",
			"type": "image",
			"x": 7000.715031355414,
			"y": -4705.252397579941,
			"width": 1191.3531811009698,
			"height": 748.444543196633,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1897782242,
			"version": 61,
			"versionNonce": 710903934,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "MtfI6yVgDfCEy6W9UKGm-",
					"type": "arrow"
				},
				{
					"id": "QtYpveVSiu8FurcPSn3cD",
					"type": "arrow"
				}
			],
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "24128ffed79cfea035e6f7055d9296df65c0eb0e",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "MtfI6yVgDfCEy6W9UKGm-",
			"type": "arrow",
			"x": 6512.285548863496,
			"y": -4080.735565450333,
			"width": 481.72534359102247,
			"height": 318.3570728602449,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1871047166,
			"version": 57,
			"versionNonce": 1402586722,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					481.72534359102247,
					-318.3570728602449
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "J3Y9HqOmAZQm7s4LGy-45",
				"focus": -0.5429851761291374,
				"gap": 5.515655346628819
			},
			"endBinding": {
				"elementId": "Gx1xNqfKce3JwJXBrzPzN",
				"focus": 0.6070651687711122,
				"gap": 6.704138900895487
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "oRkBjbwf-MDnc1HbRo8SZ",
			"type": "arrow",
			"x": 7571.7371640211895,
			"y": -3798.531194555525,
			"width": 12.31378594459784,
			"height": 160.01648329025375,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 135374910,
			"version": 40,
			"versionNonce": 546687166,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-12.31378594459784,
					-160.01648329025375
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "DxEMZcYMLY7A0xL4n4Gc2",
			"type": "image",
			"x": 8344.35922273918,
			"y": -4745.075973466666,
			"width": 1238.8544898458354,
			"height": 1367.1727515059501,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 427661602,
			"version": 101,
			"versionNonce": 857123362,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "QtYpveVSiu8FurcPSn3cD",
					"type": "arrow"
				}
			],
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "8ef05b42873fee038ea7194da136ca48d44616a6",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "QtYpveVSiu8FurcPSn3cD",
			"type": "arrow",
			"x": 8196.926179665435,
			"y": -4316.149342155366,
			"width": 146.67206751768572,
			"height": 6.121044978282953,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 2037065086,
			"version": 36,
			"versionNonce": 781844734,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					146.67206751768572,
					6.121044978282953
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "Gx1xNqfKce3JwJXBrzPzN",
				"focus": -0.025511680589351913,
				"gap": 4.857967209052731
			},
			"endBinding": {
				"elementId": "DxEMZcYMLY7A0xL4n4Gc2",
				"focus": 0.31384960029047027,
				"gap": 1
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "gLkrphHI",
			"type": "text",
			"x": 7586.4544621861605,
			"y": -4932.582259421519,
			"width": 1347.65966796875,
			"height": 135,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1757249214,
			"version": 228,
			"versionNonce": 549524962,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "ValraBa_JGVci4bGN2nmd",
					"type": "arrow"
				}
			],
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"text": "SO MODERNI NON USANO IL BANCHIERE PERCHE:\n1) Molto costoso quindi ha senso utilizzarlo solo in situazioni molto critiche.\n2) Dobbiamo sapere in anticipo quello di cui ogni processo ha bisogno.",
			"rawText": "SO MODERNI NON USANO IL BANCHIERE PERCHE:\n1) Molto costoso quindi ha senso utilizzarlo solo in situazioni molto critiche.\n2) Dobbiamo sapere in anticipo quello di cui ogni processo ha bisogno.",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 122,
			"containerId": null,
			"originalText": "SO MODERNI NON USANO IL BANCHIERE PERCHE:\n1) Molto costoso quindi ha senso utilizzarlo solo in situazioni molto critiche.\n2) Dobbiamo sapere in anticipo quello di cui ogni processo ha bisogno.",
			"lineHeight": 1.25
		},
		{
			"id": "ValraBa_JGVci4bGN2nmd",
			"type": "arrow",
			"x": 7506.377308930969,
			"y": -4698.504046333211,
			"width": 370.672559678007,
			"height": 97.2016099355751,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 721975202,
			"version": 106,
			"versionNonce": 401420606,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					370.672559678007,
					-97.2016099355751
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "gLkrphHI",
				"focus": 0.1274335832436313,
				"gap": 1.8766031527329687
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "Mg5ufHxZHpO6a_7DaZFTG",
			"type": "arrow",
			"x": 6224.363501901818,
			"y": -4096.124680854112,
			"width": 153.54963115439477,
			"height": 440.56069919930724,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 2139794722,
			"version": 169,
			"versionNonce": 229116322,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					153.54963115439477,
					-440.56069919930724
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "J3Y9HqOmAZQm7s4LGy-45",
				"focus": -0.6484938323713784,
				"gap": 20.90477075040758
			},
			"endBinding": {
				"elementId": "AGwbIvvQ",
				"focus": 0.38643707220627205,
				"gap": 7.056610135399751
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "m_-yorqLDiftg-xstkLVq",
			"type": "image",
			"x": 5079.245011926007,
			"y": -5589.754113175659,
			"width": 883.2594567095422,
			"height": 775.912358559342,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 294230498,
			"version": 187,
			"versionNonce": 133192062,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "5Bm3u2tbBsVMrgh6Zpv4C",
					"type": "arrow"
				}
			],
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "1469ca617e5cf5b55257bc845dbeebe82fbe8b40",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "AGwbIvvQ",
			"type": "text",
			"x": 6194.102185542844,
			"y": -4636.4514515655355,
			"width": 680.1905368097302,
			"height": 92.70946137671669,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 274930110,
			"version": 92,
			"versionNonce": 1895466338,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Mg5ufHxZHpO6a_7DaZFTG",
					"type": "arrow"
				},
				{
					"id": "5Bm3u2tbBsVMrgh6Zpv4C",
					"type": "arrow"
				},
				{
					"id": "1XTmi1sLHhsdeaTIveQSA",
					"type": "arrow"
				},
				{
					"id": "VmtHpnMxkK0CvMntpx2on",
					"type": "arrow"
				}
			],
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"text": "FILOSOFI A CENA",
			"rawText": "FILOSOFI A CENA",
			"fontSize": 74.16756910137333,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 65.00000000000003,
			"containerId": null,
			"originalText": "FILOSOFI A CENA",
			"lineHeight": 1.25
		},
		{
			"id": "5Bm3u2tbBsVMrgh6Zpv4C",
			"type": "arrow",
			"x": 6357.179813976551,
			"y": -4642.743899768747,
			"width": 378.6584918752833,
			"height": 283.67626899715196,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1683076450,
			"version": 40,
			"versionNonce": 367294910,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-378.6584918752833,
					-283.67626899715196
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "AGwbIvvQ",
				"focus": -0.2655486861000722,
				"gap": 6.292448203211279
			},
			"endBinding": {
				"elementId": "m_-yorqLDiftg-xstkLVq",
				"focus": -0.09386834113415915,
				"gap": 16.01685346571867
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "mH952EYF",
			"type": "text",
			"x": 6000.183054608064,
			"y": -4827.513421914426,
			"width": 447.4354724933029,
			"height": 47.393822832815346,
			"angle": 0.6480166053405494,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1424919550,
			"version": 347,
			"versionNonce": 67602722,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097024,
			"link": null,
			"locked": false,
			"text": "ORDINE ASSIMETRICO",
			"rawText": "ORDINE ASSIMETRICO",
			"fontSize": 37.915058266252274,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 33,
			"containerId": null,
			"originalText": "ORDINE ASSIMETRICO",
			"lineHeight": 1.25
		},
		{
			"id": "bmJPlCjNbTM42ZQiSYuTN",
			"type": "image",
			"x": 6055.6234156520795,
			"y": -5787.156172911819,
			"width": 1043.3167291273198,
			"height": 578.8423911041953,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1750257022,
			"version": 150,
			"versionNonce": 1223332350,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "1XTmi1sLHhsdeaTIveQSA",
					"type": "arrow"
				}
			],
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "e819e16ac83f11b142ee859db0a01db11de71970",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "1XTmi1sLHhsdeaTIveQSA",
			"type": "arrow",
			"x": 6597.768694582847,
			"y": -4638.784820986259,
			"width": 45.71238447027008,
			"height": 550.501092962194,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1550119678,
			"version": 113,
			"versionNonce": 2117997794,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-45.71238447027008,
					-550.501092962194
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "AGwbIvvQ",
				"focus": 0.19653639477799895,
				"gap": 2.333369420723102
			},
			"endBinding": {
				"elementId": "bmJPlCjNbTM42ZQiSYuTN",
				"focus": 0.0931632909250427,
				"gap": 19.027867859171238
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "CXj6MQ8J",
			"type": "text",
			"x": 6425.315937621934,
			"y": -4825.267572397425,
			"width": 312.62396240234375,
			"height": 45,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1110088930,
			"version": 71,
			"versionNonce": 470000190,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"text": "ATTESA ATTIVA",
			"rawText": "ATTESA ATTIVA",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 32,
			"containerId": null,
			"originalText": "ATTESA ATTIVA",
			"lineHeight": 1.25
		},
		{
			"id": "GLbtvMY0",
			"type": "text",
			"x": 6201.43443775022,
			"y": -5848.917306942856,
			"width": 816.4463888635813,
			"height": 59.008863499142315,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 458898018,
			"version": 60,
			"versionNonce": 1361914018,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"text": "(FAIRNESS -> ATTESA INFINITA)",
			"rawText": "(FAIRNESS -> ATTESA INFINITA)",
			"fontSize": 47.20709079931387,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 40.99999999999998,
			"containerId": null,
			"originalText": "(FAIRNESS -> ATTESA INFINITA)",
			"lineHeight": 1.25
		},
		{
			"id": "VRKZ1hpfnXF5MuCYJRcce",
			"type": "image",
			"x": 7186.7896234426,
			"y": -5743.581921356387,
			"width": 1032.479645668995,
			"height": 721.733344545317,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2140699902,
			"version": 107,
			"versionNonce": 34646654,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "VmtHpnMxkK0CvMntpx2on",
					"type": "arrow"
				}
			],
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "759de97f120d05765d1a49ae4a5ba6fd0203d0db",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "VmtHpnMxkK0CvMntpx2on",
			"type": "arrow",
			"x": 6803.073185219953,
			"y": -4641.002328628931,
			"width": 378.6249679799348,
			"height": 420.6997651652482,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 852379646,
			"version": 55,
			"versionNonce": 1686357090,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					378.6249679799348,
					-420.6997651652482
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "AGwbIvvQ",
				"focus": 0.5842144882332139,
				"gap": 4.550877063395092
			},
			"endBinding": {
				"elementId": "VRKZ1hpfnXF5MuCYJRcce",
				"focus": 0.2763600414255689,
				"gap": 5.091470242712148
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "lAZZVzmI",
			"type": "text",
			"x": 6817.2363101203255,
			"y": -4944.955137076269,
			"width": 322.5041243109605,
			"height": 82.45659648600896,
			"angle": 5.456338198765785,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1316202558,
			"version": 136,
			"versionNonce": 1775413950,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"text": "MONITOR",
			"rawText": "MONITOR",
			"fontSize": 65.96527718880716,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 57.000000000000014,
			"containerId": null,
			"originalText": "MONITOR",
			"lineHeight": 1.25
		},
		{
			"id": "7D3V9hIkMZRbuHM1ff6kO",
			"type": "image",
			"x": -375.7005090138946,
			"y": 1015.8455435573348,
			"width": 978.7129375290857,
			"height": 1175.2338255816455,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1087179874,
			"version": 112,
			"versionNonce": 1376839714,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "1zSJSVm4na2xlYGnaot8p",
					"type": "arrow"
				},
				{
					"id": "6cy3UyOrAM3xu44bTXUN3",
					"type": "arrow"
				}
			],
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "2b77fbeabf3a56eaff0da1264eacff45118a5a5f",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "1zSJSVm4na2xlYGnaot8p",
			"type": "arrow",
			"x": -66.40748334241789,
			"y": -80.69633642483632,
			"width": 37.52281864821339,
			"height": 1091.7110907350475,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1626092158,
			"version": 88,
			"versionNonce": 1105896190,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					37.52281864821339,
					1091.7110907350475
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "sBS7rS0Rk4aj3-qvxtuUo",
				"gap": 1.5600188608082135,
				"focus": 0.03590781055112479
			},
			"endBinding": {
				"elementId": "7D3V9hIkMZRbuHM1ff6kO",
				"gap": 4.830789247123562,
				"focus": -0.23977437892057374
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "iAfEmFao",
			"type": "text",
			"x": -1247.6353641777218,
			"y": 2383.6970266390913,
			"width": 1314.503662109375,
			"height": 1170,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1264154338,
			"version": 1269,
			"versionNonce": 566465506,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "6cy3UyOrAM3xu44bTXUN3",
					"type": "arrow"
				},
				{
					"id": "qbt8CuDUZNX_3hr3qm4I0",
					"type": "arrow"
				},
				{
					"id": "68i9wqr-BQZ1J7C0Nve9g",
					"type": "arrow"
				},
				{
					"id": "uOwYduGeW-m5yzMxMsCpT",
					"type": "arrow"
				}
			],
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"text": "ALGORITMI: (QDT = QUANTO DI TEMPO)\n1) FIFO -> ESEGUIAMO TASK IN ORDINE DI ARRIVO\n\n2) SJF -> ESEGUIAMO PRIMA I TASK + VELOCI\n\n2.1) PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nMI FERMO ED PASSO A QUELLO, SUCCESSIVAMENTE RIPRENDO\nDA DOVE MI ERO FERMATO.\n\n2.2) NO PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nFINISCO IL TASK CORRENTE E POI PASSO A QUELLO\n\n3) ROUND ROBIN -> OGNI TASK ACQUISISCE LA CPU PER UN\nQUANTO DI TEMPO, QUANDO SI ESAURISCE PASSO AL TASK \nSUCCESSIVO (CON PRERILASCIO) E MI METTO IN FONDO\nALLA CODA\n\n4) MAX-MIN FAIRNESS -> ROUND ROBIN ASSEGNANDO IL\nAD OGNI TASK UNA PORZIONE DI QUANTO DI TEMPO\n\n5)MFQ -> N CODE ROUND ROBIN CON PRIORITA E QUANTO\nDI TEMPO SPECIFICO, + PRIORITA IMPLICA UN QDT \n+ PICCOLO E VICEVERSA. SE SCADE IL QDT IL TASK SCENDE\n DI PRIORITA, SE RILASCIAMO IL PROCESSORE VOLONTARIAMENTE \nRIMANIAMO NELLA CODA CORRENTE E INFINE SE IL PROCESSO SI \nSOSPENDE SALE DI PRIORITA",
			"rawText": "ALGORITMI: (QDT = QUANTO DI TEMPO)\n1) FIFO -> ESEGUIAMO TASK IN ORDINE DI ARRIVO\n\n2) SJF -> ESEGUIAMO PRIMA I TASK + VELOCI\n\n2.1) PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nMI FERMO ED PASSO A QUELLO, SUCCESSIVAMENTE RIPRENDO\nDA DOVE MI ERO FERMATO.\n\n2.2) NO PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nFINISCO IL TASK CORRENTE E POI PASSO A QUELLO\n\n3) ROUND ROBIN -> OGNI TASK ACQUISISCE LA CPU PER UN\nQUANTO DI TEMPO, QUANDO SI ESAURISCE PASSO AL TASK \nSUCCESSIVO (CON PRERILASCIO) E MI METTO IN FONDO\nALLA CODA\n\n4) MAX-MIN FAIRNESS -> ROUND ROBIN ASSEGNANDO IL\nAD OGNI TASK UNA PORZIONE DI QUANTO DI TEMPO\n\n5)MFQ -> N CODE ROUND ROBIN CON PRIORITA E QUANTO\nDI TEMPO SPECIFICO, + PRIORITA IMPLICA UN QDT \n+ PICCOLO E VICEVERSA. SE SCADE IL QDT IL TASK SCENDE\n DI PRIORITA, SE RILASCIAMO IL PROCESSORE VOLONTARIAMENTE \nRIMANIAMO NELLA CODA CORRENTE E INFINE SE IL PROCESSO SI \nSOSPENDE SALE DI PRIORITA",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 1157,
			"containerId": null,
			"originalText": "ALGORITMI: (QDT = QUANTO DI TEMPO)\n1) FIFO -> ESEGUIAMO TASK IN ORDINE DI ARRIVO\n\n2) SJF -> ESEGUIAMO PRIMA I TASK + VELOCI\n\n2.1) PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nMI FERMO ED PASSO A QUELLO, SUCCESSIVAMENTE RIPRENDO\nDA DOVE MI ERO FERMATO.\n\n2.2) NO PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nFINISCO IL TASK CORRENTE E POI PASSO A QUELLO\n\n3) ROUND ROBIN -> OGNI TASK ACQUISISCE LA CPU PER UN\nQUANTO DI TEMPO, QUANDO SI ESAURISCE PASSO AL TASK \nSUCCESSIVO (CON PRERILASCIO) E MI METTO IN FONDO\nALLA CODA\n\n4) MAX-MIN FAIRNESS -> ROUND ROBIN ASSEGNANDO IL\nAD OGNI TASK UNA PORZIONE DI QUANTO DI TEMPO\n\n5)MFQ -> N CODE ROUND ROBIN CON PRIORITA E QUANTO\nDI TEMPO SPECIFICO, + PRIORITA IMPLICA UN QDT \n+ PICCOLO E VICEVERSA. SE SCADE IL QDT IL TASK SCENDE\n DI PRIORITA, SE RILASCIAMO IL PROCESSORE VOLONTARIAMENTE \nRIMANIAMO NELLA CODA CORRENTE E INFINE SE IL PROCESSO SI \nSOSPENDE SALE DI PRIORITA",
			"lineHeight": 1.25
		},
		{
			"id": "6cy3UyOrAM3xu44bTXUN3",
			"type": "arrow",
			"x": -45.12051839626275,
			"y": 2197.749376315361,
			"width": 217.77725125865834,
			"height": 161.89362534102384,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 800779198,
			"version": 1707,
			"versionNonce": 2094633790,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-217.77725125865834,
					161.89362534102384
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "7D3V9hIkMZRbuHM1ff6kO",
				"focus": -0.5005821992955272,
				"gap": 6.670007176380864
			},
			"endBinding": {
				"elementId": "3rmMBz2V577zAZST9tMiL",
				"focus": -0.3256488879842338,
				"gap": 10.939076071001864
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "ahyRjWNk",
			"type": "text",
			"x": -1278.2579536642068,
			"y": 3723.205430377718,
			"width": 1227.77978515625,
			"height": 180,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1102463294,
			"version": 254,
			"versionNonce": 95078306,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "qbt8CuDUZNX_3hr3qm4I0",
					"type": "arrow"
				}
			],
			"updated": 1693583097025,
			"link": null,
			"locked": false,
			"text": "PRIORITY INVERSION -> SE UN TASK STA FERMO DA UN PO' LO\nSCHEDULER LO SVEGLIA E GLI DA UN BOOST DI PRIORITA\n(EX: UN THREAD SOSPESO CHE ATTENDE DI ESSERE SVEGLIATO\nDA UN THREAD DI PRIORITA MOLTO INFERIORE)",
			"rawText": "PRIORITY INVERSION -> SE UN TASK STA FERMO DA UN PO' LO\nSCHEDULER LO SVEGLIA E GLI DA UN BOOST DI PRIORITA\n(EX: UN THREAD SOSPESO CHE ATTENDE DI ESSERE SVEGLIATO\nDA UN THREAD DI PRIORITA MOLTO INFERIORE)",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 167,
			"containerId": null,
			"originalText": "PRIORITY INVERSION -> SE UN TASK STA FERMO DA UN PO' LO\nSCHEDULER LO SVEGLIA E GLI DA UN BOOST DI PRIORITA\n(EX: UN THREAD SOSPESO CHE ATTENDE DI ESSERE SVEGLIATO\nDA UN THREAD DI PRIORITA MOLTO INFERIORE)",
			"lineHeight": 1.25
		},
		{
			"id": "qbt8CuDUZNX_3hr3qm4I0",
			"type": "arrow",
			"x": -809.741009475543,
			"y": 3573.0017932303895,
			"width": 10.25379625298092,
			"height": 142.4916025712705,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1312532862,
			"version": 52,
			"versionNonce": 352353150,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097026,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					10.25379625298092,
					142.4916025712705
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "3rmMBz2V577zAZST9tMiL",
				"focus": 0.3503624680221696,
				"gap": 3.127961953857948
			},
			"endBinding": {
				"elementId": "ahyRjWNk",
				"focus": -0.2064711020113422,
				"gap": 7.712034576058159
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "bN2yUoNTdjLwAY1EWH_CE",
			"type": "image",
			"x": 193.2507115044666,
			"y": 2984.8789833533388,
			"width": 1286.1357768365524,
			"height": 593.2301270658598,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1684107170,
			"version": 58,
			"versionNonce": 368411490,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "68i9wqr-BQZ1J7C0Nve9g",
					"type": "arrow"
				}
			],
			"updated": 1693583097026,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "ebd64853de77c0d7796a06e600c3eb568fa003c8",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "68i9wqr-BQZ1J7C0Nve9g",
			"type": "arrow",
			"x": 68.41009151054391,
			"y": 2904.889275409446,
			"width": 117.79440359597311,
			"height": 155.87927724395786,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1921342050,
			"version": 159,
			"versionNonce": 278944702,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097026,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					117.79440359597311,
					155.87927724395786
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "3rmMBz2V577zAZST9tMiL",
				"focus": -0.6465957545731664,
				"gap": 8.676532264654497
			},
			"endBinding": {
				"elementId": "bN2yUoNTdjLwAY1EWH_CE",
				"focus": -0.557321949221479,
				"gap": 7.046216397949593
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "3rmMBz2V577zAZST9tMiL",
			"type": "rectangle",
			"x": -1269.8829707270156,
			"y": 2370.5820777273866,
			"width": 1329.616529972905,
			"height": 1199.2917535491447,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"seed": 1756205310,
			"version": 98,
			"versionNonce": 217237282,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "6cy3UyOrAM3xu44bTXUN3",
					"type": "arrow"
				},
				{
					"id": "68i9wqr-BQZ1J7C0Nve9g",
					"type": "arrow"
				},
				{
					"id": "qbt8CuDUZNX_3hr3qm4I0",
					"type": "arrow"
				}
			],
			"updated": 1693583097026,
			"link": null,
			"locked": false
		},
		{
			"id": "XCd17DPn",
			"type": "image",
			"x": 592.5774490157419,
			"y": 4105.987360518386,
			"width": 1106.4515138185275,
			"height": 801.9113735968415,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"roundness": null,
			"seed": 51722,
			"version": 87,
			"versionNonce": 98186238,
			"updated": 1693583097026,
			"isDeleted": false,
			"groupIds": [],
			"boundElements": [
				{
					"id": "uOwYduGeW-m5yzMxMsCpT",
					"type": "arrow"
				},
				{
					"id": "JK9B4dgtDrUMlZfyeDhAm",
					"type": "arrow"
				}
			],
			"link": null,
			"locked": false,
			"fileId": "3541300b2dbb9244501297335f434a757747f70a",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "uOwYduGeW-m5yzMxMsCpT",
			"type": "arrow",
			"x": 45.513510546860516,
			"y": 3566.7839456691145,
			"width": 803.9867141496779,
			"height": 530.8595771258297,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1999358306,
			"version": 185,
			"versionNonce": 51483362,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097026,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					803.9867141496779,
					530.8595771258297
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "iAfEmFao",
				"focus": 0.17463474307273927,
				"gap": 13.086919030023182
			},
			"endBinding": {
				"elementId": "XCd17DPn",
				"focus": 0.2788354780115446,
				"gap": 8.343837723441993
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "GRVkWSDo",
			"type": "text",
			"x": 146.79765982401727,
			"y": 3728.0276770549012,
			"width": 512.6120075901304,
			"height": 67.94244500707744,
			"angle": 0.5398972279282415,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1181850658,
			"version": 166,
			"versionNonce": 514786366,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097026,
			"link": null,
			"locked": false,
			"text": "MULTIPROCESSOR",
			"rawText": "MULTIPROCESSOR",
			"fontSize": 54.3539560056619,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 47.00000000000007,
			"containerId": null,
			"originalText": "MULTIPROCESSOR",
			"lineHeight": 1.25
		},
		{
			"id": "4afkSfBr",
			"type": "text",
			"x": 1520.0252472229229,
			"y": 4230.263795159231,
			"width": 115.28941349864317,
			"height": 70.47033553540273,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 215281698,
			"version": 340,
			"versionNonce": 982609762,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583112359,
			"link": null,
			"locked": false,
			"text": "MFQ",
			"rawText": "MFQ",
			"fontSize": 56.37626842832219,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 48.999999999999986,
			"containerId": null,
			"originalText": "MFQ",
			"lineHeight": 1.25
		},
		{
			"id": "xwDxYI34",
			"type": "text",
			"x": 1166.374837854006,
			"y": 3799.8518300960295,
			"width": 1511.3516845703125,
			"height": 90,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1382484770,
			"version": 142,
			"versionNonce": 486526078,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "JK9B4dgtDrUMlZfyeDhAm",
					"type": "arrow"
				}
			],
			"updated": 1693583097026,
			"link": null,
			"locked": false,
			"text": "AFFINITY SCHEDULING -> ASSEGNARE IL PROCESSO AL PROCESSORE + AFFINE \n(QUELLO CHE DETIENE I DATI CHE MODIFICA IL TASK DEL CASO)",
			"rawText": "AFFINITY SCHEDULING -> ASSEGNARE IL PROCESSO AL PROCESSORE + AFFINE \n(QUELLO CHE DETIENE I DATI CHE MODIFICA IL TASK DEL CASO)",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 77,
			"containerId": null,
			"originalText": "AFFINITY SCHEDULING -> ASSEGNARE IL PROCESSO AL PROCESSORE + AFFINE \n(QUELLO CHE DETIENE I DATI CHE MODIFICA IL TASK DEL CASO)",
			"lineHeight": 1.25
		},
		{
			"id": "JK9B4dgtDrUMlZfyeDhAm",
			"type": "arrow",
			"x": 958.8684548708432,
			"y": 4100.702515462554,
			"width": 210.49848730613166,
			"height": 248.7856353694333,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 709555006,
			"version": 141,
			"versionNonce": 219136610,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097026,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-11.149418103263088,
					-225.0349199420516
				],
				[
					199.34906920286858,
					-248.7856353694333
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "XCd17DPn",
				"focus": -0.29106614227220035,
				"gap": 5.284845055831738
			},
			"endBinding": {
				"elementId": "xwDxYI34",
				"focus": 0.6073754660295104,
				"gap": 8.157313780294203
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "dYpybeGJBHiZyXmMb1KYv",
			"type": "image",
			"x": -926.8773692756317,
			"y": 4273.868639163048,
			"width": 1286.7740701824926,
			"height": 1064.3483346195776,
			"angle": 0,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 213447330,
			"version": 139,
			"versionNonce": 1586334910,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "VWAlwdtgv2NyqGn5dlMQg",
					"type": "arrow"
				}
			],
			"updated": 1693583097026,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "a613079fedc0e3ede8bc2ebb3a84efd49a8c7d9b",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "VWAlwdtgv2NyqGn5dlMQg",
			"type": "arrow",
			"x": 451.11769053307694,
			"y": 3855.7344034628622,
			"width": 290.23125553669115,
			"height": 402.89171719746355,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1459354174,
			"version": 100,
			"versionNonce": 1626948862,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693583097026,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-290.23125553669115,
					402.89171719746355
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "dYpybeGJBHiZyXmMb1KYv",
				"focus": 0.048730490413972545,
				"gap": 15.24251850272185
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "ywJbATZq",
			"type": "text",
			"x": 620.7425644309349,
			"y": 4085.9298191653147,
			"width": 18,
			"height": 45,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 4655614,
			"version": 3,
			"versionNonce": 1148003874,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1693583097026,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 32,
			"containerId": null,
			"originalText": "",
			"lineHeight": 1.25
		}
	],
	"appState": {
		"theme": "dark",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "hachure",
		"currentItemStrokeWidth": 4,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 0,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 36,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "triangle",
		"scrollX": 616.5278528372564,
		"scrollY": -3680.951399504285,
		"zoom": {
			"value": 0.5269963373955127
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%