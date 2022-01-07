def re_binary(a,key,low,high):
    if low>high:
        return -999
    mid=int(low+high//2)
    if a[mid]==key:
        return (mid)
    if a[mid]>key:
        re_binary(a,key,low,mid-1)
    if a[mid]<key:
        re_binary(a,key,mid+1,high)
a=[3,5,8,15,18,20,25,30]
key=int(input("enter no of search"))
x=re_binary(a,key,0,7)
if x==-999:
    print("not found")
else:
    print("number found of at",x,"position")