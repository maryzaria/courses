import re


class DomainException(Exception):
    pass


class Domain:
    def __init__(self, domain):
        if not re.fullmatch(r"[a-zA-Z]+[.][a-zA-Z]+", domain):
            raise DomainException('Недопустимый домен, url или email')
        self.domain = domain

    @classmethod
    def from_url(cls, url):
        if not re.fullmatch(r'http[s]?://[a-zA-Z]+[.][a-zA-Z]+', url):
            raise DomainException('Недопустимый домен, url или email')
        # self.domain = re.sub(r'http[s]?://', '', url)
        return Domain(re.sub(r'http[s]?://', '', url))

    @classmethod
    def from_email(cls, email):
        if not re.fullmatch(r'[a-zA-Z]+@[a-zA-Z]+[.][a-zA-Z]+', email):
            raise DomainException('Недопустимый домен, url или email')
        # self.domain = re.sub(r'http[s]?://', '', url)
        return Domain(re.sub(r'[a-zA-Z]+@', '', email))

    def __repr__(self):
        return str(self.domain)


# TEST_6:
urls = ['http://npo.com', 'http://zao.biz', 'http://ooo.edu', 'https://ooo.ru', 'http://prioskole.net',
        'http://ooo.com', 'http://bolshakova.biz', 'http://rao.biz', 'https://ip.biz', 'http://alekseev.ru',
        'http://ooo.ru', 'http://zao.biz', 'http://pk.biz', 'https://rao.biz', 'http://npo.org',
        'http://rao.com', 'http://rao.org', 'http://galkina.net', 'https://moskovskaja.biz', 'https://ao.ru']

for url in urls:
    domain = Domain.from_url(url)
    print(domain)

# TEST_7:
domains = ['nikitin..biz', '.org', 'katren.', 'kubanskaja.edu.', '.', 'i.p.com', 'ooo.info+']

for d in domains:
    try:
        domain = Domain.from_email(d)
    except DomainException as e:
        print(e)

# TEST_8:
emails = ['anan,i86@example.org', 'konovalovkondrat@@example.net', 'efimmaksimov@example..net', 'marfa_.04@example.com',
          'vlasovstanimir@example.org.', '.anikita_04@example.net', '@loginovroman@example.org',
          'novikovasinklitikija@example.net@', 'elizar_1978@example@.com', 'kasjan_1972@example.org', '@a.ru', 'abc@.ru']

for email in emails:
    try:
        domain = Domain.from_email(email)
    except DomainException as e:
        print(e)

# TEST_9:
urls = ['http://evseeva.info/', 'https:://ip.com/', 'https://www.ao.ru', 'https:///ip.ru', 'https://zao.',
        'https://.edu', 'http://oao.edu/', 'http://www.ip.com/', 'http://.org', 'http://abc.']

for url in urls:
    try:
        domain = Domain.from_url(url)
    except DomainException as e:
        print(e)