e 9 --> e 10
cars = ["AAA","BBB SS","CFC",1.3,2,3,4,5]
x=70
print(cars[0],type(cars[0]))
print(len(cars[1]))
n3=cars[2]
print(n3[1])
######################
listt=(10,20,30,40,50,60)
print("\n\n",listt,"\t",type(listt))
print(listt[3])
print(listt[1:4])
######################
listt1=[30,72,10,45]
print("\n\n",listt1,"\t",type(listt1))
listt1.append(300)
print("append(300) ##\t",listt1)
listt1.insert(2,500)
print("insert(2,500) ##\t",listt1)
###################dictionary
dic={"Ammar":80,"AHMAD":"ZZZ",17:"Killua"}
print("\n\n",dic)
print(dic[17],"\ncan do::  17 : 'Killua' ")
print(dic["AHMAD"])

student=dict(name="X6!9X",age=37,anything=214.15)
print("\n\n",student)
print(student["name"])
student['name']="ASDF ASDF"
print(student["name"])
student['name']=700
print(student["name"])
student["NEW"]="YES NEW"
print(student)
del student["NEW"]
print("del (delete) => 'NEW'\n",student)
print(student["age"],"\ncan't do:: (37 = age)\n")
print("clear student")
student.clear()
print("print student: ",student)


# for x in range(len(cars)):
#   print (cars[x],end="\n")
# print()
# print (*cars,sep=' , ')

# c=[0]
# for x in range(len(cars)):
#   if type(cars[x]) == int
#     c[x]=cars[x]