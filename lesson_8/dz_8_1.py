import re

email = '221fasd@gmail.com'
def email_parse(email):
    data = {}
    RE_USERNAME = re.compile(r"^[a-zA-Z\d_.-]{0,}")
    RE_DOMAIN = re.compile(r"@[a-z\d]{0,}")
    username = RE_USERNAME.findall(email)[0]
    domain = RE_DOMAIN.findall(email)[0][1:]
    if not username or not domain:
        raise ValueError('Неверный адрес электронной почты')
    else:
        data['user'] = username
        data['domain'] = domain
    return data

print(email_parse(email))