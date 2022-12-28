import time
import random

def SelectionSort(arr):
    res = arr.copy()
    for i in range(0, len(arr), 1):
        minIndex = res.index(min(res[i:]))
        res[i], res[minIndex] = res[minIndex], res[i]
    return res

def InsertionSort(arr):
    res = arr.copy()
    for i in range(1, len(res), 1):
        cur = i
        while res[cur] < res[cur - 1]:
            res[cur], res[cur - 1] = res[cur - 1], res[cur]
            cur -= 1
            if cur == 0:
                break
    return res

def BubbleSort(arr):
    res = arr.copy()
    for i in range(len(res) - 1, 0, -1):
        for j in range(0, i, 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res

def Merge(arr1, arr2):
    res = []
    cur1 = cur2 = 0
    while cur1 < len(arr1) and cur2 < len(arr2):
        if arr1[cur1] < arr2[cur2]:
            res.append(arr1[cur1])
            cur1 += 1
        else:
            res.append(arr2[cur2])
            cur2 += 1
    if cur1 ==len(arr1):
        while cur2 < len(arr2):
            res.append(arr2[cur2])
            cur2 += 1
    if cur2 ==len(arr2):
        while cur1 < len(arr1):
            res.append(arr1[cur1])
            cur1 += 1
    return res

def MergeSort(arr):
    if len(arr) == 1:
        return arr

    half = len(arr) // 2
    a = arr[:half]
    b = arr[half:]
    return Merge(MergeSort(a), MergeSort(b))

def ShellSort(arr):
    step = len(arr)//2
    while step > 0:
        for i in range(step, len(arr), 1):
            j = i
            delta = j - step
            while delta >= 0 and arr[delta] > arr[j]:
                arr[delta], arr[j] = arr[j], arr[delta]
                j = delta
                delta = j - step
        step //= 2
    return arr

def QuickSort(arr):
    if len(arr) < 2:
        return arr

    low, same, high = [], [], []    
    medium = arr[len(arr) // 2]

    for item in arr:
        if item < medium:
            low.append(item)
        elif item == medium:
            same.append(item)
        elif item > medium:
            high.append(item)            
    return QuickSort(low) + same + QuickSort(high)

print("go")
with open("plot.txt", "w") as file:
    random.seed()
    for size in range(100, 200, 10):
        sel = []
        ins = []
        bbl = []
        mer = []
        shl =[]
        qck = []


        for i in range(size):
            sel.append(random.random() * 1000000)
            ins.append(random.random() * 1000000)
            bbl.append(random.random() * 1000000)
            mer.append(random.random() * 1000000)
            shl.append(random.random() * 1000000)
            qck.append(random.random() * 1000000)

        start = time.process_time_ns()
        arr = SelectionSort(sel)
        tS = time.process_time_ns() - start

        start = time.process_time_ns()
        arr = InsertionSort(ins)
        tI = time.process_time_ns() - start

        start = time.process_time_ns()
        arr = BubbleSort(bbl)
        tB = time.process_time_ns() - start

        start = time.process_time_ns()
        arr = MergeSort(mer)
        tM = time.process_time_ns() - start

        start = time.process_time_ns()
        arr = ShellSort(shl)
        tSh = time.process_time_ns() - start

        start = time.process_time_ns()
        arr = QuickSort(qck)
        tQ = time.process_time_ns() - start

        string = str(size)+ "; " + str(tS)+ "; " + str(tI)+ "; " + str(tB)+ "; " + str(tM)+ "; " + str(tSh)+ "; " + str(tQ)
        file.write(string + '\n')
        print('Size ' + str(size) + " done")
            
print("done")