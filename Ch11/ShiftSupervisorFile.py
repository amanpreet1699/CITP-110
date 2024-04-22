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
class ShiftSupervisor(Employee):

    # Using init method with variables and self
    def __init__(self, employeeName, employeeNumber, annualSalary, annualProdBonus):
        Employee.__init__(self, employeeName, employeeNumber)
        self.__annualSalary = annualSalary
        self.__annualProdBonus = annualProdBonus
        
    # Defining the set_annualSalary method
    def set_annualSalary(self, annualSalary):
        self.__annualSalary = annualSalary
        
    # Defining the set_annualProdBonus method
    def set_annualProdBonus(self, annualProdBonus):
        self.__annualProdBonus = annualProdBonus
        
    # Defining the get_annualSalary method
    def get_annualSalary(self):
        return self.__annualSalary
    
    # Defining the get_annualProdBonus method
    def get_annualProdBonus(self):
        return self.__annualProdBonus
    