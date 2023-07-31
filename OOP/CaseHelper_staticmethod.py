import re


class CaseHelper:
    @staticmethod
    def is_snake(string: str) -> bool:
        return bool(re.fullmatch(r'([a-z]+_)*[a-z]+', string))

    @staticmethod
    def is_upper_camel(string: str) -> bool:
        return bool(re.fullmatch(r'([A-Z][a-z]+)+', string))

    @staticmethod
    def to_snake(string: str) -> str:
        s = [let if let.isalpha() and let.islower() else '_' + let.lower() for let in string]
        return ''.join(s).strip('_')

    @staticmethod
    def to_upper_camel(string: str) -> str:
        return ''.join(list(map(str.capitalize, string.split('_'))))



# TEST_8:
cases = ['assert_equal', 'tear_down', 'assert_raises_regex', 'assert_almost_equal', 'assert_not_almost_equal', 'beegeek']

for case in cases:
    print(CaseHelper.to_upper_camel(case))