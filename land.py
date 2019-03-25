class Land:

    price_per_meter_squared = 50
    width = 0
    length = 0

    def __init__(self):
        self.width = 0
        self.length = 0

    def get_land_price(self):
        return Land.price_per_meter_squared * self.width * self.length

    @staticmethod
    def set_price_land(get_land_price):
        Land.price_per_meter_squared = get_land_price


