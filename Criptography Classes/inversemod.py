def inversemodfind(number,m):
	# find the number that gives 1 mod (m)
	sol=int()
	while sol*number%m != 1:
		sol=sol+1
	print(sol)




inversemodfind(2,6)