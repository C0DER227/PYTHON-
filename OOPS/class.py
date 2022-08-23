#class
class employee:                       #class define
    company="Genesis mining ltd"      #object1
    salary=100                        #object2

mukesh=employee()
ravi=employee()
nishant=employee()
nitu=employee()

print(mukesh.company)
print(ravi.company)
print(nishant.company)
print(nitu.company)

employee.company="NVDIA Ltd"
print(mukesh.company)
print(ravi.company)
print(nishant.company)
print(nitu.company)

print(mukesh.salary) #class atributes
ravi.salary=30000
nitu.salary=100000
print(ravi.salary)   #instance atributes
print(nishant.salary) #class atributes
print(nitu.salary)    #instance atributes