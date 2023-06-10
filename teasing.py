# print("input the string to calculate the number of lower case and the uppercase ")
def count(letter):
    upper_count=0
    lower_count=0
    for i in letter:
        if i.isupper():
            upper_count+=1
        else:
            lower_count+=1
    return upper_count, lower_count
upper,lower =count("pYthoN")
print("the number of uppercase letter %d"%upper)
print("the number of lowercase letter %d"%lower)

"""Exercise Two"""
# multiples of 3 and 5
# def print_multiples(range_number):
#     num_list = list(range(1,range_number+1))
#     multiples = []
#     for num in num_list:
#         if(num % 3 == 0 or num % 5 == 0):
#             multiples.append(num)
#     return multiples             
# print(print_multiples(20))       
"""exercise Three"""

# float_list= [2.5, 16.42, 10.77, 8.3, 34.21] 
# # print how many numbers are less than 10
# count = 0
# for num in float_list:
#     if num < 10:
#         count +=1 
#     else: continue   
# print(count)     

""" exercise Four"""
# we are finding the maximum power of n before the value exceeds 500
# n = 3
# val = n
# power = 0
# while val < 500:
#     power += 1
#     val *= n
# print(power)
""" exercise Five"""
#We are making a multiplication table using 
# const = 3
# multi = 1
# while multi <= 12:
#     answer = multi*const
#     print("%d x %d = %d"%(const,multi,answer))
#     multi +=1

# count all even numbers between 0 to 30

# num_list = list(range(0,30,2))
# print(len(num_list))
# print(num_list)

# sum all number between 100 and 200

# num_list = list(range(100,200))
# sum = 0
# for num in num_list:
#     sum += num
# print(sum)    

""" calculating the sum of numbers in the list"""
# List = (8, 2, 3, 0, 7)
# sum = 0
# for num in List:
#     sum += num
# print(sum)    
""" Exercise Six"""
# class Employee:
#     def __init__(self, Id, Salary, Department = None):
#         self.Id = Id
#         self.Salary = Salary
#         self.Department = Department 
# James = Employee(12, 400)
# print(James.Salary)      

"""Class variables and instance variables"""
# class player:
#     teamName = "PSG"
#     def __init__(self,name,formerTeam):
#         self.name = name
#         self.formerTeam = formerTeam
# p1 = player("Messi", "Barcelona") 
    
# p2= player("Mbappe", "AS Monaco")
 
# print("Mbappe's current Team",p2.teamName) 
# print("Mbappe's former Team",p2.formerTeam) 

# """ instance methods"""

# class Employee:
#     def __init__(self,id=None,salary=None,department=None):
#         self.Id = id
#         self.salary = salary
#         self.department = department
#     def tax(self):
#         return self.salary * 0.18
#     def netSalary(self):
#         return self.salary - self.tax()
#     def salaryPerDay(self):
#         return self.salary//30
# James = Employee(123,100000) 
# print("Mbappe's net Salary = ",James.netSalary())
# print("Mbappe's salary per day = ",James.salaryPerDay()) 
# print("Mbappe's monthly tax = ",James.tax())      
