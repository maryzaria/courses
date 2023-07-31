def annual_return(start: int, percent: int, years: int):
    for _ in range(years):
        start += start * percent / 100
        yield start


# TEST_8:
for value in annual_return(0, 0, 0):
    print(round(value))