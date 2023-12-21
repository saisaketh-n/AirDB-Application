from employee import Employee

class Flight(object):
    '''Flight class models a direct flight between two airpots.'''

    def __init__(self, flight_nbr, origin_airport_code, dest_airport_code):
        '''
        Initializes a Flight object with instance variables (see below).

        Parameters:
            flight_nbr (int): flight number
            origin_airport_code (str): three-letter code of origin airport
            dest_airport_code (str): three-letter code of destination airport
        
        Instance variables:
            _flight_nbr: initialized with the value of parameter flight_nbr
            _origin_airport_code: initialized with uppercased value of parameter origin_airport_code
            _dest_airport_code: initialized with uppercased value of parameter dest_airport_code
            _crew: initialized to empty list
        '''
        self._flight_nbr = flight_nbr
        self._origin_airport_code = origin_airport_code.upper()
        self._dest_airport_code = dest_airport_code.upper()
        self._crew = []


    def flight_nbr(self):
        '''Returns the value of _flight_nbr attribute of self object.'''
        pass


    def origin_airport(self):
        '''Returns the value of _origin_airport_code attribute of self object.'''
        pass


    def dest_airport(self):
        '''Returns the value of _dest_airport_code attribute of self object.'''
        pass


    def crew(self):
        '''Returns the value of _crew attribute of self object.'''
        pass


    def deck_crew(self):
        '''Returns a list containing the deck crew (pilots) of self object.'''
        pass


    def cabin_crew(self):
        '''Returns a list containing the cabin crew (flight attendants) of self object.'''
        pass


    def add_crew_member(self, crew_member):
        '''
        Adds a member to the flight crew only if not already present in the __crew attribute of self object.
        
        Parameter:
            crew_member (Employee): crew member to add to the flight crew

        Validations and exceptions raised:
            - TypeError if crew_member is not an instance of Employee
        '''
        pass


    def remove_crew_member(self, crew_member):
        '''
        Remove a member from flight crew if present in the __crew attribute of self object.
        
        Parameter:
            crew_member (Employee): crew member to remove from the flight crew

        Validations and exceptions raised:
            - TypeError if crew_member is not an instance of Employee
        '''
        pass


    def __str__(self):
        '''Returns a printable string representation of self object.'''
        return 'Flight #: %s; Origin Airport: %s; Destination Airport: %s' % \
            (self._flight_nbr, self._origin_airport_code, self._dest_airport_code)


    def __eq__(self, other):
        '''Returns True if self object is value equivalent to other object, False otherwise.'''
        pass
