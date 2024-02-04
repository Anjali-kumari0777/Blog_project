# arr=[111,222,333] 
# for i in arr:
#         i=str(i)
#         n=len(i)
#         for j in range(n//2):
#             if i[j]!=i[n-1-i]:
#               return 0
# return 1


# arr=[3,5,40,6,1]
# n=len(arr)
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]>arr[j]:
#             arr[i],arr[j]=arr[j],arr[i]
# print(arr)   
# print(n)         
# if n%2==0:
    
#     avg=arr[n//2]+arr[n//2-1]
#     median1=avg//2
#     print(median1,'1st') 
# else:
#     median=arr[n//2]    
#     print (median,'2nd')
# -----------------------------------------------------------
# def find_indices(arr, key):
#     n = len(arr)
#     start_index = -1
#     end_index = -1

#     # Find start index
#     for i in range(n):
#         if arr[i] == key:
#             start_index = i
#             break

#     # Find end index
#     for i in range(n - 1, -1, -1):
#         if arr[i] == key:
#             end_index = i
#             break

#     return start_index, end_index

# # Example usage:
# arr = [1, 2, 3, 4, 5, 5]
# key = 5
# start, end = find_indices(arr, key)

# if start != -1 and end != -1:
#     print("Output:", start, end)
# else:
#     print("Output: -1 -1")

           
            