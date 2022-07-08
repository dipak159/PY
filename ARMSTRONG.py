num=int(input("ENTER A NUMBER:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum += digit **3
    temp //= 10
if num==sum:
    print(num,"IS AN ARMSTRONG NUMBER")
else:
    print(num,"IS NOT AN ARMSTRONG NUMBER")






