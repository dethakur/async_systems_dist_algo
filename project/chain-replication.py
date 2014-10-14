
import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('query'), da.pat.FreePattern('requestId'), da.pat.FreePattern('accountNumber')])
PatternExpr_1 = da.pat.FreePattern('node')
PatternExpr_2 = da.pat.TuplePattern([da.pat.ConstantPattern('update'), da.pat.FreePattern('requestId'), da.pat.FreePattern('accountNumber'), da.pat.FreePattern('amount'), da.pat.FreePattern('updateType')])
PatternExpr_3 = da.pat.FreePattern('node')
PatternExpr_4 = da.pat.TuplePattern([da.pat.ConstantPattern('update'), da.pat.FreePattern('requestId'), da.pat.FreePattern('accountNumber'), da.pat.FreePattern('amount'), da.pat.FreePattern('updateType'), da.pat.FreePattern('clientNode')])
PatternExpr_5 = da.pat.FreePattern('node')
PatternExpr_6 = da.pat.TuplePattern([da.pat.ConstantPattern('balance'), da.pat.FreePattern('requestId'), da.pat.FreePattern('message'), da.pat.FreePattern('balance')])
PatternExpr_7 = da.pat.FreePattern('node')
PatternExpr_8 = da.pat.TuplePattern([da.pat.ConstantPattern('updateDone'), da.pat.FreePattern('requestId'), da.pat.FreePattern('accountNumber'), da.pat.FreePattern('message'), da.pat.FreePattern('balance')])
PatternExpr_9 = da.pat.FreePattern('node')
import json
import time
from threading import Timer
from random import randint
import sys

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
        return acc.getBalance()

    def depositMoney(self, accountNumber, amount):
        acc = self.getAccountObject(accountNumber)
        acc.depositMoney(amount)
        balance = acc.getBalance()
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
        self.requestHistory = {}

    def updateRequest(self, requestId, accountNumber, amount, clientNode, updateType):
        balance = 0
        message = 'Processed'
        balance = self.getBalance(accountNumber)
        duplicate = False
        isInconsistent = False
        if (((requestId + str(accountNumber)) + updateType) in self.requestHistory):
            duplicate = True
        if ((requestId + str(accountNumber)) in self.requestHistory):
            transType = self.requestHistory[(requestId + str(accountNumber))]
            if (not (transType == updateType)):
                isInconsistent = True
        if ((not duplicate) and (not isInconsistent)):
            if (updateType == 'deposit'):
                balance = self.depositMoney(accountNumber, amount)
            elif (balance > amount):
                balance = self.withdrawMoney(accountNumber, amount)
            else:
                message = 'inSufficientFund'
            self.requestHistory[((requestId + str(accountNumber)) + updateType)] = (requestId, accountNumber, message, balance)
            self.requestHistory[(requestId + str(accountNumber))] = updateType
        if duplicate:
            el = self.requestHistory[((requestId + str(accountNumber)) + updateType)]
            balance = el[3]
            message = el[2]
        if isInconsistent:
            message = 'InconsistentWithHistory'
            balance = self.getBalance(accountNumber)
        if (self.nextServer is None):
            node = clientNode
            self.output('[Server] Processed by all the nodes. Sending the response back from Tail ({},{},{},{}) for transaction Type = {}'.format(requestId, accountNumber, message, balance, updateType))
            self._send(('updateDone', requestId, accountNumber, message, balance), node)
        else:
            node = self.nextServer
            self._send(('update', requestId, accountNumber, amount, updateType, clientNode), node)

    def withdrawMoney(self, accountNumber, amount):
        return self.accounts.withdrawMoney(accountNumber, amount)

    def depositMoney(self, accountNumber, amount):
        return self.accounts.depositMoney(accountNumber, amount)

    def getBalance(self, accountNumber):
        return self.accounts.getBalance(accountNumber)

    def _BankServer_handler_0(self, accountNumber, requestId, node):
        balance = self.getBalance(accountNumber)
        message = ''
        if (not (requestId in self.requestHistory)):
            self.requestHistory[requestId] = balance
            message = 'Processed'
        else:
            balance = self.requestHistory[requestId]
            message = 'InconsistentWithHistory'
        self.output('[Server] Processed by all the nodes. Sending the response back from Tail ({},{},{},{}) for transaction Type = getBalance'.format(requestId, accountNumber, message, balance))
        self._send(('balance', requestId, message, balance), node)
    _BankServer_handler_0._labels = None
    _BankServer_handler_0._notlabels = None

    def _BankServer_handler_1(self, updateType, amount, accountNumber, requestId, node):
        self.updateRequest(requestId, accountNumber, amount, node, updateType)
    _BankServer_handler_1._labels = None
    _BankServer_handler_1._notlabels = None

    def _BankServer_handler_2(self, amount, updateType, clientNode, requestId, node, accountNumber):
        self.updateRequest(requestId, accountNumber, amount, clientNode, updateType)
    _BankServer_handler_2._labels = None
    _BankServer_handler_2._notlabels = None

