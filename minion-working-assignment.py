from collections import Counter

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

def solution(data:list,n:int):
    # create dict from list of employee IDs
    dataDict = Counter(data)

    # loop through to remove employee IDs, as needed
    for key, keyValue in dataDict.items():
        if keyValue <= n:
            continue
        # remove employee ID from list
        removeID(data,n,key,keyValue,dataDict)

def removeID(data:list,n:int,key:int,keyValue:int,dataDict:dict):
    for id in data[:]:
            if id == key:
                data.remove(key)

if __name__ == "__main__":
    main()