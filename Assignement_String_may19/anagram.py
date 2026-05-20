s1 =  input("Enter 1 ")
s2 = input("Enter 2 ")

if len(s1)!=len(s2):
	print("String are not anagram")

else:
	visited=[]
	flag =1
	i= 0
	
	while i<len(s1):
		ch=s[i]
		
		if ch not in visited:
		
			c1=0
			c2=0
			
			j= 0
			while j<len(s1):
				
				if s1[j] ==ch:
					c1 = c1+1
			j = j+1
			
			j= 0
			while j<len(s2):
				
				if s2[j] ==ch:
					c1 = c1+1
			j = j+1
			
		if c1!=c2:
			flag = 0
			break
		visited.append(ch)
		
		i+=1
		
		
		if flag == 1:
			print("Anagram")
		
		else:
			print("not anagram")