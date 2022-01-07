def bsearch(a,key):
    i=0
    j=size-1
    flage=0
    while i<=j and flage==0:
        mid=(i+j)//2
        if a[mid]==key:
            flage=1
            pos=mid+1
        if a[mid]>key:
            j=mid-1
        if a[mid]<key:
            i=mid+1
    if flage==1:
        print("num found at",pos,"possition")
    else:
        print("found")
a=[]
size=int(input("enter no of element size:-"))
for i in range(size):
    v=int(input("enter the no of accending order:-"))
    a.append(v)
print(a)
key=int(input("enter no  to find:-"))
bsearch(a,key)


# def bsearch(a,key):
#     i=0
#     j=size-1
#     flage=0
#     while i<=j and flage==0:
#         mid=(i+j)//2
#         if a[mid]==key:
#             flage=1
#             pos=mid+1
#         if a[mid]<key:
#             j=mid-1
#         if a[mid]>key:
#             i=mid+1
#     if flage==1:
#         print("num found at",pos,"possition")
#     else:
#         print("found")
# a=[]
# size=int(input("enter no of element size:-"))
# for i in range(size):
#     v=int(input("enter the no of deccending order:-"))
#     a.append(v)
# print(a)
# key=int(input("enter no  to find:-"))
# bsearch(a,key)

