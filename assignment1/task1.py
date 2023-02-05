# Write a Python program to swap 4 variables values (input four values.
# Sample input:
# Before swapping a=2, b=56, c=78, d=9
# After Swaping a=,9, b=78, c=56, d=2

def swap():
     a = 2 
     b = 56
     c = 78 
     d = 9
     print("before swaping")
     print(f"a = {a}, b = {b}, c = {c}, d = {d}")
     temp1 = a
     a = d
     d = temp1
     temp2 = b
     b = c
     c= temp2
     print("after swaping")
     print(f"a = {a},  b = {b}, c = {c}, d = {d}")
swap()

# Write a Python program to convert temperatures to and from celsius,
# Fahrenheit.
# Formula : c/5 = f-32/9
# Expected Output :
# Enter temp in Celsius: 60°C
# Temperature in Fahrenheit is :140


def TemperatureConverter():
    selector = int(input("press 0 to convert temperature from Fahrenheit to celsius  & 1 to convert  celsius to Fahrenheit = "))
    if selector == 0:
        tocelsius()
    elif selector == 1 :
        tofahrenheit()
    else :
        print("please enter valid value")


def tofahrenheit():
    celsius = float(input("enter temperature in celsius = "))
    toFahrenheit = (celsius * 1.8) + 32 
    print(F'{toFahrenheit}F')

def tocelsius():
    
    Fahrenheit = float(input("enter temperature in Fahrenheit = "))
    toCelsius = (Fahrenheit - 32) * .5556
    print(f"{toCelsius}C")
    
# TemperatureConverter()




# Play with some of the list functions. You can find the methods you can call on an object via the dir
# and get information about them via the help command: 

List=['Benin','Bolivia','Bosnia','Botswana','Brazil','Brunei','Brunswick','Bulgaria','Burkina Faso','Burma','Burundi']
print(List)
print(f'6th Element in list = {List[6]}')
print(f'6th Element in list = {List[5:7]}')
List[4] = "America"
print(List)
List[1:3] = ["Pakistan", "Germany"]
print(List)
List.append("India")
print(List)
List.remove("Brunei")
print(List)
List.pop(1)
print(List)



# Write a Python program to count the number of strings where the string length is 2 or more and the
# first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2. 


def Compare(words):
  counter = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      counter += 1
  return counter

print(Compare(['abc', 'hello', 'australia', '1221']))




# Write a Python script to concatenate following dictionaries to create a new one.

dictionary1 = {  'name': "john", 'class': 4, 'seat' : 18895 }
dictionary2 = {'teacher': "carl",'class': 10,'id' : 2545450 }
dictionary3 = {'school': "abc",'location': "xyz road",'year' : 1999 }

dictionary1.update(dictionary2)
dictionary1.update(dictionary3)
print(dictionary1)


# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’]
# Expected Output : ['Green', 'White', 'Black']


List1=  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink']
List1.pop(0)
List1.pop(3)
List1.pop(3)
print(f'after removing 0th,4th and 5th element{List1}')
    


# List2 = ["China","INDIA","pakistan","AUSTRALIA","peru"]
# List3=[]
# for i in List2:
#     print(i)
#     i.tolower()
#     print(i)
#         # if len(j) > 5:
#         #     j.tolower()
#         #     List3.append(i)
#         #     print(List3)        
        

# Exercise
# Create a Python Program that perform  tasks for any problem of your choice:


