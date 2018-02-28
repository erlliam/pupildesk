import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Cookie": "ASP.NET_SessionId=mh1hut45uckyvyevizarbvz2",
    "DNT": "1",
    "Host": "pupilpath.skedula.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"
}

urls = [
    "https://pupilpath.skedula.com/",
    "https://pupilpath.skedula.com/redirectToAuth.aspx",
    "https://auth.ioeducation.com/users/sign_in"
]

session = requests.Session()

current = session.get(urls[0])
current = session.get(
    urls[1],
    headers=dict(headers, Referer="https://pupilpath.skedula.com/")
)

payload = {
    "user[username]": "207843822",
    "user[password]": "207843822"
}

current = session.post(
    urls[2],
    data=payload,
    headers=dict(headers, Referer="https://auth.ioeducation.com/users/sign_in")
)

f = open("test.html", "wb")
f.write(current.text.encode("utf-8"))
f.close()

