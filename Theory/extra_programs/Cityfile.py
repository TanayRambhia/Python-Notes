f1=open("cities.txt","rt")
acity=open("start_with_a.txt","wt")
bcity=open("start_with_b.txt","wt")
# Numbers inside "numbers.dat" file are stored separated with space
city_list=f1.read().split() # splitting numbers separated with space
print(city_list)
# List comprehension
city_list_a=[c  for c in city_list if c[0]=='A' or c[0]=='a']
# OR filter with lambda
city_list_a=list(filter(lambda city : city[0]=='A' or city[0]=='a' ,city_list)) 


for c in city_list_a:
		acity.write(c) # type casting to string while using write()
		acity.write(" ")
# Similarly we can exract city starts with letter 'B' or 'b'