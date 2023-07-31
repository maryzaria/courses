class HtmlTag:
    tags = []

    def __init__(self, tag, inline=False):
        self.open_tag = f'<{tag}>'
        self.close_tag = f'</{tag}>'
        self.inline = inline
        self.tags.append(tag)

    def __enter__(self):
        self.level = len(self.tags) - 1
        if self.inline:
            print(f'{"  " * self.level}{self.open_tag}', end='')
        else:
            print(f'{"  " * self.level}{self.open_tag}')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tags.pop()
        if self.inline:
            print(self.close_tag)
        else:
            print(f'{"  " * self.level}{self.close_tag}')

    def print(self, text):
        if self.inline:
            print(f"{text}", end='')
        else:
            print(f'  {"  " * self.level}{text}')


with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Здесь есть что-то интересное')
    with HtmlTag('a', True) as section:
        section.print('https://stepik.org/media/attachments/course/98974/watch_me.mp4')
