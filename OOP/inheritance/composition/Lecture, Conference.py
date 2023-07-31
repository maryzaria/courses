from datetime import time, datetime, timedelta


class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, '%H:%M')
        self.duration = datetime.strptime(duration, '%H:%M')
        self.time = timedelta(hours=self.duration.hour, minutes=self.duration.minute)
        self.end_time = self.start_time + self.time


class Conference:
    def __init__(self):
        self.presentations = []

    def add(self, lecture):
        for pres in self.presentations:
            if pres.start_time <= lecture.start_time < pres.end_time or \
                    lecture.start_time <= pres.start_time < lecture.end_time:
                raise ValueError('Провести выступление в это время невозможно')
        self.presentations.append(lecture)
        self.presentations.sort(key=lambda x: x.start_time)

    def total(self):
        s = timedelta(0, 0, 0)
        for pres in self.presentations:
            s += pres.time
        return datetime.strptime(str(s), '%H:%M:%S').strftime('%H:%M')

    def longest_lecture(self):
        return max(self.presentations, key=lambda x: x.time).duration.strftime('%H:%M')

    def longest_break(self):
        max_break = time(0, 0, 0)
        for i in range(len(self.presentations) - 1):
            pres1 = self.presentations[i]
            pres2 = self.presentations[i + 1]
            break_time = time(hour=pres2.start_time.hour - pres1.end_time.hour,
                              minute=abs(pres2.start_time.minute - pres1.end_time.minute))
            if break_time > max_break:
                max_break = break_time
        return datetime.strptime(str(max_break), '%H:%M:%S').strftime('%H:%M')


# TEST_12:
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))
conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:30'))
conference.add(Lecture('Создание, инициализация и очищение объектов', '11:00', '00:30'))
conference.add(Lecture('Унарные операторы и функции', '10:45', '00:15'))
conference.add(Lecture('Арифметические операции', '10:00', '00:30'))
conference.add(Lecture('Вызываемые объекты', '08:00', '01:00'))

print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())