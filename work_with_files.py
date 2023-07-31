import json
from datetime import time, datetime


def work_time(string):
    st, end = string.split('-')
    return int(st.split(':')[0])<=10 and int(end.split(':')[0])>=12


with open('pools.json', encoding='utf-8') as file1:
    data = json.load(file1)
    filt = list(filter(lambda x: work_time(x['WorkingHoursSummer']['Понедельник']), data))
    m = max(filt, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']))
    print(f"{m['DimensionsSummer']['Length']}x{m['DimensionsSummer']['Width']}")
    print(m['Address'])

#
# with open('data.csv', 'w', encoding='utf-8', newline='') as new:
#     head = ['name', 'phone']
#     writer = csv.DictWriter(new, fieldnames=head)
#     writer.writeheader()
#     writer.writerows(sorted(filtred, key=lambda x: x['name']))
#
#
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(clubs, file, indent='   ')
#
#
# with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as new:
#     writer = csv.DictWriter(new, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(data)
















