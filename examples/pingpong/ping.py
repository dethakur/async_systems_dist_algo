
import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('Ping')])
PatternExpr_1 = da.pat.FreePattern('p')
PatternExpr_3 = da.pat.TuplePattern([da.pat.ConstantPattern('Ping')])
PatternExpr_4 = da.pat.FreePattern('p')
PatternExpr_6 = da.pat.TuplePattern([da.pat.ConstantPattern('Ping')])
PatternExpr_7 = da.pat.FreePattern('p')
PatternExpr_8 = da.pat.TuplePattern([da.pat.ConstantPattern('Pong')])
PatternExpr_9 = da.pat.FreePattern('rclk')
PatternExpr_11 = da.pat.TuplePattern([da.pat.ConstantPattern('Pong')])
import sys

class Pong(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._PongReceivedEvent_0 = []
        self._PongReceivedEvent_1 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PongReceivedEvent_0', PatternExpr_0, sources=[PatternExpr_1], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PongReceivedEvent_1', PatternExpr_3, sources=[PatternExpr_4], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PongReceivedEvent_2', PatternExpr_6, sources=[PatternExpr_7], destinations=None, timestamps=None, record_history=None, handlers=[self._Pong_handler_0])])

    def main(self):
        _st_label_7 = 0
        while (_st_label_7 == 0):
            _st_label_7 += 1
            if (len([p for (_, (_, _, p), (_ConstantPattern10_,)) in self._PongReceivedEvent_0 if (_ConstantPattern10_ == 'Ping')]) == self.total_pings):
                _st_label_7 += 1
            else:
                super()._label('_st_label_7', block=True)
                _st_label_7 -= 1
        print('What does this list have ?', [p for (_, (_, _, p), (_ConstantPattern21_,)) in self._PongReceivedEvent_1 if (_ConstantPattern21_ == 'Ping')])

    def setup(self, total_pings, word):
        self.word = word
        self.total_pings = total_pings
        pass

    def _Pong_handler_0(self, p):
        self.output('Pinged')
        self._send(('Pong',), p)
    _Pong_handler_0._labels = None
    _Pong_handler_0._notlabels = None

class Ping(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._PingReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PingReceivedEvent_0', PatternExpr_8, sources=None, destinations=None, timestamps=[PatternExpr_9], record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PingReceivedEvent_1', PatternExpr_11, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Ping_handler_1])])

    def main(self):
        print('Value of object self in Ping ', self)
        for i in range(self.nrounds):
            clk = self.logical_clock()
            self._send(('Ping',), self.p)
            print('What is clk = ', clk)
            rclk = None

            def ExistentialOpExpr_0():
                nonlocal rclk
                for (_, (rclk, _, _), (_ConstantPattern35_,)) in self._PingReceivedEvent_0:
                    if (_ConstantPattern35_ == 'Pong'):
                        if (rclk > clk):
                            return True
                return False
            _st_label_21 = 0
            while (_st_label_21 == 0):
                _st_label_21 += 1
                if ExistentialOpExpr_0():
                    _st_label_21 += 1
                else:
                    super()._label('_st_label_21', block=True)
                    _st_label_21 -= 1
            else:
                if (_st_label_21 != 2):
                    continue
            if (_st_label_21 != 2):
                break
            print('What is rclk = ', rclk)

    def setup(self, p, nrounds):
        self.nrounds = nrounds
        self.p = p
        pass

    def _Ping_handler_1(self):
        self.output('Ponged.')
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
