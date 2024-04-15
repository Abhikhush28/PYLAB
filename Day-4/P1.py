class Car:  

    def __init__(self,mname, yr):  
        self.modelname = mname   #yeha par ham self.name ek alag vaiable hai jo constructor ke parameter le assign ho raha hai self.modelname  so isse  pata chalta hai ahi ki self.variable name kuch v le sakte hai
        self.year = yr  
 
 
    def display(self):  
        print(self.modelname,self.year)  
c1 = Car("Toyota", 2016)  
c1.display()  
 
 
c2=Car("BMW",2022)
c2.display()