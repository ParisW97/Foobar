from collections import Counter

# # list of int named 'data'
# data = [1,2,2,3,3,4,4,4,4]
# # int 'n' used for allowed instances of any number in 'data
# n = 1


def main():
    # list of int named 'data'
    data = [1,2,2,3,3,4,4,4,4]
    # int 'n' used for allowed instances of any number in 'data
    n = 3
    # print list of IDs
    print(data)
    # print address of list
    print(id(data))
    # run solution function
    solution(data,n)
    # print list of IDs
    print(data)
    # print address of list
    print(id(data))





# print(data)

# counts = Counter(data)

# # print dictionary
# print(counts)

# print keys of dictionary
# for k, elem in counts.items():
#     print(k, elem)
#     if elem <= n:
#         # allowable instances of entry
#         continue
#     # exceeds limit - remove specific entry from list
#     for i in data[:]:
#         if i == k:
#             data.remove(i)
#     print(data)
# print(data)
# print key values of dictionary

def solution(data:list,n:int):
    # create dict from list of employee IDs
    dataDict = Counter(data)

    # loop through to remove employee IDs, as needed
    for key, keyValue in dataDict.items():
        if keyValue <= n:
            continue
        # remove employee ID from list
        removeID(data,n,key,keyValue,dataDict)
        # for id in data[:]:
        #     if id == key:
        #         data.remove(key)

def removeID(data:list,n:int,key:int,keyValue:int,dataDict:dict):
    for id in data[:]:
            if id == key:
                data.remove(key)

if __name__ == "__main__":
    main()