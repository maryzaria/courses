from collections import defaultdict


def best_sender(messages, senders):
    res = defaultdict(int)
    for i in range(len(senders)):
        res[senders[i]] += len(messages[i].split())
    return max(sorted(res, reverse=True), key=res.get)


messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))

