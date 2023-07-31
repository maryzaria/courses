class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self._file = open(self.filename, 'r',encoding='utf-8')
        return (line.rstrip() for line in self._file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file:
            self._file.close()


from zipfile import ZipFile

zip_file = ZipFile('test.zip', 'w')

with Closer(zip_file) as zf:
    print(zf)