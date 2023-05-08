class NationalPark:

    def __init__(self, name):
        if type(name) == str:
            self.name = name
        else:
            raise TypeError("Name must be a string")
        
        self._trips = []
        self._visitors = []
        self._park_count = 0
        self.visitors_count = {}


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
            self._trips.append(new_trip)
            return self._trips
        else:
            return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor

        if type(new_visitor) == Visitor:
            if new_visitor not in self._visitors:
                self._visitors.append(new_visitor)
                self.visitors_count[new_visitor] = 1
                return self._visitors
            else:
                self.visitors_count[new_visitor] += 1
                return self._visitors
        else:
            return self._visitors
    
    def total_visits(self):
        return self._park_count
    
    def best_visitor(self):
        return max(self.visitors_count, key=self.visitors_count.get)