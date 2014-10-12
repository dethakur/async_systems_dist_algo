from Account import *
import random
class Accounts:

	def __init__(self):
		self.accountMap = {}
	
	def isAccountPresent(self,accountNumber):
		print("account map ",self.accountMap)
		if not accountNumber in self.accountMap:
			print('Account {} not present. Creating a new account. '.format(accountNumber))
			acc = Account(accountNumber);
			self.accountMap[accountNumber] = acc;

		print("account map ",self.accountMap)

	def setAccountMap(self,accountMap):
		self.accountMap = accountMap

	def getAccountObject(self,accountNumber):
		self.isAccountPresent(accountNumber)
		acc = self.accountMap[accountNumber]
		return acc

	def withdrawMoney(self,accountNumber,amount):
		acc = self.getAccountObject(accountNumber)
		if(acc.getBalance() > amount):
			acc.withdrawMoney(amount)

		print('Money {} withdrawn from account number {} '.format(amount,accountNumber))

		return acc.getBalance()

	def depositMoney(self,accountNumber,amount):
		acc = self.getAccountObject(accountNumber)
		acc.depositMoney(amount)
		balance =  acc.getBalance()
		print('Money {} deposited in account number {}. Balance is {} '.format(amount,accountNumber,balance))
		return balance

	def getAccMap(self):
		return self.accountMap
