from driving_license_kata.driving_license import DrivingLicense
import pytest

@pytest.fixture
def driving_license_generator():
  return DrivingLicense

# parameterized tests
testdata = [
  (["John","James","Smith","01-Jan-2000","M"],"SMITH"),
  (["John","James","Smit","01-Jan-1990","M"],"SMIT9"),
  (["John","James","Sim","01-Jan-1980","M"],"SIM99"),
  (["John","James","Si","01-Jan-1970","M"],"SI999"),
  (["John","James","Smiths","01-Jan-1960","M"],"SMITH"),
  (["John","James","Smithers","01-Jan-1940","M"],"SMITH"),
]

@pytest.mark.parametrize("input,expected", testdata)
def test_should_return_surname(input, expected, driving_license_generator):
  surname = driving_license_generator(input).get_surname()
  assert surname == expected

# test case: return a single digit from birth year
# @pytest.mark.parametrize("input,expected", testdata)
# def test_should_return_single_digit_from_birth_year(input, expected, driving_license_generator):
#   birth_year = driving_license_generator(input).get_birth_year()
#   assert birth_year == expected
  
# def test_should_return__digit_0_from_birth_year(driving_license_generator):
#   birth_year = driving_license_generator(testdata[0][0]).get_birth_year()
#   assert birth_year == "0"
  
# def test_should_return__digit_9_from_birth_year(driving_license_generator):
#   birth_year = driving_license_generator(testdata[1][0]).get_birth_year()
#   assert birth_year == "9"
  
# def test_should_return__digit_8_from_birth_year(driving_license_generator):
#   birth_year = driving_license_generator(testdata[2][0]).get_birth_year()
#   assert birth_year == "8"
  
# def test_should_return__digit_7_from_birth_year(driving_license_generator):
#   birth_year = driving_license_generator(testdata[3][0]).get_birth_year()
#   assert birth_year == "7"

# def test_should_return__digit_6_from_birth_year(driving_license_generator):
#   birth_year = driving_license_generator(testdata[4][0]).get_birth_year()
#   assert birth_year == "6"

# test case: The month of birth 

def test_should_return_birth_month_for_jan_male(driving_license_generator):
  birth_month = driving_license_generator(testdata).get_birth_month()
  assert birth_month == "01"

def test_should_return_birth_month_for_feb_male(driving_license_generator):
  birth_month = driving_license_generator(testdata).get_birth_month()
  assert birth_month == "02"