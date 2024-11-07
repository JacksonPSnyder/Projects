"""Unit test for meteoric.py"""
import meteoric
import pytest

def test_load_data():
    """Test case for load_data()"""
    result = meteoric.load_data()
    assert result[0] == ['Aachen', '1', 'Valid', 'L5', '21', 'Fell', '1880', '50.775', '6.08333', '', '', '']
    assert result[-1] == ['Zulu Queen', '30414', 'Valid', 'L3.7', '200', 'Found', '1976', '33.98333', '-115.68333', '', '', '']

def test_get_geopoint_valid_data():
    """Test case for a list containing only valid data for get_geopoint()
       min distance was calculated outside using https://www.vcalc.com/wiki/vcalc/haversine-distance
       looked through pytest docs to find .approx method"""
    meteors = [["meteor1", 1, "valid", "F1", 21, "Fell", 2000, 10, 20],
               ["meteor2", 2, "Valid", "G7", 1400, "Fell", 2001, 30, 40],
               ["meteor3", 3, "Valid", "CS3", 2500.5, "Found", 2002, 50, 60]]
    geopoint = ('12,18')

    closest_meteors, min_distance = meteoric.get_geopoint(meteors, geopoint)
    assert closest_meteors == [["meteor1", 1, "valid", "F1", 21, "Fell", 2000, 10, 20]]
    assert pytest.approx(min_distance, 0.1) == 311.6

def test_get_geopoint_invalid_data():
    """Test case for a list that contains invalid data for get_geopoint()"""
    meteors = [["meteor1", 1, "Valid", "B4", 55, "Fell", 2000, 'strings not allowed', ''],
               ["meteor2", 2, "Valid", "G7", 1400, "Fell", 2001, 30, 40],
               ["meteor3", 3, "", "", "", "", 2002]]
    geopoint = ("12,18")

    closest_meteors, min_distance = meteoric.get_geopoint(meteors, geopoint)
    assert closest_meteors == [["meteor2", 2, "Valid", "G7", 1400, "Fell", 2001, 30, 40]]
    assert pytest.approx(min_distance, 0.1) == 3025.1

def test_get_geopoint_same_distance():
    """Test case for when there are multiple meteors with the same closest distance."""
    meteors = [["meteor1", 1, "valid", "F1", 21, "Fell", 2000, 10, 20],
                ["meteor2", 2, "valid", "G9", 421, "Fell", 2000, 10, 20]]
    geopoint = ("12,18")

    closest_meteors, min_distance = meteoric.get_geopoint(meteors, geopoint)
    assert closest_meteors == [["meteor1", 1, "valid", "F1", 21, "Fell", 2000, 10, 20],
                               ["meteor2", 2, "valid", "G9", 421, "Fell", 2000, 10, 20]]
    assert pytest.approx(min_distance, 0.1) == 311.6

def test_get_year():
    """Test cases for get_year()"""
    result = [["meteor1", 1, "valid", "F1", 21, "Fell", 2002, 10, 20],
               ["meteor2", 2, "Valid", "G7", 1400, "Fell", 2001, 30, 40],
               ["meteor3", 3, "Valid", "CS3", 2500.5, "Found", 2002, 50, 60]]

    assert meteoric.get_year(result, "101") == []
    assert meteoric.get_year(result, "2001") == [["meteor2", 2, "Valid", "G7", 1400, "Fell", 2001, 30, 40]]
    assert meteoric.get_year(result, "2002") == [["meteor1", 1, "valid", "F1", 21, "Fell", 2002, 10, 20], ["meteor3", 3, "Valid", "CS3", 2500.5, "Found", 2002, 50, 60]]

def test_is_valid_geopoint_arg():
    """Test cases for the geopoint command within is_valid_arg()"""
    with pytest.raises(ValueError) as err:
        assert meteoric.is_valid_arg("geopoint", "b")
    assert str(err.value) == "Error: Coordinates must be numeric."

    with pytest.raises(ValueError) as err:
        assert meteoric.is_valid_arg("geopoint", "12")
    assert str(err.value )== "Error: Only 1 latitude and 1 longitude can be excepted."

    with pytest.raises(ValueError) as err:
        assert meteoric.is_valid_arg("geopoint", "-91,-179")
    assert str(err.value)== "Error: The latitude must be within the range [-90, 90]."

    with pytest.raises(ValueError) as err:
        assert meteoric.is_valid_arg("geopoint", "-89,-181")
    assert str(err.value)== "Error: The longitude must be within the range [-180, 180]"

    assert meteoric.is_valid_arg("geopoint", "-70,110") == True
    assert meteoric.is_valid_arg("geopoint", "90,180") == True
    assert meteoric.is_valid_arg("geopoint", "-90,-180") == True

def test_is_valid_year_arg():
    """Test cases for the year command within is_valid_arg()"""
    with pytest.raises(ValueError) as err:
        assert meteoric.is_valid_arg("year", "abc")
    assert str(err.value) == "Error: The year must be an integer."

    with pytest.raises(ValueError) as err:
        assert meteoric.is_valid_arg("year", "-1")
    assert str(err.value) == "Error: The year must be positive."

    with pytest.raises(ValueError) as err:
        meteoric.is_valid_arg("year", "1999.5")
    assert str(err.value) == "Error: The year must be an integer."

    assert meteoric.is_valid_arg("year", "1999") == True
    assert meteoric.is_valid_arg("year", "0") == True

def test_is_valid_arg_invalid_data():
    """Test case for when there is no valid data withing is_valid_arg()."""
    assert meteoric.is_valid_arg("hello", "World") == False

def test_is_valid_command():
    """Test Cases for is_valid_command()"""
    assert meteoric.is_valid_command('year') == True
    assert meteoric.is_valid_command('YEAR') == True
    assert meteoric.is_valid_command("Bob") == False
    assert meteoric.is_valid_command('count-class') == True

def test_get_count_class():
    """Test case for get_count_class()."""
    meteors = [["meteor1", 1, "valid", "F1", 21, "Fell", 2000, 10, 20],
            ["meteor2", 2, "Valid", "G7", 1400, "Fell", 2001, 30, 40],
            ["meteor3", 3, "Valid", "CS3", 2500.5, "Found", 2002, 50, 60],
            ["meteor4", 4, "Valid", "GG3", 543, "Discovered", 2004, 50, 60]]
    assert meteoric.get_count_class(meteors) == {"Fell" : 2,
                                                "Found" : 1,
                                                "Discovered" : 1
                                                }
    
def test_get_class():
    """ Test case for get_class() function."""
    meteors = [["meteor1", 1, "valid", "F1", 21, "Fell", 2000, 10, 20],
        ["meteor2", 2, "Valid", "G7", 1400, "Fell", 2001, 30, 40],
        ["meteor3", 3, "Valid", "CS3", 2500.5, "Found", 2002, 50, 60],
        ["meteor4", 4, "Valid", "f1", 543, "Discovered", 2004, 50, 60]]
    argument = "F1"
    empty_arg = "Nothing here"
    assert meteoric.get_class(meteors, argument) == [["meteor1", 1, "valid", "F1", 21, "Fell", 2000, 10, 20], ["meteor4", 4, "Valid", "f1", 543, "Discovered", 2004, 50, 60]]
    assert meteoric.get_class(meteors, empty_arg) == []
