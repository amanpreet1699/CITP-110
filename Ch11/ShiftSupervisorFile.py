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
    
    
class ShiftSupervisor(Employee):
    
    def __init__(self, employeeName, employeeNumber, annualSalary, annualProdBonus):
        Employee.__init__(self, employeeName, employeeNumber)
        self.__annualSalary = annualSalary
        self.__annualProdBonus = annualProdBonus
        
    def set_annualSalary(self, annualSalary):
        self.__annualSalary = annualSalary
        
    def set_annualProdBonus(self, annualProdBonus):
        self.__annualProdBonus = annualProdBonus
        
    def get_annualSalary(self):
        return self.__annualSalary
    
    def get_annualProdBonus(self):
        return self.__annualProdBonus
    