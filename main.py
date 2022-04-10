import pytz
import requests as r
import random
import time
from datetime import datetime

def CreateOrder(orderType, itemName = None, amount_or_place = None):
    time.sleep(float(random.randint(10, 30))/100)
    orderTime = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"
    orderTypes = {
        "plant":{"type":"item.planted","index":amount_or_place,"item":itemName,"createdAt":orderTime},
        "sell": {"type":"item.sell","item":itemName,"amount":amount_or_place,"createdAt":orderTime},
        "crafted": {"type":"item.crafted","item":itemName,"amount":amount_or_place,"createdAt":orderTime},
        "harvested": {"type":"item.harvested","index":amount_or_place,"createdAt":orderTime},
    }
    return orderTypes[orderType]

def CreateClearOrder(localData, plotNum):
    pass


useragents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 11.4; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Linux i686; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Trident/4.0;)','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)','Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.0)','Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2)','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Edg/91.0.864.37','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Edg/91.0.864.37','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.5.0 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.5.0 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.5.0 Yowser/2.5 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPod; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1','Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/34.0 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (iPad; CPU OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/34.0 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (iPod touch; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/34.0 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/89.0','Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:89.0) Gecko/89.0 Firefox/89.0','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPod touch; CPU iPhone 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1','Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 EdgiOS/46.3.13 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 OPR/63.3.3216.58675','Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 OPR/63.3.3216.58675','Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 OPR/63.3.3216.58675','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 YaBrowser/21.5.3.836 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 YaBrowser/21.5.3.836 Mobile/15E148 Safari/605.1','Mozilla/5.0 (iPod touch; CPU iPhone 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 YaBrowser/21.5.3.836 Mobile/15E148 Safari/605.1','Mozilla/5.0 (Linux; arm_64; Android 11; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 YaBrowser/21.3.4.59 Mobile Safari/537.36']


s = r.Session()
s.headers.update({'user-agent': random.choice(useragents), 'origin':'https://sunflower-land.com', 'referer':'https://sunflower-land.com/'})

while True:
    pkey = input("Private key ---> ")
    address = input("Metamask address ---> ")
    farmId = int(input("Farm id ---> "))
     # 19091


    #creating signature
    from web3.auto import w3
    from eth_account.messages import encode_defunct
    signed_message =  w3.eth.account.sign_message(encode_defunct(text="🌻 Welcome to Sunflower Land! 🌻\n\n" +"Click to sign in and accept the Sunflower Land\n" +"📜 Terms of Service:\n" +"https://docs.sunflower-land.com/support/terms-of-service\n\n" +"This request will not trigger a blockchain\n" +"transaction or cost any gas fees.\n\n" +"Your authentication status will reset after\n" +"each session.\n\n" +"👛 Wallet address:\n" +f"{address[:19]}...{address[-18:]}\n\n" + f"🔑 Nonce: 19091"),
                                                  private_key=pkey)
    sign = str(signed_message).split("signature=HexBytes('")[-1].split("'")[0]

    #getting Bearer token
    _data = {"address": address, "signature":sign}
    queryId = s.post('https://api.sunflower-land.com/login', json=_data, timeout=3)
    if queryId.status_code == 200:
        print("Successful login, Bearer "+queryId.json()['token'])
        break
    else:
        print("Unsuccessful login, message: "+queryId.text + "\n Try to reenter data")


bearerToken = "Bearer "+queryId.json()["token"]
print(bearerToken)
s.headers.update({"authorization":bearerToken})

#checking Bearer token
_data = {"sessionId":"0x0000000000000000000000000000000000000000000000000000000000000000","farmId":farmId}
respond = s.post("https://api.sunflower-land.com/session", json=_data)
if respond.status_code == 200:
    print("Successful session creation")
else:
    print(respond)
    input()

#sending requests for full automation
# while True:
#     _data = {"sessionId": "0x0000000000000000000000000000000000000000000000000000000000000000", "farmId": farmId}
#     sessiondata = s.post("https://api.sunflower-land.com/session", json=_data).json()
#     actions = []
#
#     if float(sessiondata["farm"]["balance"])>=0.4 and int(sessiondata["farm"]["stock"]["Pumpkin Soup"])==1:
#         print("Trying to buy pumpkin soup ingredients")
#         if "Pumpkin Seed" in sessiondata["farm"]["inventory"]:
#             if sessiondata["farm"]["inventory"]["Pumpkin Seed"] < 5:
#                 actions.append(CreateOrder("crafted", "Pumpkin Seed", 5-sessiondata["farm"]["inventory"]["Pumpkin Seed"]))
#         else:
#             actions.append(CreateOrder("crafted", "Pumpkin Seed", 5))
#
#         actions.extend([CreateOrder("plant", "Pumpkin Seed", i) for i in range(5)])


plantName = input("Plant name ---> ")
growTime = int(input("Grow time in sec ---> "))
numberOfPlots = int(input("number of plots ---> "))

actions = []
actions.append(CreateOrder("crafted", plantName+" Seed", numberOfPlots))

_data = {"sessionId": "0x0000000000000000000000000000000000000000000000000000000000000000", "farmId": farmId, "actions":actions}
respond = s.post("https://api.sunflower-land.com/autosave", json=_data)

if respond.status_code == 200:
    print(f"Successfully bought {numberOfPlots} {plantName}s")
else:
    print(respond)
    input()

actions = []
actions.extend([CreateOrder("plant", plantName+" Seed", i) for i in range(numberOfPlots)])

_data = {"sessionId": "0x0000000000000000000000000000000000000000000000000000000000000000", "farmId": farmId, "actions":actions}
respond = s.post("https://api.sunflower-land.com/autosave", json=_data)
if respond.status_code == 200:
    print(f"Successfully planted {numberOfPlots} {plantName}s, waiting for {growTime}")
else:
    print(respond)
    input()

time.sleep(growTime+5)

while True:
    actions = []
    actions.extend([CreateOrder("harvested", amount_or_place=i) for i in range(numberOfPlots)])
    _data = {"sessionId": "0x0000000000000000000000000000000000000000000000000000000000000000", "farmId": farmId, "actions": actions}
    respond = s.post("https://api.sunflower-land.com/autosave", json=_data)
    if respond.status_code == 200:
        print(f"Successfully harvested {numberOfPlots} {plantName}s")
    else:
        print(respond.text)
        input()

    actions = []
    actions.append(CreateOrder("sell", plantName, numberOfPlots))
    actions.append(CreateOrder("crafted", plantName+" Seed", numberOfPlots))
    _data = {"sessionId": "0x0000000000000000000000000000000000000000000000000000000000000000", "farmId": farmId, "actions": actions}
    respond = s.post("https://api.sunflower-land.com/autosave", json=_data)
    if respond.status_code == 200:
        print(f"Successfully sold {numberOfPlots} {plantName}s and bought {numberOfPlots} {plantName} Seeds")
    else:
        print(respond.text)
        input()

    actions = []
    actions.extend([CreateOrder("plant", plantName+" Seed", i) for i in range(numberOfPlots)])
    _data = {"sessionId": "0x0000000000000000000000000000000000000000000000000000000000000000", "farmId": farmId, "actions": actions}
    respond = s.post("https://api.sunflower-land.com/autosave", json=_data)
    if respond.status_code != 200:
        print(respond)
        input()
    else:
        print(f"Successfully planted {numberOfPlots} {plantName}s, waiting for {growTime}\n")

    time.sleep(growTime + 5)
