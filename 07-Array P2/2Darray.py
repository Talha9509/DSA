import numpy as np

twoDarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDarray)

# new=np.insert(twoDarray,3,[[0,0,0]],axis=1)
# print(new)

# new2=np.append(twoDarray,[[0,0,0]],axis=0)
# print(new2)

# new3=np.append(twoDarray,[[0],[0],[0]],axis=1)
# print(new3)

# def accessElem(arr,rowi,coli):
#     if rowi>=len(arr) and coli>=len(arr):
#         print("Incorrect index")
#     else:
#         print(arr[rowi][coli])

# accessElem(twoDarray,0,1)


# def traverseElem(arr):
#     for i in range(len(arr)):
#        for j in range(len(arr[i])):
#            print(arr[i][j],end="")

# traverseElem(new)


# def searchElem(arr,searchElem):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j]==searchElem:
#                 return (f"Element at {i} {j}")
#     return "not found"

# print(searchElem(twoDarray,3))

new4=np.delete(twoDarray,0,axis=1)
print(new4)