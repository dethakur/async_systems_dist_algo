
import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('Ping')])
PatternExpr_1 = da.pat.FreePattern('p2')
PatternExpr_3 = da.pat.TuplePattern([da.pat.ConstantPattern('Ping')])
PatternExpr_4 = da.pat.FreePattern('p2')
PatternExpr_5 = da.pat.TuplePattern([da.pat.ConstantPattern('Pong')])
PatternExpr_6 = da.pat.FreePattern('rclk')
PatternExpr_8 = da.pat.TuplePattern([da.pat.ConstantPattern('Ponged')])
PatternExpr_9 = da.pat.FreePattern('rclk')
PatternExpr_11 = da.pat.TuplePattern([da.pat.ConstantPattern('Pong')])
import sys
import inspect

class Pong(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._PongReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PongReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PongReceivedEvent_1', PatternExpr_3, sources=[PatternExpr_4], destinations=None, timestamps=None, record_history=None, handlers=[self._Pong_handler_0])])

    def main(self):
        _st_label_8 = 0
        while (_st_label_8 == 0):
            _st_label_8 += 1
            if (len([p2 for (_, (_, _, p2), (_ConstantPattern10_,)) in self._PongReceivedEvent_0 if (_ConstantPattern10_ == 'Ping')]) == self.total_pings):
                _st_label_8 += 1
            else:
                super()._label('_st_label_8', block=True)
                _st_label_8 -= 1

    def setup(self, total_pings, word):
        self.word = word
        self.total_pings = total_pings
        pass

    def _Pong_handler_0(self, p2):
        print('Values on receiver are', inspect.getargspec(receive))
        self.output('Pinged')
        self._send(('Pong',), p2)
        self._send(('Ponged',), p2)
    _Pong_handler_0._labels = None
    _Pong_handler_0._notlabels = None

class Ping(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._PingReceivedEvent_0 = []
        self._PingReceivedEvent_1 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PingReceivedEvent_0', PatternExpr_5, sources=None, destinations=None, timestamps=[PatternExpr_6], record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PingReceivedEvent_1', PatternExpr_8, sources=None, destinations=None, timestamps=[PatternExpr_9], record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PingReceivedEvent_2', PatternExpr_11, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Ping_handler_1])])

    def main(self):
        print('Value of object self in Ping ', self)
        for i in range(self.nrounds):
            clk = self.logical_clock()
            self._send(('Ping',), self.p2)
            print('What is clk = ', clk)
            rclk = None

            def ExistentialOpExpr_0():
                nonlocal rclk
                for (_, (rclk, _, _), (_ConstantPattern24_,)) in self._PingReceivedEvent_0:
                    if (_ConstantPattern24_ == 'Pong'):
                        if (rclk > clk):
                            return True
                return False
            _st_label_23 = 0
            while (_st_label_23 == 0):
                _st_label_23 += 1
                if ExistentialOpExpr_0():
                    _st_label_23 += 1
                else:
                    super()._label('_st_label_23', block=True)
                    _st_label_23 -= 1
            else:
                if (_st_label_23 != 2):
                    continue
            if (_st_label_23 != 2):
                break
            rclk = None

            def ExistentialOpExpr_1():
                nonlocal rclk
                for (_, (rclk, _, _), (_ConstantPattern35_,)) in self._PingReceivedEvent_1:
                    if (_ConstantPattern35_ == 'Ponged'):
                        if (rclk > clk):
                            return True
                return False
            _st_label_24 = 0
            while (_st_label_24 == 0):
                _st_label_24 += 1
                if ExistentialOpExpr_1():
                    _st_label_24 += 1
                else:
                    super()._label('_st_label_24', block=True)
                    _st_label_24 -= 1
            else:
                if (_st_label_24 != 2):
                    continue
            if (_st_label_24 != 2):
                break
            print('What is rclk = ', rclk)

    def setup(self, p2, nrounds):
        self.p2 = p2
        self.nrounds = nrounds
        pass

    def _Ping_handler_1(self):
        self.output('Pong.')
    _Ping_handler_1._labels = None
    _Ping_handler_1._notlabels = None

def main():
    nrounds = (int(sys.argv[1]) if (len(sys.argv) > 1) else 3)
    npings = (int(sys.argv[2]) if (len(sys.argv) > 2) else 3)
    da.api.config(clock='Lamport')
    print('Is setup called 1 ?')
    pong = da.api.new(Pong, [(nrounds * npings), 'sexy'], num=1)
    print('Is setup called 2?')
    ping = da.api.new(Ping, [pong, nrounds], num=npings)
    print('Is setup called 3?')
    print('Is setup called 4?')
    da.api.start(pong)
    da.api.start(ping)
