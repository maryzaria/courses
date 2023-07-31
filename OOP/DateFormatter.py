from datetime import date


class DateFormatter:
    __codes = {
        "ru": r"%d.%m.%Y",
        "us": r"%m-%d-%Y",
        "ca": r"%Y-%m-%d",
        "br": r"%d/%m/%Y",
        "fr": r"%d.%m.%Y",
        "pt": r"%d-%m-%Y"}

    def __init__(self, country_code):
        self.code = country_code

    def __call__(self, d: date):
        return d.strftime(self.__codes[self.code])