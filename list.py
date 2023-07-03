#list mutable 

# l=[10,20,30]
# #6677
# l[5]=66
# print(l)

#traversing the elements of list:
#by using while
# list=[1,2,3,4,5,6,7,8,9]
# i=0
# while i<len(list):
#     print(list[i])
#     i=+1

#by using for loop:
# for i in list:
#     if i%2==1:
#         print(i)

# list=["a","b","c","d"]
# x=len(list)#3
# for i in range(x):
#     print(list[i],"is at +ve index :",i, " and for -ve index ",i-x)


#function of list

#can one tell me what is diff b/w function and method 

# def f1():    
#     print("function")# out the class

# class stu:
#     def i(self):
#         print("method")#inside the class

# f1()
# s=stu()
# s.i()


#len(list)
#count()


# print(list.count(6))
# print(list.index(6))

# n=int(input("enter the value to check in list"))#10
# list=[1,2,3,4,5,7,8,9]
# if n in list:
#     print(n,"is available at the index ",list.index(n))
# else:
#     print("your value is not found")

#i want to add all elements to list upto 100 which are divisiable by 10

# l=[]
# for x in range(0,101,10):
#     l.append(x)
# print(l)
#if x%10==0:

# #insert()
# list=[1,2,3,4,5,7,8,9]
# # list.insert(1,30)
# list.insert(-10,777)
# print(list)


#extend()
# l1=["aman","venkat","bindu"]
# l2=[2,3,4,5]
# l1.extend(l2)
# print(l1)
# print(l2)

#pop()
# l1=[2,3,4,5,3,3,6,7]
# print(l1.remove(10))
# # print(l1.pop(2))
# print(l1)

# num = 1
# for i in range(1, 5):
#     pattern = ""
#     for j in range(i):
#         pattern = str(num) + pattern
#         num += 1
#     print(pattern)
# 1
# 32
# 654
# 10987


# word = "python"

# for i in range(len(word)):
#     pattern = word[:i+1] * (i + 1)
#     print(pattern)



# l=["20","appLe"]
# l.sort(reverse=False)
# print(l)


# x=[[10,20,30],[40,50,60],[70,80,90]]
# # print(x)
# # print("elements row wise")
# # for r in x:
# #     print(r)
# print("elemets in matrix style")
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         print(x[i][j],end=" ")
#     print()    

# l1=[x**2 for x in range(1,11)]
# l2=[x for x in l1 if x%2!=0]
# print(l1)
# print(l2)

# l=[x**2 for x in range(1,21) if(x**2)%2==0]
# print(l)


# n1=[10,20,30,40]
# n2=[30,40,50,60]
# n3=[x for x in n1 if x not in n2]
# print(n3)

x=[50,70,80]
y=[50,70,80,90]
print(x<y)







