from string import ascii_uppercase as up, ascii_lowercase as low


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, word):
        res = [up[(self.shift + up.index(w)) % 26] if w in up else w for w in word]
        res = [low[(self.shift + low.index(w)) % 26] if w in low else w for w in res]
        return ''.join(res)

    def decode(self, word):
        res = [up[(up.index(w) - self.shift) % 26] if w in up else w for w in word]
        res = [low[(low.index(w) - self.shift) % 26] if w in low else w for w in res]
        return ''.join(res)


# TEST_4:
cipher = CaesarCipher(15)

words = ['EvEr', 'WoUlD', 'CeRtAiN', 'WhIcH', 'WiTh', 'ThErE', 'EnViRoNmEnTaL', 'StRuCtUrE', 'NeWs', 'ThRoW', 'NoTe',
         'If', 'WiN', 'ShOuLdEr', 'NeEd', 'WhErE', 'MeThOd', 'FiRsT', 'CiViL', 'BaSe']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

# TEST_5:
cipher = CaesarCipher(15)

words = ['civil😀', 'so😁', 'region☺', 'beat☺', 'artist😍', 'choice🙃', 'include🤭', 'degree😝', 'push🤪', 'side😏', 'size🤥',
         'policy🤨', '🤨🤥😏🤪😝🤭🙃😍☺😁😀']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

# TEST_6:
cipher = CaesarCipher(1)
print(cipher.encode('ZzzZzz'))
print(cipher.decode('AaaAaa'))


