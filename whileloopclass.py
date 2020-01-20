#3rd class while loop
i=1
while i<12:
	r=i*1
	print("1 X",i,"=",r)
	i+=1;
else:
	print("done")
#function

c = "Ogbomoso"
d= "Ilorin"
def okada(current=c,destination=d):
  print("I am going from ",current,"to",destination)

okada("SQI","Lactech")
okada("Home","SQI")
okada("Hostel","Ibada")
okada()