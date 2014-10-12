from Accounts import * 
class BankServer:

	def __init__(self,processObj):
		#print('new bank server object created')
		self.accounts = Accounts()
		self.processObj = processObj
		self.nextServer = None

	def withdrawMoney(self,accountNumber,amount):
		self.accounts.withdrawMoney(accountNumber,amount)

	def depositMoney(self,accountNumber,amount):
		self.accounts.depositMoney(accountNumber,amount)
		#print('head server map = ',self.getAccountMap())

	def getBalance(self,accountNumber):
		self.accounts.getBalance(accountNumber)

	def getProcessObject(self):
		#print('type of process object ',self.processObj)
		return self.processObj

	def addNextServer(self,nextServer):
		self.nextServer = nextServer

	def getNextServer(self):
		return self.nextServer 

	def getAccountMap(self):
		return self.accounts.getAccMap()
