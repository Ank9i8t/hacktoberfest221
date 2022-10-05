A = []
n = int(input("Enter number of elements: "))

for i in range(n):
        elm = int(input("Enter the element: "))
        A.append(elm)
l = len(A)
i = 0
print(f"Old list Was {A}")
while i!=l:
	N = l-i-1
	for j in range(N):
		if A[j]>=A[j+1]:
			A[j],A[j+1]=A[j+1],A[j]
	i+=1
print(f"New list is {A}")
