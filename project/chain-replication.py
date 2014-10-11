
import da
from BankChain import *
from BankServer import *

class server(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._events.extend([])

    def main(self):
        pass

    def setup(self):
        _st_label_6 = 0
        while (_st_label_6 == 0):
            _st_label_6 += 1
            if False:
                _st_label_6 += 1
            else:
                super()._label('_st_label_6', block=True)
                _st_label_6 -= 1
        pass

class client(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._events.extend([])

    def main(self):
        pass

    def setup(self):
        _st_label_12 = 0
        while (_st_label_12 == 0):
            _st_label_12 += 1
            if False:
                _st_label_12 += 1
            else:
                super()._label('_st_label_12', block=True)
                _st_label_12 -= 1
        pass

def main():
    serverCount = 10
    serverList = []
    for index in range(0, 10):
        serverVar = da.api.new(server, num=1)
        serverList.append(serverVar)
    print(serverList)
    bankChain = BankChain()
    bankChain.createChain(serverList, 'abcde')
    allServers = bankChain.getAllServers('abcde')
    print('No Problem till here')
