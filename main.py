from datetime import datetime


class OperationTracker:
    operation_log = []

    @staticmethod
    def log_operation(operation_name, tank_name, volume, success):
        operation_time = datetime.now()
        OperationTracker.operation_log.append((operation_time, operation_name, tank_name, volume, success))


class Tank:
    tanks = []

    def __init__(self, name, volume, capacity):
        self.name = name
        self.capacity = capacity
        self.water_volume = 0
        self.operations_history = []
        Tank.tanks.append(self)

    def pour_water(self, volume):
        success = self.water_volume + volume < self.capacity
        if success:
            self.water_volume += volume
        else:
            print(f"you are not allowed to add more water than {self.capacity - self.water_volume}")
        OperationTracker.log_operation('pour_water', self.name, volume, success)

    def pour_out_water(self, volume):
        success = volume <= self.water_volume
        if success:
            self.water_volume -= volume
        else:
            print(f"Cannot pour out more than {self.water_volume} water.")
        OperationTracker.log_operation('pour_out_water', self.name, volume, success)

    def transfer_water(self, from_tank, volume):
        success = self.water_volume + volume <= self.capacity and from_tank.water_volume >= volume
        if success:
            from_tank.water_volume -= volume
            self.water_volume += volume
        else:
            print("Transfer is not possible.")
        OperationTracker.log_operation('transfer_water', self.name, volume, success)

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
    tank.pour_water(100)
    tank.pour_out_water(50)
    tank2 = Tank('tank2', 100, 500)
    tank2.pour_water(400)
    tank2.pour_out_water(50)
    tank.transfer_water(tank2, 500)
    print(Tank.find_most_water().name)
    print(Tank.find_most_filled().name)
    print([tank.name for tank in Tank.find_empty_tanks()])
