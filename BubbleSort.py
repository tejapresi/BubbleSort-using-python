#taking input for the integer array
A = list(map(int,input().split()))

#loop_pass variable is used for finding number of passes
loop_pass = 1

#iterating loop starting index to second last index of array
for i in range(0,len(A)-1):

	#iterating nested loop from 0 to len(A)-i-1
	for j in range(0,len(A)-i-1):
		
		#if the value present in current index is greater than value present in the next index
		if A[j]>A[j+1]:
			#swap those values in the array
			A[j+1],A[j] = A[j],A[j+1]

	#Printing the array in each pass
	print(f"Pass {loop_pass}: {A}")

	#incrementing loop_pass value
	loop_pass += 1

#printing the sorted array
print("Sorted array: ",A)