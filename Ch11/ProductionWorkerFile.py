# Define the class
class Employee:
    # Using init method with variables and self
    def __init__(self, employeeName, employeeNumber):
        self.__employeeName = employeeName
        self.__employeeNumber = employeeNumber
        
    # Defining the set_employeeName method
    def set_employeeName(self, employeeName):
        self.__employeeName = employeeName
        
    # Defining the set_employeeNumber method
    def set_employeeNumber(self, employeeNumber):
        self.__employeeNumber = employeeNumber
        
    # Defining the get_employeeName method
    def get_employeeName(self):
        return self.__employeeName
    
    # Defining the get_employeeNumber method
    def get_employeeNumber(self):
        return self.__employeeNumber

    
# Define the class
class ProductionWorker(Employee):
    
    # Using init method with variables and self
    def __init__(self, employeeName, employeeNumber, shiftNumber, hourlyRate):
        Employee.__init__(self, employeeName, employeeNumber)
        self.__shiftNumber = shiftNumber
        self.__hourlyRate = hourlyRate
        
    # Defining the set_employeeName method
    def set_shiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber
        
    # Defining the set_hourlyRate method
    def set_hourlyRate(self, hourlyRate):
        self.__hourlyRate = hourlyRate
        
    # Defining the get_shiftNumber method
    def get_shiftNumber(self):
        return self.__shiftNumber
    
    # Defining the get_hourlyRate method
    def get_hourlyRate(self):
        return self.__hourlyRate
    

        