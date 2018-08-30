nums=str(input("Enter your number in base 10 = "))
base=int(input("Enter the desired base = "))
answer=[]
if base<=10:
    if base==2:
        print("\nBinary equivalent of {} = ".format(nums),end="")
    elif base==8:
        print("\nOctal equivalent of {} = ".format(nums),end="")
    while nums!="0":
        for i in range(len(list(nums.split()))):
            x=int(nums)%base
            answer.insert(0,x)
            nums=str(int(nums)//base)
            if nums=="0":
                print(str(answer).replace(",","").replace("[","").replace("]","").replace(" ",""))
                break
elif base==16:
    print("\nHexadecimal equivalent of {} = ".format(nums),end='')
    print(hex(int(nums))[2:])