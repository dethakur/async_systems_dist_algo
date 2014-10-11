from Account import *
import random
class Accounts:
	accountMap = {};

	def __init__(self):
		self.accountMap = {}
	
	def isAccountPresent(accountNumber):
		if not accountNumber in accountMap:
			acc = Account(accountNumber);
			self.accountMap[accountNumber] = acc;


	def getAccountObject(accountNumber):
		isAccountPresent(accountNumber)
		acc = self.accountMap[accountNumber]
		return acc

	def withdrawMoney(accountNumber,amount):
		acc = getAccountObject(accountNumber)
		if(acc.getBalance() > amount):
			acc.withdrawMoney(amount)

		return acc.getBalance()

	def depositMoney(accountNumber,amount):
		acc = getAccountObject(accountNumber)
		acc.depositMoney(accountNumber)
		return acc.getBalance()

	def getBalance(accountNumber):
		acc = getAccountObject()
		return acc.getBalance()

