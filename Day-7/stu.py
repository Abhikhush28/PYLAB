class Student:    
    count = 0    
    def __init__(self):    
        Student.count = Student.count + 1    
s1=Student()    
s2=Student()    
s3=Student()    
print("The number of students:",Student.count)



# # 1	getattr(obj,name,default) 	It is used to access the attribute of the object.
# 2	setattr(obj, name,value)   	It is used to set a particular value to the specific attribute of an object.
# 3	delattr(obj, name)         	It is used to delete a specific attribute.
# 4	hasattr(obj, name)	       It returns true if the object contains some specific attribute.