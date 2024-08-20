#problem1
num1=0
num2=1

n=int(input(" write the nth: "))
if n == 1 :
        print(0)
elif n==2:
        print(1)
else:
        for i in range (2,n):
            num3=num1+num2
            num1=num2
            num2=num3
        print(num3)


#problem2

num=int(input("what is the limit"))


for i in range (num+1):
            if (i == 0 or i == 1):
                print(str(i) + "is not prime")
            else:
                for j in range(2,i):
                    if i%j==0:
                        print(str(i) +" is not prime")
                        break
                    elif j==i-1:
                         print(str(i) +"is prime")



#problem3
person1={
        "name": "Merna Botros",
        "age":16,
        "hobby":"chess"
    }
print(person1)
print(person1.get("name"))
print(person1["hobby"])


#add
person1.update({"fav_color":"red"})
person1["fav_tasony"]="vero"
print(person1)



#remove
person1.popitem()#remove random item
print(person1)
person1.pop("name")#remove item by key
print(person1)
del person1["age"]
print(person1)