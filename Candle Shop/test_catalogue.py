from catalogue import Catalogue
from candle import Candle


def test_new_catalogue_constructed_correctly():
    cat = Catalogue()
    assert cat.list_of_candles == []

def test_add_candle_one_candle():
    cat = Catalogue()
    cupcake = Candle ("Cupcake", 101, "Cake", "Tealight", "4 Hours", "38mm x 16mm", "£1.75")
    cat.add_candle(cupcake)
    assert cat.list_of_candles == [cupcake]

def test_add_candle_candle_already_present():
     cat = Catalogue()
     cupcake = Candle ("Cupcake", 101, "Cake", "Tealight", "4 Hours", "38mm x 16mm", "£1.75")
     cat.add_candle(cupcake)
     cupcake2 = cupcake
     cat.add_candle(cupcake2)
     assert cat.list_of_candles == [cupcake]

def test_add_candle_candle_id_already_present():
     cat = Catalogue()
     cupcake = Candle ("Cupcake", 101, "Cake", "Tealight", "4 Hours", "38mm x 16mm", "£1.75")
     rainbows = Candle ("Rainbows", 101, "Rainbow Drops", "Jar", "20 Hours", "180mm x 130mm", "£9.99" )
     cat.add_candle(cupcake)
     cat.add_candle(rainbows)
     assert cat.list_of_candles == [cupcake]

def test_list_all_candles_for_new_catalogue():
     cat = Catalogue()
     assert cat.list_all_candles() == []

def test_list_all_candles_after_one_added():
    cat = Catalogue()
    cupcake = Candle ("Cupcake", 101, "Cake", "Tealight", "4 Hours", "38mm x 16mm", "£1.75")
    cat.add_candle(cupcake)
    assert cat.list_all_candles() == [cupcake]

def test_delete_candle_removes_the_candle_from_list():
    cat = Catalogue()
    cupcake = Candle("Cupcake", 1001, "Cake", "Tealight", "4 Hours", "38mm x 16mm", "£1.75")
    cupcake2 = cupcake
    cat.add_candle(cupcake)
    cat.add_candle(cupcake2) 
    cat.delete_candle(1001)
    assert cat.list_of_candles == [cupcake2]





