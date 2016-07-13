sum = 0
arr = [1,2]

# recursive function that takes a num parameter 
# in this case the third Fib value is inputted
# first to seed the Fibonacci sequence.
def recursiveFib(num) : 
	if(arr[-1] < 4000000) :
		arr.append(num)
		recursiveFib(arr[-2]+arr[-1])

recursiveFib(3)

# find sum of even numbers
for num in arr :
	if(num%2 == 0) :
		sum += num

print "Sum value:"
print sum