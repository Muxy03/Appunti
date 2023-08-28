---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
SISTEMA
OPERATIVO ^3SATz2X4

RUOLI OS:

1) ARBITRO = il sistema operativo
fa da arbitro per le richieste di accesso alle
risorse. Ma c’è anche un ruolo di arbitraggio
nella gestione della memoria allocata dalle
applicazioni. Deve anche risolvere i problemi
legati alle comunicazioni tra utenti e
applicazioni

2) ILLUSIONISTA = è il ruolo fondamentale, 
illudiamo infatti l’utente
facendogli credere di avere 
a disposizione delle risorse che in realtà non ha.

3) COLLANTE =  cioè il S.O ci permette di mettere 
le cose insieme e di farle funzionare, mette a disposizione 
interfacce tra le applicazioni in modo da farle lavorare in
modo uniforme sulle risorse messe da lui a disposizione. ^7b76g4mh

KERNEL MODE (+ PRIVILEGI)
USER MODE (- PRIVILEGI) ^lzdCIGOY

User-level upcall, le upcall sono un meccanismo all’opposto del system call, ci permettono
infatti di transire da kernel a user mode, il sistema operativo dice al processo utente di
riprendere l’esecuzione, non è un vero e proprio servizio ma sono delle chiamate che
vanno nel verso opposto. Sarebbero l’equivalente dei segnali che abbiamo nel mondo
unix.
Alla base di questa transizione tra user mode e kernel mode c’è il concetto di interruzione,
le interruzioni che sono generate dai dispositivi e le eccezioni che sono lanciate da eventi
sincroni dovute ad istruzioni non legittime sono interpretabili come una sorta di interruzioni,
lo stesso sono le system call, le abbiamo infatti chiamate system software, queste
interruzioni ci permettono dunque di transire dallo stato user allo stato kernel.
Ora ci poniamo il problema di dire come facciamo a gestire le interruzioni in modo safe
essendo un meccanismo molto importante?
Non dobbiamo poter transire da user a kernel se non ne abbiamo il diritto. ^RZmoXXLl


