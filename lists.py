"list" ''''--> consider this list as array just that it would 
creat memory at dynamic time,4,2,1 
  dynamic memory storage'''

'''array
create array of int 4 [ ][ ][ ][ ]
you can apply indexing static memory size 
--memory wastage -extra memory has been allocated 
--memory leakage -less memory intialized, large elements came
             '''

a1 = ["ram", 56, "hello",10.4,10]
a2 = ("sai",555,True)
print(type(a1))
print(type(a1[4]))
print(a1)
print(type(a1[0]))
print(type(a1[1]))
print(type(a2[0000000]))


'property of list'
#1.hetrogenious object
#2.insertion order is preserved
#2.dupicates are allowed
#4.growable in nature
#5.LIFO last in first out is supports


#insert methood
#syntax is ----> n.insert(index,value)

# at the any place you want to place a value

a1.insert(3,"srinu")
print(a1)

#append

# value always at end

a1.append("sony")
print(a1)

#extend

#

a1.extend(a2)
for i in a2:
    a1.append(i)
print(a1)


#pop()  remove from the end

a1.pop()
print(a1)

#remove

a1.remove("srinu")
print(a1)
#len is a length of list
print(len(a1))


print(a1.index("hello"))
print(a1.index("sai"))
print(a1.index(10))

#a1.sort()
a3 = [10,8,56,45,85,558,]
a3.sort()
print(a3)

#clear
a3.clear()
print(a3)
a3=[1]
print(a3)

# not working this
''' 
print(a2.reverse("hello"))
a2.reverse()
print(a2)'''
