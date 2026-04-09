#NAMA  :SAIFUL BAHRI
#NIM   :241011400864
#KELAS :03TPLP022


import random

def linear_search(arr, target):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == target:
            return count
    return -1

def binary_search(arr, target):
    count = 0
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        count += 1
        if arr[mid] == target:
            return count
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Membuat list acak yang sudah diurutkan
arr = sorted([random.randint(1, 50) for _ in range(10)])

# Memilih target acak dari list
target = random.choice(arr)

# Melakukan linear search dan binary search
linear_count = linear_search(arr, target)
binary_count = binary_search(arr, target)

print(f"List: {arr}")
print(f"Target: {target}")
print(f"Linear Search: {linear_count} operasi pemeriksaan")
print(f"Binary Search: {binary_count} operasi pemeriksaan")

if linear_count > binary_count:
    print("Binary Search lebih efisien daripada Linear Search")
elif linear_count < binary_count:
    print("Linear Search lebih efisien daripada Binary Search")
else:
    print("Linear Search dan Binary Search memiliki efisiensi yang sama")

