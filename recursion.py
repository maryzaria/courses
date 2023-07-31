import os


def obhod_files(path, lvl=1):
    """path - the path to the folder"""
    print(f'Level: {lvl}, Content: {", ".join(os.listdir(path))}')
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            print('Спускаемся в', path+'\\'+i)
            obhod_files(f'{path}\\{i}', lvl+1)
            print('Возвращаемся в', path)


p = 'C:\\Users\\Maria\\PycharmProjects\\pythonProject\\desktop'
# obhod_files(p)


def sum_rec(arr):
    """Summa of elements in array"""
    if len(arr) == 0:
        return 0
    return arr[0] + sum_rec(arr[1:])


def rec_sum_arr(arr):
    """Count of elements in array"""
    if len(arr) == 0:
        return 0
    return 1 + sum_rec(arr[1:])


def rec_max_num(lst: list[int]) -> int:
    """Largest number in the list"""
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    sub_max = rec_max_num(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


def rec_binary_search(arr: list[int], goal: int, start, end) -> int:
    """Base and recursive case for binary search"""
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        guess = arr[mid]
        if guess == goal:
            return mid
        if guess > goal:
            return rec_binary_search(arr, goal, start, mid - 1)
        else:
            return rec_binary_search(arr, goal, mid + 1, end)


def print_num():
    numbers = [1, 2, 3, 4, 5]

    def rec(n):
        if n < len(numbers):
            print(f'Элемент {n}: {numbers[n]}')
            rec(n + 1)
    rec(0)


def num(n):
    if n != 0:
        num(int(input()))
    print(n)


def triangle(h):
    if h > 0:
        triangle(h-1)
        print('*'*h)


def clock():
    def print_clock(n=1, x=16):
        if n < 4:
            print(f'{str(n) * x}'.center(16))
            print_clock(n + 1, x - 4)
        print(f'{str(n) * x}'.center(16))
    print_clock()


def sum_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_digits(number // 10)
#print(sum_digits(int(input())))


funk = lambda x: 1 if x < 10 else funk(x//10) +1


def number_of_frogs(year):
    frogs = {1: 77}
    res = frogs.get(year)
    if res is None:
        res = 3*(number_of_frogs(year-1)-30)
        frogs[year] = res
    return res


def range_sum(numbers, start, end):
    if start > end:
        return 0
    return numbers[start] + range_sum(numbers, start+1, end)


#print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 0))


def get_pow(a, n):
    if n == 0:
        return 1
    return a * get_pow(a, n-1)


get_pow1 = lambda a, n: 1 if n == 0 else a*get_pow1(a, n-1)
#print(get_pow1(2, 10))


def get_fast_pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return get_fast_pow(a**2, n//2)
    else:
        return a * get_fast_pow(a, n-1)


def recursive_sum(a, b):
    if b == 0:
        return a
    return recursive_sum(a + 1, b - 1)


def is_power(number):
    if number == 1:
        return True
    if number % 2 != 0 or number == 0:
        return False
    return is_power(number // 2)


def tribonacci(n):
    nums = {1: 1, 2: 1, 3: 1}
    def summa_tr(n):
        res = nums.get(n)
        if res is None:
            res = summa_tr(n-1) + summa_tr(n-2) + summa_tr(n-3)
            nums[n] = res
        return res
    return summa_tr(n)


def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


to_binary1 = lambda n: str(n % 2) if n <= 1 else to_binary(n//2) + str(n % 2)


def to_binary(n):
    if n <= 1:
        return str(n % 2)
    return to_binary(n//2) + str(n % 2)


def recursive_sum(nested_lists):
    s = 0
    if type(nested_lists) == int:
        s += nested_lists
    if type(nested_lists) == list:
        for num in nested_lists:
            s += recursive_sum(num)
    return s


def linear(nested_lists):
    res = []
    for num in nested_lists:
        if type(num) == list:
            res.extend(linear(num))
        else:
            res.append(num)
    return res


def get_value(nested_dicts, key):
    value = nested_dicts.get(key)
    if value is None:
        for k, v in nested_dicts.items():
            if isinstance(v, dict):
                value = get_value(v, key)
                if value is not None:
                    return value
    return value


def get_all_values(nested_dicts, key):
    res = set()
    for k, v in nested_dicts.items():
        if isinstance(v, dict):
            res.update(get_all_values(v, key))
        if key in nested_dicts:
            res.add(nested_dicts[key])
    return res


def dict_travel(nested_dicts):
    # for key, value in sorted(dicts.items()):
    #         if isinstance(value, dict):
    #             dict_travel({f'{key}.{k}': v for k, v in value.items()})
    #         else:
    #             print(f'{key}: {value}')'
    path = []

    def rec(dicts, path):
        for key, value in sorted(dicts.items()):
            if not isinstance(value, dict):
                print(f'{".".join(path +[key])}: {value}')
            elif isinstance(value, dict):
                rec(value, path +[key])
    rec(nested_dicts, path)


data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}
dict_travel(data)

