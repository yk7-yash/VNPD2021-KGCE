def Arraystring(string, n):
    for i in range(n):
        print(string[i], end = " ")
        
def sort(s, n):
    for i in range(1, n):
        temp = s[i]
 
        # Insert s[j] at its correct position
        j = i - 1
        while j >= 0 and len(temp) < len(s[j]):
            s[j + 1] = s[j]
            j -= 1
 
        s[j + 1] = temp
 
# Driver code
if __name__ == "__main__":

    n = int(input())
    
    arr = input()
    arr = arr.split()
    if (n>0):
      sort(arr,n)
      Arraystring(arr,n)
      print(arr[0])
      
    else:
      print("Invalid Input")
