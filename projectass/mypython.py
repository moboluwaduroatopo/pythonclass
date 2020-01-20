print("ENTER USSD")


options="""
1. Open Account
2. Upgrade/Migrate
3. Balance
4. Transfer
5. Recharge
6. Exit"""
BankList="""
Select the Bank you wish to Transfer to:
1. Access Bank
2. Fidelity Bank
3. Guarantee Trust Bank
4. Heritage Bank
5. Polaris Bank
6. Stanbic IBTC
7. Unity Bank
8. Wema Bank
0. To go Back"""

#exit="""sys.exit"""*
restart='0'

USSD=input()
if(USSD=="*833#"):
	while restart not in ('1'):
		print("options")
		print(options)
		print("select an option")


		choice=input()
		if(choice=="1"):
			print("Please Enter Your BVN")
			print("Reply 0 if you don't have a BVN")
			returncode=input()
			if(returncode=="0"):
				print("Kindly visit our nearest branch to register for your BVN")
				print("For more info call: +2348138633842. Thank you.")
				break
			else:
			 	print("The BVN you entered is incorrect, kindly visit the nearest branch to resolve this issue. Thank you.")
			 	break

		if(choice=="2"):
			print("This feature will soon be available. Thank you.")
			break
		if(choice=="3"):
			print("Your Balance is: N000,000.00")
			print("Thank you.")
			break
		if(choice=="4"):
			print("Enter 's' for Self and 'o' for Others")
			returncode=input()
			if (returncode=="o"):
				print(BankList)
				returncode=input()
				if (returncode=="1"):
					# print("Enter Third Party Account Number:")
					# print("Reply 0 to Start-Over")
					Accountnum=input('Enter Third Party Account Number: ')
					Amounttra=input('Enter Amount to Transfer: ')
					print('you Transfer #', Amounttra ,'to', Accountnum )
					print("Transfer to Third-Party was Successful")
					print("Thank you.")

					break
				if (returncode=="0"):
					pass
			else:
				Accountnum=input('Enter Third Party Account Number: ')
				Amounttra=input('Enter Amount to Transfer: ')
				print('you Transfer #', Amounttra ,'to', Accountnum )
				print("Transfer was Successful")
				print("Thank you.")
				# print('s')		
					# restart=('0')
					# print("enter")
		if(choice=="5"):
			print("Enter 1 for SELF and 2 for THIRD-PARTY")
			print("Reply 0 to Start Over")
			returncode=input()
			if (returncode=="1"):
				print("Enter Preferred Amount")
				# print("Reply 0 to Start Over")
				Recharge=input()
				print(Recharge, "was Recharge Successfully to u. Thank You.")
				break
			if (returncode=="0"):
				pass	
			# if (returncode=="0"):
			# 	print(options)
			# else:
			# 	print("Your SELF Recharge was done Successfully. Thank You.")
			if returncode=="2":
				# print("Enter THIRD-PARTY mobile number")
				# print("Reply 0 to Start Over")
				mobnumber=input("Enter THIRD-PARTY mobile number: ")
				Amount=input("Enter Preffered Amount: ")
				print(Amount, "was Rechard successful to", mobnumber,".", "Thank You.")
				break
			
			# else:
			# 	print("Enter Preffered Amount")
			# 	print("Reply 0 to Start Over")
			# 	returncode=input()
			# 	if (returncode=="0"):
			# 		print(options)
			# 	else:
			# 		print("Rechard for THIRD-PARTY was successful. Thank You.")
		if(choice=="6"):
			print("Thank You")
			break			
					# choice=input()
					# else:
					# 	print("Enter Amount to Transfer")
					# 		# print("Reply 0 to Start-Over")
					# 	returncode=input()
					# 	if (returncode=="0"):
					# 		restart=('0')
					# 			# print(options)
					# 		choice=input()
					# 	else:
					# 		print("Transfer to Third-Party was Successful")
					# 		break

# 		else:
# 			print("Enter Third Party Account Number:")
# 			print("Reply 0 to Start-Over")
# 			returncode=input()
# 			if (returncode=="0"):
# 				print(options)
# 			else:
# 				print("Enter Amount to Transfer:")
# 				print("Reply 0 to Start-Over")
# 				returncode=input()
# 				if (returncode=="0"):
# 					print(options)
# 				else:
# 					print("Transfer to Third-Party was Successful")
# 	else:
# 		print("Enter your Account Number:")
# 		print("Reply 0 to Start-Over")
# 		returncode=input()
# 		if (returncode=="0"):
# 			print(options)
# 			print("select an option")
# 		else:
# 			print("Enter Amount to Transfer:")
# 			print("Reply 0 to Start-Over")
# 			returncode=input()
# 			if (returncode=="0"):
# 				print(options)
# 				print("select an option")
# 			else:
# 				print("Transfer Done Successfully. Thank you.")


# elif(choice=="6"):
#     print("Thank You")
else:
	print("Unrecognised USSD; Kindly input a correct one. Thank you.")