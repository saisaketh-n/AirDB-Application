# pickle module is used for saving and loading an Airline object to and from external files.
import pickle

from employee import Employee
from flight import Flight

class Airline(object):
    '''Airline class models an airline with a list of employees and flights.'''

    def __init__(self, name, airline_code, primary_hub_code):
        '''
        Initializes an Airline object with instance variables (see below).

        Parameters:
            name (str): airline name
            airline_code (str): two-character code of airline
            primary_hub_code (str): three-letter code of airline's primary hub airport
        
        Instance variables:
            _name: initialized with the value of parameter name
            _airline_code: initialized with uppercased value of parameter airline_code
            _primary_hub_code: initialized with uppercased value of parameter primary_hub_code
            _employees: initialized to empty list
            __lights: initialized to empty list
        '''
        self._name = name
        self._airline_code = airline_code.upper()
        self._primary_hub_code = primary_hub_code.upper()
        self._employees = []
        self._flights = []


    def name(self):
        '''Returns the value of _name attribute of self object.'''
        pass


    def airline_code(self):
        '''Returns the value of _airline_code attribute of self object.'''
        pass


    def primary_hub_code(self):
        '''Returns the value of _primary_hub_code attribute of self object.'''
        pass


    def employees(self):
        '''Returns the value of _employees attribute of self object.'''
        return self._employees


    def flights(self):
        '''Returns the value of _flights attribute of self object.'''
        return self._flights


    def add_employee(self, employee):
        '''
        Adds an employee to the list of employees of this airline.

        Parameter:
            employee (Employee): employee to add to the list of employees after validation(s)

        Validations and exceptions raised:
            - TypeError if employee is not an instance of Employee
            - ValueError if employee is already present in the list of employees
            - ValueError if there exists an employee in the list with the same employee id
                (can't have two employees with the same employee id)

        Implementation requirements:
            - Must make use of find_employee()
        '''
        pass


    def remove_employee(self, employee_id):
        '''
        Removes the employee with given employee id from the list of employees.
        Removing an employee also requires that you remove this employee from the crew of any flights
        where this employee is assigned as a member.

        Parameter:
            employee_id (str): id of the employee to be removed from the list of employees

        Validations and exceptions raised:
            - ValueError if employee with given id not found in the list of employees

        Implementation requirements:
            - Must make use of find_employee()     
        '''
        pass


    def find_employee(self, employee_id):
        '''
        Returns the employee with the given employee id.

        Parameter:
            employee_id (str): id of the employee to find in the list of employees

        Returns: Employee instance if found or None otherwise
        '''
        pass


    def add_flight(self, flight):
        '''
        Adds a flight to the list of flights of this airline.

        Parameter:
            flight (Flight): flight to add to the list of flights after validation(s)

        Validations and exceptions raised:
            - TypeError if flight is not an instance of Flight
            - ValueError if flight is already present in the list of flights
            - ValueError if there exists a flight in the list with the same flight number
                (can't have two flights with the same flight number)

        Implementation requirements:
            - Must make use of find_flight()
        '''
        pass


    def remove_flight(self, flight_nbr):
        '''
        Removes the flight with given flight number from the list of flights.

        Parameter:
            flight_nbr (int): number of the flight to remove from the list of flights

        Validations and exceptions raised:
            - ValueError if flight with given number not found in the list of flights

        Implementation requirements:
            - Must make use of find_flight()     
        '''
        pass


    def find_flight(self, flight_nbr):
        '''
        Returns the flight with the given flight_nbr.

        Parameter:
            flight_nbr (int): number of the flight to find in the list of flights

        Returns: Flight instance if found or None otherwise
        '''
        pass


    def find_flights(self, origin, dest):
        '''
        Returns a list of flights between origin airport and destination airport. The returned
        list could be empty if there are no flights between origin and destination airports.

        Parameters:
            origin (str): code of origin airport
            dest (str): code of destination airport
        '''
        pass


    def flight_crew(self, flight_nbr):
        '''
        Returns a list of crew for the flight with given flight number. The returned
        list could be empty if the flight has no crew assigned yet.

        Parameters:
            flight_nbr (int): flight number

        Validations and exceptions raised:
            - ValueError if flight with given number not found in the list of flights

        Implementation requirements:
            - Must make use of find_flight()
        '''
        pass


    def add_crew_to_flight(self, flight_nbr, employee_id):
        '''
        Adds a member to the crew of the flight with given flight number.

        Parameters:
            flight_nbr (int): flight number
            empolyee_id (str): id of the employee to be added to the flight crew

        Validations and exceptions raised:
            - ValueError if flight with given number not found in the list of flights
            - ValueError if employee with given id not found in the list of employees
            - ValueError if employee to add is already a member of the flight crew

        Implementation requirements:
            - Must make use of find_flight()
            - Must make use of find_employee()
        '''
        pass


    def remove_crew_from_flight(self, flight_nbr, employee_id):
        '''
        Removes a member from the crew of the flight with given flight number.

        Parameters:
            flight_nbr (int): flight number
            empolyee_id (str): id of the employee to remove from the flight crew

        Validations and exceptions raised:
            - ValueError if flight with given number not found in the list of flights
            - ValueError if employee with given id not found in the list of employees
            - ValueError if employee to remove is not a member of the flight crew

        Implementation requirements:
            - Must make use of find_flight()
            - Must make use of find_employee()
        '''
        pass


    def __str__(self):
        '''Returns a printable string representation of Airline object.'''
        return 'Airline: %s; Airline Code: %s; Primary Hub Code: %s' % (self._name,
            self._airline_code, self._primary_hub_code)


    def __eq__(self, other):
        '''Returns True if self object is value equivalent to other object, False otherwise.'''
        pass


    def save_to_file(self, filename):
        '''
        Saves the self Airline instance to the specified file using Python object serialization.

        Parameter:
            filename (str): name of the file to save the airline database to
        '''
        with open(filename, 'wb') as outfile:
            pickle.dump(self, outfile, pickle.DEFAULT_PROTOCOL)


    @staticmethod
    def load_from_file(filename):
        '''
        Loads the airline database information from the specified file and returns
        an Airline object with all its data.

        Parameter:
            filename (str): name of the file to load the airline database from
        '''
        with open(filename, 'rb') as infile:
            airline = pickle.load(infile)  
            return airline
