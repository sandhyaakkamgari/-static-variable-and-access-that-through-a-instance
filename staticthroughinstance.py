class MyClass:
    class_variable = 10  # This is a class variable
obj = MyClass()
print(obj.class_variable)  #accessing class variable through instance
print(MyClass.class_variable) #accessing class variable through class