class client(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_clientReceivedEvent_0', PatternExpr_6, sources=[PatternExpr_7], destinations=None, timestamps=None, record_history=None, handlers=[self._client_handler_3]), da.pat.EventPattern(da.pat.ReceivedEvent, '_clientReceivedEvent_1', PatternExpr_8, sources=[PatternExpr_9], destinations=None, timestamps=None, record_history=None, handlers=[self._client_handler_4])])

    def main(self):
        randomOp = ['deposit', 'getBalance', 'withdraw']
        for el in self.operationArr:
            transType = (el['type'] if (not (el['type'] == 'random')) else randomOp[randint(0, 2)])
            accNumber = (el['accountNumber'] if isinstance(el['accountNumber'], int) else randint(1, 9))
            transId = (el['request_id'] if isinstance(el['request_id'], int) else randint(1, 9))
            clientId = str(self.id).split(',')[1].strip()
            requestId = ((((self.bankName + '.') + str(transId)) + '.') + clientId)
            self.output('[Client] Sending to Server. Request Id = {} and transaction type = {}'.format(requestId, transType))
            if (transType == 'getBalance'):
                self.getBalance(requestId, accNumber)
            else:
                amount = (el['amount'] if isinstance(el['amount'], int) else randint(1, 9))
                self.updateMoney(requestId, accNumber, amount, transType)
        _st_label_132 = 0
        while (_st_label_132 == 0):
            _st_label_132 += 1
            if False:
                _st_label_132 += 1
            else:
                super()._label('_st_label_132', block=True)
                _st_label_132 -= 1

    def setup(self, head, tail, operationArr, bankName):
        self.tail = tail
        self.operationArr = operationArr
        self.bankName = bankName
        self.head = head
        if (not hasattr('self', 'bankServerMap')):
            self.bankServerMap = {}
        if (not (bankName in self.bankServerMap)):
            self.bankServerMap[bankName] = {}
            self.bankServerMap[bankName]['head'] = head
            self.bankServerMap[bankName]['tail'] = tail

    def updateMoney(self, requestId, accountNumber, amount, updateType):
        node = self.bankServerMap[self.bankName]['head']
        self._send(('update', requestId, accountNumber, amount, updateType), node)

    def getBalance(self, requestId, accountNumber):
        node = self.bankServerMap[self.bankName]['tail']
        self._send(('query', requestId, accountNumber), node)

    def _client_handler_3(self, message, node, requestId, balance):
        self.output('[Client] Balance Query Processed. Final response = ({},{},{}) '.format(requestId, message, balance))
    _client_handler_3._labels = None
    _client_handler_3._notlabels = None

    def _client_handler_4(self, accountNumber, requestId, node, balance, message):
        self.output('[Client] Withdraw/Deposit Processed. Final response = ({},{},{},{}) '.format(requestId, accountNumber, message, balance))
    _client_handler_4._labels = None
    _client_handler_4._notlabels = None

def main():
    path = 'project/config.json'
    if (len(sys.argv) > 1):
        path = sys.argv[1]
    variable = open(path)
    x = variable.read()
    sample = json.loads(x)
    serverList = []
    clientList = []
    timerList = []
    for el in sample['config']:
        tempServerList = []
        size = int(el['length_of_chain'])
        bankName = el['bank_name']
        startUpDelay = 0
        if ('startUpDelay' in el):
            startUpDelay = el['startUpDelay']
        for index in range(size):
            serverVar = da.api.new(BankServer, num=1)
            tempServerList.append(serverVar)
            if (startUpDelay == 0):
                serverList.append(serverVar)
            else:
                timers = Timer(startUpDelay, da.api.start, serverVar)
                timerList.append(timers)
        for i in range((size - 1)):
            currentServer = tempServerList[i]
            nextServer = tempServerList[(i + 1)]
            da.api.setup(currentServer, (Accounts(), nextServer))
        da.api.setup(tempServerList[(size - 1)], (Accounts(), None))
        head = tempServerList[0]
        tail = tempServerList[(size - 1)]
        for clientEl in el['clients']:
            operationArr = clientEl['operation']
            customer = da.api.new(client, num=1)
            da.api.setup(customer, (head, tail, operationArr, bankName))
            if (startUpDelay == 0):
                clientList.append(customer)
            else:
                timers = Timer(startUpDelay, da.api.start, customer)
                timerList.append(timers)
    for el in serverList:
        da.api.start(el)
    for el in clientList:
        da.api.start(el)
    for el in timerList:
        el.start()
