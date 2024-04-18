class student:
      def __init__(self , x,y ):
        self.name=x
        self.age=y
s1=student("Abhishek", 21)                     # how many bytes required to store object s1
print("Name  = " , s1.name)
print("Age   = " , s1.age)