

# TEST_3:
with open('file.txt', 'w') as file:
    print('Есть всего два типа языков программирования: те, на которые люди всё время ругаются, и те, которые никто не использует.', file=file)

file = open('file.txt')

with Reloopable(file) as reloopable:
    for _ in range(20):
        for line in reloopable:
            print(line.strip())