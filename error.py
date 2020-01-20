
try:
	file=open('myfile1.txt')
	file.write('this is a text example')
	print('file write succesfully')
# except nosuchfileordirectory:
# 	print('file does not exit')
except Exception as r:
	print('no permission to write to the file')	
finally:
	print('Thank u')