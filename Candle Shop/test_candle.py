from candle import Candle

def test_new_candle_constructed_correctly():
    cupcake = Candle ("Cupcake", 101, "Cake", "Tealight", "4 Hours", "38mm x 16mm", "£1.75")
    assert cupcake.unique_id == 101
    assert cupcake.fragrance == "Cake"
    assert cupcake.candle_type == "Tealight"
    assert cupcake.burn_time == "4 Hours"

def test_str_returns_correct_string():
     cupcake = Candle ("Cupcake", 101, "Cake", "Tealight", "4 Hours", "38mm x 16mm", "£1.75")
     correct_str = ("Name: Cupcake ID: 101 Fragrance: Cake Type: Tealight Burn Time: 4 Hours Dimensions: 38mm x 16mm Price: £1.75.")
     assert str(cupcake) == correct_str
