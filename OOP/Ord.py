class Ord:
    def __getattr__(self, attr):
        return ord(attr)


obj = Ord()

print(obj.в)
print(obj.г)