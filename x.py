
def sortList(L):
     for i in range(len(L)):
          for j in range(i, len(L)):
               if L[i] > L[j]:
                    temp = L[i]
                    L[i] = L[j]
                    L[j] = temp
          return L
# Test Cases
print(sortList([1,2,3,4,5]))
print(sortList([5,4,3,2,1]))
print(sortList([4,2,5,1,3]))