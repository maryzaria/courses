from datetime import date


class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')

    def low_temperature(self):
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, data: date):
        print(data.strftime('%d.%m.%Y'))
        super().rain()

    def snow(self, data):
        print(data.strftime('%d.%m.%Y'))
        super().snow()

    def low_temperature(self, data):
        print(data.strftime('%d.%m.%Y'))
        super().low_temperature()


from datetime import date

weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)

weatherwarning.rain(dt)
weatherwarning.snow(dt)
weatherwarning.low_temperature(dt)