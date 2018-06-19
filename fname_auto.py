arr = []
filenamee = 'Value'
counter1 = 1
counter2 = 2
list1 = []
list2 = range(30)    #random number, given len needed
for x in list2:
    counter1 = str(counter1)
    full_name = (filenamee+counter1)
    list1.append(full_name)
    counter1 = counter2
    counter2+=1

for x in list1:
    y = "/usr/bin/"+ x
    arr.append(y)
print arr
