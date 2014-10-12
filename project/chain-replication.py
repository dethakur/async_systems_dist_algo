
import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('query'), da.pat.FreePattern('accountNumber')])
PatternExpr_1 = da.pat.FreePattern('node')
PatternExpr_2 = da.pat.TuplePattern([da.pat.ConstantPattern('update'), da.pat.FreePattern('accountNumber'), da.pat.FreePattern('amount'), da.pat.FreePattern('updateType')])
PatternExpr_3 = da.pat.FreePattern('node')
PatternExpr_4 = da.pat.TuplePattern([da.pat.ConstantPattern('update'), da.pat.FreePattern('accountNumber'), da.pat.FreePattern('amount'), da.pat.FreePattern('updateType'), da.pat.FreePattern('clientNode')])
PatternExpr_5 = da.pat.FreePattern('node')
PatternExpr_6 = da.pat.TuplePattern([da.pat.ConstantPattern('balance'), da.pat.FreePattern('balance')])
PatternExpr_7 = da.pat.FreePattern('node')
PatternExpr_8 = da.pat.TuplePattern([da.pat.ConstantPattern('updateDone'), da.pat.FreePattern('balance')])
PatternExpr_9 = da.pat.FreePattern('node')
serverName = 'abcde'
import time

class Account():

    def __init__(self, accountNumber):
        self.accountNumber = accountNumber
        self.accountBalance = 0

    def depositMoney(self, amount):
        self.accountBalance = (self.accountBalance + amount)

    def withdrawMoney(self, amount):
        self.accountBalance = (self.accountBalance - amount)

    def getBalance(self):
        return self.accountBalance

class Accounts():

    def __init__(self):
        self.accountMap = {}

    def isAccountPresent(self, accountNumber):
        if (not (accountNumber in self.accountMap)):
            print('Account {} not present. Creating a new account. '.format(accountNumber))
            acc = Account(accountNumber)
            self.accountMap[accountNumber] = acc

    def setAccountMap(self, accountMap):
        self.accountMap = accountMap

    def getAccountObject(self, accountNumber):
        self.isAccountPresent(accountNumber)
        acc = self.accountMap[accountNumber]
        return acc

    def withdrawMoney(self, accountNumber, amount):
        acc = self.getAccountObject(accountNumber)
        if (acc.getBalance() > amount):
            acc.withdrawMoney(amount)
        print('Money {} withdrawn from account number {} '.format(amount, accountNumber))
        return acc.getBalance()

    def depositMoney(self, accountNumber, amount):
        acc = self.getAccountObject(accountNumber)
        acc.depositMoney(amount)
        balance = acc.getBalance()
        print('Money {} deposited - acc no {}. Balance is {} '.format(amount, accountNumber, balance))
        return balance

    def getBalance(self, accountNumber):
        acc = self.getAccountObject(accountNumber)
        return acc.getBalance()

class BankServer(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_BankServerReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=None, handlers=[self._BankServer_handler_0]), da.pat.EventPattern(da.pat.ReceivedEvent, '_BankServerReceivedEvent_1', PatternExpr_2, sources=[PatternExpr_3], destinations=None, timestamps=None, record_history=None, handlers=[self._BankServer_handler_1]), da.pat.EventPattern(da.pat.ReceivedEvent, '_BankServerReceivedEvent_2', PatternExpr_4, sources=[PatternExpr_5], destinations=None, timestamps=None, record_history=None, handlers=[self._BankServer_handler_2])])

    def main(self):
        _st_label_47 = 0
        while (_st_label_47 == 0):
            _st_label_47 += 1
            if False:
                _st_label_47 += 1
            else:
                super()._label('_st_label_47', block=True)
                _st_label_47 -= 1

    def setup(self, accounts, nextServer):
        self.accounts = accounts
        self.nextServer = nextServer
        pass

    def updateRequest(self, accountNumber, amount, clientNode, updateType):
        print('Deposit request received by the server')
        balance = 0
        if (updateType == 'deposit'):
            balance = self.depositMoney(accountNumber, amount)
        else:
            balance = self.withdrawMoney(accountNumber, amount)
        if (self.nextServer is None):
            node = clientNode
            self._send(('updateDone', balance), node)
        else:
            node = self.nextServer
            self._send(('update', accountNumber, amount, updateType, clientNode), node)

    def withdrawMoney(self, accountNumber, amount):
        return self.accounts.withdrawMoney(accountNumber, amount)

    def depositMoney(self, accountNumber, amount):
        return self.accounts.depositMoney(accountNumber, amount)

    def getBalance(self, accountNumber):
        return self.accounts.getBalance(accountNumber)

    def _BankServer_handler_0(self, accountNumber, node):
        balance = self.getBalance(accountNumber)
        self._send(('balance', balance), node)
    _BankServer_handler_0._labels = None
    _BankServer_handler_0._notlabels = None

    def _BankServer_handler_1(self, updateType, amount, accountNumber, node):
        self.updateRequest(accountNumber, amount, node, updateType)
    _BankServer_handler_1._labels = None
    _BankServer_handler_1._notlabels = None

    def _BankServer_handler_2(self, amount, accountNumber, node, clientNode, updateType):
        self.updateRequest(accountNumber, amount, clientNode, updateType)
    _BankServer_handler_2._labels = None
    _BankServer_handler_2._notlabels = None

