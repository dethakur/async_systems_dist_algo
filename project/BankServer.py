from Accounts import *
class BankServer:

	accounts = None
	processObj = None
	nextServer = None;

	def __init__(self,processObj):
		accounts = Accounts()
		self.processObj = processObj

	def withdrawMoney(self,accountNumber,amount):
		accounts.withdrawMoney(accountNumber,amount)

	def depositMoney(self,accountNumber,amount):
		accounts.depositMoney(accountNumber,amount)

	def getBalance(self,accountNumber):
		accounts.getBalance(accountNumber)

	def getProcessObject(self):
		return processObj

	def addNextServer(self,nextServer):
		self.nextServer = nextServer
