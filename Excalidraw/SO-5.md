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

Nella bsp ci sono thread di lunghezza variabile che vengono eseguiti, prima di passare alla ^YR8inbTo

prossima esecuzione c’è però una barriera, i thread devono infatti sincronizzarsi. ^LANKscsX

Il tempo di esecuzione è dettato quindi dal thread più lungo ^fPQzxBrZ

ADDRESS TRANSLATION ^csv9an0l

PROBLEMI: POCO FLESSIBILE E FRAMMENTAZIONE ^hkFJF4Uc


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
00191f0ba092228633209e228aa7affc2212547a: [[Pasted Image 20230902221130_668.png]]
35e11bf9682e5fedf799263320562726c4dbb687: [[Pasted Image 20230902221531_700.png]]
9e601f3a5891476cc21b146c71af34dbf552ed46: [[Pasted Image 20230902221817_807.png]]
6d192e9ecfd1f127040f49016d924509cbf06a7a: [[Pasted Image 20230902222203_170.png]]
a456e8d616a72eb2522d24bb787f2a57f55106c6: [[Pasted Image 20230902222333_196.png]]
e39d59e560645cfdac6900dc32cfbf99f84408c5: [[Pasted Image 20230902222703_201.png]]
5caead1268cc985f7db01c97264e767b0654acba: [[Pasted Image 20230902223915_498.png]]
546cd0e1266543e6297b5549cf2791c49ab6ded0: [[Pasted Image 20230902224038_587.png]]
fdac1316ee03a2a45ca87d752ba981866ac31b0e: [[Pasted Image 20230902224253_668.png]]
9f7f45a7193e2f59b916a8a8544981085d30001d: [[Pasted Image 20230902224440_777.png]]
e4f1eafacc383821b645360c5f6eeb4d1f371a0c: [[Pasted Image 20230902225955_797.png]]
71c9315cbaf7291a243962937b1724f63eeaa5af: [[Pasted Image 20230902231207_589.png]]
227edf29f313074ff16fd05750a0e9a7a1e6f363: [[Pasted Image 20230902231826_076.png]]
f849373ecaf67d092f1be833e0cf23c5c5212e7b: [[Pasted Image 20230902231841_098.png]]
75bc1fc729ae3620a2364e9e5f9de9cfddcd970c: [[Pasted Image 20230902232341_109.png]]
103efc88f7adc96b6896916861fd47c40bf0938f: [[Pasted Image 20230903003426_343.png]]
b1b03a9389e5d98105c5846f9a3f237bde29c831: [[Pasted Image 20230903003828_691.png]]
73360c3a546d67223f20a20861100eb6533f723a: [[Pasted Image 20230903003945_730.png]]
7a156dc65c1c3eb2ead82f3f7bcfa45402171301: [[Pasted Image 20230903011105_011.png]]
12d13934062c81e68c589b3526cd41fe267e4105: [[Pasted Image 20230903013835_134.png]]
eeac4cdb843be046116eeade3335929837cd77b4: [[Pasted Image 20230903013920_158.png]]
8c7bc1ccfb189d7eadea6c308e8a155a036044de: [[Pasted Image 20230903014136_265.png]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.9.19",
	"elements": [
		{
			"type": "rectangle",
			"version": 79,
			"versionNonce": 1015189604,
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
			"updated": 1693689492375,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 12,
			"versionNonce": 788010972,
			"isDeleted": false,
			"id": "6MYYHsQ9",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -90.6462287902832,
			"y": -133.25635528564453,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 50.01995849609375,
			"height": 25,
			"seed": 692398758,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492375,
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
			"version": 163,
			"versionNonce": 1847256036,
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
			"updated": 1693689492376,
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
			"version": 353,
			"versionNonce": 2082615578,
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
			"updated": 1693746738807,
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
			"version": 45,
			"versionNonce": 6080356,
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
			"updated": 1693689492376,
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
			"version": 251,
			"versionNonce": 1430794906,
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
			"updated": 1693746738808,
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
			"version": 71,
			"versionNonce": 1201027812,
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
			"updated": 1693689492376,
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
			"version": 53,
			"versionNonce": 1344951644,
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
			"updated": 1693689492376,
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
			"version": 86,
			"versionNonce": 1582644836,
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
			"updated": 1693689492376,
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
			"version": 295,
			"versionNonce": 1123800090,
			"isDeleted": false,
			"id": "h5bAaNe2fUIJNhaIFsjMt",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -125.13624954223633,
			"y": -113.16194378653809,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 316.5211660179895,
			"height": 109.33134756055583,
			"seed": 1262744870,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693746738808,
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
					-316.5211660179895,
					109.33134756055583
				]
			]
		},
		{
			"type": "image",
			"version": 115,
			"versionNonce": 1567085028,
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
			"updated": 1693689492376,
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
			"version": 114,
			"versionNonce": 1797369436,
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
			"updated": 1693689492376,
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
			"version": 118,
			"versionNonce": 333182308,
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
			"updated": 1693689492377,
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
			"version": 104,
			"versionNonce": 538149596,
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
			"updated": 1693689492377,
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
			"version": 139,
			"versionNonce": 1056942308,
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
			"updated": 1693689492377,
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
			"version": 253,
			"versionNonce": 1893123932,
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
			"updated": 1693689492377,
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
			"version": 34,
			"versionNonce": 1113648228,
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
			"updated": 1693689492377,
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
			"version": 54,
			"versionNonce": 1102937052,
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
			"updated": 1693689492377,
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
			"version": 187,
			"versionNonce": 1607319524,
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
			"updated": 1693689492377,
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
			"version": 265,
			"versionNonce": 484024412,
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
			"updated": 1693689492377,
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
			"version": 69,
			"versionNonce": 1867785060,
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
			"updated": 1693689492377,
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
			"version": 54,
			"versionNonce": 2046637276,
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
			"updated": 1693689492377,
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
			"version": 203,
			"versionNonce": 390207204,
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
			"updated": 1693689492378,
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
			"version": 372,
			"versionNonce": 112867676,
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
			"updated": 1693689492378,
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
			"version": 313,
			"versionNonce": 69573220,
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
			"updated": 1693689492378,
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
			"version": 129,
			"versionNonce": 1851960796,
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
			"updated": 1693689492378,
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
			"version": 463,
			"versionNonce": 550284772,
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
			"updated": 1693689492378,
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
			"version": 891,
			"versionNonce": 570987100,
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
			"updated": 1693689492378,
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
			"version": 250,
			"versionNonce": 1313165668,
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
			"updated": 1693689492379,
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
			"version": 104,
			"versionNonce": 545122012,
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
			"updated": 1693689492379,
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
			"version": 163,
			"versionNonce": 467502308,
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
			"updated": 1693689492379,
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
			"version": 67,
			"versionNonce": 1045736284,
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
			"updated": 1693689492379,
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
			"version": 252,
			"versionNonce": 2133018724,
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
			"updated": 1693689492379,
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
			"version": 129,
			"versionNonce": 1843322844,
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
			"updated": 1693689492379,
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
			"version": 197,
			"versionNonce": 199531492,
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
			"updated": 1693689492379,
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
			"version": 186,
			"versionNonce": 120489052,
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
			"updated": 1693689492379,
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
			"version": 138,
			"versionNonce": 741310308,
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
			"updated": 1693689492379,
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
			"version": 209,
			"versionNonce": 269850844,
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
			"updated": 1693689492379,
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
			"version": 96,
			"versionNonce": 1481765604,
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
			"updated": 1693689492380,
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
			"version": 67,
			"versionNonce": 69606748,
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
			"updated": 1693689492380,
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
			"version": 81,
			"versionNonce": 1322907236,
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
			"updated": 1693689492380,
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
			"version": 40,
			"versionNonce": 481432028,
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
			"updated": 1693689492380,
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
			"version": 85,
			"versionNonce": 1284868580,
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
			"updated": 1693689492380,
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
			"version": 92,
			"versionNonce": 415987292,
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
			"updated": 1693689492380,
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
			"version": 123,
			"versionNonce": 1150463332,
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
			"updated": 1693689492380,
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
			"version": 82,
			"versionNonce": 88361692,
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
			"updated": 1693689492380,
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
			"version": 161,
			"versionNonce": 404709604,
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
			"updated": 1693689492380,
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
			"version": 334,
			"versionNonce": 78548828,
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
			"updated": 1693689492380,
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
			"version": 183,
			"versionNonce": 1321837668,
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
			"updated": 1693689492380,
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
			"version": 174,
			"versionNonce": 391922652,
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
			"updated": 1693689492381,
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
			"version": 312,
			"versionNonce": 1314879460,
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
			"updated": 1693689492381,
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
			"version": 504,
			"versionNonce": 1667197020,
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
			"updated": 1693689492381,
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
			"version": 115,
			"versionNonce": 317643620,
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
			"updated": 1693689492381,
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
			"version": 205,
			"versionNonce": 1985287578,
			"isDeleted": false,
			"id": "GgjyNIzY13dUTdHHEKPUK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -25.997107372175577,
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
			"updated": 1693746738809,
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
			"version": 80,
			"versionNonce": 1724239588,
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
			"updated": 1693689492381,
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
			"version": 94,
			"versionNonce": 745406812,
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
			"updated": 1693689492381,
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
			"version": 106,
			"versionNonce": 443699812,
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
			"updated": 1693689492381,
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
			"version": 43,
			"versionNonce": 979203548,
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
			"updated": 1693689492381,
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
			"version": 45,
			"versionNonce": 1019373028,
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
			"updated": 1693689492381,
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
			"version": 59,
			"versionNonce": 862607964,
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
			"updated": 1693689492382,
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
			"version": 98,
			"versionNonce": 1388579172,
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
			"width": 1089.2735779567101,
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
			"updated": 1693689492382,
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
			"version": 65,
			"versionNonce": 845590236,
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
			"updated": 1693689492382,
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
			"version": 85,
			"versionNonce": 264584420,
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
			"updated": 1693689492382,
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
			"version": 42,
			"versionNonce": 669283164,
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
			"updated": 1693689492382,
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
			"version": 62,
			"versionNonce": 223608932,
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
			"updated": 1693689492382,
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
			"version": 94,
			"versionNonce": 573941724,
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
			"updated": 1693689492383,
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
			"type": "image",
			"version": 183,
			"versionNonce": 54416356,
			"isDeleted": false,
			"id": "N4ixpycSJ-mC-P7y-wHQ9",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1544.357541413392,
			"y": 435.24766722718164,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 728.3321894209117,
			"height": 1033.085389600871,
			"seed": 1478684770,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492383,
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
			"type": "arrow",
			"version": 122,
			"versionNonce": 359418972,
			"isDeleted": false,
			"id": "tOIRODLH46AHXrAISlD-K",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2100.127781048343,
			"y": 331.41466204654836,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 32.88578130027827,
			"height": 100.54066694964177,
			"seed": 602049378,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492383,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-32.88578130027827,
					100.54066694964177
				]
			]
		},
		{
			"type": "image",
			"version": 119,
			"versionNonce": 2140288868,
			"isDeleted": false,
			"id": "_fWmRN9P-xP4yJ09hj9NM",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2723.927785277215,
			"y": 892.0007670648413,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 973.802138863129,
			"height": 1023.4859214581867,
			"seed": 1697018594,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "9WGYd08Enxk5Miavu74wb",
					"type": "arrow"
				}
			],
			"updated": 1693689492383,
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
			"type": "arrow",
			"version": 188,
			"versionNonce": 593125596,
			"isDeleted": false,
			"id": "9WGYd08Enxk5Miavu74wb",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2544.630835927974,
			"y": 332.2732754341271,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 388.4293172850216,
			"height": 557.8847982804895,
			"seed": 897114594,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492383,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					388.4293172850216,
					557.8847982804895
				]
			]
		},
		{
			"type": "image",
			"version": 143,
			"versionNonce": 513649380,
			"isDeleted": false,
			"id": "J_rwX2Wf7G9Fsn6w2q2iQ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 706.4904583797397,
			"y": 1683.0687010205904,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 840.4415237666473,
			"height": 541.3324225134519,
			"seed": 881921406,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492383,
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
			"type": "image",
			"version": 149,
			"versionNonce": 1670505820,
			"isDeleted": false,
			"id": "Do10efRIVP1H-E0-0gN-y",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1732.830641390917,
			"y": 1655.1702279476458,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 952.9945283562978,
			"height": 756.316483104529,
			"seed": 450729022,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "AKcO4al7sLLMmc8z6opMG",
					"type": "arrow"
				}
			],
			"updated": 1693689492383,
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
			"type": "arrow",
			"version": 63,
			"versionNonce": 1122938468,
			"isDeleted": false,
			"id": "AKcO4al7sLLMmc8z6opMG",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1977.7811457632083,
			"y": 1471.664726123822,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 168.10046181063308,
			"height": 179.69550865126052,
			"seed": 1328546914,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492383,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					168.10046181063308,
					179.69550865126052
				]
			]
		},
		{
			"type": "arrow",
			"version": 53,
			"versionNonce": 728029660,
			"isDeleted": false,
			"id": "cfgrdvpC9IcaqDH4mgArK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1739.0012608260492,
			"y": 1472.6690912177978,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 341.35536719616744,
			"height": 202.52120766734515,
			"seed": 932713598,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492383,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-341.35536719616744,
					202.52120766734515
				]
			]
		},
		{
			"type": "text",
			"version": 152,
			"versionNonce": 1297301988,
			"isDeleted": false,
			"id": "eCA7dzpo",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 221.94641580214642,
			"y": 2462.717732430397,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1334.34033203125,
			"height": 135,
			"seed": 1434402274,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "aHYIC6pTlufm3WJZqpPse",
					"type": "arrow"
				}
			],
			"updated": 1693689492384,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "la signal invece di segnalare e basta segnaliamo passando la lock, \ncosì che chi viene risvegliato ha già la lock, e non la deve riacquisire, \nsicuramente se gli passo la lock non potrà essere scavalcato da un altro.",
			"rawText": "la signal invece di segnalare e basta segnaliamo passando la lock, \ncosì che chi viene risvegliato ha già la lock, e non la deve riacquisire, \nsicuramente se gli passo la lock non potrà essere scavalcato da un altro.",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "la signal invece di segnalare e basta segnaliamo passando la lock, \ncosì che chi viene risvegliato ha già la lock, e non la deve riacquisire, \nsicuramente se gli passo la lock non potrà essere scavalcato da un altro.",
			"lineHeight": 1.25,
			"baseline": 122
		},
		{
			"type": "arrow",
			"version": 40,
			"versionNonce": 1441087068,
			"isDeleted": false,
			"id": "aHYIC6pTlufm3WJZqpPse",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 950.6175836401818,
			"y": 2238.398755728431,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 73.9796442725152,
			"height": 220.2049007749556,
			"seed": 1046107390,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492384,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-73.9796442725152,
					220.2049007749556
				]
			]
		},
		{
			"type": "image",
			"version": 124,
			"versionNonce": 1423533412,
			"isDeleted": false,
			"id": "f5_9i_uRtbWAKmkNVORBd",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 572.2914204844761,
			"y": -2000.6410486861423,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 730.0292735435199,
			"height": 750.2277119419573,
			"seed": 151955746,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492384,
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
			"type": "arrow",
			"version": 198,
			"versionNonce": 199561948,
			"isDeleted": false,
			"id": "3uphtt1sOucM0fWULkfC_",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 454.0500513667779,
			"y": -798.779070116273,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 249.42803304134566,
			"height": 445.2900539338166,
			"seed": 883726178,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492384,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					249.42803304134566,
					-445.2900539338166
				]
			]
		},
		{
			"type": "text",
			"version": 179,
			"versionNonce": 1590630628,
			"isDeleted": false,
			"id": "9okUCD0N",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 5.280197117783722,
			"x": 588.4730295788286,
			"y": -1148.693766143094,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 48.02403259277344,
			"height": 45,
			"seed": 168133986,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492384,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "SO",
			"rawText": "SO",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "SO",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "image",
			"version": 120,
			"versionNonce": 200693596,
			"isDeleted": false,
			"id": "YJ56e-w7FODgCK3V0INDz",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1427.6423595098597,
			"y": -2483.475214563668,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 633.7764193834333,
			"height": 898.1517257548084,
			"seed": 130639778,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492384,
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
			"type": "arrow",
			"version": 79,
			"versionNonce": 381836388,
			"isDeleted": false,
			"id": "i8vGygleUbwU6lzZhPaOV",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 949.5343328112874,
			"y": -2003.1387938514283,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 471.8109369339402,
			"height": 118.48235326027066,
			"seed": 543442530,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492384,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
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
			]
		},
		{
			"type": "text",
			"version": 60,
			"versionNonce": 1919618012,
			"isDeleted": false,
			"id": "LPBdSKDN",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1050.3488722629681,
			"y": -2164.6345198361387,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 339.51611328125,
			"height": 45,
			"seed": 1550156002,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492384,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "MULTIPROCESSOR",
			"rawText": "MULTIPROCESSOR",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "MULTIPROCESSOR",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "image",
			"version": 130,
			"versionNonce": 109129700,
			"isDeleted": false,
			"id": "EiRKym6Hjms99AEwzpnXT",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2128.8114951883163,
			"y": -2338.959208208529,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 957.0580474805957,
			"height": 307.0875231089313,
			"seed": 620500578,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Zse60mBZPeijsBEl9a9Cq",
					"type": "arrow"
				}
			],
			"updated": 1693689492384,
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
			"type": "arrow",
			"version": 82,
			"versionNonce": 22360156,
			"isDeleted": false,
			"id": "Zse60mBZPeijsBEl9a9Cq",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2063.4796787966625,
			"y": -2076.7558585948573,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 62.025980545592574,
			"height": 45.11778070688024,
			"seed": 1716176610,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492384,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					62.025980545592574,
					-45.11778070688024
				]
			]
		},
		{
			"type": "image",
			"version": 63,
			"versionNonce": 1310298980,
			"isDeleted": false,
			"id": "Ni2b4gCXH7PSUYt8DC2hv",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2222.5759747132242,
			"y": -3354.16572256615,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 729.8625748628623,
			"height": 937.4257234762784,
			"seed": 51372478,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492385,
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
			"type": "arrow",
			"version": 37,
			"versionNonce": 1753662684,
			"isDeleted": false,
			"id": "u8IR1j5l0NIYkwa6boT4k",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2585.148063514718,
			"y": -2336.2780451387825,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.262662208670918,
			"height": 77.58364095396882,
			"seed": 1135725666,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492385,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "Ni2b4gCXH7PSUYt8DC2hv",
				"focus": 0.14667099028240896,
				"gap": 2.8783129971200196
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
					-8.262662208670918,
					-77.58364095396882
				]
			]
		},
		{
			"type": "image",
			"version": 307,
			"versionNonce": 1540982500,
			"isDeleted": false,
			"id": "_hMUSQMBVHG3rJp6j5SZn",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3087.3064782702945,
			"y": -2611.7958721777595,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 767.5223851169984,
			"height": 207.35483791467294,
			"seed": 1078825954,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "c7rUTrlSV7BwaxpjvJtdF",
					"type": "arrow"
				}
			],
			"updated": 1693689492385,
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
			"type": "arrow",
			"version": 125,
			"versionNonce": 227658076,
			"isDeleted": false,
			"id": "c7rUTrlSV7BwaxpjvJtdF",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2959.1897405329482,
			"y": -2527.5462584882216,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 126.51367305395206,
			"height": 0.4086945190779261,
			"seed": 1683533502,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492385,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					126.51367305395206,
					-0.4086945190779261
				]
			]
		},
		{
			"type": "image",
			"version": 88,
			"versionNonce": 609159780,
			"isDeleted": false,
			"id": "dFGQEkltkEe7FW9Y8Javi",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3234.0727403952064,
			"y": -2211.27116586203,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 968.8526382481123,
			"height": 689.6281835112288,
			"seed": 173975010,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Des8uDswl4Z9d0bK3f_9e",
					"type": "arrow"
				}
			],
			"updated": 1693689492385,
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
			"type": "arrow",
			"version": 34,
			"versionNonce": 1405631964,
			"isDeleted": false,
			"id": "Des8uDswl4Z9d0bK3f_9e",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3082.9363042590294,
			"y": -2164.3516106484817,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 149.92885412486612,
			"height": 127.10978398614498,
			"seed": 59469438,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492385,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "dFGQEkltkEe7FW9Y8Javi",
				"focus": -0.3189046626501807,
				"gap": 1.2075820113107056
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
					149.92885412486612,
					127.10978398614498
				]
			]
		},
		{
			"type": "image",
			"version": 116,
			"versionNonce": 1514675684,
			"isDeleted": false,
			"id": "KEV9dhg-uE77EEzqp_yjt",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1231.277214800669,
			"y": -3478.927860544447,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 771.4396817365322,
			"height": 828.8873176105292,
			"seed": 521853602,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "wykyrnYbWtddKWrJVn8Vf",
					"type": "arrow"
				}
			],
			"updated": 1693689492385,
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
			"type": "arrow",
			"version": 33,
			"versionNonce": 1681662556,
			"isDeleted": false,
			"id": "wykyrnYbWtddKWrJVn8Vf",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2219.7814261556014,
			"y": -2797.1688318837996,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 215.12133137681826,
			"height": 185.50421936760495,
			"seed": 1411284798,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492385,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-215.12133137681826,
					-185.50421936760495
				]
			]
		},
		{
			"type": "text",
			"version": 56,
			"versionNonce": 651346276,
			"isDeleted": false,
			"id": "IMHqHh61",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1370.9949968813842,
			"y": -3528.390943275007,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 451.29620361328125,
			"height": 45,
			"seed": 1885050622,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492385,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "SCRITTORI E LETTORI",
			"rawText": "SCRITTORI E LETTORI",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "SCRITTORI E LETTORI",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "image",
			"version": 174,
			"versionNonce": 1975482076,
			"isDeleted": false,
			"id": "4o3EJWSb2aKipO9XBkCM8",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3068.149068055894,
			"y": -3324.1214171669662,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 792.3966749663367,
			"height": 620.7362734262406,
			"seed": 1738706046,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "aAXK3BkfvbyYKR7pE8DfQ",
					"type": "arrow"
				}
			],
			"updated": 1693689492386,
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
			"type": "image",
			"version": 77,
			"versionNonce": 1631384804,
			"isDeleted": false,
			"id": "Fr9G0zyg_eQH_nsERuJd-",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4014.63620186357,
			"y": -3533.7971348841784,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 785.3328087117804,
			"height": 670.0260074326698,
			"seed": 112630398,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "aAXK3BkfvbyYKR7pE8DfQ",
					"type": "arrow"
				}
			],
			"updated": 1693689492386,
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
			"type": "arrow",
			"version": 52,
			"versionNonce": 350501724,
			"isDeleted": false,
			"id": "aAXK3BkfvbyYKR7pE8DfQ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3863.661282613328,
			"y": -3097.9907426915306,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 149.20202379664488,
			"height": 129.87966649368673,
			"seed": 1227952610,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492386,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					149.20202379664488,
					-129.87966649368673
				]
			]
		},
		{
			"type": "image",
			"version": 95,
			"versionNonce": 1192540260,
			"isDeleted": false,
			"id": "j1SWFSNhGa3R86-A4TQOE",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4007.300589164267,
			"y": -4084.26387107757,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 825.0138097214664,
			"height": 381.5092761717764,
			"seed": 1721660258,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492386,
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
			"type": "arrow",
			"version": 51,
			"versionNonce": 1811705820,
			"isDeleted": false,
			"id": "RLUkEL1BGck52YLce3o_f",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4414.845052385159,
			"y": -3533.034884519741,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.4452838438101026,
			"height": 159.9556930506842,
			"seed": 632663102,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492386,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "j1SWFSNhGa3R86-A4TQOE",
				"focus": -0.006725171725662479,
				"gap": 9.76401733536818
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
					3.4452838438101026,
					-159.9556930506842
				]
			]
		},
		{
			"type": "image",
			"version": 106,
			"versionNonce": 875039716,
			"isDeleted": false,
			"id": "QtUn3g4CxEk_dHoTtRv9Q",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4986.281589997467,
			"y": -4532.329141339253,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 899.9837758439571,
			"height": 383.9216504096246,
			"seed": 284384994,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "z5DxXU2PkkD9nL76DPdy2",
					"type": "arrow"
				}
			],
			"updated": 1693689492387,
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
			"type": "arrow",
			"version": 55,
			"versionNonce": 186258524,
			"isDeleted": false,
			"id": "z5DxXU2PkkD9nL76DPdy2",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4831.9915268498,
			"y": -4011.3813811403297,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 150.52397167309664,
			"height": 262.0402067845689,
			"seed": 144354238,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492387,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "QtUn3g4CxEk_dHoTtRv9Q",
				"focus": 0.7412659105425456,
				"gap": 3.766091474570203
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
					150.52397167309664,
					-262.0402067845689
				]
			]
		},
		{
			"type": "image",
			"version": 84,
			"versionNonce": 1518661476,
			"isDeleted": false,
			"id": "wfb7M3gVgnWLzy5DpEkKO",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4994.7052582284605,
			"y": -4096.275067968423,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 895.4965348630544,
			"height": 882.7297818202003,
			"seed": 550659682,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492387,
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
			"type": "arrow",
			"version": 45,
			"versionNonce": 806299868,
			"isDeleted": false,
			"id": "Vq6PYQi7MmlvOJOTPgMhc",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 4838.272491630656,
			"y": -3840.3021474090365,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 145.59920212299858,
			"height": 43.405096855315605,
			"seed": 1070485602,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492387,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					145.59920212299858,
					43.405096855315605
				]
			]
		},
		{
			"type": "image",
			"version": 124,
			"versionNonce": 2054775524,
			"isDeleted": false,
			"id": "J3Y9HqOmAZQm7s4LGy-45",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 6015.490150055246,
			"y": -4075.2199101037045,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 850.5483394929693,
			"height": 850.5483394929693,
			"seed": 386707774,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492387,
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
			"type": "arrow",
			"version": 37,
			"versionNonce": 242068828,
			"isDeleted": false,
			"id": "8jRc7W5FuPrramsfiRcnH",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 5891.631304462309,
			"y": -3748.487394908773,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 120.82566383193534,
			"height": 6.174816969307358,
			"seed": 432251134,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492387,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					120.82566383193534,
					-6.174816969307358
				]
			]
		},
		{
			"type": "image",
			"version": 57,
			"versionNonce": 445867620,
			"isDeleted": false,
			"id": "a_tg_dSRudUDNXu3eIoxx",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 7015.997508303727,
			"y": -3805.4944185858612,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1156.533888205735,
			"height": 468.066760256152,
			"seed": 775569442,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492387,
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
			"type": "image",
			"version": 64,
			"versionNonce": 394764764,
			"isDeleted": false,
			"id": "Gx1xNqfKce3JwJXBrzPzN",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 7000.715031355414,
			"y": -4705.252397579941,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1191.3531811009698,
			"height": 748.444543196633,
			"seed": 1897782242,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492387,
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
			"type": "arrow",
			"version": 60,
			"versionNonce": 1067514340,
			"isDeleted": false,
			"id": "MtfI6yVgDfCEy6W9UKGm-",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 6512.285548863496,
			"y": -4080.735565450333,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 481.72534359102247,
			"height": 318.3570728602449,
			"seed": 1871047166,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492388,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					481.72534359102247,
					-318.3570728602449
				]
			]
		},
		{
			"type": "arrow",
			"version": 43,
			"versionNonce": 1114572380,
			"isDeleted": false,
			"id": "oRkBjbwf-MDnc1HbRo8SZ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 7571.7371640211895,
			"y": -3798.531194555525,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.31378594459784,
			"height": 160.01648329025375,
			"seed": 135374910,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492388,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-12.31378594459784,
					-160.01648329025375
				]
			]
		},
		{
			"type": "image",
			"version": 104,
			"versionNonce": 615521636,
			"isDeleted": false,
			"id": "DxEMZcYMLY7A0xL4n4Gc2",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 8344.35922273918,
			"y": -4745.075973466666,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1238.8544898458354,
			"height": 1367.1727515059501,
			"seed": 427661602,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "QtYpveVSiu8FurcPSn3cD",
					"type": "arrow"
				}
			],
			"updated": 1693689492388,
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
			"type": "arrow",
			"version": 39,
			"versionNonce": 1408621276,
			"isDeleted": false,
			"id": "QtYpveVSiu8FurcPSn3cD",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 8196.926179665435,
			"y": -4316.149342155366,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 146.67206751768572,
			"height": 6.121044978282953,
			"seed": 2037065086,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492388,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					146.67206751768572,
					6.121044978282953
				]
			]
		},
		{
			"type": "text",
			"version": 231,
			"versionNonce": 1930350820,
			"isDeleted": false,
			"id": "gLkrphHI",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 7586.4544621861605,
			"y": -4932.582259421519,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1347.6602783203125,
			"height": 135,
			"seed": 1757249214,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "ValraBa_JGVci4bGN2nmd",
					"type": "arrow"
				}
			],
			"updated": 1693689492388,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "SO MODERNI NON USANO IL BANCHIERE PERCHE:\n1) Molto costoso quindi ha senso utilizzarlo solo in situazioni molto critiche.\n2) Dobbiamo sapere in anticipo quello di cui ogni processo ha bisogno.",
			"rawText": "SO MODERNI NON USANO IL BANCHIERE PERCHE:\n1) Molto costoso quindi ha senso utilizzarlo solo in situazioni molto critiche.\n2) Dobbiamo sapere in anticipo quello di cui ogni processo ha bisogno.",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "SO MODERNI NON USANO IL BANCHIERE PERCHE:\n1) Molto costoso quindi ha senso utilizzarlo solo in situazioni molto critiche.\n2) Dobbiamo sapere in anticipo quello di cui ogni processo ha bisogno.",
			"lineHeight": 1.25,
			"baseline": 122
		},
		{
			"type": "arrow",
			"version": 109,
			"versionNonce": 648945500,
			"isDeleted": false,
			"id": "ValraBa_JGVci4bGN2nmd",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 7506.377308930969,
			"y": -4698.504046333211,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 370.672559678007,
			"height": 97.2016099355751,
			"seed": 721975202,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492388,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "gLkrphHI",
				"focus": 0.1274335832436313,
				"gap": 1.8766031527329687
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
					370.672559678007,
					-97.2016099355751
				]
			]
		},
		{
			"type": "arrow",
			"version": 172,
			"versionNonce": 2051740772,
			"isDeleted": false,
			"id": "Mg5ufHxZHpO6a_7DaZFTG",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 6224.363501901818,
			"y": -4096.124680854112,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 153.54963115439477,
			"height": 440.56069919930724,
			"seed": 2139794722,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492388,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					153.54963115439477,
					-440.56069919930724
				]
			]
		},
		{
			"type": "image",
			"version": 190,
			"versionNonce": 1927926748,
			"isDeleted": false,
			"id": "m_-yorqLDiftg-xstkLVq",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 5079.245011926007,
			"y": -5589.754113175659,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 883.2594567095422,
			"height": 775.912358559342,
			"seed": 294230498,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "5Bm3u2tbBsVMrgh6Zpv4C",
					"type": "arrow"
				}
			],
			"updated": 1693689492388,
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
			"type": "text",
			"version": 95,
			"versionNonce": 1748166628,
			"isDeleted": false,
			"id": "AGwbIvvQ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 6194.102185542844,
			"y": -4636.4514515655355,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 680.0872802734375,
			"height": 92.70946137671666,
			"seed": 274930110,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492388,
			"link": null,
			"locked": false,
			"fontSize": 74.16756910137333,
			"fontFamily": 1,
			"text": "FILOSOFI A CENA",
			"rawText": "FILOSOFI A CENA",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "FILOSOFI A CENA",
			"lineHeight": 1.25,
			"baseline": 65
		},
		{
			"type": "arrow",
			"version": 43,
			"versionNonce": 381352028,
			"isDeleted": false,
			"id": "5Bm3u2tbBsVMrgh6Zpv4C",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 6357.179813976551,
			"y": -4642.743899768747,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 378.6584918752833,
			"height": 283.67626899715196,
			"seed": 1683076450,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492389,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-378.6584918752833,
					-283.67626899715196
				]
			]
		},
		{
			"type": "text",
			"version": 350,
			"versionNonce": 13912932,
			"isDeleted": false,
			"id": "mH952EYF",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0.6480166053405494,
			"x": 6000.183054608064,
			"y": -4827.513421914426,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 447.3307189941406,
			"height": 47.393822832815346,
			"seed": 1424919550,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492389,
			"link": null,
			"locked": false,
			"fontSize": 37.915058266252274,
			"fontFamily": 1,
			"text": "ORDINE ASSIMETRICO",
			"rawText": "ORDINE ASSIMETRICO",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "ORDINE ASSIMETRICO",
			"lineHeight": 1.25,
			"baseline": 33
		},
		{
			"type": "image",
			"version": 153,
			"versionNonce": 1576242396,
			"isDeleted": false,
			"id": "bmJPlCjNbTM42ZQiSYuTN",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 6055.6234156520795,
			"y": -5787.156172911819,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1043.3167291273198,
			"height": 578.8423911041953,
			"seed": 1750257022,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "1XTmi1sLHhsdeaTIveQSA",
					"type": "arrow"
				}
			],
			"updated": 1693689492389,
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
			"type": "arrow",
			"version": 116,
			"versionNonce": 1451048676,
			"isDeleted": false,
			"id": "1XTmi1sLHhsdeaTIveQSA",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 6597.768694582847,
			"y": -4638.784820986259,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 45.71238447027008,
			"height": 550.501092962194,
			"seed": 1550119678,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492389,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-45.71238447027008,
					-550.501092962194
				]
			]
		},
		{
			"type": "text",
			"version": 74,
			"versionNonce": 1243976028,
			"isDeleted": false,
			"id": "CXj6MQ8J",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 6425.315937621934,
			"y": -4825.267572397425,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 312.6241455078125,
			"height": 45,
			"seed": 1110088930,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492389,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "ATTESA ATTIVA",
			"rawText": "ATTESA ATTIVA",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "ATTESA ATTIVA",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "text",
			"version": 63,
			"versionNonce": 29082212,
			"isDeleted": false,
			"id": "GLbtvMY0",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 6201.43443775022,
			"y": -5848.917306942856,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 816.1090087890625,
			"height": 59.008863499142336,
			"seed": 458898018,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492389,
			"link": null,
			"locked": false,
			"fontSize": 47.20709079931387,
			"fontFamily": 1,
			"text": "(FAIRNESS -> ATTESA INFINITA)",
			"rawText": "(FAIRNESS -> ATTESA INFINITA)",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "(FAIRNESS -> ATTESA INFINITA)",
			"lineHeight": 1.25,
			"baseline": 41
		},
		{
			"type": "image",
			"version": 110,
			"versionNonce": 1520633308,
			"isDeleted": false,
			"id": "VRKZ1hpfnXF5MuCYJRcce",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 7186.7896234426,
			"y": -5743.581921356387,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1032.479645668995,
			"height": 721.733344545317,
			"seed": 2140699902,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "VmtHpnMxkK0CvMntpx2on",
					"type": "arrow"
				}
			],
			"updated": 1693689492389,
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
			"type": "arrow",
			"version": 58,
			"versionNonce": 1499321828,
			"isDeleted": false,
			"id": "VmtHpnMxkK0CvMntpx2on",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 6803.073185219953,
			"y": -4641.002328628931,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 378.6249679799348,
			"height": 420.6997651652482,
			"seed": 852379646,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492389,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					378.6249679799348,
					-420.6997651652482
				]
			]
		},
		{
			"type": "text",
			"version": 139,
			"versionNonce": 1417538140,
			"isDeleted": false,
			"id": "lAZZVzmI",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 5.456338198765785,
			"x": 6817.2363101203255,
			"y": -4944.955137076269,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 322.44427490234375,
			"height": 82.45659648600895,
			"seed": 1316202558,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492389,
			"link": null,
			"locked": false,
			"fontSize": 65.96527718880716,
			"fontFamily": 1,
			"text": "MONITOR",
			"rawText": "MONITOR",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "MONITOR",
			"lineHeight": 1.25,
			"baseline": 57
		},
		{
			"type": "image",
			"version": 115,
			"versionNonce": 712079716,
			"isDeleted": false,
			"id": "7D3V9hIkMZRbuHM1ff6kO",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -375.7005090138946,
			"y": 1015.8455435573348,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 978.7129375290857,
			"height": 1175.2338255816455,
			"seed": 1087179874,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492390,
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
			"type": "arrow",
			"version": 143,
			"versionNonce": 980154138,
			"isDeleted": false,
			"id": "1zSJSVm4na2xlYGnaot8p",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -66.40748334241789,
			"y": -80.69633642483632,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 37.52281864821339,
			"height": 1091.7110907350475,
			"seed": 1626092158,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693746738810,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					37.52281864821339,
					1091.7110907350475
				]
			]
		},
		{
			"type": "text",
			"version": 1272,
			"versionNonce": 1883548900,
			"isDeleted": false,
			"id": "iAfEmFao",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1247.6353641777218,
			"y": 2383.6970266390913,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1314.5045166015625,
			"height": 1170,
			"seed": 1264154338,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
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
			"updated": 1693689492390,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "ALGORITMI: (QDT = QUANTO DI TEMPO)\n1) FIFO -> ESEGUIAMO TASK IN ORDINE DI ARRIVO\n\n2) SJF -> ESEGUIAMO PRIMA I TASK + VELOCI\n\n2.1) PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nMI FERMO ED PASSO A QUELLO, SUCCESSIVAMENTE RIPRENDO\nDA DOVE MI ERO FERMATO.\n\n2.2) NO PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nFINISCO IL TASK CORRENTE E POI PASSO A QUELLO\n\n3) ROUND ROBIN -> OGNI TASK ACQUISISCE LA CPU PER UN\nQUANTO DI TEMPO, QUANDO SI ESAURISCE PASSO AL TASK \nSUCCESSIVO (CON PRERILASCIO) E MI METTO IN FONDO\nALLA CODA\n\n4) MAX-MIN FAIRNESS -> ROUND ROBIN ASSEGNANDO IL\nAD OGNI TASK UNA PORZIONE DI QUANTO DI TEMPO\n\n5)MFQ -> N CODE ROUND ROBIN CON PRIORITA E QUANTO\nDI TEMPO SPECIFICO, + PRIORITA IMPLICA UN QDT \n+ PICCOLO E VICEVERSA. SE SCADE IL QDT IL TASK SCENDE\n DI PRIORITA, SE RILASCIAMO IL PROCESSORE VOLONTARIAMENTE \nRIMANIAMO NELLA CODA CORRENTE E INFINE SE IL PROCESSO SI \nSOSPENDE SALE DI PRIORITA",
			"rawText": "ALGORITMI: (QDT = QUANTO DI TEMPO)\n1) FIFO -> ESEGUIAMO TASK IN ORDINE DI ARRIVO\n\n2) SJF -> ESEGUIAMO PRIMA I TASK + VELOCI\n\n2.1) PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nMI FERMO ED PASSO A QUELLO, SUCCESSIVAMENTE RIPRENDO\nDA DOVE MI ERO FERMATO.\n\n2.2) NO PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nFINISCO IL TASK CORRENTE E POI PASSO A QUELLO\n\n3) ROUND ROBIN -> OGNI TASK ACQUISISCE LA CPU PER UN\nQUANTO DI TEMPO, QUANDO SI ESAURISCE PASSO AL TASK \nSUCCESSIVO (CON PRERILASCIO) E MI METTO IN FONDO\nALLA CODA\n\n4) MAX-MIN FAIRNESS -> ROUND ROBIN ASSEGNANDO IL\nAD OGNI TASK UNA PORZIONE DI QUANTO DI TEMPO\n\n5)MFQ -> N CODE ROUND ROBIN CON PRIORITA E QUANTO\nDI TEMPO SPECIFICO, + PRIORITA IMPLICA UN QDT \n+ PICCOLO E VICEVERSA. SE SCADE IL QDT IL TASK SCENDE\n DI PRIORITA, SE RILASCIAMO IL PROCESSORE VOLONTARIAMENTE \nRIMANIAMO NELLA CODA CORRENTE E INFINE SE IL PROCESSO SI \nSOSPENDE SALE DI PRIORITA",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "ALGORITMI: (QDT = QUANTO DI TEMPO)\n1) FIFO -> ESEGUIAMO TASK IN ORDINE DI ARRIVO\n\n2) SJF -> ESEGUIAMO PRIMA I TASK + VELOCI\n\n2.1) PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nMI FERMO ED PASSO A QUELLO, SUCCESSIVAMENTE RIPRENDO\nDA DOVE MI ERO FERMATO.\n\n2.2) NO PRERILASCIO -> QUANDO ARRIVA UN TASK + VELOCE\nFINISCO IL TASK CORRENTE E POI PASSO A QUELLO\n\n3) ROUND ROBIN -> OGNI TASK ACQUISISCE LA CPU PER UN\nQUANTO DI TEMPO, QUANDO SI ESAURISCE PASSO AL TASK \nSUCCESSIVO (CON PRERILASCIO) E MI METTO IN FONDO\nALLA CODA\n\n4) MAX-MIN FAIRNESS -> ROUND ROBIN ASSEGNANDO IL\nAD OGNI TASK UNA PORZIONE DI QUANTO DI TEMPO\n\n5)MFQ -> N CODE ROUND ROBIN CON PRIORITA E QUANTO\nDI TEMPO SPECIFICO, + PRIORITA IMPLICA UN QDT \n+ PICCOLO E VICEVERSA. SE SCADE IL QDT IL TASK SCENDE\n DI PRIORITA, SE RILASCIAMO IL PROCESSORE VOLONTARIAMENTE \nRIMANIAMO NELLA CODA CORRENTE E INFINE SE IL PROCESSO SI \nSOSPENDE SALE DI PRIORITA",
			"lineHeight": 1.25,
			"baseline": 1157
		},
		{
			"type": "arrow",
			"version": 1710,
			"versionNonce": 626262876,
			"isDeleted": false,
			"id": "6cy3UyOrAM3xu44bTXUN3",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -45.12051839626275,
			"y": 2197.749376315361,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 217.77725125865834,
			"height": 161.89362534102384,
			"seed": 800779198,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492390,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					-217.77725125865834,
					161.89362534102384
				]
			]
		},
		{
			"type": "text",
			"version": 257,
			"versionNonce": 207974500,
			"isDeleted": false,
			"id": "ahyRjWNk",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1278.2579536642068,
			"y": 3723.205430377718,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1227.780517578125,
			"height": 180,
			"seed": 1102463294,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "qbt8CuDUZNX_3hr3qm4I0",
					"type": "arrow"
				}
			],
			"updated": 1693689492390,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "PRIORITY INVERSION -> SE UN TASK STA FERMO DA UN PO' LO\nSCHEDULER LO SVEGLIA E GLI DA UN BOOST DI PRIORITA\n(EX: UN THREAD SOSPESO CHE ATTENDE DI ESSERE SVEGLIATO\nDA UN THREAD DI PRIORITA MOLTO INFERIORE)",
			"rawText": "PRIORITY INVERSION -> SE UN TASK STA FERMO DA UN PO' LO\nSCHEDULER LO SVEGLIA E GLI DA UN BOOST DI PRIORITA\n(EX: UN THREAD SOSPESO CHE ATTENDE DI ESSERE SVEGLIATO\nDA UN THREAD DI PRIORITA MOLTO INFERIORE)",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "PRIORITY INVERSION -> SE UN TASK STA FERMO DA UN PO' LO\nSCHEDULER LO SVEGLIA E GLI DA UN BOOST DI PRIORITA\n(EX: UN THREAD SOSPESO CHE ATTENDE DI ESSERE SVEGLIATO\nDA UN THREAD DI PRIORITA MOLTO INFERIORE)",
			"lineHeight": 1.25,
			"baseline": 167
		},
		{
			"type": "arrow",
			"version": 55,
			"versionNonce": 1798518748,
			"isDeleted": false,
			"id": "qbt8CuDUZNX_3hr3qm4I0",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -809.741009475543,
			"y": 3573.0017932303895,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.25379625298092,
			"height": 142.4916025712705,
			"seed": 1312532862,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492390,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					10.25379625298092,
					142.4916025712705
				]
			]
		},
		{
			"type": "image",
			"version": 61,
			"versionNonce": 2124530660,
			"isDeleted": false,
			"id": "bN2yUoNTdjLwAY1EWH_CE",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 193.2507115044666,
			"y": 2984.8789833533388,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1286.1357768365524,
			"height": 593.2301270658598,
			"seed": 1684107170,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "68i9wqr-BQZ1J7C0Nve9g",
					"type": "arrow"
				}
			],
			"updated": 1693689492391,
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
			"type": "arrow",
			"version": 162,
			"versionNonce": 137878620,
			"isDeleted": false,
			"id": "68i9wqr-BQZ1J7C0Nve9g",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 68.41009151054391,
			"y": 2904.889275409446,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 117.79440359597311,
			"height": 155.87927724395786,
			"seed": 1921342050,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492391,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					117.79440359597311,
					155.87927724395786
				]
			]
		},
		{
			"type": "rectangle",
			"version": 101,
			"versionNonce": 487040868,
			"isDeleted": false,
			"id": "3rmMBz2V577zAZST9tMiL",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1269.8829707270156,
			"y": 2370.5820777273866,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1329.616529972905,
			"height": 1199.2917535491447,
			"seed": 1756205310,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
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
			"updated": 1693689492391,
			"link": null,
			"locked": false
		},
		{
			"type": "image",
			"version": 92,
			"versionNonce": 1446244572,
			"isDeleted": false,
			"id": "XCd17DPn",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 592.5774490157419,
			"y": 4105.987360518386,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1106.4515138185275,
			"height": 801.9113735968415,
			"seed": 51722,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "uOwYduGeW-m5yzMxMsCpT",
					"type": "arrow"
				},
				{
					"id": "JK9B4dgtDrUMlZfyeDhAm",
					"type": "arrow"
				},
				{
					"id": "8im3i7WVUOLfNAzpcWE4W",
					"type": "arrow"
				},
				{
					"id": "ARBHeTsODlk9wUjHs4wm8",
					"type": "arrow"
				}
			],
			"updated": 1693689492391,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "3541300b2dbb9244501297335f434a757747f70a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 188,
			"versionNonce": 1273305828,
			"isDeleted": false,
			"id": "uOwYduGeW-m5yzMxMsCpT",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 45.513510546860516,
			"y": 3566.7839456691145,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 803.9867141496779,
			"height": 530.8595771258297,
			"seed": 1999358306,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492391,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
			"points": [
				[
					0,
					0
				],
				[
					803.9867141496779,
					530.8595771258297
				]
			]
		},
		{
			"type": "text",
			"version": 169,
			"versionNonce": 616133980,
			"isDeleted": false,
			"id": "GRVkWSDo",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0.5398972279282415,
			"x": 146.79765982401727,
			"y": 3728.0276770549012,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 512.515380859375,
			"height": 67.94244500707737,
			"seed": 1181850658,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492391,
			"link": null,
			"locked": false,
			"fontSize": 54.3539560056619,
			"fontFamily": 1,
			"text": "MULTIPROCESSOR",
			"rawText": "MULTIPROCESSOR",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "MULTIPROCESSOR",
			"lineHeight": 1.25,
			"baseline": 47
		},
		{
			"type": "text",
			"version": 343,
			"versionNonce": 902307428,
			"isDeleted": false,
			"id": "4afkSfBr",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1520.0252472229229,
			"y": 4230.263795159231,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"width": 115.2547607421875,
			"height": 70.47033553540274,
			"seed": 215281698,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492391,
			"link": null,
			"locked": false,
			"fontSize": 56.37626842832219,
			"fontFamily": 1,
			"text": "MFQ",
			"rawText": "MFQ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "MFQ",
			"lineHeight": 1.25,
			"baseline": 49
		},
		{
			"type": "text",
			"version": 145,
			"versionNonce": 18508252,
			"isDeleted": false,
			"id": "xwDxYI34",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1166.374837854006,
			"y": 3799.8518300960295,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1511.3525390625,
			"height": 90,
			"seed": 1382484770,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "JK9B4dgtDrUMlZfyeDhAm",
					"type": "arrow"
				}
			],
			"updated": 1693689492391,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "AFFINITY SCHEDULING -> ASSEGNARE IL PROCESSO AL PROCESSORE + AFFINE \n(QUELLO CHE DETIENE I DATI CHE MODIFICA IL TASK DEL CASO)",
			"rawText": "AFFINITY SCHEDULING -> ASSEGNARE IL PROCESSO AL PROCESSORE + AFFINE \n(QUELLO CHE DETIENE I DATI CHE MODIFICA IL TASK DEL CASO)",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "AFFINITY SCHEDULING -> ASSEGNARE IL PROCESSO AL PROCESSORE + AFFINE \n(QUELLO CHE DETIENE I DATI CHE MODIFICA IL TASK DEL CASO)",
			"lineHeight": 1.25,
			"baseline": 77
		},
		{
			"type": "arrow",
			"version": 144,
			"versionNonce": 58634724,
			"isDeleted": false,
			"id": "JK9B4dgtDrUMlZfyeDhAm",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 958.8684548708432,
			"y": 4100.702515462554,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 210.49848730613166,
			"height": 248.7856353694333,
			"seed": 709555006,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492392,
			"link": null,
			"locked": false,
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
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "triangle",
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
			]
		},
		{
			"type": "image",
			"version": 143,
			"versionNonce": 2120797788,
			"isDeleted": false,
			"id": "dYpybeGJBHiZyXmMb1KYv",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -926.8773692756317,
			"y": 4273.868639163048,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1286.7740701824926,
			"height": 1064.3483346195778,
			"seed": 213447330,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "VWAlwdtgv2NyqGn5dlMQg",
					"type": "arrow"
				},
				{
					"id": "h038ezCf3rCaDqPoM13rI",
					"type": "arrow"
				}
			],
			"updated": 1693689492392,
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
			"type": "arrow",
			"version": 103,
			"versionNonce": 337040740,
			"isDeleted": false,
			"id": "VWAlwdtgv2NyqGn5dlMQg",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 451.11769053307694,
			"y": 3855.7344034628622,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 290.23125553669115,
			"height": 402.89171719746355,
			"seed": 1459354174,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492392,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "dYpybeGJBHiZyXmMb1KYv",
				"focus": 0.048730490413972545,
				"gap": 15.24251850272185
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
					-290.23125553669115,
					402.89171719746355
				]
			]
		},
		{
			"type": "text",
			"version": 51,
			"versionNonce": 2104926940,
			"isDeleted": false,
			"id": "YR8inbTo",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2617.9472462873914,
			"y": 4640.061291753219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1606.428466796875,
			"height": 45,
			"seed": 1164272228,
			"groupIds": [
				"GqLqTHx4vXfy9zd8Son4o"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "h038ezCf3rCaDqPoM13rI",
					"type": "arrow"
				}
			],
			"updated": 1693689492392,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "Nella bsp ci sono thread di lunghezza variabile che vengono eseguiti, prima di passare alla",
			"rawText": "Nella bsp ci sono thread di lunghezza variabile che vengono eseguiti, prima di passare alla",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Nella bsp ci sono thread di lunghezza variabile che vengono eseguiti, prima di passare alla",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "text",
			"version": 50,
			"versionNonce": 886999268,
			"isDeleted": false,
			"id": "LANKscsX",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2617.9472462873914,
			"y": 4695.061291753219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1445.112548828125,
			"height": 45,
			"seed": 937649628,
			"groupIds": [
				"GqLqTHx4vXfy9zd8Son4o"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492392,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "prossima esecuzione c’è però una barriera, i thread devono infatti sincronizzarsi.",
			"rawText": "prossima esecuzione c’è però una barriera, i thread devono infatti sincronizzarsi.",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "prossima esecuzione c’è però una barriera, i thread devono infatti sincronizzarsi.",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "text",
			"version": 52,
			"versionNonce": 1960175452,
			"isDeleted": false,
			"id": "fPQzxBrZ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2617.9472462873914,
			"y": 4755.061291753219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1084.6083984375,
			"height": 45,
			"seed": 919827940,
			"groupIds": [
				"GqLqTHx4vXfy9zd8Son4o"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693689492392,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "Il tempo di esecuzione è dettato quindi dal thread più lungo",
			"rawText": "Il tempo di esecuzione è dettato quindi dal thread più lungo",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Il tempo di esecuzione è dettato quindi dal thread più lungo",
			"lineHeight": 1.25,
			"baseline": 32
		},
		{
			"type": "arrow",
			"version": 97,
			"versionNonce": 1499712612,
			"isDeleted": false,
			"id": "h038ezCf3rCaDqPoM13rI",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -937.9472462873914,
			"y": 4465.061291753219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 599.9999999999998,
			"height": 180,
			"seed": 112169956,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492392,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "dYpybeGJBHiZyXmMb1KYv",
				"focus": 0.6039270309030671,
				"gap": 11.069877011759672
			},
			"endBinding": {
				"elementId": "YR8inbTo",
				"focus": 0.3283098595574018,
				"gap": 5
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
					-532.4999999999998,
					-10
				],
				[
					-599.9999999999998,
					170
				]
			]
		},
		{
			"type": "image",
			"version": 54,
			"versionNonce": 953719772,
			"isDeleted": false,
			"id": "xjd1I3YifkiLZGIUquEcJ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1894.552753712609,
			"y": 4728.061291753219,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1414.9999999999995,
			"height": 674.8461538461537,
			"seed": 1024577756,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "oS-MTjA0L-iAg7skZNUk9",
					"type": "arrow"
				}
			],
			"updated": 1693689492392,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "00191f0ba092228633209e228aa7affc2212547a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 79,
			"versionNonce": 1400152036,
			"isDeleted": false,
			"id": "oS-MTjA0L-iAg7skZNUk9",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1694.5527537126086,
			"y": 4536.030615322698,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 697.5000000000005,
			"height": 213.56550168296542,
			"seed": 1050942180,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492393,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "xjd1I3YifkiLZGIUquEcJ",
				"focus": 0.13000393435540272,
				"gap": 10.500000000000455
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
					485.3947368421057,
					-32.03482525244481
				],
				[
					697.5000000000005,
					181.53067643052063
				]
			]
		},
		{
			"type": "image",
			"version": 64,
			"versionNonce": 1133559900,
			"isDeleted": false,
			"id": "knrcoNiy7MeGwjSu-gDCL",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 467.0527537126088,
			"y": 5336.061291753219,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1356.9646799116992,
			"height": 675.4999999999998,
			"seed": 1118525796,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "8im3i7WVUOLfNAzpcWE4W",
					"type": "arrow"
				}
			],
			"updated": 1693689492393,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "35e11bf9682e5fedf799263320562726c4dbb687",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 33,
			"versionNonce": 186581860,
			"isDeleted": false,
			"id": "8im3i7WVUOLfNAzpcWE4W",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1172.5722422810015,
			"y": 4915.061291753219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.8073099527882732,
			"height": 407.5,
			"seed": 3134564,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492393,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "XCd17DPn",
				"focus": -0.04384830792495182,
				"gap": 7.16255763799154
			},
			"endBinding": {
				"elementId": "knrcoNiy7MeGwjSu-gDCL",
				"focus": 0.042023512351687775,
				"gap": 13.5
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
					0.8073099527882732,
					407.5
				]
			]
		},
		{
			"type": "image",
			"version": 44,
			"versionNonce": 2094027996,
			"isDeleted": false,
			"id": "faNjAI4QVgKTyD0mSorak",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2378.052753712609,
			"y": 4022.061291753219,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1368.6386292834904,
			"height": 461.0000000000004,
			"seed": 975477220,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "ARBHeTsODlk9wUjHs4wm8",
					"type": "arrow"
				}
			],
			"updated": 1693689492393,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "9e601f3a5891476cc21b146c71af34dbf552ed46",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 43,
			"versionNonce": 917567204,
			"isDeleted": false,
			"id": "ARBHeTsODlk9wUjHs4wm8",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1704.5527537126086,
			"y": 4255.061291753219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 670.0000000000005,
			"height": 75,
			"seed": 139601764,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492393,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "XCd17DPn",
				"focus": -0.40903377010047665,
				"gap": 5.523790878339241
			},
			"endBinding": {
				"elementId": "faNjAI4QVgKTyD0mSorak",
				"focus": 0.48679024305162444,
				"gap": 3.5
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
					670.0000000000005,
					-75
				]
			]
		},
		{
			"type": "text",
			"version": 129,
			"versionNonce": 36264284,
			"isDeleted": false,
			"id": "csv9an0l",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -5186.256770096917,
			"y": 2537.3231965151267,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 860.0650024414062,
			"height": 84.99999999999997,
			"seed": 1876956892,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "QPtsrmgsemiC3vXa7MSqy",
					"type": "arrow"
				}
			],
			"updated": 1693689492393,
			"link": null,
			"locked": false,
			"fontSize": 67.99999999999997,
			"fontFamily": 1,
			"text": "ADDRESS TRANSLATION",
			"rawText": "ADDRESS TRANSLATION",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "ADDRESS TRANSLATION",
			"lineHeight": 1.25,
			"baseline": 60
		},
		{
			"type": "rectangle",
			"version": 74,
			"versionNonce": 905171172,
			"isDeleted": false,
			"id": "oCXYkXzwh9Y5X0mTOrd5p",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -5232.923436763585,
			"y": 2503.9898631817923,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 973.3333333333339,
			"height": 133.33333333333326,
			"seed": 1525060580,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "QSIKvlQnYJLZVLcCiRh1l",
					"type": "arrow"
				},
				{
					"id": "ghWKvZnajcFiFm5wroEI8",
					"type": "arrow"
				},
				{
					"id": "QPtsrmgsemiC3vXa7MSqy",
					"type": "arrow"
				},
				{
					"id": "Q9ofxvbH9_9gotaON1lyP",
					"type": "arrow"
				},
				{
					"id": "pdEF1MMhFqfv1H29n1ZJe",
					"type": "arrow"
				},
				{
					"id": "dB1p5FJvXVScv8NQpYpjN",
					"type": "arrow"
				}
			],
			"updated": 1693694318727,
			"link": null,
			"locked": false
		},
		{
			"type": "image",
			"version": 257,
			"versionNonce": 9586396,
			"isDeleted": false,
			"id": "PUrNR7rQgMfxGhL1C9cZC",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -5408.256770096919,
			"y": 1406.8231965151267,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1477.333333333334,
			"height": 669.6947791164662,
			"seed": 78112612,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "QSIKvlQnYJLZVLcCiRh1l",
					"type": "arrow"
				}
			],
			"updated": 1693694322948,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "6d192e9ecfd1f127040f49016d924509cbf06a7a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 575,
			"versionNonce": 1549483996,
			"isDeleted": false,
			"id": "QSIKvlQnYJLZVLcCiRh1l",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -4744.712479667889,
			"y": 2493.9898631817923,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 92.16778831988995,
			"height": 394.6385542168655,
			"seed": 1178534492,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693694322949,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "oCXYkXzwh9Y5X0mTOrd5p",
				"focus": -0.033491686460808294,
				"gap": 9.999999999999886
			},
			"endBinding": {
				"elementId": "PUrNR7rQgMfxGhL1C9cZC",
				"focus": -0.12313057673097913,
				"gap": 22.833333333333712
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
					92.16778831988995,
					-394.6385542168655
				]
			]
		},
		{
			"type": "image",
			"version": 168,
			"versionNonce": 392641116,
			"isDeleted": false,
			"id": "ePeSelMdwJVQ_EP4aEKgp",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -8990.090103430251,
			"y": 1262.323196515125,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1571.8181818181813,
			"height": 699.9999999999998,
			"seed": 1048751588,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "ghWKvZnajcFiFm5wroEI8",
					"type": "arrow"
				},
				{
					"id": "dOcpqU7__of5Zb_VKRcaf",
					"type": "arrow"
				},
				{
					"id": "Lhg7JPeISSmGXvJYoF8Zz",
					"type": "arrow"
				}
			],
			"updated": 1693697877986,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "a456e8d616a72eb2522d24bb787f2a57f55106c6",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 337,
			"versionNonce": 438915932,
			"isDeleted": false,
			"id": "ghWKvZnajcFiFm5wroEI8",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -5245.565061980859,
			"y": 2537.3231965151253,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 2154.025041449393,
			"height": 772.6197292905285,
			"seed": 1219696484,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693697877986,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "oCXYkXzwh9Y5X0mTOrd5p",
				"focus": -0.6033056213664323,
				"gap": 12.64162521727394
			},
			"endBinding": {
				"elementId": "ePeSelMdwJVQ_EP4aEKgp",
				"focus": -0.21556688724272835,
				"gap": 18.68181818181847
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
					-2154.025041449393,
					-772.6197292905285
				]
			]
		},
		{
			"type": "image",
			"version": 85,
			"versionNonce": 281085660,
			"isDeleted": false,
			"id": "FKPhYTtTAqCbeVsRwdAqw",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -9178.923436763585,
			"y": 2149.1565298484584,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1747.2245862884156,
			"height": 792.9999999999998,
			"seed": 137989348,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "dOcpqU7__of5Zb_VKRcaf",
					"type": "arrow"
				}
			],
			"updated": 1693689492394,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "e39d59e560645cfdac6900dc32cfbf99f84408c5",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 295,
			"versionNonce": 603532380,
			"isDeleted": false,
			"id": "dOcpqU7__of5Zb_VKRcaf",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -8647.176733354145,
			"y": 1968.489863181795,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 91.79049220768866,
			"height": 168.8333333333312,
			"seed": 1425566948,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693697877987,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ePeSelMdwJVQ_EP4aEKgp",
				"focus": 0.6546052930228361,
				"gap": 6.166666666670153
			},
			"endBinding": {
				"elementId": "FKPhYTtTAqCbeVsRwdAqw",
				"focus": -0.025775733629462876,
				"gap": 11.83333333333212
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
					91.79049220768866,
					168.8333333333312
				]
			]
		},
		{
			"type": "text",
			"version": 189,
			"versionNonce": 1014561892,
			"isDeleted": false,
			"id": "hkFJF4Uc",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -8979.590103430255,
			"y": 1100.6565298484595,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1393.913330078125,
			"height": 64.99999999999982,
			"seed": 1440491236,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Lhg7JPeISSmGXvJYoF8Zz",
					"type": "arrow"
				}
			],
			"updated": 1693694284618,
			"link": null,
			"locked": false,
			"fontSize": 51.99999999999985,
			"fontFamily": 1,
			"text": "PROBLEMI: POCO FLESSIBILE E FRAMMENTAZIONE",
			"rawText": "PROBLEMI: POCO FLESSIBILE E FRAMMENTAZIONE",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "PROBLEMI: POCO FLESSIBILE E FRAMMENTAZIONE",
			"lineHeight": 1.25,
			"baseline": 46
		},
		{
			"type": "arrow",
			"version": 325,
			"versionNonce": 476497244,
			"isDeleted": false,
			"id": "Lhg7JPeISSmGXvJYoF8Zz",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -8254.159470633696,
			"y": 1247.3231965151256,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 4.321696248231092,
			"height": 73.33333333333326,
			"seed": 170093156,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693697877987,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ePeSelMdwJVQ_EP4aEKgp",
				"focus": -0.03292083712466538,
				"gap": 14.999999999999545
			},
			"endBinding": {
				"elementId": "hkFJF4Uc",
				"focus": -0.031116274795945528,
				"gap": 8.333333333333144
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
					-4.321696248231092,
					-73.33333333333326
				]
			]
		},
		{
			"type": "image",
			"version": 219,
			"versionNonce": 1071251420,
			"isDeleted": false,
			"id": "wpuZzUVVJ-n-8SAriR3NT",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -5463.755715244595,
			"y": 4311.323196515127,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1697.9989451476767,
			"height": 1072.0632700632684,
			"seed": 1458259940,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "6LUp-UssvhbjFyCpqvAHf",
					"type": "arrow"
				}
			],
			"updated": 1693689492395,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "5caead1268cc985f7db01c97264e767b0654acba",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "image",
			"version": 65,
			"versionNonce": 1118534628,
			"isDeleted": false,
			"id": "puROzBw-KhEkCazLbc9qK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -5994.5901034302515,
			"y": 3008.15652984846,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1783.333333333333,
			"height": 1017.7609427609426,
			"seed": 1657539300,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "QPtsrmgsemiC3vXa7MSqy",
					"type": "arrow"
				},
				{
					"id": "6LUp-UssvhbjFyCpqvAHf",
					"type": "arrow"
				},
				{
					"id": "Uz5DAZeDGu9mYPro4Z7wL",
					"type": "arrow"
				},
				{
					"id": "35qL8J5TXwIuOSjVgPM_n",
					"type": "arrow"
				}
			],
			"updated": 1693689492395,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "546cd0e1266543e6297b5549cf2791c49ab6ded0",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 87,
			"versionNonce": 751150172,
			"isDeleted": false,
			"id": "QPtsrmgsemiC3vXa7MSqy",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -4796.112715132734,
			"y": 2630.65652984846,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 75.50779508384494,
			"height": 373.33333333333303,
			"seed": 2053274852,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492395,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "csv9an0l",
				"focus": 0.06810340847808899,
				"gap": 8.333333333333485
			},
			"endBinding": {
				"elementId": "puROzBw-KhEkCazLbc9qK",
				"focus": 0.12823141644283478,
				"gap": 4.1666666666667425
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
					-75.50779508384494,
					373.33333333333303
				]
			]
		},
		{
			"type": "arrow",
			"version": 252,
			"versionNonce": 656039780,
			"isDeleted": false,
			"id": "6LUp-UssvhbjFyCpqvAHf",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -4827.618427069926,
			"y": 4037.323196515127,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 208.22647915110883,
			"height": 260,
			"seed": 172256100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492395,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "puROzBw-KhEkCazLbc9qK",
				"gap": 11.405723905724471,
				"focus": 0.10683961519750088
			},
			"endBinding": {
				"elementId": "wpuZzUVVJ-n-8SAriR3NT",
				"gap": 14,
				"focus": 0.3409775089721245
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
					208.22647915110883,
					260
				]
			]
		},
		{
			"type": "image",
			"version": 103,
			"versionNonce": 902346972,
			"isDeleted": false,
			"id": "B1KE1C-GT_PLp5SgpD344",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -7689.923436763585,
			"y": 4417.989863181792,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1989.5882352941132,
			"height": 605.333333333332,
			"seed": 1753994340,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Uz5DAZeDGu9mYPro4Z7wL",
					"type": "arrow"
				}
			],
			"updated": 1693689492395,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "fdac1316ee03a2a45ca87d752ba981866ac31b0e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 219,
			"versionNonce": 1927336676,
			"isDeleted": false,
			"id": "Uz5DAZeDGu9mYPro4Z7wL",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -5996.256770096918,
			"y": 3653.0395657792596,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 429.95002938802463,
			"height": 754.2836307358666,
			"seed": 2104432612,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492395,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "puROzBw-KhEkCazLbc9qK",
				"gap": 1.666666666666515,
				"focus": 0.6908918766123399
			},
			"endBinding": {
				"elementId": "B1KE1C-GT_PLp5SgpD344",
				"gap": 10.666666666666515,
				"focus": 0.07737316458713513
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
					-429.95002938802463,
					754.2836307358666
				]
			]
		},
		{
			"type": "image",
			"version": 80,
			"versionNonce": 1182088540,
			"isDeleted": false,
			"id": "rXwE1m8IWeL1MmXuUZPPC",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -3980.83177009692,
			"y": 3157.3231965151263,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1836.1000000000022,
			"height": 406.6666666666672,
			"seed": 545785948,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "35qL8J5TXwIuOSjVgPM_n",
					"type": "arrow"
				}
			],
			"updated": 1693689492395,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "9f7f45a7193e2f59b916a8a8544981085d30001d",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 63,
			"versionNonce": 1955386980,
			"isDeleted": false,
			"id": "35qL8J5TXwIuOSjVgPM_n",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -4206.256770096919,
			"y": 3403.5809028643416,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 220,
			"height": 39.51736729387312,
			"seed": 1376542052,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492395,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "puROzBw-KhEkCazLbc9qK",
				"focus": 0.04061602390911027,
				"gap": 4.999999999999545
			},
			"endBinding": {
				"elementId": "rXwE1m8IWeL1MmXuUZPPC",
				"focus": 0.441214241721377,
				"gap": 5.424999999999272
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
					220,
					-39.51736729387312
				]
			]
		},
		{
			"type": "image",
			"version": 105,
			"versionNonce": 136131036,
			"isDeleted": false,
			"id": "UV8g0mFDq0mmEhTpLypL0",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -8420.756770096918,
			"y": 3131.3231965151263,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1881.551622418878,
			"height": 978.6666666666661,
			"seed": 615309540,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Q9ofxvbH9_9gotaON1lyP",
					"type": "arrow"
				},
				{
					"id": "9JtqcgSt0gp4tbAjtiMZR",
					"type": "arrow"
				},
				{
					"id": "7VE5nd2KJytk5m1nOHz9j",
					"type": "arrow"
				}
			],
			"updated": 1693689492396,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "e4f1eafacc383821b645360c5f6eeb4d1f371a0c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 46,
			"versionNonce": 2028759524,
			"isDeleted": false,
			"id": "Q9ofxvbH9_9gotaON1lyP",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -5242.923436763585,
			"y": 2583.989863181793,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1560,
			"height": 530,
			"seed": 2127114596,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492396,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "oCXYkXzwh9Y5X0mTOrd5p",
				"focus": 0.6698286977343851,
				"gap": 10
			},
			"endBinding": {
				"elementId": "UV8g0mFDq0mmEhTpLypL0",
				"focus": -0.3419725585924327,
				"gap": 17.33333333333303
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
					-1560,
					530
				]
			]
		},
		{
			"type": "image",
			"version": 82,
			"versionNonce": 701666908,
			"isDeleted": false,
			"id": "MJ7Xl1eaz47Wp2ia89XrY",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -11200.090103430251,
			"y": 2731.489863181793,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1691.3448275862074,
			"height": 1225.0000000000005,
			"seed": 928122980,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "9JtqcgSt0gp4tbAjtiMZR",
					"type": "arrow"
				}
			],
			"updated": 1693689492396,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "71c9315cbaf7291a243962937b1724f63eeaa5af",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 102,
			"versionNonce": 51219812,
			"isDeleted": false,
			"id": "9JtqcgSt0gp4tbAjtiMZR",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -8426.256770096918,
			"y": 3363.765637486791,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1069.1080459770146,
			"height": 254.6603648707769,
			"seed": 647170916,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689492396,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "UV8g0mFDq0mmEhTpLypL0",
				"gap": 5.5,
				"focus": 0.050763572205323806
			},
			"endBinding": {
				"elementId": "MJ7Xl1eaz47Wp2ia89XrY",
				"gap": 13.380459770113703,
				"focus": -0.5399795965000368
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
					-1069.1080459770146,
					-254.6603648707769
				]
			]
		},
		{
			"type": "arrow",
			"version": 50,
			"versionNonce": 1755936732,
			"isDeleted": false,
			"id": "7VE5nd2KJytk5m1nOHz9j",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -8426.256770096918,
			"y": 3840.6565298484593,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 481.49234262560276,
			"height": 390.0000000000018,
			"seed": 1504731868,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689504961,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "UV8g0mFDq0mmEhTpLypL0",
				"focus": 0.4367031580708397,
				"gap": 5.5
			},
			"endBinding": {
				"elementId": "RwA2z3ppYRq8_fir2zcNE",
				"focus": -0.22061997440077738,
				"gap": 8.639678030301639
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
					-481.49234262560276,
					390.0000000000018
				]
			]
		},
		{
			"type": "image",
			"version": 73,
			"versionNonce": 1963654620,
			"isDeleted": false,
			"id": "RwA2z3ppYRq8_fir2zcNE",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -9791.377982218128,
			"y": 4239.296207878762,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1222.3636363636351,
			"height": 824.3847780126841,
			"seed": 1332513508,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "7VE5nd2KJytk5m1nOHz9j",
					"type": "arrow"
				},
				{
					"id": "F2TCauT8acjEJwYzIuD1B",
					"type": "arrow"
				},
				{
					"id": "F28S1FB7HwnoVx07U4E5u",
					"type": "arrow"
				}
			],
			"updated": 1693689824818,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "227edf29f313074ff16fd05750a0e9a7a1e6f363",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "image",
			"version": 75,
			"versionNonce": 1966653156,
			"isDeleted": false,
			"id": "k-EBqLoIUMjQBwXsanex4",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -11213.150709490856,
			"y": 4248.47802606058,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1306.4992025518325,
			"height": 768.7272727272717,
			"seed": 1963199964,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "F2TCauT8acjEJwYzIuD1B",
					"type": "arrow"
				}
			],
			"updated": 1693689533069,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "f849373ecaf67d092f1be833e0cf23c5c5212e7b",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 26,
			"versionNonce": 685570404,
			"isDeleted": false,
			"id": "F2TCauT8acjEJwYzIuD1B",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -9794.741618581766,
			"y": 4651.023480606034,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 105.45454545454595,
			"height": 23.636363636363967,
			"seed": 2010720996,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689533502,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "RwA2z3ppYRq8_fir2zcNE",
				"focus": -0.24996809091689393,
				"gap": 3.363636363637852
			},
			"endBinding": {
				"elementId": "k-EBqLoIUMjQBwXsanex4",
				"focus": -0.2888559666824974,
				"gap": 6.455342902710981
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
					-105.45454545454595,
					-23.636363636363967
				]
			]
		},
		{
			"type": "image",
			"version": 56,
			"versionNonce": 894580444,
			"isDeleted": false,
			"id": "TIRNzjezbMrXu2JZ_I-4X",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -10075.196164036313,
			"y": 5408.457824040379,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1003.1390406800238,
			"height": 1034.2222222222217,
			"seed": 117701220,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "F28S1FB7HwnoVx07U4E5u",
					"type": "arrow"
				}
			],
			"updated": 1693689824818,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "75bc1fc729ae3620a2364e9e5f9de9cfddcd970c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 29,
			"versionNonce": 1327948380,
			"isDeleted": false,
			"id": "F28S1FB7HwnoVx07U4E5u",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -9342.418386258536,
			"y": 5078.902268484824,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 102.22222222222263,
			"height": 320,
			"seed": 1267588068,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693689824818,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "RwA2z3ppYRq8_fir2zcNE",
				"focus": 0.03457918510457906,
				"gap": 15.221282593377055
			},
			"endBinding": {
				"elementId": "TIRNzjezbMrXu2JZ_I-4X",
				"focus": -0.058874010921854125,
				"gap": 9.555555555555202
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
					-102.22222222222263,
					320
				]
			]
		},
		{
			"type": "image",
			"version": 94,
			"versionNonce": 1305607780,
			"isDeleted": false,
			"id": "6Fk93cKJKGqSqF-jpMBfD",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -3798.7517195918654,
			"y": 2046.2911573737142,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1097.3237221494107,
			"height": 989.6666666666672,
			"seed": 1038481508,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "pdEF1MMhFqfv1H29n1ZJe",
					"type": "arrow"
				}
			],
			"updated": 1693694076159,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "103efc88f7adc96b6896916861fd47c40bf0938f",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 28,
			"versionNonce": 397081316,
			"isDeleted": false,
			"id": "pdEF1MMhFqfv1H29n1ZJe",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -4253.529497369644,
			"y": 2570.0133795959364,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 442.2222222222217,
			"height": 37.777777777777374,
			"seed": 1668183900,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693694076159,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "oCXYkXzwh9Y5X0mTOrd5p",
				"focus": -0.39481664515392717,
				"gap": 6.0606060606078245
			},
			"endBinding": {
				"elementId": "6Fk93cKJKGqSqF-jpMBfD",
				"focus": -0.2115728788921435,
				"gap": 12.555555555556566
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
					442.2222222222217,
					37.777777777777374
				]
			]
		},
		{
			"type": "image",
			"version": 69,
			"versionNonce": 1171311204,
			"isDeleted": false,
			"id": "WxURfEehertANuQYuPcSH",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -7142.243783083933,
			"y": 620.2673478499046,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1457.0632183908046,
			"height": 1119.3333333333335,
			"seed": 815942492,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "dB1p5FJvXVScv8NQpYpjN",
					"type": "arrow"
				},
				{
					"id": "scmqa6cA4LPADyByePLze",
					"type": "arrow"
				},
				{
					"id": "RSicHzFuFCDNxllEmPGZ2",
					"type": "arrow"
				}
			],
			"updated": 1693697924131,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "b1b03a9389e5d98105c5846f9a3f237bde29c831",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 23,
			"versionNonce": 412095588,
			"isDeleted": false,
			"id": "dB1p5FJvXVScv8NQpYpjN",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -5122.577116417266,
			"y": 2498.2673478499046,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1023.333333333333,
			"height": 736.666666666667,
			"seed": 831999068,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693694318727,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "oCXYkXzwh9Y5X0mTOrd5p",
				"focus": -0.476045287167947,
				"gap": 5.722515331887735
			},
			"endBinding": {
				"elementId": "WxURfEehertANuQYuPcSH",
				"focus": 0.3587114802788188,
				"gap": 21.999999999999545
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
					-1023.333333333333,
					-736.666666666667
				]
			]
		},
		{
			"type": "image",
			"version": 67,
			"versionNonce": 299069276,
			"isDeleted": false,
			"id": "wDJiFwZtsNF1jcVLqNpca",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -7232.410449750599,
			"y": -1085.7326521500956,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1726.3333333333328,
			"height": 1333.50225502255,
			"seed": 744723172,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "scmqa6cA4LPADyByePLze",
					"type": "arrow"
				},
				{
					"id": "lo-DG5y_ypaiIROisCIoq",
					"type": "arrow"
				}
			],
			"updated": 1693696452221,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "73360c3a546d67223f20a20861100eb6533f723a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 52,
			"versionNonce": 1422674012,
			"isDeleted": false,
			"id": "scmqa6cA4LPADyByePLze",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -6521.737691853788,
			"y": 611.6006811832381,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 53.85849397766469,
			"height": 356.66666666666674,
			"seed": 595895140,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693696452221,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "WxURfEehertANuQYuPcSH",
				"focus": -0.04089438370193215,
				"gap": 8.666666666666515
			},
			"endBinding": {
				"elementId": "wDJiFwZtsNF1jcVLqNpca",
				"focus": 0.319673456187357,
				"gap": 7.164411644117081
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
					-53.85849397766469,
					-356.66666666666674
				]
			]
		},
		{
			"type": "image",
			"version": 91,
			"versionNonce": 730299364,
			"isDeleted": false,
			"id": "Dep3wp6VUSTYcK6NIc7SK",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -9149.243783083935,
			"y": -1557.399318816762,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1491.4859437751004,
			"height": 1198,
			"seed": 1604424796,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "lo-DG5y_ypaiIROisCIoq",
					"type": "arrow"
				}
			],
			"updated": 1693697906417,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "7a156dc65c1c3eb2ead82f3f7bcfa45402171301",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 131,
			"versionNonce": 1421660900,
			"isDeleted": false,
			"id": "lo-DG5y_ypaiIROisCIoq",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -7239.243783083935,
			"y": -569.1059051328675,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 393.33333333333303,
			"height": 88.69983729092496,
			"seed": 547907932,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693697906418,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "wDJiFwZtsNF1jcVLqNpca",
				"focus": -0.04394878225995392,
				"gap": 6.833333333337123
			},
			"endBinding": {
				"elementId": "Dep3wp6VUSTYcK6NIc7SK",
				"focus": 0.1652096603777695,
				"gap": 25.180722891566802
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
					-393.33333333333303,
					-88.69983729092496
				]
			]
		},
		{
			"type": "image",
			"version": 55,
			"versionNonce": 477765084,
			"isDeleted": false,
			"id": "EqnWtKw36qBuo3CR_m8pt",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -9525.743783083934,
			"y": -167.56598548342822,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1849.6666666666663,
			"height": 1069.9675448644518,
			"seed": 331901412,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "RSicHzFuFCDNxllEmPGZ2",
					"type": "arrow"
				},
				{
					"id": "AT6unOT_U0ndhxbMMuUzk",
					"type": "arrow"
				}
			],
			"updated": 1693698108970,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "12d13934062c81e68c589b3526cd41fe267e4105",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 23,
			"versionNonce": 1704058340,
			"isDeleted": false,
			"id": "RSicHzFuFCDNxllEmPGZ2",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -7145.910449750601,
			"y": 914.9340145165718,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 523.3333333333339,
			"height": 470,
			"seed": 384731868,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693697924131,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "WxURfEehertANuQYuPcSH",
				"focus": -0.32338923995443986,
				"gap": 3.666666666668334
			},
			"endBinding": {
				"elementId": "EqnWtKw36qBuo3CR_m8pt",
				"focus": -0.5559622881559444,
				"gap": 6.83333333333303
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
					-523.3333333333339,
					-470
				]
			]
		},
		{
			"type": "image",
			"version": 69,
			"versionNonce": 330597212,
			"isDeleted": false,
			"id": "X6CkBf7Sc_VRnYvQr6LYC",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -11338.410449750601,
			"y": -448.065985483428,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1570.7071960297765,
			"height": 1699.3154362416105,
			"seed": 344357724,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "WjRirQWrzJrMb8IyhFfhi",
					"type": "arrow"
				}
			],
			"updated": 1693697966167,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "eeac4cdb843be046116eeade3335929837cd77b4",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 64,
			"versionNonce": 947412060,
			"isDeleted": false,
			"id": "WjRirQWrzJrMb8IyhFfhi",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -9519.243783083935,
			"y": 398.26734784990504,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 233.33333333333394,
			"height": 42.502923470322116,
			"seed": 525708380,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693697966231,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "X6CkBf7Sc_VRnYvQr6LYC",
				"gap": 15.126137303555879,
				"focus": -0.19304551278545146
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
					-233.33333333333394,
					-42.502923470322116
				]
			]
		},
		{
			"type": "image",
			"version": 173,
			"versionNonce": 2004623386,
			"isDeleted": false,
			"id": "MJjD-pZXi-oplRx2zMSmZ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -11198.025834365988,
			"y": 1268.1928099846689,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1679.0384615384633,
			"height": 1483.801431127014,
			"seed": 798342492,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "AT6unOT_U0ndhxbMMuUzk",
					"type": "arrow"
				}
			],
			"updated": 1693756066719,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "8c7bc1ccfb189d7eadea6c308e8a155a036044de",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 129,
			"versionNonce": 1748132250,
			"isDeleted": false,
			"id": "AT6unOT_U0ndhxbMMuUzk",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -9259.3179966173,
			"y": 906.6006811832386,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 352.0728477446519,
			"height": 349.09212880143,
			"seed": 1569429476,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693756066720,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "EqnWtKw36qBuo3CR_m8pt",
				"gap": 4.199121802214904,
				"focus": 0.07695158470079755
			},
			"endBinding": {
				"elementId": "MJjD-pZXi-oplRx2zMSmZ",
				"gap": 12.5,
				"focus": -0.008645162971283527
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
					-352.0728477446519,
					349.09212880143
				]
			]
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
		"scrollX": 6741.74222472666,
		"scrollY": -1115.5947968576743,
		"zoom": {
			"value": 0.65
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
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