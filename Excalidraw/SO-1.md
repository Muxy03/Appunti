---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
GERARCHIA DELLA MEMORIA ^iALG2Gey

1. LOC. SPAZIALE
2. LOC. TEMPORALE ^R644Xznp

Terminologia AMAT: 

hit -> quando vado a cercare qualcosa in una memoria piccola, che è un sottoinsieme
della memoria complessiva e lo trovo.

Hit rate -> la percentuale di volte che troviamo quello che stiamo cercando.
L’hit si risolve in un tempo di accesso alla cache, molto spesso questo tempo è detto hitTime
(Tc1)

miss -> opposto di hit

miss rate -> percentuale di volte che mi dice quante volte non troviamo quello
che stiamo cercando
 
misstime -> il tempo che devo spendere per ottenere quell’elemento in caso di miss

missPenalty -> il tempo che ci metto a richiedere il blocco di dati e a salvarlo nella cache.

Il tempo che impiego per andare a fare l’amat, è l’hitTime del livello 1, sommato al missRate
del livello 1, moltiplicato per l’hitTime del livello successivo se lo troviamo sommato al
missRate moltiplicato per i livelli successivi ecct…
La moltiplicazione dei livelli successivi è una miss Penalty.
Tutto questo funziona perché vale il principio di località spaziale e temporale. ^MAXYarNV


