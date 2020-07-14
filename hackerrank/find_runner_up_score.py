if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    to_list = list(arr)
    #print(to_list)
    top_value = max(to_list)
    cleaned_list = [x for x in to_list if x != top_value]
    print(max(cleaned_list))
    
    
    



OR



    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(max([x for x in arr if x != max(arr)]))    
