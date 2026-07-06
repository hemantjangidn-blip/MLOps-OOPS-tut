# initiate a class called employee

class Employee:
    # a constructor/magic method/ dunder method
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
    
    #creating methods in class    
    def travel(self,destination):
        print(f"you have to travel to {destination}")
    
    def presentation(self,day):
        print(f"you have to give presentation on {day}")
    
    def report(self,day):
        print(f"you have to report on {day}...")
    
sam = Employee()
sam.travel("Kerala")
sam.presentation("Monday")
sam.report("Thursday")