class client(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_clientReceivedEvent_0', PatternExpr_6, sources=[PatternExpr_7], destinations=None, timestamps=None, record_history=None, handlers=[self._client_handler_3]), da.pat.EventPattern(da.pat.ReceivedEvent, '_clientReceivedEvent_1', PatternExpr_8, sources=[PatternExpr_9], destinations=None, timestamps=None, record_history=None, handlers=[self._client_handler_4])])

    def main(self):
        print('Client process started')
        self.updateMoney(12345, serverName, 1000, 'deposit')
        self.updateMoney(12345, serverName, 2000, 'deposit')
        self.updateMoney(12345, serverName, 3000, 'deposit')
        self.updateMoney(12345, serverName, 1500, 'withdraw')
        time.sleep(1)
        self.getBalance(12345, serverName)
        _st_label_98 = 0
        while (_st_label_98 == 0):
            _st_label_98 += 1
            if False:
                _st_label_98 += 1
            else:
                super()._label('_st_label_98', block=True)
                _st_label_98 -= 1

    def setup(self, head, tail, bankName):
        self.tail = tail
        self.head = head
        self.bankName = bankName
        if (not hasattr('self', 'bankServerMap')):
            self.bankServerMap = {}
        if (not (bankName in self.bankServerMap)):
            self.bankServerMap[bankName] = {}
            self.bankServerMap[bankName]['head'] = head
            self.bankServerMap[bankName]['tail'] = tail

    def updateMoney(self, accountNumber, bankName, amount, updateType):
        node = self.bankServerMap[bankName]['head']
        self._send(('update', accountNumber, amount, updateType), node)

    def getBalance(self, accountNumber, bankName):
        node = self.bankServerMap[bankName]['tail']
        self._send(('query', accountNumber), node)

    def _client_handler_3(self, balance, node):
        print('Balance Query Processed. Current balance = {} '.format(balance))
    _client_handler_3._labels = None
    _client_handler_3._notlabels = None

    def _client_handler_4(self, balance, node):
        print('Withdraw/Deposit Done. Final balance = {} '.format(balance))
    _client_handler_4._labels = None
    _client_handler_4._notlabels = None

def main():
    serverCount = 10
    serverList = []
    for index in range(serverCount):
        serverVar = da.api.new(BankServer, num=1)
        serverList.append(serverVar)
    for i in range((serverCount - 1)):
        el = serverList[i]
        nextEl = serverList[(i + 1)]
        da.api.setup(el, (Accounts(), nextEl))
    da.api.setup(serverList[(serverCount - 1)], (Accounts(), None))
    head = serverList[0]
    tail = serverList[(serverCount - 1)]
    print(serverList)
    for el in serverList:
        da.api.start(el)
    customer = da.api.new(client, num=1)
    da.api.setup(customer, (head, tail, serverName))
    da.api.start(customer)
    print('No Problem till here')
