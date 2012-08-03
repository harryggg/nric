import random
#NRIC=S95(JC1 Singporean)+number of baby before u
#generation list of numbers of babies b4 you
weight=[2,7,6,5,4,3,2]
alphabet=['J','Z','I','H','G','F','E','D','C','B','A']

    
def checksum_gen(nric):
    n=nric[1:]
    checksum=0
    for w_index in range(7):
        checksum+=int(n[w_index])*weight[w_index]
        
    return alphabet[checksum%11]

def quick_sort(n):
    if n==[]:return []
    pivot=n[0]
    big=[]
    small=[]
    for element in n[1:]:
        if element>=pivot:
            big.append(element)
        else:
            small.append(element)
    return quick_sort(small)+[pivot]+quick_sort(big)
            
def gen_student():
    
        index=random.randint(0,len(babynumber)-1)
        nric='S95'+babynumber[index]
        del babynumber[index]
        nric+=checksum_gen(nric)
        student=namelist[random.randint(0,len(namelist)-1)]+' '+surnamelist[random.randint(0,len(surnamelist)-1)]
        file.write(student+':'+nric+'\n')
        list.append(student+':'+nric)
    


#main

name=open('name.txt','r')
namelist=[]
for row in name.readlines():
    namelist.append(row[:-1][0].upper()+row[:-1][1:].lower())
name.close()
surname=open('surname.txt','r')
surnamelist=[]
for row in surname.readlines():
   surnamelist.append(row[:-1])
surname.close() 
    
babynumber=[]
for i in range(40000):
    number=str(i)
    babynumber.append((5-len(number))*'0'+number)
list=[]

file=open('STUDENTS.DAT','w')
for i in range(10000):
    gen_student()
file.close()

list=quick_sort(list)

for element in list:
    print(element)

        
        


