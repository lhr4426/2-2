# 1번 정답

def heapify(arr, i, n) :
  l = i * 2
  r = i * 2 + 1
  ci = i
  if l <= n and arr[ci] < arr[l] :
    ci = l
  if r <= n and arr[ci] < arr[r] :
    ci = r
  if ci != i :
    arr[i], arr[ci] = arr[ci], arr[i]
    heapify(arr, ci, n)

def heap_sort(arr):
  n = len(arr)
  arr = [0] + arr
  
  while n>0:
    for i in range(n//2, 0, -1) :
        heapify(arr, i, n)
    arr[1], arr[n] = arr[n], arr[1]  
    n -= 1

  return arr[1:]

a = [7,9,4,8,6,3,5]
print(a)
print(heap_sort(a))