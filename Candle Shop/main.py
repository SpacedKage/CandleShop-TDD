from candle import Candle

cupcake = Candle ("Cupcake", 101, "Cake", "Tealight", "4 Hours", "38mm x 16mm", "£1.75")
Stinky = Candle ("Stinky", 102, "Marmite", "Votive", "8 Hours", "90mm x 100mm", "£3.50")
Warmers = Candle ("Warmers", 103, "Cinnamon", "Pillar", "16 Hours", "100mm x 120mm", "£7.99")
Dreams = Candle ("Dreams", 104, "Cut grass", "Tealight", "4 Hours", "38mm x 16mm", "£1.75")
Rainbows = Candle ("Rainbows", 105, "Rainbow Drops", "Jar", "20 Hours", "180mm x 130mm", "£9.99" )
misty = Candle ("Misty", 106, "Fresh Breeze", "Tealight", "4 Hours", "38mm x 16mm", "£1.75")
Lucky = Candle ("Lucky", 107, "Unscented", "Tealight", "4 Hours", "38mm x 16mm", "1.75")
Brite = Candle ("Brite", 108, "Lemon", "Pillar", "16 Hours", "100mm x 120mm", "£7.99")
Classy = Candle ("Classy", 109, "Lavender", "Jar", "20 Hours", "180mm x 130mm", "£9.99")

list_of_all_candles = [cupcake, Stinky, Warmers, Dreams, Rainbows ,misty ,Lucky ,Brite, Classy]
list_of_all_unique_id = [101, 102, 103, 104, 105, 106, 107, 108, 109]
list_of_all_fragrance = ["Cake, Marmite, Cinnamon, Cut-grass, Rainbow-Drops, Fresh-Breeze, Lemon, Lavender"]
list_of_all_candle_types_and_prices = ["Tealight £1.75, Votive £3.50, Pillar £7.99, Jar £9.99"]
list_of_all_burn_times = ["4 Hours, 8 Hours, 16 Hours, 20 Hours"]
list_of_all_dimensions = ["38mm x 16mm, 100mm x 120mm, 180mm x 130mm, 90mm x 100mm"]


print(f"Candles Available in store: {cupcake.name} {Stinky.name} {Warmers.name} {Dreams.name} {Rainbows.name} {misty.name} {Lucky.name} {Brite.name} {Classy.name}.")
print(f"Candle Fragrances: {cupcake.fragrance} {Stinky.fragrance} {Warmers.fragrance} {Dreams.fragrance} {Rainbows.fragrance} {misty.fragrance} {Lucky.fragrance} {Brite.fragrance} {Classy.fragrance}")
print(f"Candle Type & Price: {list_of_all_candle_types_and_prices}.")
print(f"Burn Time: {list_of_all_burn_times}.")
print(f"Candle ID: {list_of_all_unique_id}.")
print(f"Dimensions: {list_of_all_dimensions}.")





user_input_candle = [] 
max_length_list = 12
while len(user_input_candle) < max_length_list:
    item = input("User may add a Candle: ")
    user_input_candle.append(item)
    print (user_input_candle)
print(user_input_candle)




