nums=str(input("Enter your number in base 10 = "))
base=int(input("Enter the desired base = "))
answer=[]
while nums!="0":
    for i in range(len(list(nums.split()))):
        x=int(nums)%base
        answer.insert(0,x)
        nums=str(int(nums)//base)
        if nums=="0":
            print("\n"+str(answer).replace(",","").replace("[","").replace("]","").replace(" ",""))
            break
