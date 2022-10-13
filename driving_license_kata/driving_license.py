class DrivingLicense:
  
  def __init__(self,data:list) -> None:
    self._data = data
    
  def get_license_number(self) -> str:
    pass
  
  def get_surname(self) -> str:
    surname = self._data[2][0:5]
    while len(surname) < 5:
       surname += "9"
    return surname.upper()
       
  def get_birth_year(self) -> str:
    birth_year = self._data[3][-2]
    return birth_year
  
  def get_birth_month(self) -> str:
    return "01"