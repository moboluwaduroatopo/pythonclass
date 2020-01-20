
# how to show text in the file 
# myfile =open("myfile.txt", "r")
# # with open("myfile.txt") as myfile2:
# print(myfile.read())
# print(myfile.readline())
# for x in myfile:
# 	print(x)
# myfile.close()

# how to add text to my file
# with open("myfile.txt","a") as myfile:
# 	myfile.write("i just added a new text cxvmmcx again")
# 	print("write successful")

# how to create newfile and write to it
# with open("newfile.txt","a") as myfile:
# 	myfile.write("i just create newfile and write to it")
# 	print("write successful")

# colorchooser

# how to delete file
import os
# if os.path.exists("index.html"):
if os.path.exists("folder"):
	# os.remove("index.html")
	os.rmdir("folder")
	print("file removed successful")

else:
	print("file doesn't exists")
