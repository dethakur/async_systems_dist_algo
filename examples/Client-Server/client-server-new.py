
import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('update')])
PatternExpr_1 = da.pat.FreePattern('head')
PatternExpr_2 = da.pat.TuplePattern([da.pat.ConstantPattern('updateChain'), da.pat.FreePattern('child')])
PatternExpr_3 = da.pat.FreePattern('head')
PatternExpr_4 = da.pat.TuplePattern([da.pat.ConstantPattern('query')])
PatternExpr_5 = da.pat.FreePattern('tail')
PatternExpr_6 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_7 = da.pat.FreePattern('child')
PatternExpr_8 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_9 = da.pat.FreePattern('tail')
import sys

class server(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_serverReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=None, handlers=[self._server_handler_0]), da.pat.EventPattern(da.pat.ReceivedEvent, '_serverReceivedEvent_1', PatternExpr_2, sources=[PatternExpr_3], destinations=None, timestamps=None, record_history=None, handlers=[self._server_handler_1]), da.pat.EventPattern(da.pat.ReceivedEvent, '_serverReceivedEvent_2', PatternExpr_4, sources=[PatternExpr_5], destinations=None, timestamps=None, record_history=None, handlers=[self._server_handler_2])])

    def main(self):
        _st_label_7 = 0
        while (_st_label_7 == 0):
            _st_label_7 += 1
            if False:
                _st_label_7 += 1
            else:
                super()._label('_st_label_7', block=True)
                _st_label_7 -= 1

    def setup(self, nextServer):
        self.nextServer = nextServer
        pass

    def _server_handler_0(self, head):
        print('Update message received by head = ', self)
        child = head
        head = self.nextServer
        self._send(('updateChain', child), head)
    _server_handler_0._labels = None
    _server_handler_0._notlabels = None

    def _server_handler_1(self, child, head):
        print('-----------------------------------')
        print('Updating Chain = ', self)
        print('-----------------------------------')
        if hasattr(self, 'nextServer'):
            head = self.nextServer
            self._send(('updateChain', child), head)
        else:
            print('All Servers updated. Now request received by Tail. Sending response back to client ', self)
            self._send(('done',), child)
    _server_handler_1._labels = None
    _server_handler_1._notlabels = None

    def _server_handler_2(self, tail):
        if hasattr(self, 'nextServer'):
            tail = self.nextServer
            self._send(('done',), tail)
        self.output('Query message received by tail')
    _server_handler_2._labels = None
    _server_handler_2._notlabels = None

class client(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_clientReceivedEvent_0', PatternExpr_6, sources=[PatternExpr_7], destinations=None, timestamps=None, record_history=None, handlers=[self._client_handler_3]), da.pat.EventPattern(da.pat.ReceivedEvent, '_clientReceivedEvent_1', PatternExpr_8, sources=[PatternExpr_9], destinations=None, timestamps=None, record_history=None, handlers=[self._client_handler_4])])

    def main(self):
        self.output('Client sending update message')
        print('Client calling update to ', self.head)
        self._send(('update',), self.head)
        _st_label_34 = 0
        while (_st_label_34 == 0):
            _st_label_34 += 1
            if False:
                _st_label_34 += 1
            else:
                super()._label('_st_label_34', block=True)
                _st_label_34 -= 1

    def setup(self, head, tail):
        self.tail = tail
        self.head = head
        pass

    def _client_handler_3(self, child):
        self.output('Update Finished. Message Received by the client')
    _client_handler_3._labels = None
    _client_handler_3._notlabels = None

    def _client_handler_4(self, tail):
        self.output('Query Finished. Message Received by the client')
    _client_handler_4._labels = None
    _client_handler_4._notlabels = None

def main():
    da.api.config(clock='Lamport')
    chainLength = 10
    serverList = []
    for index in range(0, 10):
        serverVar = da.api.new(server, num=1)
        serverList.append(serverVar)
    print(serverList)
    for index in range(0, 9):
        currServer = serverList[index]
        nextServer = serverList[(index + 1)]
        da.api.setup(currServer, nextServer)
    for index in range(0, 10):
        da.api.start(serverList[index])
    head = serverList[0]
    tail = serverList[9]
    customer = da.api.new(client, num=1)
    da.api.setup(customer, (head, tail))
    da.api.start(customer)
