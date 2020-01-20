
if self.balance <= self.withdraw:
			showinfo("Warming","Insufficient balance")
			print('Insufficient balance')
		else:
			self.id=self.res[0] || self.mydata
			self.balance=self.amount[]
			self.balance=self.balance - self.withdraw
			self.result=round(self.withdraw,2)
			print(self.balance)
			self.sql = "UPDATE account_info SET amount = %s WHERE customer_id = %s"
			self.val = (self.balance,self.id)
			self.mycursor.execute(self.sql, self.val)
			self.mycon.commit()