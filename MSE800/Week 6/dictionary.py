# #{key_expression : value_expression for item in iterable if condition}

# numbers = [1,2,3,4,5]
# squares = {str(n): n**2 for n in numbers}
# print(squares)

# #Analyze the code with short description and share your answers here: 

# dict1 ={'a':1 , 'b' : 2, 'c' : 3}
# dict2 ={'d':4 , 'e' : 5, 'f' : 6}

# merged_dict = {**{k: v for k,v in dict1.items() if v <2 },
#               **{k1: v1 for k1,v1 in dict2.items() if v1 <3}}

# print(merged_dict)



# dict1 ={'a':1 , 'b' : 5}
# dict2 ={'b':8 , 'r' : 90}
# dict3 ={'a':1 , 'b' : 2, 'c' : 3}

# x,_,y = {5,"ttt",3}
# print(_)

# _ = 5
# print(_)


# a = 5
# a = "fgfgdfdf"


# if (a is not int):
#     a = "fgfgdfdf"
#     print('int')
    
    
# print(a)

# names = ['a','b','c','d']
# ages = [25,35,67]

# paired = list[zip(names, ages)]
# print(paired)

# print(type(paired))

# print(paired)


ids = [1,2,3,4]
names = ['Alice','Bob','Cathy', 'Mike']
grades = ['A','B', 'A+', 'A']


students = list(zip(ids,names, grades))


for i, student in enumerate(students):
    index, name,grade = student    
    print(dict[index, (name, grade)])



data =[]

print(type(data))

for i in range(5):
    data.append(lambda a, i=i*3: i*a)


print(data[0](5))
print(data[1](5))
print(data[3](5))

data2 = []

def cal(i,a):
    i=i*3;
    return i*a

numbers = [5,3,4,6,1]
for i in range(len(numbers)):
    data2.append(cal(i,numbers[i]))
    
    
print(data2)    
#print(data2[0])
#print(data2[1])
#print(data2[4])
    



#Develop a dictionary data type with using the following sample code
# (value should blist(zip(ids,names, grades))e a combination of two strings names and grades)

#students_2 = list(zip(names, grades))



#dict1 = dict('ids',students_2)

#print(dict1)