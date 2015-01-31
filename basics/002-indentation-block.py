# no delimiters for statements blocks
# blocks are delimited based on indentation level
# if block is required statement ends with colon (example: while)
i = 0
total = 0
while i < 30:
	total = total+365
	i = i+1
	print "year ", i, ": acumulated days ", total

print "this line is out of block. TOTAL DAYS: ", total

	
	
