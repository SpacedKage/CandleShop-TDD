from candle import Candle


class Catalogue:
    def __init__(self):
        self.list_of_candles = []

    def add_candle(self, candle):
        if candle in self.list_of_candles:
            return
        for c in self.list_of_candles:
            if c.unique_id == candle.unique_id:
                return
        self.list_of_candles.append(candle)
    
    def list_all_candles(self):
        return self.list_of_candles



    def delete_candle(self, unique_id):
        for candle in self.list_of_candles:
            if id == candle.unique_id:
                self.list_of_candles.remove(candle)
                
        
    

        