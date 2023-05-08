class Visitor:

    def __init__(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self.name = name
        else:
            raise TypeError("Name must be string between 1 and 15 characters")
        
        self.trip_list = []
        self.park_list = []


    def get_name(self):
        return self._name

    def set_name(self, name):
        if hasattr(self, "name"):
            raise ValueError("Name cannot be changed")
        else:
            self._name = name

    name = property(get_name, set_name)

    def trips(self, new_trip=None):
        from classes.trip import Trip
        
        if type(new_trip) == Trip:
            self.trip_list.append(new_trip)
            return self.trip_list
        else:
            return self.trip_list
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        
        if type(new_national_park) == NationalPark:
            if new_national_park not in self.park_list:
                self.park_list.append(new_national_park)
                return self.park_list
        else:
            return self.park_list