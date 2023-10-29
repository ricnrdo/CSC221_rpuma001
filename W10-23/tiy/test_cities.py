from city_functions import city_country

def test_city_country():
    formatted_place = city_country("santiago", "chile")
    assert formatted_place == "Santiago, Chile"

def test_city_country_population():
    formatted_place = city_country("santiago", "chile", "500000")
    assert formatted_place == "Santiago, Chile - population 500000"