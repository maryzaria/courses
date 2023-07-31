class Gun:
    def __init__(self):
        self.count = 0

    def shoot(self):
        if not self.count % 2:
            print('pif')
        else:
            print('paf')
        self.count += 1

    def shots_count(self):
        return self.count

    def shots_reset(self):
        self.count = 0


gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())