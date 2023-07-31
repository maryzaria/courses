def print_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('Файл не найден')


def non_closed_files(files):
    return [file for file in files if not file.closed]


def log_for(logfile, date_str):
    with (open(logfile, 'r', encoding='utf-8') as input_file,
          open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as output_file):
        for line in input_file:
            date, *info = line.split()
            if date == date_str:
                print(' '.join(info), file=output_file)