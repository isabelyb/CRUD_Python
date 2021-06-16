import random

def binary_search(data, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1




if __name__ == '__main__':

    data = [random.randint(0, 100) for i in range(10)]
    data.sort()
    
    target = int(input('What number would you like to find? '))
    found = binary_search(data, target, 0, len(data)-1)
    if found:
        print(f'The number: {target} is in the list')
    else:
        print(f'The number: {target} is not in the list')
    
    print(data)