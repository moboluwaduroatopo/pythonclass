# input("Enter a USSD")
print("Enter a USSD")
a = input()
USSD="1.Account info 2.Tariff plan migration 3.Data Service 4.Roaming& INT'l offers 5.My Services"
if a=="*123#":
	print(USSD)
	b=input()
	if b=="1" or b=="2" or b=="3" or b=="4" or b=="5":
		print('success')
	else:
		print ('not')
else:
  print("wrong USSD")	