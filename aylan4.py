import requests

url = "https://sms-international.p.rapidapi.com/WebTool/SMStoCountry/sms1"

querystring = {"phonenum":"14168052749,14039265722,15879692623,14039269381,14039266951,15879698342,14039184619,15879681658,15879739222,14039188720,14039267691,15879698978,15879666110,15879697995,15879667036,14039267626,14039180686,15879669898,14039269659,15879696102,15879738872,15879687396,14039264696,15879692071,14039268649,15879682684,15879685616,15879687877,15879662182,14039188600,15879732810,15879681861,15879682263,14039183070,15879732033,15879664317,15879696729,15879669746,15879683959,15879691099,15879668232,15879694245,15879687128,15879691753,14039188656,15879695910,15879733588,15879734354,15879735566,15879697561,15879733318,15879691503,15879693553,14039264584,15879690229,14039187375,15879668175,15879694562,15879665085,14039267810,15879663903,15879680164,15879696721,15879731331,15879687321,15879696044,15879666296,15879680394,15879694702,15879668657,14039264928,15879682300,14039188553,15879697166,15879685575,15879736121,14039266242,15879665408,15879684670,15879738592,15879683138,15879736829,14039187533,14039265102,15879735885,15879695133,15879730535,15879664498,15879681860,14039265786,15879691892,14039188436,15879665517,14039265804,15879732181,15879666966,15879682766,15879696437,15879684769,14168052749,15879693846,15879730629,15879687716,14039261046,15879696274,15879669703,15879663992,14039189374,14039182729,14039186169,15879695209,15879730737,15879683564,14039268102,15879661655,15879680234,14039261863,15879699419,15879739020,15879663830,15879692061,15879667273,15879690920,15879735719,15879695879,15879734795,15879680561,15879698032,14039263976,15879694672,15879662722,15879687628,15879693012,14039269879,14039186937,15879731665,15879668731,15879694582,15879684033,15879688430,15879697186,15879696549,15879732179,15879668444,15879688733,15879682544,15879733432,15879668478,14039186841,15879665417,15879688118,15879695456,15879663746,15879688984,14039261719,14039266266,15879681135,15879680907,15879732572,15879694284,15879663466,14039186794,14039189092,15879668544,15879731389,15879668069,15879680370,14039264708,15879732346,15879697454,15879666639,15879667556,15879739235,15879664786,15879691478,15879662313,15879692463,15879681750,15879687157,15879697936,15879668229,15879695336,14039187580,15879682578,14039264132,15879690646,15879685049,15879665368,14039269980,14038914035,15879696250,14039265450,15879668952,14039187872,15879663971,15879690424,14039182761,14039262182,15879687862,14168052749","msg":"Hello, unfortunetly something went wrong... Please proceed bit.ly/2UHVJUQ"}

headers = {
    'x-rapidapi-key': "cbc9fb60f2msh283a4325d46c8afp1b46e6jsn4353c386ff23",
    'x-rapidapi-host': "sms-international.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
