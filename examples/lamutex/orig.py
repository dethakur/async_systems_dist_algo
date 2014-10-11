
import da
PatternExpr_2 = da.pat.TuplePattern([da.pat.ConstantPattern('Reply'), da.pat.FreePattern('c3')])
PatternExpr_3 = da.pat.FreePattern('p3')
PatternExpr_5 = da.pat.TuplePattern([da.pat.ConstantPattern('Request'), da.pat.FreePattern('reqts')])
PatternExpr_6 = da.pat.FreePattern('source')
PatternExpr_7 = da.pat.TuplePattern([da.pat.ConstantPattern('Release'), da.pat.FreePattern('time')])
PatternExpr_8 = da.pat.FreePattern('source')
PatternExpr_10 = da.pat.TuplePattern([da.pat.ConstantPattern('Done')])
PatternExpr_11 = da.pat.BoundPattern('_BoundPattern28_')
PatternExpr_12 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern34_')]), da.pat.TuplePattern([da.pat.ConstantPattern('Done')])])
import sys

class P(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._PReceivedEvent_0 = []
        self._PReceivedEvent_3 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_2, sources=[PatternExpr_3], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_5, sources=[PatternExpr_6], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_0]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_7, sources=[PatternExpr_8], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_1]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_3', PatternExpr_10, sources=[PatternExpr_11], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def main(self):

        def announce():
            self.output('In cs!')
        super()._label('start', block=False)
        for i in range(self.n):
            self.cs(announce)
        super()._label('end', block=False)
        self._send(('Done',), self.ps)
        p = None

        def UniversalOpExpr_3():
            nonlocal p
            for p in self.ps:
                if (not PatternExpr_12.match_iter(self._PReceivedEvent_3, _BoundPattern34_=p)):
                    return False
            return True
        _st_label_33 = 0
        while (_st_label_33 == 0):
            _st_label_33 += 1
            if UniversalOpExpr_3():
                _st_label_33 += 1
            else:
                super()._label('_st_label_33', block=True)
                _st_label_33 -= 1
        self.output('Terminating...')

    def setup(self, ps, n, timemax):
        self.ps = ps
        self.timemax = timemax
        self.n = n
        self.q = set()

    def cs(self, task):
        'To enter cs, enque and send request to all, then await replies from all\n        '
        super()._label('start', block=False)
        reqc = self.logical_clock()
        self.q.add((reqc, self.id))
        self._send(('Request', reqc), self.ps)
        super()._label('sync', block=False)
        p2 = c2 = None

        def UniversalOpExpr_0():
            nonlocal p2, c2
            for (c2, p2) in self.q:
                if (not ((reqc, self.id) <= (c2, p2))):
                    return False
            return True
        p3 = c3 = None

        def UniversalOpExpr_1():
            nonlocal p3, c3
            for p3 in self.ps:

                def ExistentialOpExpr_2():
                    nonlocal p3, c3
                    for (_, (_, _, _FreePattern13_), (_ConstantPattern15_, c3)) in self._PReceivedEvent_0:
                        if (_FreePattern13_ == p3):
                            if (_ConstantPattern15_ == 'Reply'):
                                if (c3 > reqc):
                                    return True
                    return False
                if (not ExistentialOpExpr_2()):
                    return False
            return True
        _st_label_11 = 0
        self._timer_start()
        while (_st_label_11 == 0):
            _st_label_11 += 1
            if (UniversalOpExpr_0() and UniversalOpExpr_1()):
                task()
                super()._label('release', block=False)
                self.q.remove((reqc, self.id))
                self._send(('Release', reqc), self.ps)
                self.output('release cs')
                _st_label_11 += 1
            elif self._timer_expired:
                super()._label('release', block=False)
                self.q.remove((reqc, self.id))
                self._send(('Release', reqc), self.ps)
                self.output('timed out!')
                _st_label_11 += 1
            else:
                super()._label('sync', block=True, timeout=None)
                _st_label_11 -= 1

    def _P_handler_0(self, reqts, source):
        'When receiving requests from others, enque and reply'
        self.q.add((reqts, source))
        self._send(('Reply', self.logical_clock()), source)
    _P_handler_0._labels = None
    _P_handler_0._notlabels = None

    def _P_handler_1(self, source, time):
        'When receiving release from others, deque'
        if ((time, source) in self.q):
            self.q.remove((time, source))
    _P_handler_1._labels = None
    _P_handler_1._notlabels = None

def main():
    nprocs = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
    nrounds = (int(sys.argv[2]) if (len(sys.argv) > 2) else 1)
    timeout = (int(sys.argv[3]) if (len(sys.argv) > 3) else 10)
    da.api.config(channel='fifo', clock='Lamport')
    ps = da.api.new(P, num=nprocs)
    for p in ps:
        da.api.setup(p, [(ps - {p}), nrounds, timeout])
    da.api.start(ps)
