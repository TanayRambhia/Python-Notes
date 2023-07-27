f1=open("numbers.dat","rt")
pos=open("positive.dat","wt")
neg=open("negative.dat","wt")
# Numbers inside "numbers.dat" file are stored separated with space
char_list=f1.read().split() # splitting numbers separated with space
num_list=list(map(lambda e : int(e),char_list)) # Coverting chars to integers
print(num_list)
for num in num_list:
	if num>0:
		pos.write(str(num)) # type casting to string while writing data to file
		pos.write(" ")
	elif num<0:
		neg.write(str(num))
		neg.write(" ")