d=lambda p:p*5
t=lambda p:p*2
x=7
x=d(x)
x=t(x)
x=d(x)
print(x)

my_list=[1,2,3,4,5,6,7,8]
new_list=list(map(lambda x: x*2+2-4,my_list))
print(new_list)

my_list=[1,2,3,4,5,6,7,8]
new_list=list(filter(lambda x: x%2!=0,my_list))
print(new_list)

