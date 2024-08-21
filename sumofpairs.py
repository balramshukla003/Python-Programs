
# value=input("Enter Digit seperate by space:")
# a= [int(x) for x in value.split()]
a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
z=[]
count =0
for i in range(len(a)-1):
      b=a[i]
      for j in range (len(a)-1):
            c=a[j]
            if b+c==9:
                  z.append(b)
                  print(b,"+",c,"= 9")
            elif b-c==9:
                  print(b,"-",c,"=9")
count=int(len(z)/2)               
print(z)
print("Total number Of Unique pairs whose Sum=9:",count)