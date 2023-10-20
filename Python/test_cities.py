"""Test cases to check is the functions are working as expected. 
Use cmd python3 -m pytest in terminal to run this script assuming this is the only test file in the folder where the program resides"""

from city_functions import city_country


def test_city_country():
    formatted_name = city_country("boston", "united States")
    assert formatted_name == "Boston, United States"


def test_city_country_population():
    formatted_name = city_country("santiago", "chile", 5000000)
    assert formatted_name == "Santiago, Chile - population 5000000"
