def skobki(st: list[str]) -> bool:
    if st[0] == ')':
        return False
    if st.count('(') != st.count(')'):
        return False
    return True


string = list(input())
print(skobki(string))
