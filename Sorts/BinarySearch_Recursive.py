"""
@author: Maneesh D
@email: maneeshd77@gmail.com

Binary Search (Recursive)
Array should have been sorted first
"""


def binary_search(data, left, right, key):
    if right >= left:
        mid = (left + (right - left)) // 2
            
        if data[mid] == key:
            return mid
        elif key < data[mid]:
            return binary_search(data, left, mid-1, key)
        else:
            return binary_search(data, mid+1, right, key)
    else:
        return -1
    
    
if __name__ == "__main__":
    num_range = list(range(1, 1000001))
    while True:
        try:
            num_to_search = int(input("Enter a number in the range [1, 1000000] to search: "))
            index = binary_search(num_range, 0, len(num_range)-1, num_to_search)
            if index >= 0:
                print("%d found at index=%d in the number list." % (num_to_search, index))
            else:
                print("%d not found in the number list." % num_to_search)
            break
        except ValueError:
            print("\n!!! Please enter a valid number in the range [1, 1000000] !!!\n")
            continue
        except KeyboardInterrupt:
            print("\n!!! Cancelled by user...Exiting... !!!\n")
            exit(1)
        except Exception as e:
            print("Unexpected Error:")
            print(e)
            exit(1)
    print("\n<!---- Thank You ----!>")