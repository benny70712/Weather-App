import pytest
from project import check_command_line_arg , kelvin_to_celsius, kelvin_to_fahrenheit, get_weather_data

def test_check_command_line_args():
    with pytest.raises(SystemExit):
        check_command_line_arg()


def test_kelvin_to_celsius():
    assert kelvin_to_celsius(300) == 27
    assert kelvin_to_celsius(0) == -273
    assert kelvin_to_celsius(50) == -223


def test_kelvin_to_fahrenheit():
    assert kelvin_to_fahrenheit(50) == -370
    assert kelvin_to_fahrenheit(0) == -460
    assert kelvin_to_fahrenheit(700) == 800


def test_get_weather_data():
    assert get_weather_data("a") == None
    assert get_weather_data("1") == None
    assert get_weather_data("aba") == None




