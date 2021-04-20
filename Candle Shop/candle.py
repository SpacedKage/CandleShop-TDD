
class Candle:
    """The base class for all candles"""

    def __init__(self, name, unique_id, fragrance, candle_type, burn_time, dimensions, price):
        self.name = name
        self.unique_id = unique_id
        self.fragrance = fragrance
        self.candle_type = candle_type
        self.burn_time = burn_time
        self.dimensions = dimensions
        self.price = price


    def __str__(self):
        return f"Name: {self.name} ID: {self.unique_id} Fragrance: {self.fragrance} Type: {self.candle_type} Burn Time: {self.burn_time} Dimensions: {self.dimensions} Price: {self.price}."

    