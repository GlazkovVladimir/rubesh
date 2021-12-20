class Employee:
    print("Дом милый дом")
 
    emp_count = 0  
  
    def __init__(self, name,):  
        self.name = name  
        
    def display_employee(self):  
        print('количество этажей: {} .format(self.name, self.salary))  
  
 
emp1 = Employee("3 этажа")  
# Это создаст второй объект класса Employee  
emp2 = Employee("Мария")  
emp1.display_employee()  
emp2.display_employee()  