# Embedded files
35f1f2d80a8a235945aeed63ae67cb2443c1c4f3: [[Pasted Image 20230816151316_032.png]]
7d80f518c63d08a53314efff4a80d91b884f30fb: [[Pasted Image 20230816153330_196.png]]
54e49632af7ca32dca19f3044e6c5767578648fb: [[Pasted Image 20230816153430_233.png]]
6cd81e64bd637f64e723f013051864a99c972f0c: [[Pasted Image 20230816154349_527.png]]
d18f4f5c557ddf8e5c7f884003963f557444a04f: [[Pasted Image 20230816154858_719.png]]
a09e1a5771f230a659549e5f7260ce9ce344af99: [[Pasted Image 20230816160942_731.png]]
d8d96fef583ee0c80695e9561fbc622c0a5d9fbd: [[Pasted Image 20230816160959_308.png]]
db27c593ac5bbd57383ce973d216c9701ffad165: [[Pasted Image 20230816161059_356.png]]
0bf3c62f9d19b0b5df75d72bbcd3ca408a9d909f: [[Pasted Image 20230816161830_142.png]]
e2f93ed4ac1c0a912db5d9d9bf93226caaa74722: [[Pasted Image 20230816162032_148.png]]
39cc7fa6b8642a491721c8cab67d6d4fe1abbc69: [[Pasted Image 20230823192121_691.png]]
d3a243b0514f63a479a387391cbb3612422ecce9: [[Pasted Image 20230823192322_747.png]]
08ea15968dd1e9f0323d4a769fe4ae9918a29444: [[Pasted Image 20230823192354_767.png]]
cc7df6a3201843fba2cac0edb56253e01edf0240: [[Pasted Image 20230823192524_829.png]]
78dfc551890610a5ba574a455113a4090c96ac15: [[Pasted Image 20230823192912_950.png]]
8eb6c19ff550df4d9bd51af51189ec5a1e32d719: [[Pasted Image 20230823193131_014.png]]
ff0e2b176103b88fbdee38d23a9d5c6fb551f4be: [[Pasted Image 20230823193537_858.png]]
d07c8a606282f0d73da5d67e0b72311daddaec9e: [[Pasted Image 20230823193634_143.png]]
f422eeff83fd0b907315572ef3aeafc6ee22d8e6: [[Pasted Image 20230823193916_695.png]]
cae8cf1449992a9a719962f82e749105d85b425d: [[Pasted Image 20230823193934_216.png]]
16d7367621b0d22a06aa9b8864fd7665c8517342: [[Pasted Image 20230823194225_322.png]]
edc293eb0b29c27ba20617befe78612485833125: [[Pasted Image 20230823194940_617.png]]
becda6340219cacc238cfee3a96dd6874416f3b8: [[Pasted Image 20230823195046_679.png]]
3c9f22170827d7e8baf0b557d067dee0d082e531: [[Pasted Image 20230823195416_360.png]]
44b4fd3fcd5a7674dda2a20276f8e965b26fa61f: [[Pasted Image 20230823195432_746.png]]
270d44b5c92439574dffbd367eba83509d1e0631: [[Pasted Image 20230823200524_014.png]]
dcf56ec1e87cca76f5a408c95219626fd795330f: [[Pasted Image 20230823200610_048.png]]
ec786c42763136dfd85f146e6b14dbc6d9293fbf: [[Pasted Image 20230823200710_098.png]]
d9f6118908369ae10753d3ac4f1ba130901fdcd6: [[Pasted Image 20230823201311_266.png]]
d059e2f4ce92bda24a40843f90b18a0807e9b8da: [[Pasted Image 20230823201428_328.png]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.9.16",
	"elements": [
		{
			"type": "rectangle",
			"version": 358,
			"versionNonce": 1606774313,
			"isDeleted": false,
			"id": "Tkdr0rp5CKBkz0aZ8AJFF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 286.5805154623645,
			"y": 192.85608414486666,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 188,
			"height": 190,
			"seed": 2107499367,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "iALG2Gey"
				},
				{
					"id": "0jTl0JR64JjdXGDXTHZRj",
					"type": "arrow"
				},
				{
					"id": "WxNa7pHvBYOOPpElgvkFe",
					"type": "arrow"
				},
				{
					"id": "K6LLaevce8UEOWacbWahd",
					"type": "arrow"
				},
				{
					"id": "t_3C1_gBrg9NiHA4exDeM",
					"type": "arrow"
				},
				{
					"id": "HrxCaL0L-AzBkLyze6v7X",
					"type": "arrow"
				}
			],
			"updated": 1692814679886,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 345,
			"versionNonce": 1688271721,
			"isDeleted": false,
			"id": "iALG2Gey",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 298.38653810640744,
			"y": 235.35608414486666,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 164.38795471191406,
			"height": 105,
			"seed": 459601993,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1692814685933,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "GERARCHIA\nDELLA \nMEMORIA",
			"rawText": "GERARCHIA DELLA MEMORIA",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Tkdr0rp5CKBkz0aZ8AJFF",
			"originalText": "GERARCHIA DELLA MEMORIA",
			"lineHeight": 1.25,
			"baseline": 94
		},
		{
			"type": "image",
			"version": 296,
			"versionNonce": 1674059463,
			"isDeleted": false,
			"id": "fEr4IivkV4A9CKHvriwGH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 782.2035030878033,
			"y": 265.23132888858896,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 501.3906145029883,
			"height": 344.9679158279613,
			"seed": 816659015,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "0jTl0JR64JjdXGDXTHZRj",
					"type": "arrow"
				}
			],
			"updated": 1692814423640,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "35f1f2d80a8a235945aeed63ae67cb2443c1c4f3",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 1216,
			"versionNonce": 340491975,
			"isDeleted": false,
			"id": "0jTl0JR64JjdXGDXTHZRj",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 476.1805215658801,
			"y": 300.0357623423705,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 303.3491935516313,
			"height": 111.57939518460478,
			"seed": 289049031,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692814687494,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Tkdr0rp5CKBkz0aZ8AJFF",
				"gap": 1.600006103515625,
				"focus": -0.1689037149324852
			},
			"endBinding": {
				"elementId": "fEr4IivkV4A9CKHvriwGH",
				"gap": 2.673787970291869,
				"focus": -0.25348080350679675
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
					303.3491935516313,
					111.57939518460478
				]
			]
		},
		{
			"type": "rectangle",
			"version": 225,
			"versionNonce": 1888511847,
			"isDeleted": false,
			"id": "NERTXZOihWz9nguG2ize9",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 222.96533877284787,
			"y": 549.7390208215405,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 226,
			"height": 136,
			"seed": 1628309481,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "R644Xznp"
				},
				{
					"id": "WxNa7pHvBYOOPpElgvkFe",
					"type": "arrow"
				}
			],
			"updated": 1692195664206,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 208,
			"versionNonce": 1821992585,
			"isDeleted": false,
			"id": "R644Xznp",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 231.29539400966428,
			"y": 592.7390208215405,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 209.3398895263672,
			"height": 50,
			"seed": 1119090345,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1692195664206,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "1. LOC. SPAZIALE\n2. LOC. TEMPORALE",
			"rawText": "1. LOC. SPAZIALE\n2. LOC. TEMPORALE",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "NERTXZOihWz9nguG2ize9",
			"originalText": "1. LOC. SPAZIALE\n2. LOC. TEMPORALE",
			"lineHeight": 1.25,
			"baseline": 43
		},
		{
			"type": "arrow",
			"version": 563,
			"versionNonce": 807276007,
			"isDeleted": false,
			"id": "WxNa7pHvBYOOPpElgvkFe",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 354.582481602489,
			"y": 384.7560398943784,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.055336626822054,
			"height": 159.296513689199,
			"seed": 1800468809,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692814687494,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Tkdr0rp5CKBkz0aZ8AJFF",
				"gap": 1.8999557495117188,
				"focus": 0.19772112762565555
			},
			"endBinding": {
				"elementId": "NERTXZOihWz9nguG2ize9",
				"gap": 5.686467237963143,
				"focus": 0.0333394711966644
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
					-10.055336626822054,
					159.296513689199
				]
			]
		},
		{
			"type": "rectangle",
			"version": 439,
			"versionNonce": 313954953,
			"isDeleted": false,
			"id": "xLjYOxIz1kiL7JELFD2IN",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -874.6117303286776,
			"y": 297.19227308420864,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1029.2861176327215,
			"height": 776.117646774952,
			"seed": 861409641,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "K6LLaevce8UEOWacbWahd",
					"type": "arrow"
				},
				{
					"id": "tZNcmNhKeQtjAX-Ut2udW",
					"type": "arrow"
				}
			],
			"updated": 1692192816479,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 425,
			"versionNonce": 277200711,
			"isDeleted": false,
			"id": "MAXYarNV",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -866.8703662649223,
			"y": 382.2437496052695,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1011.905517578125,
			"height": 619.4836086978917,
			"seed": 1270626889,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1692818568117,
			"link": null,
			"locked": false,
			"fontSize": 21.54725595470928,
			"fontFamily": 1,
			"text": "Terminologia AMAT: \n\nhit -> quando vado a cercare qualcosa in una memoria piccola, che è un sottoinsieme\ndella memoria complessiva e lo trovo.\n\nHit rate -> la percentuale di volte che troviamo quello che stiamo cercando.\nL’hit si risolve in un tempo di accesso alla cache, molto spesso questo tempo è detto hitTime\n(Tc1)\n\nmiss -> opposto di hit\n\nmiss rate -> percentuale di volte che mi dice quante volte non troviamo quello\nche stiamo cercando\n \nmisstime -> il tempo che devo spendere per ottenere quell’elemento in caso di miss\n\nmissPenalty -> il tempo che ci metto a richiedere il blocco di dati e a salvarlo nella cache.\n\nIl tempo che impiego per andare a fare l’amat, è l’hitTime del livello 1, sommato al missRate\ndel livello 1, moltiplicato per l’hitTime del livello successivo se lo troviamo sommato al\nmissRate moltiplicato per i livelli successivi ecct…\nLa moltiplicazione dei livelli successivi è una miss Penalty.\nTutto questo funziona perché vale il principio di località spaziale e temporale.",
			"rawText": "Terminologia AMAT: \n\nhit -> quando vado a cercare qualcosa in una memoria piccola, che è un sottoinsieme\ndella memoria complessiva e lo trovo.\n\nHit rate -> la percentuale di volte che troviamo quello che stiamo cercando.\nL’hit si risolve in un tempo di accesso alla cache, molto spesso questo tempo è detto hitTime\n(Tc1)\n\nmiss -> opposto di hit\n\nmiss rate -> percentuale di volte che mi dice quante volte non troviamo quello\nche stiamo cercando\n \nmisstime -> il tempo che devo spendere per ottenere quell’elemento in caso di miss\n\nmissPenalty -> il tempo che ci metto a richiedere il blocco di dati e a salvarlo nella cache.\n\nIl tempo che impiego per andare a fare l’amat, è l’hitTime del livello 1, sommato al missRate\ndel livello 1, moltiplicato per l’hitTime del livello successivo se lo troviamo sommato al\nmissRate moltiplicato per i livelli successivi ecct…\nLa moltiplicazione dei livelli successivi è una miss Penalty.\nTutto questo funziona perché vale il principio di località spaziale e temporale.",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Terminologia AMAT: \n\nhit -> quando vado a cercare qualcosa in una memoria piccola, che è un sottoinsieme\ndella memoria complessiva e lo trovo.\n\nHit rate -> la percentuale di volte che troviamo quello che stiamo cercando.\nL’hit si risolve in un tempo di accesso alla cache, molto spesso questo tempo è detto hitTime\n(Tc1)\n\nmiss -> opposto di hit\n\nmiss rate -> percentuale di volte che mi dice quante volte non troviamo quello\nche stiamo cercando\n \nmisstime -> il tempo che devo spendere per ottenere quell’elemento in caso di miss\n\nmissPenalty -> il tempo che ci metto a richiedere il blocco di dati e a salvarlo nella cache.\n\nIl tempo che impiego per andare a fare l’amat, è l’hitTime del livello 1, sommato al missRate\ndel livello 1, moltiplicato per l’hitTime del livello successivo se lo troviamo sommato al\nmissRate moltiplicato per i livelli successivi ecct…\nLa moltiplicazione dei livelli successivi è una miss Penalty.\nTutto questo funziona perché vale il principio di località spaziale e temporale.",
			"lineHeight": 1.25,
			"baseline": 610
		},
		{
			"type": "arrow",
			"version": 558,
			"versionNonce": 1293007111,
			"isDeleted": false,
			"id": "K6LLaevce8UEOWacbWahd",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 275.5923157036134,
			"y": 269.9628867048247,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 115.20081693348925,
			"height": 53.624247113837555,
			"seed": 1866723591,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692814687494,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Tkdr0rp5CKBkz0aZ8AJFF",
				"gap": 10.98819975875108,
				"focus": 0.46239992421939696
			},
			"endBinding": {
				"elementId": "xLjYOxIz1kiL7JELFD2IN",
				"gap": 5.717111466080269,
				"focus": -0.19031360093242047
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
					-115.20081693348925,
					53.624247113837555
				]
			]
		},
		{
			"type": "image",
			"version": 296,
			"versionNonce": 1721880649,
			"isDeleted": false,
			"id": "uVxR1WGyX4F0hesgN5soI",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1121.9742841909547,
			"y": 1623.6181951078293,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 762.9908432847598,
			"height": 518.9752317591588,
			"seed": 669219015,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "tZNcmNhKeQtjAX-Ut2udW",
					"type": "arrow"
				},
				{
					"id": "M9-ocjc_x7utS3SLhVX_M",
					"type": "arrow"
				}
			],
			"updated": 1692192903269,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "7d80f518c63d08a53314efff4a80d91b884f30fb",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 741,
			"versionNonce": 1204079177,
			"isDeleted": false,
			"id": "tZNcmNhKeQtjAX-Ut2udW",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -602.6798102870217,
			"y": 1076.644897159536,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 188.7027326725206,
			"height": 95.84295668568052,
			"seed": 1650463399,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692192901040,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "xLjYOxIz1kiL7JELFD2IN",
				"focus": 0.7906011785646618,
				"gap": 3.334977300375158
			},
			"endBinding": {
				"elementId": "7H6cNfd53um0RHupvtKUH",
				"focus": 0.4647591260958847,
				"gap": 3.223248966125084
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
					188.7027326725206,
					95.84295668568052
				]
			]
		},
		{
			"type": "image",
			"version": 549,
			"versionNonce": 1067097961,
			"isDeleted": false,
			"id": "7H6cNfd53um0RHupvtKUH",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -953.3049866512914,
			"y": 1175.7111028113416,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 994.0000000000001,
			"height": 346,
			"seed": 1070842055,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "tZNcmNhKeQtjAX-Ut2udW",
					"type": "arrow"
				},
				{
					"id": "M9-ocjc_x7utS3SLhVX_M",
					"type": "arrow"
				}
			],
			"updated": 1692192901039,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "54e49632af7ca32dca19f3044e6c5767578648fb",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 886,
			"versionNonce": 1819467561,
			"isDeleted": false,
			"id": "M9-ocjc_x7utS3SLhVX_M",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -885.0612120979287,
			"y": 1523.7259227761062,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 89.39881937486234,
			"height": 97.610923287795,
			"seed": 591721801,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692192903269,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "7H6cNfd53um0RHupvtKUH",
				"focus": 0.41495370988597763,
				"gap": 2.014819964764797
			},
			"endBinding": {
				"elementId": "uVxR1WGyX4F0hesgN5soI",
				"focus": -0.7651225943380663,
				"gap": 2.281349043928003
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
					-89.39881937486234,
					97.610923287795
				]
			]
		},
		{
			"type": "image",
			"version": 126,
			"versionNonce": 1237859079,
			"isDeleted": false,
			"id": "uKim9r9Ok2tyHMca4y6xM",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 490.0074274157927,
			"y": 742.8223914892988,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 993.2670019801623,
			"height": 961.7347162030143,
			"seed": 1996427785,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "t_3C1_gBrg9NiHA4exDeM",
					"type": "arrow"
				},
				{
					"id": "m3spKwSRsAJgkLnWPaCqw",
					"type": "arrow"
				},
				{
					"id": "wqjH-Ouf0wC8Lz4nNDbDR",
					"type": "arrow"
				}
			],
			"updated": 1692195001025,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "6cd81e64bd637f64e723f013051864a99c972f0c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 182,
			"versionNonce": 1621295143,
			"isDeleted": false,
			"id": "t_3C1_gBrg9NiHA4exDeM",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 477.3752801432131,
			"y": 347.2762669842283,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 361.05422317194245,
			"height": 393.01954498944303,
			"seed": 1248951847,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692814687494,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Tkdr0rp5CKBkz0aZ8AJFF",
				"gap": 2.7947646808486297,
				"focus": -0.22785698925877487
			},
			"endBinding": {
				"elementId": "uKim9r9Ok2tyHMca4y6xM",
				"gap": 2.526579515627418,
				"focus": 0.3152917224004767
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
					361.05422317194245,
					393.01954498944303
				]
			]
		},
		{
			"id": "N5MMm0Kb6HmKqq-tvk-gF",
			"type": "image",
			"x": 1628.360533437387,
			"y": 471.7729341117472,
			"width": 826.9280648543008,
			"height": 608.3500366210938,
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
			"seed": 2034966119,
			"version": 80,
			"versionNonce": 37623815,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Dpw9ItlGAFzqsYmEcxqVT",
					"type": "arrow"
				}
			],
			"updated": 1692193747946,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "d18f4f5c557ddf8e5c7f884003963f557444a04f",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "Dpw9ItlGAFzqsYmEcxqVT",
			"type": "arrow",
			"x": 1216.3268912850374,
			"y": 746.4964710374788,
			"width": 397.80956868424255,
			"height": 172.441130626504,
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
			"seed": 1278190377,
			"version": 94,
			"versionNonce": 309601991,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692193751446,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					157.07500158407152,
					-141.7090353660351
				],
				[
					397.80956868424255,
					-172.441130626504
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "N5MMm0Kb6HmKqq-tvk-gF",
				"focus": 0.7185476996940595,
				"gap": 14.224073468107008
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "8z645TeAM90FRPg7gyuPk",
			"type": "image",
			"x": 1686.466551738563,
			"y": 1168.7936932669336,
			"width": 869.0714808872768,
			"height": 608.3500366210938,
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
			"seed": 1989820425,
			"version": 38,
			"versionNonce": 2029472807,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "m3spKwSRsAJgkLnWPaCqw",
					"type": "arrow"
				}
			],
			"updated": 1692194980859,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "a09e1a5771f230a659549e5f7260ce9ce344af99",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "m3spKwSRsAJgkLnWPaCqw",
			"type": "arrow",
			"x": 1483.3117470121215,
			"y": 1301.1678064766052,
			"width": 199.75844008621198,
			"height": 104.147498763562,
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
			"seed": 820018857,
			"version": 28,
			"versionNonce": 1751937769,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692194980859,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					199.75844008621198,
					104.147498763562
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "uKim9r9Ok2tyHMca4y6xM",
				"focus": -0.24529717980488464,
				"gap": 1
			},
			"endBinding": {
				"elementId": "8z645TeAM90FRPg7gyuPk",
				"focus": -0.30273533710840483,
				"gap": 3.3963646402295353
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "0vzXcpEaHD88KcvGLgQSL",
			"type": "image",
			"x": 1253.2312106925515,
			"y": 2025.2367305009689,
			"width": 870.7755426145068,
			"height": 608.3500366210938,
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
			"seed": 1062895945,
			"version": 33,
			"versionNonce": 971904423,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "wqjH-Ouf0wC8Lz4nNDbDR",
					"type": "arrow"
				},
				{
					"id": "1D-6qJJ2n0eA7Ud_AuWka",
					"type": "arrow"
				}
			],
			"updated": 1692195055756,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "d8d96fef583ee0c80695e9561fbc622c0a5d9fbd",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "wqjH-Ouf0wC8Lz4nNDbDR",
			"type": "arrow",
			"x": 1157.2103029076688,
			"y": 1707.9408907333213,
			"width": 447.3225136581459,
			"height": 315.8574774807214,
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
			"seed": 1337509671,
			"version": 47,
			"versionNonce": 1110580457,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692195001025,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					447.3225136581459,
					315.8574774807214
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "uKim9r9Ok2tyHMca4y6xM",
				"focus": 0.43751273694105614,
				"gap": 3.383783041008428
			},
			"endBinding": {
				"elementId": "0vzXcpEaHD88KcvGLgQSL",
				"focus": 0.4026118946872694,
				"gap": 1.4383622869261217
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "q53tI-DOX6KOwLxOyeKIx",
			"type": "image",
			"x": 169.92720175848712,
			"y": 2141.5491004193022,
			"width": 811.4425031150259,
			"height": 608.3500366210938,
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
			"seed": 2067555655,
			"version": 39,
			"versionNonce": 1641522793,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "1D-6qJJ2n0eA7Ud_AuWka",
					"type": "arrow"
				}
			],
			"updated": 1692195059328,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "db27c593ac5bbd57383ce973d216c9701ffad165",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "1D-6qJJ2n0eA7Ud_AuWka",
			"type": "arrow",
			"x": 1246.6320284139438,
			"y": 2157.610973970157,
			"width": 259.51525398920944,
			"height": 240.7346322299295,
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
			"seed": 1207023945,
			"version": 127,
			"versionNonce": 2009647175,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692195059751,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-259.51525398920944,
					240.7346322299295
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "0vzXcpEaHD88KcvGLgQSL",
				"focus": 0.8216908279961004,
				"gap": 6.599182278607714
			},
			"endBinding": {
				"elementId": "q53tI-DOX6KOwLxOyeKIx",
				"focus": 0.4912497290807964,
				"gap": 5.74706955122133
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "J2q27C7By-00xKeDnmU6T",
			"type": "image",
			"x": -228.17425215097234,
			"y": -267.6290420596264,
			"width": 532.3047862115969,
			"height": 369.74098238578205,
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
			"seed": 1261414025,
			"version": 6,
			"versionNonce": 292303433,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "HrxCaL0L-AzBkLyze6v7X",
					"type": "arrow"
				},
				{
					"id": "B7OCP7liRJk9WFFGN2Hp2",
					"type": "arrow"
				}
			],
			"updated": 1692195639860,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "0bf3c62f9d19b0b5df75d72bbcd3ca408a9d909f",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "HrxCaL0L-AzBkLyze6v7X",
			"type": "arrow",
			"x": 381.22957889038213,
			"y": 189.06205470127134,
			"width": 135.7071049996182,
			"height": 274.6647235725153,
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
			"seed": 1756442151,
			"version": 142,
			"versionNonce": 791263689,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692814687494,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					59.60368455708607,
					-186.0894609069074
				],
				[
					-76.10342044253213,
					-274.6647235725153
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "Tkdr0rp5CKBkz0aZ8AJFF",
				"gap": 3.7940294435953206,
				"focus": -0.2490936836978886
			},
			"endBinding": {
				"elementId": "J2q27C7By-00xKeDnmU6T",
				"focus": -0.49419050996942615,
				"gap": 1
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "dgWA5y2pkRinMhkkLFUk8",
			"type": "image",
			"x": -1023.0519179375772,
			"y": -164.4811838619616,
			"width": 594.7925100812483,
			"height": 358.0962888516524,
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
			"seed": 506260103,
			"version": 154,
			"versionNonce": 1582286151,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "B7OCP7liRJk9WFFGN2Hp2",
					"type": "arrow"
				},
				{
					"id": "G6EkmAfL5_9hTHLPc3yg4",
					"type": "arrow"
				}
			],
			"updated": 1692811297364,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "e2f93ed4ac1c0a912db5d9d9bf93226caaa74722",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "B7OCP7liRJk9WFFGN2Hp2",
			"type": "arrow",
			"x": -231.5770675453739,
			"y": -91.70167896574964,
			"width": 193.28789077795057,
			"height": 39.091951118108284,
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
			"seed": 1635094215,
			"version": 64,
			"versionNonce": 811446983,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692195639860,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-193.28789077795057,
					39.091951118108284
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "J2q27C7By-00xKeDnmU6T",
				"focus": 0.2658574740902794,
				"gap": 3.402815394401557
			},
			"endBinding": {
				"elementId": "dgWA5y2pkRinMhkkLFUk8",
				"focus": -0.02651629731683888,
				"gap": 3.3944495330043765
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "dcJDF5bY3MjhXk9GMhXwi",
			"type": "image",
			"x": -1641.169254846412,
			"y": 294.560410658382,
			"width": 655.8731147963581,
			"height": 149.06207154462683,
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
			"seed": 1231185127,
			"version": 141,
			"versionNonce": 809215015,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "G6EkmAfL5_9hTHLPc3yg4",
					"type": "arrow"
				},
				{
					"id": "NQTI-5kXCP1OWKxWZYSb0",
					"type": "arrow"
				},
				{
					"id": "dkKJ-SwyWRWSwACEwD0QS",
					"type": "arrow"
				}
			],
			"updated": 1692811444752,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "39cc7fa6b8642a491721c8cab67d6d4fe1abbc69",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "G6EkmAfL5_9hTHLPc3yg4",
			"type": "arrow",
			"x": -1026.805239465526,
			"y": -8.687298575248803,
			"width": 318.14754924965064,
			"height": 295.42270882318775,
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
			"seed": 1836811655,
			"version": 234,
			"versionNonce": 1901785671,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692811301235,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-318.14754924965064,
					54.91828610365252
				],
				[
					-275.5385005401365,
					295.42270882318775
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "dgWA5y2pkRinMhkkLFUk8",
				"focus": 0.3265776031128176,
				"gap": 3.753321527948856
			},
			"endBinding": {
				"elementId": "dcJDF5bY3MjhXk9GMhXwi",
				"focus": 0.07468935809834897,
				"gap": 7.825000410443067
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "jXzBRHUSfsQklTYcdhJvR",
			"type": "image",
			"x": -2038.717484732379,
			"y": 610.1486393583641,
			"width": 521.3043187810246,
			"height": 294.39064050291535,
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
			"seed": 1737383049,
			"version": 179,
			"versionNonce": 892797353,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "NQTI-5kXCP1OWKxWZYSb0",
					"type": "arrow"
				},
				{
					"id": "_WTtHkVMzW5au79mvFfl_",
					"type": "arrow"
				}
			],
			"updated": 1692811532244,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "d3a243b0514f63a479a387391cbb3612422ecce9",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "NQTI-5kXCP1OWKxWZYSb0",
			"type": "arrow",
			"x": -1571.3306206213485,
			"y": 445.31507201225554,
			"width": 180.41363734345146,
			"height": 162.8727757697227,
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
			"seed": 1069915657,
			"version": 369,
			"versionNonce": 489819913,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692811438968,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-180.41363734345146,
					162.8727757697227
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "dcJDF5bY3MjhXk9GMhXwi",
				"gap": 1.6925898092466696,
				"focus": 0.42443015162523584
			},
			"endBinding": {
				"elementId": "jXzBRHUSfsQklTYcdhJvR",
				"gap": 1.9607915763858728,
				"focus": -0.3278231983650521
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "A-eYwAI_KjgVH-lOLMYnp",
			"type": "image",
			"x": -1460.1120431565796,
			"y": 601.0495819692912,
			"width": 533.9298590511244,
			"height": 319.9922100477629,
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
			"seed": 147493511,
			"version": 87,
			"versionNonce": 430081863,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "dkKJ-SwyWRWSwACEwD0QS",
					"type": "arrow"
				}
			],
			"updated": 1692811444752,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "08ea15968dd1e9f0323d4a769fe4ae9918a29444",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "dkKJ-SwyWRWSwACEwD0QS",
			"type": "arrow",
			"x": -1220.2312116705803,
			"y": 443.78921446247443,
			"width": 14.824999212177545,
			"height": 150.53132174266682,
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
			"seed": 1275938281,
			"version": 50,
			"versionNonce": 1037915593,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692811444752,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					14.824999212177545,
					150.53132174266682
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "dcJDF5bY3MjhXk9GMhXwi",
				"focus": -0.25544546579853616,
				"gap": 1
			},
			"endBinding": {
				"elementId": "A-eYwAI_KjgVH-lOLMYnp",
				"focus": 0.014716719317403518,
				"gap": 6.729045764149987
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "AdzkK7-Wiqw0XX6nBw_vE",
			"type": "image",
			"x": -2204.3121633864816,
			"y": 1017.6425990178118,
			"width": 601.8746009869849,
			"height": 222.75260967900667,
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
			"seed": 1436590471,
			"version": 109,
			"versionNonce": 135980169,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "_WTtHkVMzW5au79mvFfl_",
					"type": "arrow"
				}
			],
			"updated": 1692811532244,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "cc7df6a3201843fba2cac0edb56253e01edf0240",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "_WTtHkVMzW5au79mvFfl_",
			"type": "arrow",
			"x": -1800.111721043203,
			"y": 907.8317945840254,
			"width": 35.824158209586585,
			"height": 106.38691039062292,
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
			"seed": 190901287,
			"version": 52,
			"versionNonce": 519178599,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692811532244,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-35.824158209586585,
					106.38691039062292
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "jXzBRHUSfsQklTYcdhJvR",
				"focus": -0.09228374461174135,
				"gap": 3.2925147227458638
			},
			"endBinding": {
				"elementId": "AdzkK7-Wiqw0XX6nBw_vE",
				"focus": 0.08504209614275983,
				"gap": 3.4238940431635
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "vz0EunVoG0R9u6cerHFAL",
			"type": "image",
			"x": -223.3206695177205,
			"y": -700.8231311862875,
			"width": 509.06342547997366,
			"height": 329.70128354917335,
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
			"seed": 944642983,
			"version": 494,
			"versionNonce": 596323367,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "jQavoq4wvh13Oj3UFNBOe",
					"type": "arrow"
				},
				{
					"id": "Y_YihFRFSbGVe-g9StE7T",
					"type": "arrow"
				}
			],
			"updated": 1692811902566,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "78dfc551890610a5ba574a455113a4090c96ac15",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "jQavoq4wvh13Oj3UFNBOe",
			"type": "arrow",
			"x": 442.41987402416066,
			"y": 4.862247180305758,
			"width": 173.3015743938957,
			"height": 486.4318727797434,
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
			"seed": 2084665833,
			"version": 224,
			"versionNonce": 1856268039,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692811792560,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					28.267294754650266,
					-254.40644733988427
				],
				[
					-145.03427963924543,
					-486.4318727797434
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "vz0EunVoG0R9u6cerHFAL",
				"focus": -0.5972056316192468,
				"gap": 11.642838422662038
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "B4H_PWvw_jNb-k_7CO180",
			"type": "image",
			"x": -1045.7507729181993,
			"y": -652.0703803014978,
			"width": 548.9700575486198,
			"height": 337.15284356296513,
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
			"seed": 774548425,
			"version": 134,
			"versionNonce": 163647303,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Y_YihFRFSbGVe-g9StE7T",
					"type": "arrow"
				}
			],
			"updated": 1692811902566,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "8eb6c19ff550df4d9bd51af51189ec5a1e32d719",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "Y_YihFRFSbGVe-g9StE7T",
			"type": "arrow",
			"x": -226.14098840151155,
			"y": -549.3272287584749,
			"width": 269.2841321941876,
			"height": 8.92652010709287,
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
			"seed": 1996110983,
			"version": 75,
			"versionNonce": 254430665,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692811902566,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-269.2841321941876,
					8.92652010709287
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "vz0EunVoG0R9u6cerHFAL",
				"focus": 0.12629671168298293,
				"gap": 2.820318883791032
			},
			"endBinding": {
				"elementId": "B4H_PWvw_jNb-k_7CO180",
				"focus": -0.2688211350350842,
				"gap": 1.355594773880341
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "R39YDJjsQ_bUc9Fbjztjl",
			"type": "image",
			"x": 752.9642094460787,
			"y": -404.3341593774869,
			"width": 795.9999999999999,
			"height": 137,
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
			"seed": 1655058313,
			"version": 250,
			"versionNonce": 1717185511,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "hIBO77BYzK0KMGkLj5Lj6",
					"type": "arrow"
				},
				{
					"id": "dcZ8KBKmwTuuPAhwLwsm4",
					"type": "arrow"
				}
			],
			"updated": 1692812193373,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "ff0e2b176103b88fbdee38d23a9d5c6fb551f4be",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "hIBO77BYzK0KMGkLj5Lj6",
			"type": "arrow",
			"x": 472.3609409581409,
			"y": -128.72173685133586,
			"width": 276.72291786790856,
			"height": 162.60639163304282,
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
			"seed": 520251719,
			"version": 233,
			"versionNonce": 1355808359,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692813850591,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					78.85117354418674,
					-126.58753355606345
				],
				[
					276.72291786790856,
					-162.60639163304282
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "R39YDJjsQ_bUc9Fbjztjl",
				"focus": 0.2032571623881335,
				"gap": 3.880350620029276
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "UaRj7AKiQFulGakBqXI9g",
			"type": "image",
			"x": 1674.6009164469826,
			"y": -504.15238306864876,
			"width": 879,
			"height": 414,
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
			"seed": 1206460135,
			"version": 43,
			"versionNonce": 1300594569,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "dcZ8KBKmwTuuPAhwLwsm4",
					"type": "arrow"
				},
				{
					"id": "piWQeSXQFN2rvam1yBJx3",
					"type": "arrow"
				}
			],
			"updated": 1692812383560,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "d07c8a606282f0d73da5d67e0b72311daddaec9e",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "dcZ8KBKmwTuuPAhwLwsm4",
			"type": "arrow",
			"x": 1556.9360283948893,
			"y": -348.4800155680095,
			"width": 111.58167159895265,
			"height": 22.3163570211629,
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
			"seed": 1220837511,
			"version": 39,
			"versionNonce": 1687955977,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692812193373,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					111.58167159895265,
					-22.3163570211629
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "R39YDJjsQ_bUc9Fbjztjl",
				"focus": 0.4628531581074449,
				"gap": 7.971818948810551
			},
			"endBinding": {
				"elementId": "UaRj7AKiQFulGakBqXI9g",
				"focus": 0.5519181896057525,
				"gap": 6.083216453140608
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "jIO4_5ajcefRcQH06bfVt",
			"type": "image",
			"x": 2591.8432240132934,
			"y": -1084.1894033660935,
			"width": 854,
			"height": 459,
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
			"seed": 1663944681,
			"version": 54,
			"versionNonce": 667781063,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "kP7Hn5Xa_l3_AeY2mmJxM",
					"type": "arrow"
				}
			],
			"updated": 1692812392240,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "f422eeff83fd0b907315572ef3aeafc6ee22d8e6",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "2Y2eNuWRK7Rspk0Kh337Q",
			"type": "image",
			"x": 1653.101337545207,
			"y": -1104.069068397257,
			"width": 680.6254398109311,
			"height": 457.10185787302305,
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
			"seed": 528252617,
			"version": 99,
			"versionNonce": 1138537639,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "piWQeSXQFN2rvam1yBJx3",
					"type": "arrow"
				},
				{
					"id": "kP7Hn5Xa_l3_AeY2mmJxM",
					"type": "arrow"
				}
			],
			"updated": 1692812392240,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "cae8cf1449992a9a719962f82e749105d85b425d",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "piWQeSXQFN2rvam1yBJx3",
			"type": "arrow",
			"x": 2103.872586145616,
			"y": -509.90169873981347,
			"width": 104.14299943209312,
			"height": 130.92261650680257,
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
			"seed": 2098694695,
			"version": 38,
			"versionNonce": 1463474567,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692812383560,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-104.14299943209312,
					-130.92261650680257
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "UaRj7AKiQFulGakBqXI9g",
				"focus": 0.2631824848771657,
				"gap": 5.749315671164709
			},
			"endBinding": {
				"elementId": "2Y2eNuWRK7Rspk0Kh337Q",
				"focus": 0.34546582761394906,
				"gap": 6.142895277618095
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "kP7Hn5Xa_l3_AeY2mmJxM",
			"type": "arrow",
			"x": 2337.450524404571,
			"y": -922.0104364146403,
			"width": 252.9185993996507,
			"height": 20.828565834360234,
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
			"seed": 2043941031,
			"version": 65,
			"versionNonce": 2096336201,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692812392240,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					252.9185993996507,
					-20.828565834360234
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "2Y2eNuWRK7Rspk0Kh337Q",
				"focus": -0.07077774106333573,
				"gap": 3.7237470484329833
			},
			"endBinding": {
				"elementId": "jIO4_5ajcefRcQH06bfVt",
				"focus": 0.4663851133509368,
				"gap": 1.4741002090718212
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "edD6JbUcVM1Tw3Aflxmmr",
			"type": "image",
			"x": 1058.1836007131799,
			"y": -23.733460409979514,
			"width": 850.346718508331,
			"height": 237.03044418350694,
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
			"seed": 1749665801,
			"version": 158,
			"versionNonce": 1309827497,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "76VxL1gNEqFt7-A7ms_IH",
					"type": "arrow"
				},
				{
					"id": "9xfPsSRLyD2VbSmPdrlIz",
					"type": "arrow"
				}
			],
			"updated": 1692814429123,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "16d7367621b0d22a06aa9b8864fd7665c8517342",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "76VxL1gNEqFt7-A7ms_IH",
			"type": "arrow",
			"x": 464.7802754925194,
			"y": 198.91959813289793,
			"width": 586.9715806643546,
			"height": 158.81612280255126,
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
			"seed": 1972334729,
			"version": 167,
			"versionNonce": 469543271,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692814429124,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					586.9715806643546,
					-158.81612280255126
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "edD6JbUcVM1Tw3Aflxmmr",
				"focus": 0.7341224879347489,
				"gap": 6.431744556305944
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "9xfPsSRLyD2VbSmPdrlIz",
			"type": "arrow",
			"x": 1912.150749804727,
			"y": 106.62521593545999,
			"width": 149.25196421604574,
			"height": 99.80540989743908,
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
			"seed": 1628945353,
			"version": 681,
			"versionNonce": 160490631,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692814429124,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					149.25196421604574,
					99.80540989743908
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "edD6JbUcVM1Tw3Aflxmmr",
				"focus": -0.6826073905105747,
				"gap": 3.620430583215807
			},
			"endBinding": {
				"elementId": "NDvaTju9mg704EC1xhAbN",
				"focus": -0.593515815246255,
				"gap": 9.790834359234509
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "Dy2qSRPUJ4DUab-xNwlrG",
			"type": "arrow",
			"x": 2889.193548380007,
			"y": 161.31527076571868,
			"width": 107.6094268661841,
			"height": 9.138919737548974,
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
			"seed": 236783783,
			"version": 753,
			"versionNonce": 1369518985,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692814427208,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					107.6094268661841,
					9.138919737548974
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "NDvaTju9mg704EC1xhAbN",
				"gap": 1,
				"focus": -0.37132367710677844
			},
			"endBinding": {
				"elementId": "VCiZkEZ9AkY3PQVohSpE7",
				"gap": 5.376402156353379,
				"focus": 0.003201122157815131
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "NDvaTju9mg704EC1xhAbN",
			"type": "image",
			"x": 2071.193548380007,
			"y": 18.857035795796207,
			"width": 817,
			"height": 383,
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
			"seed": 1218477799,
			"version": 202,
			"versionNonce": 508973513,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "9xfPsSRLyD2VbSmPdrlIz",
					"type": "arrow"
				},
				{
					"id": "Dy2qSRPUJ4DUab-xNwlrG",
					"type": "arrow"
				}
			],
			"updated": 1692814427207,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "edc293eb0b29c27ba20617befe78612485833125",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "VCiZkEZ9AkY3PQVohSpE7",
			"type": "image",
			"x": 3002.1793774025446,
			"y": -16.294244905342737,
			"width": 852.7357047069644,
			"height": 448.49767167978746,
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
			"seed": 955598473,
			"version": 191,
			"versionNonce": 2121984553,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Dy2qSRPUJ4DUab-xNwlrG",
					"type": "arrow"
				},
				{
					"id": "ivnop_6wuDHU5niWaM0Zy",
					"type": "arrow"
				}
			],
			"updated": 1692814426127,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "becda6340219cacc238cfee3a96dd6874416f3b8",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "LqPB6jskOrbDuaYGuejlz",
			"type": "image",
			"x": 4116.293199868679,
			"y": 69.69006677808625,
			"width": 962,
			"height": 306,
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
			"seed": 1883526601,
			"version": 147,
			"versionNonce": 1828131401,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "ivnop_6wuDHU5niWaM0Zy",
					"type": "arrow"
				},
				{
					"id": "zKa-BnmgOQqxh1kJJS27n",
					"type": "arrow"
				}
			],
			"updated": 1692814431538,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "3c9f22170827d7e8baf0b557d067dee0d082e531",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "ivnop_6wuDHU5niWaM0Zy",
			"type": "arrow",
			"x": 3855.915082109509,
			"y": 321.5445713417854,
			"width": 256.0483051318506,
			"height": 189.87439191427256,
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
			"seed": 792707431,
			"version": 329,
			"versionNonce": 986702121,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692814431538,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					256.0483051318506,
					-189.87439191427256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "VCiZkEZ9AkY3PQVohSpE7",
				"focus": 0.7952054998012887,
				"gap": 1
			},
			"endBinding": {
				"elementId": "LqPB6jskOrbDuaYGuejlz",
				"focus": 0.8846957178140686,
				"gap": 4.32981262731937
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "2Uo2g86ptGgXXH4-bLjc7",
			"type": "image",
			"x": 5314.046742240657,
			"y": -28.39758010843559,
			"width": 805.7731962221369,
			"height": 408.9238598210245,
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
			"seed": 755690183,
			"version": 128,
			"versionNonce": 1033997705,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "zKa-BnmgOQqxh1kJJS27n",
					"type": "arrow"
				}
			],
			"updated": 1692814436412,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "44b4fd3fcd5a7674dda2a20276f8e965b26fa61f",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "zKa-BnmgOQqxh1kJJS27n",
			"type": "arrow",
			"x": 5079.930396536673,
			"y": 141.16799675950728,
			"width": 222.7766198853542,
			"height": 149.4240564417824,
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
			"seed": 1113109993,
			"version": 348,
			"versionNonce": 1594422377,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692814436412,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					222.7766198853542,
					149.4240564417824
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "LqPB6jskOrbDuaYGuejlz",
				"focus": -0.852537255011839,
				"gap": 1.6371966679935213
			},
			"endBinding": {
				"elementId": "2Uo2g86ptGgXXH4-bLjc7",
				"focus": -0.8265648669946366,
				"gap": 11.33972581863054
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "GCG3U9RJgxjm5DWCCeFzz",
			"type": "arrow",
			"x": 475.61692666034713,
			"y": -160.20589439121102,
			"width": 282.5710135463225,
			"height": 366.1166020667948,
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
			"seed": 571615305,
			"version": 487,
			"versionNonce": 1888314215,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692813937159,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					119.33378559962335,
					-300.38868275743704
				],
				[
					282.5710135463225,
					-366.1166020667948
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "LLLwrTujUuoSjSEXYwzVS",
				"focus": -0.3003323265061934,
				"gap": 3.8288323571661635
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "LLLwrTujUuoSjSEXYwzVS",
			"type": "image",
			"x": 762.0167725638358,
			"y": -1122.7973215107572,
			"width": 686.6423659051295,
			"height": 638.5693881288078,
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
			"seed": 1855971911,
			"version": 86,
			"versionNonce": 1915189449,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "GCG3U9RJgxjm5DWCCeFzz",
					"type": "arrow"
				},
				{
					"id": "qRYIZpGb-0dDaD-VO9mPN",
					"type": "arrow"
				},
				{
					"id": "QDIaAQyfo12q1Wo6bL5B-",
					"type": "arrow"
				}
			],
			"updated": 1692814027221,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "270d44b5c92439574dffbd367eba83509d1e0631",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "IFcFwbTs2uOdP-3TfC9HM",
			"type": "image",
			"x": 33.056322246950515,
			"y": -1679.2529851184174,
			"width": 568.8846198916517,
			"height": 448.869628567668,
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
			"seed": 440791401,
			"version": 174,
			"versionNonce": 1436334697,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "qRYIZpGb-0dDaD-VO9mPN",
					"type": "arrow"
				}
			],
			"updated": 1692814452175,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "dcf56ec1e87cca76f5a408c95219626fd795330f",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "qRYIZpGb-0dDaD-VO9mPN",
			"type": "arrow",
			"x": 761.0167725638358,
			"y": -1116.375238105092,
			"width": 155.4342380802558,
			"height": 229.66348372950256,
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
			"seed": 1459122055,
			"version": 123,
			"versionNonce": 751535433,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692814452175,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-155.4342380802558,
					-229.66348372950256
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "LLLwrTujUuoSjSEXYwzVS",
				"focus": -0.23477731606918253,
				"gap": 1
			},
			"endBinding": {
				"elementId": "IFcFwbTs2uOdP-3TfC9HM",
				"focus": -0.4915065971424225,
				"gap": 3.64159234497788
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "-PrJEWKIjV8vB1XHLtRl6",
			"type": "image",
			"x": 697.4235814448498,
			"y": -1573.355676128621,
			"width": 856.0000000000001,
			"height": 337,
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
			"seed": 488670727,
			"version": 35,
			"versionNonce": 976189353,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "QDIaAQyfo12q1Wo6bL5B-",
					"type": "arrow"
				}
			],
			"updated": 1692814027221,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "ec786c42763136dfd85f146e6b14dbc6d9293fbf",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "QDIaAQyfo12q1Wo6bL5B-",
			"type": "arrow",
			"x": 1070.6187378283928,
			"y": -1123.6581390543172,
			"width": 5.738725246414333,
			"height": 110.18350721795628,
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
			"seed": 1639623369,
			"version": 33,
			"versionNonce": 1086329927,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692814027221,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-5.738725246414333,
					-110.18350721795628
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "LLLwrTujUuoSjSEXYwzVS",
				"focus": -0.05013179532036371,
				"gap": 1
			},
			"endBinding": {
				"elementId": "-PrJEWKIjV8vB1XHLtRl6",
				"focus": 0.15900723518045812,
				"gap": 2.5140298563476335
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"type": "image",
			"version": 111,
			"versionNonce": 9274281,
			"isDeleted": false,
			"id": "d9zPGKRHqhu_mQrF8v7vg",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -885.8857560955438,
			"y": -1176.9887036339906,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 676.0013932736645,
			"height": 370.65350545031214,
			"seed": 1943863657,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "BMeumApWK7raQ4Jreb75Y",
					"type": "arrow"
				}
			],
			"updated": 1692814636732,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "d9f6118908369ae10753d3ac4f1ba130901fdcd6",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "XDOsh63-sUb-pl59F8vK0",
			"type": "image",
			"x": -90.93540764182842,
			"y": -1070.280944987503,
			"width": 671.6369245698771,
			"height": 215.8832971831748,
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
			"seed": 2142982375,
			"version": 115,
			"versionNonce": 1314325705,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "24l8GN_QrUlQLeF_-9-fJ",
					"type": "arrow"
				},
				{
					"id": "BMeumApWK7raQ4Jreb75Y",
					"type": "arrow"
				}
			],
			"updated": 1692814636732,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "d059e2f4ce92bda24a40843f90b18a0807e9b8da",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "24l8GN_QrUlQLeF_-9-fJ",
			"type": "arrow",
			"x": 471.0566010151465,
			"y": -128.216564811416,
			"width": 215.6344110964826,
			"height": 836.9344676253688,
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
			"seed": 256672457,
			"version": 579,
			"versionNonce": 1074383657,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692814626327,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					215.6344110964826,
					-736.9627168358436
				],
				[
					116.34679746459187,
					-836.9344676253688
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "XDOsh63-sUb-pl59F8vK0",
				"focus": -0.779449508243387,
				"gap": 6.701881551689667
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "BMeumApWK7raQ4Jreb75Y",
			"type": "arrow",
			"x": -93.25299019633621,
			"y": -989.7070149956854,
			"width": 114.27376253239504,
			"height": 39.28160303249081,
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
			"seed": 1524540233,
			"version": 41,
			"versionNonce": 706693191,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1692814636732,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-114.27376253239504,
					-39.28160303249081
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "XDOsh63-sUb-pl59F8vK0",
				"focus": -0.3978281049934735,
				"gap": 2.317582554507794
			},
			"endBinding": {
				"elementId": "d9zPGKRHqhu_mQrF8v7vg",
				"focus": -0.5118322166817927,
				"gap": 2.3576100931480823
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
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
		"currentItemFontSize": 28,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "triangle",
		"scrollX": 3415.095831552926,
		"scrollY": 2054.4267777908053,
		"zoom": {
			"value": 0.31191981267184016
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