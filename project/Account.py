class Account:

	def __init__(self,accountNumber):
		self.accountNumber = accountNumber
		self.accountBalance = 0

	def depositMoney(self,amount):
		self.accountBalance = self.accountBalance + amount;

	def withdrawMoney(self,amount):
		self.accountBalance = self.accountBalance - amount;

	def getBalance(self):
		return self.accountBalance

	