import requests
from lxml import html

session = requests.session()

login_url = "https://auth.ioeducation.com/users/sign_in"

payload = {
    "user[username]": "<user>",
    "user[password]": "<pass>",
    "authenticity_token": "<token>"
}

result = session.get(login_url)
tree = html.fromstring(result.text)
token = tree.xpath("//input[@name='authenticity_token']/@value")[0]

payload["authenticity_token"] = token
payload["user[username]"] = "207843822"
payload["user[password]"] = "207843822"

result = session.post(
    login_url,
    data = payload,
    headers = dict(referer=login_url)
)

login_button = "https://pupilpath.skedula.com/redirectToAuth.aspx?ReturnUrl=/home/dashboard/"

result = session.get(
    login_button,
    headers = dict(referer=login_button)
)

dashboard = "https://pupilpath.skedula.com/auth/login/loginPupilPath.aspx"

"""
12X271 - East Bronx Academy for the Future
DBN = 12X271
2017-2018: Term 2
Term = 172
"""
tree = html.fromstring(result.text)
print(tree)

DBN = "//select[@id='DBN']/optgroup/option/@value"
DBN = tree.xpath(DBN)
Term = "//select[@id='Term']/option/@value"
Term = tree.xpath(Term)
Student = "//select[@id='Student']/option/@value"
Student = tree.xpath(Student)
print(DBN, Term, Student)

payload = {
    "DBN": "12X271",
    "Term": "172",
    "Student": "207843822"
}

result = session.post(
    dashboard,
    data = payload
)

print(result.text.encode("utf-8"))

f = open("test.html", "w")
f.write(result.text)
f.close()