# Embedded files
44d9def2995561d24c6d6689b0a803952e3ae514: [[Pasted Image 20230823214713_053.png]]
f8a416ea08022fdeb69a5d3ac8bbc97379a734b3: [[Pasted Image 20230823214728_073.png]]
975aff3fe0a25c2ce6e5b952470fa10f44c4bc58: [[Pasted Image 20230823215230_328.png]]
6160dd4b25bf3dee6c828a9a7e954f0903fd2480: [[Pasted Image 20230823215633_479.png]]
53d682a9dfb5703a305ddd5558879342998d0544: [[Pasted Image 20230823215818_529.png]]
8c4d3982de557d37cc18e640a71ed2c8273e2edf: [[Pasted Image 20230823220522_818.png]]
9de377579c39594fc9f995791505beb7d32ab081: [[Pasted Image 20230823220737_880.png]]
cc7eae7b94e757094543e884a6e38c8d9ff60b23: [[Pasted Image 20230823221153_046.png]]
95c29439bb15b38fdae3154f414a85436fde46c2: [[Pasted Image 20230823222038_316.png]]
c4e2aad1bb0c15609522187ec53d80e69c151e26: [[Pasted Image 20230823222341_436.png]]
b7eaeb6adbe67ed0d7c74b5f828fc43f8244d488: [[Pasted Image 20230823222912_623.png]]
1ae534569cb6acb736577a1aeca1ebba6545e6e8: [[Pasted Image 20230824025454_526.png]]
5b14233ac530a5d4bf40359decceeeae904b3e9a: [[Pasted Image 20230824025542_664.png]]
a61ffd48d1361de6c01dbf447438efd801fd439e: [[Pasted Image 20230824025700_723.png]]
7e21ff9a947ae52b8a391ab0f2992b4830ac97ae: [[Pasted Image 20230824025745_766.png]]
17d4753fa11e19a5058503b346bbb335d019655a: [[Pasted Image 20230824030146_876.png]]
0d17bdc6333bf5b1ca2c978f881796d0ce59387c: [[Pasted Image 20230824030516_962.png]]
5679b1c3f2c1b941ed6421d819e8e1a7f12968bd: [[Pasted Image 20230824030616_995.png]]
f94f8c5a5d0bddc27e02fa69492aabfe96a9ec30: [[Pasted Image 20230824030747_046.png]]
9382617dc9aac6f3289008f358ae16880bb61c75: [[Pasted Image 20230824031033_147.png]]
9e7fa91cd80af4ed830c06e23084bbc097435f83: [[Pasted Image 20230824031849_350.png]]
1fa9ca8ff23500333157f2641a388be1790e506c: [[Pasted Image 20230824032320_501.png]]
76f0217b64107ab0c9d9cedfff155b07dec6604e: [[Pasted Image 20230826153654_950.png]]
3071e1c5ac8a5a0f53bca501d540d39915e485d6: [[Pasted Image 20230826153740_991.png]]
b3d1fca1fa506ba34d3e0caa2ab15ca9fdce85ae: [[Pasted Image 20230826153928_935.png]]
d465b9bfe794c3a34f70b8a443efc640fe6c897c: [[Pasted Image 20230826154657_910.png]]
2f295192e8bc7c88e175e12ea10e2c9a0746d784: [[Pasted Image 20230826154800_928.png]]
076e4bb8289208bc83cb55166b187c777db48de2: [[Pasted Image 20230826224123_946.png]]
ef82398518a63b16ed733a81b14b07fdd808d3d8: [[Pasted Image 20230826224416_074.png]]
f3d7532999819a775eef1d75e2309ba0ef123217: [[Pasted Image 20230826224546_124.png]]
22b903194d3b2c8c5bbf267b525cf564a2e1a4be: [[Pasted Image 20230826224759_265.png]]
0e0c537c0852fd6ac855232841bd57977f383766: [[Pasted Image 20230826225046_277.png]]
b646af3c8bc69cf733ceea1c11da0b9ea2a3f599: [[Pasted Image 20230826225303_365.png]]
963b96549724834edde21621cbea1ac29705ad8b: [[Pasted Image 20230826225403_392.png]]
9d673efaddb57ffe4bc8badac6b404baf3425751: [[Pasted Image 20230826225533_443.png]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.9.17",
	"elements": [
		{
			"type": "rectangle",
			"version": 151,
			"versionNonce": 1266017382,
			"isDeleted": false,
			"id": "9Mu00ZyXA6NsPuqtVJKmO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -369.84081084426225,
			"y": -41.255899790418994,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 141,
			"height": 90,
			"seed": 2090124359,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "3SATz2X4"
				},
				{
					"id": "fmkB6Qv9yVphej1w3tKkd",
					"type": "arrow"
				},
				{
					"id": "wy0LpvAImYx-eBCBaM59H",
					"type": "arrow"
				},
				{
					"id": "U1FiafJ_kPPjYu9dHYMWG",
					"type": "arrow"
				},
				{
					"id": "9gpWU2EUN_rU1GDipcFhC",
					"type": "arrow"
				},
				{
					"id": "boJDv75J7xI4uOkDwpGBD",
					"type": "arrow"
				},
				{
					"id": "qcG_c3DzJQhCL8UCKycBq",
					"type": "arrow"
				},
				{
					"id": "Svip9CmKK-q5XCJuB5XjY",
					"type": "arrow"
				}
			],
			"updated": 1692967183906,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 114,
			"versionNonce": 1829957513,
			"isDeleted": false,
			"id": "3SATz2X4",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -359.2107754438716,
			"y": -21.255899790418994,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 119.73992919921875,
			"height": 50,
			"seed": 728095913,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1692822081332,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "SISTEMA\nOPERATIVO",
			"rawText": "SISTEMA\nOPERATIVO",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "9Mu00ZyXA6NsPuqtVJKmO",
			"originalText": "SISTEMA\nOPERATIVO",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "image",
			"version": 135,
			"versionNonce": 1072170855,
			"isDeleted": false,
			"id": "n6TwzXGDzz_JOVcZvhAiQ",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -360.7361989541282,
			"y": -456.43190120873385,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 399,
			"height": 178,
			"seed": 1587932903,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "fmkB6Qv9yVphej1w3tKkd",
					"type": "arrow"
				}
			],
			"updated": 1692838936044,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "44d9def2995561d24c6d6689b0a803952e3ae514",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 351,
			"versionNonce": 2029200294,
			"isDeleted": false,
			"id": "fmkB6Qv9yVphej1w3tKkd",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -291.8080598338838,
			"y": -42.923151377333056,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 98.97888900005827,
			"height": 233.6299656517133,
			"seed": 1504743977,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083333524,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "9Mu00ZyXA6NsPuqtVJKmO",
				"gap": 1.6672515869140625,
				"focus": -0.13664045245189402
			},
			"endBinding": {
				"elementId": "n6TwzXGDzz_JOVcZvhAiQ",
				"gap": 1.8787841796875,
				"focus": -0.029124245565021818
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
					98.97888900005827,
					-233.6299656517133
				]
			]
		},
		{
			"type": "image",
			"version": 191,
			"versionNonce": 1708422121,
			"isDeleted": false,
			"id": "MxXKAfPswyZSkalvfHV-D",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 115.32554615355798,
			"y": -664.9328424999525,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 578.151613153963,
			"height": 686.7384643554688,
			"seed": 1878565543,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "wy0LpvAImYx-eBCBaM59H",
					"type": "arrow"
				}
			],
			"updated": 1692838937911,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "f8a416ea08022fdeb69a5d3ac8bbc97379a734b3",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 329,
			"versionNonce": 76476966,
			"isDeleted": false,
			"id": "wy0LpvAImYx-eBCBaM59H",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -226.7786160200435,
			"y": -24.06977252696298,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 338.019811587664,
			"height": 245.6521128781278,
			"seed": 2020427591,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083333524,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "9Mu00ZyXA6NsPuqtVJKmO",
				"gap": 2.06219482421875,
				"focus": 0.2589480713068431
			},
			"endBinding": {
				"elementId": "MxXKAfPswyZSkalvfHV-D",
				"gap": 4.0843505859375,
				"focus": 0.29127943125426303
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
					338.019811587664,
					-245.6521128781278
				]
			]
		},
		{
			"type": "text",
			"version": 449,
			"versionNonce": 2043346534,
			"isDeleted": false,
			"id": "7b76g4mh",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1920.35774928337,
			"y": 307.6211913810364,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 728.736375664882,
			"height": 594.4324667350251,
			"seed": 2076442055,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "JxtxzxKkvwut4VIRk1LjY",
					"type": "arrow"
				}
			],
			"updated": 1693083398493,
			"link": null,
			"locked": false,
			"fontSize": 25.02873544147474,
			"fontFamily": 1,
			"text": "RUOLI OS:\n\n1) ARBITRO = il sistema operativo\nfa da arbitro per le richieste di accesso alle\nrisorse. Ma c’è anche un ruolo di arbitraggio\nnella gestione della memoria allocata dalle\napplicazioni. Deve anche risolvere i problemi\nlegati alle comunicazioni tra utenti e\napplicazioni\n\n2) ILLUSIONISTA = è il ruolo fondamentale, \nilludiamo infatti l’utente\nfacendogli credere di avere \na disposizione delle risorse che in realtà non ha.\n\n3) COLLANTE =  cioè il S.O ci permette di mettere \nle cose insieme e di farle funzionare, mette a disposizione \ninterfacce tra le applicazioni in modo da farle lavorare in\nmodo uniforme sulle risorse messe da lui a disposizione.",
			"rawText": "RUOLI OS:\n\n1) ARBITRO = il sistema operativo\nfa da arbitro per le richieste di accesso alle\nrisorse. Ma c’è anche un ruolo di arbitraggio\nnella gestione della memoria allocata dalle\napplicazioni. Deve anche risolvere i problemi\nlegati alle comunicazioni tra utenti e\napplicazioni\n\n2) ILLUSIONISTA = è il ruolo fondamentale, \nilludiamo infatti l’utente\nfacendogli credere di avere \na disposizione delle risorse che in realtà non ha.\n\n3) COLLANTE =  cioè il S.O ci permette di mettere \nle cose insieme e di farle funzionare, mette a disposizione \ninterfacce tra le applicazioni in modo da farle lavorare in\nmodo uniforme sulle risorse messe da lui a disposizione.",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "RUOLI OS:\n\n1) ARBITRO = il sistema operativo\nfa da arbitro per le richieste di accesso alle\nrisorse. Ma c’è anche un ruolo di arbitraggio\nnella gestione della memoria allocata dalle\napplicazioni. Deve anche risolvere i problemi\nlegati alle comunicazioni tra utenti e\napplicazioni\n\n2) ILLUSIONISTA = è il ruolo fondamentale, \nilludiamo infatti l’utente\nfacendogli credere di avere \na disposizione delle risorse che in realtà non ha.\n\n3) COLLANTE =  cioè il S.O ci permette di mettere \nle cose insieme e di farle funzionare, mette a disposizione \ninterfacce tra le applicazioni in modo da farle lavorare in\nmodo uniforme sulle risorse messe da lui a disposizione.",
			"lineHeight": 1.25,
			"baseline": 584
		},
		{
			"type": "rectangle",
			"version": 398,
			"versionNonce": 1040479802,
			"isDeleted": false,
			"id": "tMwKHX-bMYlvaYne57U5H",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1951.9051599724746,
			"y": 287.33522274569316,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 784.7830060026483,
			"height": 624.4527841342863,
			"seed": 779139719,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "JxtxzxKkvwut4VIRk1LjY",
					"type": "arrow"
				},
				{
					"id": "0Yexm0Hn6ojcFpu91Od47",
					"type": "arrow"
				}
			],
			"updated": 1693083393564,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 555,
			"versionNonce": 692952826,
			"isDeleted": false,
			"id": "JxtxzxKkvwut4VIRk1LjY",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -367.89821944302327,
			"y": 17.147140534336074,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 789.4481981499262,
			"height": 398.69552594244686,
			"seed": 311332521,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083393564,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "tMwKHX-bMYlvaYne57U5H",
				"gap": 9.775736376876807,
				"focus": 0.03798584601775003
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
					-789.4481981499262,
					398.69552594244686
				]
			]
		},
		{
			"type": "image",
			"version": 205,
			"versionNonce": 982814330,
			"isDeleted": false,
			"id": "koqJnps1QjzkmCYnzb2UL",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2992.5621364633303,
			"y": 807.4851711168362,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 815.7666406515044,
			"height": 402.27881668768845,
			"seed": 1250729575,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "0Yexm0Hn6ojcFpu91Od47",
					"type": "arrow"
				}
			],
			"updated": 1693083385692,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "975aff3fe0a25c2ce6e5b952470fa10f44c4bc58",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 1083,
			"versionNonce": 387557498,
			"isDeleted": false,
			"id": "0Yexm0Hn6ojcFpu91Od47",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1956.247166282314,
			"y": 649.0388270364847,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 216.21672366197618,
			"height": 229.15720901145664,
			"seed": 872902823,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083393564,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "tMwKHX-bMYlvaYne57U5H",
				"gap": 4.3420063098396895,
				"focus": 0.5098688099027249
			},
			"endBinding": {
				"elementId": "koqJnps1QjzkmCYnzb2UL",
				"gap": 4.3316058675354725,
				"focus": 0.48380272801721147
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
					-216.21672366197618,
					229.15720901145664
				]
			]
		},
		{
			"type": "image",
			"version": 190,
			"versionNonce": 2054486761,
			"isDeleted": false,
			"id": "C-G0rfRYLlyp4N_JknpHi",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1541.0975802297307,
			"y": -878.2737954333791,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 601.8229543902678,
			"height": 747.5635558807885,
			"seed": 1132359303,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "U1FiafJ_kPPjYu9dHYMWG",
					"type": "arrow"
				}
			],
			"updated": 1692839297162,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "6160dd4b25bf3dee6c828a9a7e954f0903fd2480",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 280,
			"versionNonce": 1902715046,
			"isDeleted": false,
			"id": "U1FiafJ_kPPjYu9dHYMWG",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -372.5207674423876,
			"y": -40.992521576004066,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 565.620372241709,
			"height": 173.74927333548945,
			"seed": 166976583,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083333524,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "9Mu00ZyXA6NsPuqtVJKmO",
				"gap": 2.6799565981252726,
				"focus": 0.33390536508117025
			},
			"endBinding": {
				"elementId": "C-G0rfRYLlyp4N_JknpHi",
				"gap": 1.1334861553661995,
				"focus": 0.4224793371913505
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
					-565.620372241709,
					-173.74927333548945
				]
			]
		},
		{
			"type": "image",
			"version": 189,
			"versionNonce": 1508183431,
			"isDeleted": false,
			"id": "dqbHwML9jwDXQa38PWa23",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -131.47897248536367,
			"y": 329.4426244869668,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1011.232227787355,
			"height": 581.716498382777,
			"seed": 113875911,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "WAQQA5Kpe2ucvQMGSeuHu",
					"type": "arrow"
				},
				{
					"id": "A6-XIMb_8vxiehKFt25Uz",
					"type": "arrow"
				}
			],
			"updated": 1692821127707,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "53d682a9dfb5703a305ddd5558879342998d0544",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 141,
			"versionNonce": 21522342,
			"isDeleted": false,
			"id": "WAQQA5Kpe2ucvQMGSeuHu",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -239.13427321148276,
			"y": 45.3676388525285,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 195.14123118813006,
			"height": 281.03247218601166,
			"seed": 2143428391,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692967183907,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "dqbHwML9jwDXQa38PWa23",
				"focus": -0.3025149609247945,
				"gap": 3.0425134484266323
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
					195.14123118813006,
					281.03247218601166
				]
			]
		},
		{
			"type": "image",
			"version": 41,
			"versionNonce": 1438450953,
			"isDeleted": false,
			"id": "14_-cp3d86LvBpVoPjqHa",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1047.6534811660654,
			"y": 334.870339083424,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1053.5337020268921,
			"height": 532.0120401416027,
			"seed": 789462025,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "A6-XIMb_8vxiehKFt25Uz",
					"type": "arrow"
				},
				{
					"id": "FyGX4oFRvCC7aIT9JPso2",
					"type": "arrow"
				}
			],
			"updated": 1692821260925,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "8c4d3982de557d37cc18e640a71ed2c8273e2edf",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 25,
			"versionNonce": 1826730601,
			"isDeleted": false,
			"id": "A6-XIMb_8vxiehKFt25Uz",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 883.5443346392459,
			"y": 610.5602752229931,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 159.3107373432207,
			"height": 53.10359228563652,
			"seed": 1866399751,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692821127707,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "dqbHwML9jwDXQa38PWa23",
				"focus": 0.3484172576845196,
				"gap": 3.791079337254587
			},
			"endBinding": {
				"elementId": "14_-cp3d86LvBpVoPjqHa",
				"focus": 0.49957117552626823,
				"gap": 4.798409183598778
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
					159.3107373432207,
					-53.10359228563652
				]
			]
		},
		{
			"type": "image",
			"version": 120,
			"versionNonce": 1187512999,
			"isDeleted": false,
			"id": "mcGD24x_bkJb2FBgvV-ox",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1081.7025943126494,
			"y": 1076.0318870832448,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 906.3251628693657,
			"height": 980.3596294015142,
			"seed": 992384967,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "FyGX4oFRvCC7aIT9JPso2",
					"type": "arrow"
				}
			],
			"updated": 1692821262714,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "9de377579c39594fc9f995791505beb7d32ab081",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 90,
			"versionNonce": 203363783,
			"isDeleted": false,
			"id": "FyGX4oFRvCC7aIT9JPso2",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1586.1790446345194,
			"y": 873.0927798933099,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 13.004243478640547,
			"height": 196.074866115232,
			"seed": 669472455,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692821262714,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "14_-cp3d86LvBpVoPjqHa",
				"focus": 0.011649504317602567,
				"gap": 6.210400668283114
			},
			"endBinding": {
				"elementId": "mcGD24x_bkJb2FBgvV-ox",
				"focus": 0.2003066860481914,
				"gap": 6.864241074702932
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
					13.004243478640547,
					196.074866115232
				]
			]
		},
		{
			"type": "image",
			"version": 104,
			"versionNonce": 1134186406,
			"isDeleted": false,
			"id": "-SRj_CA8-CLMGr0MMuBfk",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -822.5714047730813,
			"y": -998.159426651919,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 781,
			"height": 431,
			"seed": 929481959,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "9gpWU2EUN_rU1GDipcFhC",
					"type": "arrow"
				},
				{
					"id": "WGGfeQm0VOvESzJwrIkNY",
					"type": "arrow"
				},
				{
					"id": "jjNcynNMP8F51PWePmeYH",
					"type": "arrow"
				}
			],
			"updated": 1693083419537,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "cc7eae7b94e757094543e884a6e38c8d9ff60b23",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 252,
			"versionNonce": 191475494,
			"isDeleted": false,
			"id": "9gpWU2EUN_rU1GDipcFhC",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -316.64483739369507,
			"y": -42.255899790418994,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 219.84373432082396,
			"height": 521.5224064711938,
			"seed": 1085232329,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083333524,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "9Mu00ZyXA6NsPuqtVJKmO",
				"gap": 1,
				"focus": 0.023325487934916105
			},
			"endBinding": {
				"elementId": "-SRj_CA8-CLMGr0MMuBfk",
				"gap": 3.3811203903062506,
				"focus": 0.40861728942817427
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
					-219.84373432082396,
					-521.5224064711938
				]
			]
		},
		{
			"type": "text",
			"version": 52,
			"versionNonce": 1768728969,
			"isDeleted": false,
			"id": "lzdCIGOY",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 229.718868553143,
			"y": -815.501172585221,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 427.2518615722656,
			"height": 70,
			"seed": 1772067399,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1692821943365,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "KERNEL MODE (+ PRIVILEGI)\nUSER MODE (- PRIVILEGI)",
			"rawText": "KERNEL MODE (+ PRIVILEGI)\nUSER MODE (- PRIVILEGI)",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "KERNEL MODE (+ PRIVILEGI)\nUSER MODE (- PRIVILEGI)",
			"lineHeight": 1.25,
			"baseline": 59
		},
		{
			"type": "rectangle",
			"version": 58,
			"versionNonce": 92298121,
			"isDeleted": false,
			"id": "6CR09fYriekjhcx2U_YsO",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 213.10509129421325,
			"y": -822.7499080736359,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 470.8288823180469,
			"height": 87.43961388183288,
			"seed": 808669063,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "WGGfeQm0VOvESzJwrIkNY",
					"type": "arrow"
				},
				{
					"id": "y5zR0_pc2S3wGKEczAdzH",
					"type": "arrow"
				},
				{
					"id": "gdvlIlzBSC24grh-056Xi",
					"type": "arrow"
				}
			],
			"updated": 1692838671577,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 40,
			"versionNonce": 411895175,
			"isDeleted": false,
			"id": "WGGfeQm0VOvESzJwrIkNY",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -30.38052947539859,
			"y": -767.595715310928,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 242.1403851302489,
			"height": 8.071335760982038,
			"seed": 409972487,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692821967263,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "-SRj_CA8-CLMGr0MMuBfk",
				"focus": 0.12451342136345071,
				"gap": 11.190875297682737
			},
			"endBinding": {
				"elementId": "6CR09fYriekjhcx2U_YsO",
				"focus": 0.08782620338502163,
				"gap": 1.3452356393629543
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
					242.1403851302489,
					-8.071335760982038
				]
			]
		},
		{
			"type": "image",
			"version": 273,
			"versionNonce": 466572838,
			"isDeleted": false,
			"id": "QQGlDxs6iu3DkQ4K-J_J0",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1149.8261271867718,
			"y": 997.0604710783209,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1163.4811496764871,
			"height": 314.2472143394992,
			"seed": 1790342185,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "boJDv75J7xI4uOkDwpGBD",
					"type": "arrow"
				},
				{
					"id": "mMuhqm0-pGaGWp0sDIuqg",
					"type": "arrow"
				},
				{
					"id": "CkJI9iDgFqewXhQ5y3Kh4",
					"type": "arrow"
				}
			],
			"updated": 1693083374674,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "95c29439bb15b38fdae3154f414a85436fde46c2",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 721,
			"versionNonce": 1994425510,
			"isDeleted": false,
			"id": "boJDv75J7xI4uOkDwpGBD",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -318.01111973784344,
			"y": 57.21100488635,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 272.0443293785219,
			"height": 936.1654909424417,
			"seed": 1229362471,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083374675,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "9Mu00ZyXA6NsPuqtVJKmO",
				"gap": 8.46690467676899,
				"focus": 0.03794243158633724
			},
			"endBinding": {
				"elementId": "QQGlDxs6iu3DkQ4K-J_J0",
				"gap": 3.6839752495291123,
				"focus": -0.10949901428441934
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
					-272.0443293785219,
					936.1654909424417
				]
			]
		},
		{
			"type": "image",
			"version": 246,
			"versionNonce": 1017066599,
			"isDeleted": false,
			"id": "4Mgr-CQr9GxT4ANKHWbGH",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2070.768880252145,
			"y": 1451.3274460514017,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1187.111133678742,
			"height": 915.8142710577164,
			"seed": 50059433,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "mMuhqm0-pGaGWp0sDIuqg",
					"type": "arrow"
				},
				{
					"id": "ISBMKLl262PzpM5-fmUrB",
					"type": "arrow"
				}
			],
			"updated": 1692838506380,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "c4e2aad1bb0c15609522187ec53d80e69c151e26",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 397,
			"versionNonce": 492311334,
			"isDeleted": false,
			"id": "mMuhqm0-pGaGWp0sDIuqg",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -827.0934673037614,
			"y": 1312.680097143907,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 294.76969664842727,
			"height": 137.6473489074947,
			"seed": 1599214473,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083374675,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "QQGlDxs6iu3DkQ4K-J_J0",
				"focus": -0.08441299729367555,
				"gap": 1.3724117260870798
			},
			"endBinding": {
				"elementId": "4Mgr-CQr9GxT4ANKHWbGH",
				"focus": -0.398557826752609,
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
					-294.76969664842727,
					137.6473489074947
				]
			]
		},
		{
			"type": "arrow",
			"version": 279,
			"versionNonce": 1897791910,
			"isDeleted": false,
			"id": "CkJI9iDgFqewXhQ5y3Kh4",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -478.9998027960189,
			"y": 1312.5229304086768,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 399.5000049535354,
			"height": 197.14532684297365,
			"seed": 1742404327,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083374675,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "QQGlDxs6iu3DkQ4K-J_J0",
				"focus": 0.25636780042881907,
				"gap": 1.2152449908568315
			},
			"endBinding": {
				"elementId": "vmNNuWE-4yTnP8QkvlCc9",
				"focus": 0.22749758427135736,
				"gap": 5.440261668091011
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
					399.5000049535354,
					197.14532684297365
				]
			]
		},
		{
			"type": "image",
			"version": 90,
			"versionNonce": 1439865799,
			"isDeleted": false,
			"id": "vmNNuWE-4yTnP8QkvlCc9",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -652.3162057058203,
			"y": 1515.1085189197415,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1431.2032504692208,
			"height": 376.3323288086397,
			"seed": 972112841,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "CkJI9iDgFqewXhQ5y3Kh4",
					"type": "arrow"
				}
			],
			"updated": 1692822552294,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "b7eaeb6adbe67ed0d7c74b5f828fc43f8244d488",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "image",
			"version": 86,
			"versionNonce": 648576233,
			"isDeleted": false,
			"id": "L-13VZJPQXf452bfbRco0",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2214.5198904416447,
			"y": 2638.164229814481,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1596.1739386321935,
			"height": 524.4571512648636,
			"seed": 1936810889,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "ZwgQN87G-ME1cjHrxC25D",
					"type": "arrow"
				}
			],
			"updated": 1692838550262,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "1ae534569cb6acb736577a1aeca1ebba6545e6e8",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 60,
			"versionNonce": 188917417,
			"isDeleted": false,
			"id": "ISBMKLl262PzpM5-fmUrB",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1528.1360886917105,
			"y": 2371.8152391347066,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 176.36072640218345,
			"height": 267.9991204340695,
			"seed": 984343207,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692838506380,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "4Mgr-CQr9GxT4ANKHWbGH",
				"focus": 0.39706723714097797,
				"gap": 4.673522025588682
			},
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
					176.36072640218345,
					267.9991204340695
				]
			]
		},
		{
			"type": "image",
			"version": 195,
			"versionNonce": 473626569,
			"isDeleted": false,
			"id": "Mfa1e_92U_05qQcj7aeQX",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -2215.8805084074743,
			"y": 3317.048452518014,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1599.9113540250826,
			"height": 434.23154009112915,
			"seed": 1197854825,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "ZwgQN87G-ME1cjHrxC25D",
					"type": "arrow"
				}
			],
			"updated": 1692838550262,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "5b14233ac530a5d4bf40359decceeeae904b3e9a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 38,
			"versionNonce": 1406722599,
			"isDeleted": false,
			"id": "ZwgQN87G-ME1cjHrxC25D",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -1408.8332974875996,
			"y": 3171.256684079508,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.916061661588628,
			"height": 140.05107653945697,
			"seed": 2142244551,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692838550262,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "L-13VZJPQXf452bfbRco0",
				"focus": -0.025862633573353125,
				"gap": 8.635303000163276
			},
			"endBinding": {
				"elementId": "Mfa1e_92U_05qQcj7aeQX",
				"focus": -0.013358853157436974,
				"gap": 5.740691899049125
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
					-6.916061661588628,
					140.05107653945697
				]
			]
		},
		{
			"type": "image",
			"version": 189,
			"versionNonce": 1680146377,
			"isDeleted": false,
			"id": "kaDGxgkkh3BLuD7UStFp1",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 822.504577041251,
			"y": -1605.7350513014078,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1033.556337394638,
			"height": 1014.7887774419466,
			"seed": 1289438727,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "y5zR0_pc2S3wGKEczAdzH",
					"type": "arrow"
				},
				{
					"id": "l6e_WEalyXhHTNjz1LQCc",
					"type": "arrow"
				},
				{
					"id": "79whhoCH_H4-6NZIMSJuC",
					"type": "arrow"
				}
			],
			"updated": 1692839881979,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "a61ffd48d1361de6c01dbf447438efd801fd439e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 65,
			"versionNonce": 347563207,
			"isDeleted": false,
			"id": "y5zR0_pc2S3wGKEczAdzH",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 473.1165030329711,
			"y": -823.9198964715871,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 345.80529079219764,
			"height": 337.160188627567,
			"seed": 255640649,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692838635081,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "6CR09fYriekjhcx2U_YsO",
				"focus": -0.07651539055917869,
				"gap": 1.1699883979512151
			},
			"endBinding": {
				"elementId": "kaDGxgkkh3BLuD7UStFp1",
				"focus": 0.5637474622017146,
				"gap": 3.582783216082248
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
					345.80529079219764,
					-337.160188627567
				]
			]
		},
		{
			"type": "image",
			"version": 133,
			"versionNonce": 2049838202,
			"isDeleted": false,
			"id": "r_XoYdqmlqo8DKkVM0LNB",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -563.8568144740384,
			"y": -1522.7239252614863,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1165.6878192518416,
			"height": 432.2382482238741,
			"seed": 1681661703,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "gdvlIlzBSC24grh-056Xi",
					"type": "arrow"
				}
			],
			"updated": 1693083105444,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "7e21ff9a947ae52b8a391ab0f2992b4830ac97ae",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 168,
			"versionNonce": 165459450,
			"isDeleted": false,
			"id": "gdvlIlzBSC24grh-056Xi",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 373.0677518513092,
			"y": -824.6302782313684,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 31.385342652608017,
			"height": 253.5880164430224,
			"seed": 385260583,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083105444,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "6CR09fYriekjhcx2U_YsO",
				"focus": -0.28985292686101266,
				"gap": 1.8803701577323864
			},
			"endBinding": {
				"elementId": "r_XoYdqmlqo8DKkVM0LNB",
				"focus": -0.48299367632612233,
				"gap": 12.267382363221486
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
					-31.385342652608017,
					-253.5880164430224
				]
			]
		},
		{
			"type": "image",
			"version": 290,
			"versionNonce": 63003719,
			"isDeleted": false,
			"id": "F3-EqBMHvaX2l8hSo-M-N",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 925.40817985728,
			"y": -539.6775765847644,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1000.056816389559,
			"height": 836.3419314729941,
			"seed": 1839451465,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "qcG_c3DzJQhCL8UCKycBq",
					"type": "arrow"
				}
			],
			"updated": 1692838958702,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "17d4753fa11e19a5058503b346bbb335d019655a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 159,
			"versionNonce": 880667686,
			"isDeleted": false,
			"id": "qcG_c3DzJQhCL8UCKycBq",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -227.84081084426225,
			"y": 5.770087568325998,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1147.0590742133459,
			"height": 116.7977393520029,
			"seed": 2019752487,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083333524,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "9Mu00ZyXA6NsPuqtVJKmO",
				"gap": 1,
				"focus": -0.10070041692765391
			},
			"endBinding": {
				"elementId": "F3-EqBMHvaX2l8hSo-M-N",
				"gap": 6.189916488196332,
				"focus": -0.6302034902751285
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
					1147.0590742133459,
					116.7977393520029
				]
			]
		},
		{
			"type": "image",
			"version": 84,
			"versionNonce": 874386279,
			"isDeleted": false,
			"id": "ychXhsBVyeTsI8cOud7VB",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2326.9478656493507,
			"y": -669.894727494794,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1010.7106580935373,
			"height": 898.1151064055285,
			"seed": 2038747785,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "lbI5ee3bgs5HvlnbZw6Fm",
					"type": "arrow"
				},
				{
					"id": "ojwOYIb89Bm9JIxKE-CH4",
					"type": "arrow"
				}
			],
			"updated": 1692839184608,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "0d17bdc6333bf5b1ca2c978f881796d0ce59387c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 49,
			"versionNonce": 82715465,
			"isDeleted": false,
			"id": "lbI5ee3bgs5HvlnbZw6Fm",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1924.6142917626723,
			"y": -116.1366619451851,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 392.49925081869947,
			"height": 225.03298952369232,
			"seed": 327151177,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692839127342,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "ychXhsBVyeTsI8cOud7VB",
				"focus": 0.5626840306366988,
				"gap": 9.83432306797863
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
					392.49925081869947,
					-225.03298952369232
				]
			]
		},
		{
			"type": "image",
			"version": 179,
			"versionNonce": 771034759,
			"isDeleted": false,
			"id": "bet6GGDvuB_aSCPr3YF6R",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2300.265598648665,
			"y": 348.5113716435151,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1265.047163578126,
			"height": 200.9888016899826,
			"seed": 13598951,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "ojwOYIb89Bm9JIxKE-CH4",
					"type": "arrow"
				}
			],
			"updated": 1692839184609,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "5679b1c3f2c1b941ed6421d819e8e1a7f12968bd",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 36,
			"versionNonce": 856455817,
			"isDeleted": false,
			"id": "ojwOYIb89Bm9JIxKE-CH4",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2866.560737160007,
			"y": 233.23940557704884,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 106.41077390603868,
			"height": 113.38869720757225,
			"seed": 812288713,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692839184609,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ychXhsBVyeTsI8cOud7VB",
				"focus": 0.42283616480034913,
				"gap": 5.019026666314289
			},
			"endBinding": {
				"elementId": "bet6GGDvuB_aSCPr3YF6R",
				"focus": 0.18747028092483203,
				"gap": 1.8832688588939845
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
					106.41077390603868,
					113.38869720757225
				]
			]
		},
		{
			"type": "image",
			"version": 488,
			"versionNonce": 713153338,
			"isDeleted": false,
			"id": "Dr-_iKkPdB6kOm9AWRBtG",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -3200.6369963362804,
			"y": 91.34742251385501,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1017.5623681997765,
			"height": 449.3664686412436,
			"seed": 267660361,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Svip9CmKK-q5XCJuB5XjY",
					"type": "arrow"
				}
			],
			"updated": 1693083403456,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "f94f8c5a5d0bddc27e02fa69492aabfe96a9ec30",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 1016,
			"versionNonce": 689689786,
			"isDeleted": false,
			"id": "Svip9CmKK-q5XCJuB5XjY",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -370.84081084426225,
			"y": -0.42746348388075717,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1808.1405507610375,
			"height": 226.02210036300227,
			"seed": 968148103,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083403457,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "9Mu00ZyXA6NsPuqtVJKmO",
				"gap": 1,
				"focus": 0.2437436309699484
			},
			"endBinding": {
				"elementId": "Dr-_iKkPdB6kOm9AWRBtG",
				"gap": 4.093266531204108,
				"focus": -0.09131827133476521
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
					-1808.1405507610375,
					226.02210036300227
				]
			]
		},
		{
			"type": "image",
			"version": 127,
			"versionNonce": 1776053626,
			"isDeleted": false,
			"id": "Bg2c6QLx6PErJNOyfDJ4q",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 2173.9353697883157,
			"y": -1549.4119413380793,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1319.714860881438,
			"height": 658.0883756674194,
			"seed": 1729393575,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "l6e_WEalyXhHTNjz1LQCc",
					"type": "arrow"
				},
				{
					"id": "niQqyyCO4xhP-FGMO4phL",
					"type": "arrow"
				},
				{
					"id": "WiCSPrFcNIMobB_dELGJT",
					"type": "arrow"
				}
			],
			"updated": 1693083093613,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "9382617dc9aac6f3289008f358ae16880bb61c75",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 124,
			"versionNonce": 1498101798,
			"isDeleted": false,
			"id": "l6e_WEalyXhHTNjz1LQCc",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1858.1096335988523,
			"y": -1212.1438358048802,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 311.09978605511924,
			"height": 64.65205556352089,
			"seed": 143986505,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083078759,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "kaDGxgkkh3BLuD7UStFp1",
				"focus": -0.013408037479861521,
				"gap": 2.0487191629631525
			},
			"endBinding": {
				"elementId": "Bg2c6QLx6PErJNOyfDJ4q",
				"focus": 0.41731251359209126,
				"gap": 4.7259501343442025
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
					311.09978605511924,
					-64.65205556352089
				]
			]
		},
		{
			"type": "text",
			"version": 343,
			"versionNonce": 325033274,
			"isDeleted": false,
			"id": "RZmoXXLl",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -574.8650494230133,
			"y": -2333.0994570740577,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1638.2994384765625,
			"height": 582.8186807897832,
			"seed": 1183001865,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1693083107586,
			"link": null,
			"locked": false,
			"fontSize": 35.86576497167896,
			"fontFamily": 1,
			"text": "User-level upcall, le upcall sono un meccanismo all’opposto del system call, ci permettono\ninfatti di transire da kernel a user mode, il sistema operativo dice al processo utente di\nriprendere l’esecuzione, non è un vero e proprio servizio ma sono delle chiamate che\nvanno nel verso opposto. Sarebbero l’equivalente dei segnali che abbiamo nel mondo\nunix.\nAlla base di questa transizione tra user mode e kernel mode c’è il concetto di interruzione,\nle interruzioni che sono generate dai dispositivi e le eccezioni che sono lanciate da eventi\nsincroni dovute ad istruzioni non legittime sono interpretabili come una sorta di interruzioni,\nlo stesso sono le system call, le abbiamo infatti chiamate system software, queste\ninterruzioni ci permettono dunque di transire dallo stato user allo stato kernel.\nOra ci poniamo il problema di dire come facciamo a gestire le interruzioni in modo safe\nessendo un meccanismo molto importante?\nNon dobbiamo poter transire da user a kernel se non ne abbiamo il diritto.",
			"rawText": "User-level upcall, le upcall sono un meccanismo all’opposto del system call, ci permettono\ninfatti di transire da kernel a user mode, il sistema operativo dice al processo utente di\nriprendere l’esecuzione, non è un vero e proprio servizio ma sono delle chiamate che\nvanno nel verso opposto. Sarebbero l’equivalente dei segnali che abbiamo nel mondo\nunix.\nAlla base di questa transizione tra user mode e kernel mode c’è il concetto di interruzione,\nle interruzioni che sono generate dai dispositivi e le eccezioni che sono lanciate da eventi\nsincroni dovute ad istruzioni non legittime sono interpretabili come una sorta di interruzioni,\nlo stesso sono le system call, le abbiamo infatti chiamate system software, queste\ninterruzioni ci permettono dunque di transire dallo stato user allo stato kernel.\nOra ci poniamo il problema di dire come facciamo a gestire le interruzioni in modo safe\nessendo un meccanismo molto importante?\nNon dobbiamo poter transire da user a kernel se non ne abbiamo il diritto.",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "User-level upcall, le upcall sono un meccanismo all’opposto del system call, ci permettono\ninfatti di transire da kernel a user mode, il sistema operativo dice al processo utente di\nriprendere l’esecuzione, non è un vero e proprio servizio ma sono delle chiamate che\nvanno nel verso opposto. Sarebbero l’equivalente dei segnali che abbiamo nel mondo\nunix.\nAlla base di questa transizione tra user mode e kernel mode c’è il concetto di interruzione,\nle interruzioni che sono generate dai dispositivi e le eccezioni che sono lanciate da eventi\nsincroni dovute ad istruzioni non legittime sono interpretabili come una sorta di interruzioni,\nlo stesso sono le system call, le abbiamo infatti chiamate system software, queste\ninterruzioni ci permettono dunque di transire dallo stato user allo stato kernel.\nOra ci poniamo il problema di dire come facciamo a gestire le interruzioni in modo safe\nessendo un meccanismo molto importante?\nNon dobbiamo poter transire da user a kernel se non ne abbiamo il diritto.",
			"lineHeight": 1.25,
			"baseline": 568
		},
		{
			"type": "rectangle",
			"version": 357,
			"versionNonce": 70510906,
			"isDeleted": false,
			"id": "DeBcjSlh-9xlUSTb6z1Hm",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -625.003853836062,
			"y": -2362.213437581685,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1714.7860009809267,
			"height": 647.1877815911504,
			"seed": 2009870569,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "79whhoCH_H4-6NZIMSJuC",
					"type": "arrow"
				},
				{
					"id": "05_N4FDqZktA2evIK1Moh",
					"type": "arrow"
				}
			],
			"updated": 1693083273137,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 666,
			"versionNonce": 1428281062,
			"isDeleted": false,
			"id": "79whhoCH_H4-6NZIMSJuC",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 1046.3058193460251,
			"y": -1607.0670036478643,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 127.39316415248777,
			"height": 428.92935199447265,
			"seed": 868502217,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083153584,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "kaDGxgkkh3BLuD7UStFp1",
				"focus": -0.81563318007402,
				"gap": 1.3319523464564327
			},
			"endBinding": {
				"elementId": "DeBcjSlh-9xlUSTb6z1Hm",
				"focus": -0.9166445662191961,
				"gap": 1.8574193079293764
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
					127.39316415248777,
					-94.0434776327254
				],
				[
					45.3337471067689,
					-428.92935199447265
				]
			]
		},
		{
			"type": "image",
			"version": 127,
			"versionNonce": 1005625978,
			"isDeleted": false,
			"id": "yqg_TsAT-oythfyIHrcTA",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3781.301885262519,
			"y": -1924.7447252251427,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1248.2750166245498,
			"height": 1275.8701730388766,
			"seed": 1299912583,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "niQqyyCO4xhP-FGMO4phL",
					"type": "arrow"
				},
				{
					"id": "MDHf9tyvFUb3p2ObYGIBV",
					"type": "arrow"
				},
				{
					"id": "hVSlDbN0sA9_knaMBAsKi",
					"type": "arrow"
				},
				{
					"id": "l_SgSpWHxTSs_bfxdGK10",
					"type": "arrow"
				}
			],
			"updated": 1693057632286,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "9e7fa91cd80af4ed830c06e23084bbc097435f83",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 95,
			"versionNonce": 1513576698,
			"isDeleted": false,
			"id": "niQqyyCO4xhP-FGMO4phL",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 3500.2993419534737,
			"y": -1257.1433530728193,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 275.4860214923956,
			"height": 209.4016206482163,
			"seed": 814730823,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1693083082602,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Bg2c6QLx6PErJNOyfDJ4q",
				"focus": 0.5656633654922336,
				"gap": 6.6491112837200035
			},
			"endBinding": {
				"elementId": "yqg_TsAT-oythfyIHrcTA",
				"focus": 0.5918501643983676,
				"gap": 5.516521816649856
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
					275.4860214923956,
					-209.4016206482163
				]
			]
		},
		{
			"type": "image",
			"version": 92,
			"versionNonce": 266716745,
			"isDeleted": false,
			"id": "6FAU9eMOlM-BMqFzN-lQ8",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 5256.594606436426,
			"y": -1761.3034012034707,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1424.9987067103148,
			"height": 903.4421081004601,
			"seed": 2030333735,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "MDHf9tyvFUb3p2ObYGIBV",
					"type": "arrow"
				}
			],
			"updated": 1692840200118,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "1fa9ca8ff23500333157f2641a388be1790e506c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 42,
			"versionNonce": 1496673191,
			"isDeleted": false,
			"id": "MDHf9tyvFUb3p2ObYGIBV",
			"fillStyle": "hachure",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": 5029.883307933205,
			"y": -1377.8055234718859,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 221.36398231717976,
			"height": 38.943718629904424,
			"seed": 1120648711,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1692840200118,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "yqg_TsAT-oythfyIHrcTA",
				"focus": 0.02522295820030342,
				"gap": 1
			},
			"endBinding": {
				"elementId": "6FAU9eMOlM-BMqFzN-lQ8",
				"focus": 0.40455332144363204,
				"gap": 5.347316186041553
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
					221.36398231717976,
					-38.943718629904424
				]
			]
		},
		{
			"id": "FqtQgGruiUxdXAjEryx-0",
			"type": "image",
			"x": 3854.403179338896,
			"y": -453.09657776417316,
			"width": 1436.9730661062035,
			"height": 895.4846760544989,
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
			"seed": 593704486,
			"version": 106,
			"versionNonce": 1290531450,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "UmjhwW2Uze_6hbRMWLB_7",
					"type": "arrow"
				},
				{
					"id": "brNIUK2BPXQhOQv1mIK9J",
					"type": "arrow"
				}
			],
			"updated": 1693057060859,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "76f0217b64107ab0c9d9cedfff155b07dec6604e",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "UmjhwW2Uze_6hbRMWLB_7",
			"type": "arrow",
			"x": 4402.614187415537,
			"y": -650.057519140246,
			"width": 105.01724893682695,
			"height": 187.82015293303334,
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
			"seed": 2027052794,
			"version": 73,
			"versionNonce": 7847930,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693057021915,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					105.01724893682695,
					187.82015293303334
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "FqtQgGruiUxdXAjEryx-0",
				"focus": 0.19632024227373113,
				"gap": 9.140788443039355
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "wJks-zrgvSuQYGfSZmFv4",
			"type": "image",
			"x": 3992.950347495097,
			"y": 572.0108353124303,
			"width": 1183.87935793223,
			"height": 1643.9651747589737,
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
			"seed": 2126734118,
			"version": 165,
			"versionNonce": 114891770,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "brNIUK2BPXQhOQv1mIK9J",
					"type": "arrow"
				}
			],
			"updated": 1693057060859,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "3071e1c5ac8a5a0f53bca501d540d39915e485d6",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "brNIUK2BPXQhOQv1mIK9J",
			"type": "arrow",
			"x": 4562.694837252342,
			"y": 452.0833594150224,
			"width": 6.058646551314268,
			"height": 113.09604450817642,
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
			"seed": 906236390,
			"version": 38,
			"versionNonce": 511415098,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693057060859,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					6.058646551314268,
					113.09604450817642
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "FqtQgGruiUxdXAjEryx-0",
				"focus": 0.04673597936264235,
				"gap": 9.695261124696685
			},
			"endBinding": {
				"elementId": "wJks-zrgvSuQYGfSZmFv4",
				"focus": 0.044441591440929976,
				"gap": 6.831431389231625
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "2Z67HEmmag311IJ0JI-e3",
			"type": "image",
			"x": 5597.482558291373,
			"y": -764.3466836190081,
			"width": 1240.656220801556,
			"height": 1448.3764404182548,
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
			"seed": 385428646,
			"version": 112,
			"versionNonce": 1205333798,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "hVSlDbN0sA9_knaMBAsKi",
					"type": "arrow"
				}
			],
			"updated": 1693057175949,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "b3d1fca1fa506ba34d3e0caa2ab15ca9fdce85ae",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "hVSlDbN0sA9_knaMBAsKi",
			"type": "arrow",
			"x": 5030.690207213378,
			"y": -856.9434832152949,
			"width": 561.440988090968,
			"height": 151.64273191292477,
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
			"seed": 771639142,
			"version": 147,
			"versionNonce": 1784077734,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693057175950,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					561.440988090968,
					151.64273191292477
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "yqg_TsAT-oythfyIHrcTA",
				"focus": 0.3228511659907505,
				"gap": 1.1133053263092734
			},
			"endBinding": {
				"elementId": "2Z67HEmmag311IJ0JI-e3",
				"focus": 0.5563854851181804,
				"gap": 5.351362987027187
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "KqRkwAkMVUCfmnXrYFL45",
			"type": "image",
			"x": 4932.9421558161785,
			"y": -3414.9645435238035,
			"width": 1072.1619857885778,
			"height": 1384.128851218699,
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
			"seed": 1392490342,
			"version": 112,
			"versionNonce": 1955753850,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "l_SgSpWHxTSs_bfxdGK10",
					"type": "arrow"
				},
				{
					"id": "SLzdiEddlWS1kp32eoI-J",
					"type": "arrow"
				},
				{
					"id": "w3rK65PTb_L_nu61x4grS",
					"type": "arrow"
				},
				{
					"id": "YY39JU54WS47GSU5ge4P3",
					"type": "arrow"
				}
			],
			"updated": 1693082763197,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "d465b9bfe794c3a34f70b8a443efc640fe6c897c",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "l_SgSpWHxTSs_bfxdGK10",
			"type": "arrow",
			"x": 4447.272915657017,
			"y": -1935.996120876698,
			"width": 478.30341243599196,
			"height": 886.2069281632123,
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
			"seed": 2094955942,
			"version": 361,
			"versionNonce": 780434214,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693057642823,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-4.141186299979381,
					-788.8898011994527
				],
				[
					474.1622261360126,
					-886.2069281632123
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "yqg_TsAT-oythfyIHrcTA",
				"focus": 0.07209934888031581,
				"gap": 11.251395651555185
			},
			"endBinding": {
				"elementId": "KqRkwAkMVUCfmnXrYFL45",
				"focus": 0.26302227766808717,
				"gap": 11.507014023149168
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "DO60YEWg93sqLjb7W2rRf",
			"type": "image",
			"x": 6807.8995474314615,
			"y": -3374.374421214362,
			"width": 1555.223780992415,
			"height": 1327.324644003188,
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
			"seed": 1355963130,
			"version": 138,
			"versionNonce": 1130974970,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "SLzdiEddlWS1kp32eoI-J",
					"type": "arrow"
				}
			],
			"updated": 1693057689632,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "2f295192e8bc7c88e175e12ea10e2c9a0746d784",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "SLzdiEddlWS1kp32eoI-J",
			"type": "arrow",
			"x": 6008.523332701392,
			"y": -2740.845916345783,
			"width": 778.519680571474,
			"height": 4.718339266624298,
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
			"seed": 1625245222,
			"version": 85,
			"versionNonce": 1574315578,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693057689632,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					778.519680571474,
					4.718339266624298
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "KqRkwAkMVUCfmnXrYFL45",
				"focus": -0.03051217210311386,
				"gap": 3.4191910966355863
			},
			"endBinding": {
				"elementId": "DO60YEWg93sqLjb7W2rRf",
				"focus": 0.030785459110717367,
				"gap": 20.856534158595423
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "xFdFqXPlbUAFKnMmPLD3z",
			"type": "image",
			"x": 6226.3014374073255,
			"y": -4283.834334664405,
			"width": 1561.6915863889424,
			"height": 510.90753416434205,
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
			"seed": 1107908730,
			"version": 127,
			"versionNonce": 1404687674,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "w3rK65PTb_L_nu61x4grS",
					"type": "arrow"
				},
				{
					"id": "iHadgQvECLpDq1GeXvczm",
					"type": "arrow"
				}
			],
			"updated": 1693082516684,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "076e4bb8289208bc83cb55166b187c777db48de2",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "w3rK65PTb_L_nu61x4grS",
			"type": "arrow",
			"x": 5426.477589548197,
			"y": -3438.192650292631,
			"width": 776.5324408574279,
			"height": 613.3290550760457,
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
			"seed": 1457242042,
			"version": 130,
			"versionNonce": 1024573946,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693082483776,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					207.95269630930125,
					-508.0365013017863
				],
				[
					776.5324408574279,
					-613.3290550760457
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "KqRkwAkMVUCfmnXrYFL45",
				"focus": -0.40926225879202366,
				"gap": 23.228106768827388
			},
			"endBinding": {
				"elementId": "xFdFqXPlbUAFKnMmPLD3z",
				"focus": 0.43007963896801527,
				"gap": 23.291407001700463
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "iHadgQvECLpDq1GeXvczm",
			"type": "arrow",
			"x": 7792.440243786485,
			"y": -4028.866859427457,
			"width": 481.71330556712746,
			"height": 398.85759641501227,
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
			"seed": 1073025766,
			"version": 170,
			"versionNonce": 607841018,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693082663957,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					481.71330556712746,
					-398.85759641501227
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "xFdFqXPlbUAFKnMmPLD3z",
				"focus": 0.7203327190440111,
				"gap": 4.447219990216581
			},
			"endBinding": {
				"elementId": "ph-yWOtg5iOYq3Bd-9_T9",
				"focus": 0.5630015404853062,
				"gap": 10.944934409349116
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "ph-yWOtg5iOYq3Bd-9_T9",
			"type": "image",
			"x": 8285.098483762962,
			"y": -4912.995285553579,
			"width": 1529.2033642835613,
			"height": 913.2742314471269,
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
			"seed": 2118525798,
			"version": 275,
			"versionNonce": 1690740922,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "iHadgQvECLpDq1GeXvczm",
					"type": "arrow"
				}
			],
			"updated": 1693082663521,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "ef82398518a63b16ed733a81b14b07fdd808d3d8",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "kwVBUqQiXaiEue1zqcDyw",
			"type": "image",
			"x": 3346.0350849932174,
			"y": -4139.288675231865,
			"width": 1312.750672255824,
			"height": 1081.7614424686492,
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
			"seed": 1478751354,
			"version": 267,
			"versionNonce": 664193894,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "YY39JU54WS47GSU5ge4P3",
					"type": "arrow"
				},
				{
					"id": "AUn7DhJsLj9E19po-RDCV",
					"type": "arrow"
				}
			],
			"updated": 1693082877094,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "f3d7532999819a775eef1d75e2309ba0ef123217",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "YY39JU54WS47GSU5ge4P3",
			"type": "arrow",
			"x": 5304.017262594194,
			"y": -3439.9258968907507,
			"width": 639.652479975086,
			"height": 313.24532647168826,
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
			"seed": 444661734,
			"version": 74,
			"versionNonce": 1716154426,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693082763197,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-639.652479975086,
					-313.24532647168826
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "KqRkwAkMVUCfmnXrYFL45",
				"focus": 0.666485863447478,
				"gap": 24.961353366947264
			},
			"endBinding": {
				"elementId": "kwVBUqQiXaiEue1zqcDyw",
				"focus": -0.5554001171356661,
				"gap": 5.579025370067029
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "56VTkSgv2pGR3w-fFnPOl",
			"type": "image",
			"x": 1557.0570484348386,
			"y": -4003.598415456743,
			"width": 1546.10599402203,
			"height": 789.1841189390137,
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
			"seed": 27910778,
			"version": 83,
			"versionNonce": 1891346918,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "AUn7DhJsLj9E19po-RDCV",
					"type": "arrow"
				}
			],
			"updated": 1693082877094,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "22b903194d3b2c8c5bbf267b525cf564a2e1a4be",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "AUn7DhJsLj9E19po-RDCV",
			"type": "arrow",
			"x": 3343.6134583576827,
			"y": -3594.7844145311656,
			"width": 236.90815050692618,
			"height": 0,
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
			"seed": 1854656890,
			"version": 39,
			"versionNonce": 380923558,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693082877094,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-236.90815050692618,
					0
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "kwVBUqQiXaiEue1zqcDyw",
				"focus": -0.006699331893557334,
				"gap": 2.4216266355347216
			},
			"endBinding": {
				"elementId": "56VTkSgv2pGR3w-fFnPOl",
				"focus": 0.036042137987243233,
				"gap": 3.542265393887874
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "sBrRiVGxA_YzQ3sNiLiYS",
			"type": "image",
			"x": 2035.5509488232983,
			"y": -3089.8663748279855,
			"width": 1104.2757995876361,
			"height": 1419.7831708983895,
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
			"seed": 1263377274,
			"version": 254,
			"versionNonce": 1071595878,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "WiCSPrFcNIMobB_dELGJT",
					"type": "arrow"
				}
			],
			"updated": 1693083195867,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "0e0c537c0852fd6ac855232841bd57977f383766",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "WiCSPrFcNIMobB_dELGJT",
			"type": "arrow",
			"x": 2944.2892275050535,
			"y": -1559.0241049575877,
			"width": 52.45758685116243,
			"height": 98.84633897274148,
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
			"seed": 1350952678,
			"version": 158,
			"versionNonce": 501129190,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693083195868,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-52.45758685116243,
					-98.84633897274148
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "Bg2c6QLx6PErJNOyfDJ4q",
				"focus": 0.34751825045660323,
				"gap": 9.612163619508408
			},
			"endBinding": {
				"elementId": "sBrRiVGxA_YzQ3sNiLiYS",
				"focus": 0.08513166648860354,
				"gap": 12.212759999267064
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "Oo1tegfNIN3HoFLhOitmf",
			"type": "image",
			"x": -72.66372367523218,
			"y": -4235.265194651984,
			"width": 1247.2848806716588,
			"height": 1725.8438366238058,
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
			"seed": 1748737446,
			"version": 171,
			"versionNonce": 353024614,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "GbIuPnTIZ1fT9Ik73iawF",
					"type": "arrow"
				}
			],
			"updated": 1693083206360,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "b646af3c8bc69cf733ceea1c11da0b9ea2a3f599",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "GbIuPnTIZ1fT9Ik73iawF",
			"type": "arrow",
			"x": 2036.3595248477754,
			"y": -2511.6414307499685,
			"width": 850.9597751073607,
			"height": 499.09656690118436,
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
			"seed": 1765210682,
			"version": 49,
			"versionNonce": 935038758,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693083206360,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-850.9597751073607,
					-499.09656690118436
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": {
				"elementId": "Oo1tegfNIN3HoFLhOitmf",
				"focus": -0.008536794285688097,
				"gap": 10.778592743988156
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "UiEQCUAWIAmzRjlf3IhyG",
			"type": "image",
			"x": -2353.3312057963713,
			"y": -2492.411156668468,
			"width": 1312.1641745514014,
			"height": 1088.3659760192952,
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
			"seed": 926931174,
			"version": 101,
			"versionNonce": 1277321914,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "05_N4FDqZktA2evIK1Moh",
					"type": "arrow"
				}
			],
			"updated": 1693083273137,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "963b96549724834edde21621cbea1ac29705ad8b",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "05_N4FDqZktA2evIK1Moh",
			"type": "arrow",
			"x": -628.3194823202352,
			"y": -2053.1090220610668,
			"width": 409.2591196833332,
			"height": 94.8283078816687,
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
			"seed": 1181693222,
			"version": 46,
			"versionNonce": 2132193786,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693083273137,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-409.2591196833332,
					94.8283078816687
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "DeBcjSlh-9xlUSTb6z1Hm",
				"focus": 0.4096095827468445,
				"gap": 3.315628484173203
			},
			"endBinding": {
				"elementId": "UiEQCUAWIAmzRjlf3IhyG",
				"focus": 0.20510987701583888,
				"gap": 3.588429241401286
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "5ue-f5PQBSbQrTbbPSzE4",
			"type": "image",
			"x": -2867.7518134540637,
			"y": -1363.563934285129,
			"width": 974.5684681279291,
			"height": 1390.0423940140463,
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
			"seed": 2061532218,
			"version": 225,
			"versionNonce": 2147222694,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "jjNcynNMP8F51PWePmeYH",
					"type": "arrow"
				}
			],
			"updated": 1693083423376,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "9d673efaddb57ffe4bc8badac6b404baf3425751",
			"scale": [
				1,
				1
			]
		},
		{
			"id": "jjNcynNMP8F51PWePmeYH",
			"type": "arrow",
			"x": -822.8608400994246,
			"y": -960.6757466385675,
			"width": 1054.8665310571475,
			"height": 147.28485872193232,
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
			"seed": 2040884794,
			"version": 164,
			"versionNonce": 1223888122,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1693083430913,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1054.8665310571475,
					-147.28485872193232
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "-SRj_CA8-CLMGr0MMuBfk",
				"focus": 0.4571927695767217,
				"gap": 1
			},
			"endBinding": {
				"elementId": "5ue-f5PQBSbQrTbbPSzE4",
				"focus": -0.6678557189599186,
				"gap": 15.455974169562523
			},
			"startArrowhead": null,
			"endArrowhead": "triangle"
		},
		{
			"id": "6XbykSlwHJm587Lap42Lg",
			"type": "image",
			"x": 8263.883540000608,
			"y": -5228.640860078834,
			"width": 1435.2233781291243,
			"height": 1602.4777560528332,
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
			"seed": 1825695398,
			"version": 199,
			"versionNonce": 307242022,
			"isDeleted": true,
			"boundElements": [
				{
					"id": "iHadgQvECLpDq1GeXvczm",
					"type": "arrow"
				}
			],
			"updated": 1693082640325,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "e3e3d4e38755365c16f6c70f5a17b523e00b8dae",
			"scale": [
				1,
				1
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
		"currentItemFontSize": 28,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "triangle",
		"scrollX": 1511.1814901605035,
		"scrollY": 5488.506267077687,
		"zoom": {
			"value": 0.1
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