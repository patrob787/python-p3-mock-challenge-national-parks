from classes.visitor import Visitor
from classes.national_park import NationalPark

class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        
        visitor.trips(self)
        visitor.national_parks(self.national_park)

        national_park.trips(self)
        national_park.visitors(self.visitor)
        national_park._park_count += 1
        
        if type(start_date) == str:
            self.start_date = start_date
        else:
            raise TypeError("Start Date must be a string")
        
        if type(end_date) == str:
            self.end_date = end_date
        else:
            raise TypeError("Name must be a string")
        
    def get_visitor(self):
        return self._visitor
    
    def set_visitor(self, visitor):
        if type(visitor) == Visitor:
            self._visitor = visitor
        else:
            raise TypeError("Visitor is not object")
        
    visitor = property(get_visitor, set_visitor)

    def get_national_park(self):
        return self._national_park
    
    def set_national_park(self, national_park):
        if type(national_park) == NationalPark:
            self._national_park = national_park
        else:
            raise TypeError("Park is not object")
        
    national_park = property(get_national_park, set_national_park)
