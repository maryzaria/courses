class DevelopmentTeam:
    def __init__(self):
        self._juniors = ()
        self._seniors = ()

    def add_junior(self, *args):
        self._juniors += args

    def add_senior(self, *args):
        self._seniors += args

    def __iter__(self):
        for jun in self._juniors:
            yield jun, 'junior'

        for senior in self._seniors:
            yield senior, 'senior'


# TEST_5:
smart_monkey = DevelopmentTeam()

smart_monkey.add_senior('Gvido', 'Alan')
smart_monkey.add_junior('Denis')

print(list(smart_monkey))
