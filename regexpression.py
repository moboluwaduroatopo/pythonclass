# regular expression
import re
from os.path import exists
# re.match(pattern, string, flags=0)
# re.search(patern, string, flags=0)

# line = "Cats are smarter than dogs"
# # \[
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

# if matchObj:
# 	print("matchObj.group() :", matchObj.group())
#    # print "matchObj.group() :", matchObj.group()
#    print ("matchObj.group(1) :", matchObj.group(1))
#    print ("matchObj.group(2) :", matchObj.group(2))
# else:
#    print ("No match!!")
# count =1
count = 2
content=[]
if exists('myfile.txt'):
	with open('myfile.txt') as infile:
		for line in infile:
			searchobj=re.search(r'\[', line, re.M|re.I)
			if searchobj:
				infile2=line
				splitobj=infile2.split(' ', 2)
				# print(splitobj)
				code=splitobj[0]+splitobj[1]
				reminder=splitobj[2].split('[')
				title=reminder[0]
				unit=reminder[1].split(']')
				unit=unit[0]
				print(code, title, unit)
			if not searchobj:
				content.append(line)
				if line.startswith('('+str(count)+')'):
					break
				descript=' '.join(content)	
				print(descript)
			count +=1	

