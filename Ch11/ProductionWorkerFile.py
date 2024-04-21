class Employee:
    
    def __init__(self, employeeName, employeeNumber):
        self.__employeeName = employeeName
        self.__employeeNumber = employeeNumber
        
    def set_employeeName(self, employeeName):
        self.__employeeName = employeeName
        
    def set_employeeNumber(self, employeeNumber):
        self.__employeeNumber = employeeNumber
        
    def get_employeeName(self):
        return self.__employeeName
    
    def get_employeeNumber(self):
        return self.__employeeNumber
    
class ProductionWorker(Employee):
    
    def __init__(self, employeeName, employeeNumber, shiftNumber, hourlyRate):
        Employee.__init__(self, employeeName, employeeNumber)
        self.__shiftNumber = shiftNumber
        self.__hourlyRate = hourlyRate
        
    def set_shiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber
        
    def set_hourlyRate(self, hourlyRate):
        self.__hourlyRate = hourlyRate
        
    def get_shiftNumber(self):
        return self.__shiftNumber
    
    def get_hourlyRate(self):
        return self.__hourlyRate
    

        