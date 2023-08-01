class Tank:
    tanks = []

    def __init__(self, name, volume, capacity):
        self.name = name
        self.capacity = capacity
        self.water_volume = 0
        Tank.tanks.append(self)

    def pour_water(self, volume):
        if self.water_volume + volume > self.capacity:
            print(f"you are not allowed to add more water than {self.capacity - self.water_volume}")
        else:
            self.water_volume += volume

    def pour_out_water(self, volume):
        if volume <= self.water_volume:
            self.water_volume -= volume
        else:
            print(f"Cannot pour out more than {self.water_volume} water.")

    def transfer_water(self, from_tank, volume):
        if self.water_volume + volume <= self.capacity:
            from_tank.water_volume -= volume
            self.water_volume += volume
        else:
            print("Transfer is not possible.")

    @classmethod
    def find_most_water(cls):
        return max(cls.tanks, key=lambda tank: tank.water_volume, default=None)

    @classmethod
    def find_most_filled(cls):
        def fill_ratio(tank):
            return tank.water_volume / tank.capacity

        return max(cls.tanks, key=fill_ratio, default=None)

    @classmethod
    def find_empty_tanks(cls):
        return list(filter(lambda tank: tank.water_volume == 0, cls.tanks))


if __name__ == '__main__':
    tank = Tank('tank', 100, 200)
