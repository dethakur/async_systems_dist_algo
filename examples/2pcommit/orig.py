
import da
PatternExpr_1 = da.pat.TuplePattern([da.pat.ConstantPattern('Vote'), da.pat.ConstantPattern('ready'), da.pat.BoundPattern('_BoundPattern3_'), da.pat.BoundPattern('_BoundPattern4_')])
PatternExpr_4 = da.pat.TuplePattern([da.pat.ConstantPattern('Done'), da.pat.BoundPattern('_BoundPattern19_'), da.pat.BoundPattern('_BoundPattern20_')])
PatternExpr_7 = da.pat.TuplePattern([da.pat.ConstantPattern('Vote'), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern35_'), da.pat.FreePattern('c')])
PatternExpr_9 = da.pat.TuplePattern([da.pat.ConstantPattern('Vote'), da.pat.ConstantPattern('ready'), da.pat.FreePattern('tid'), da.pat.FreePattern('c')])
PatternExpr_2 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Vote'), da.pat.ConstantPattern('ready'), da.pat.BoundPattern('_BoundPattern15_'), da.pat.BoundPattern('_BoundPattern16_')])])
PatternExpr_5 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Done'), da.pat.BoundPattern('_BoundPattern30_'), da.pat.BoundPattern('_BoundPattern31_')])])
PatternExpr_11 = da.pat.TuplePattern([da.pat.ConstantPattern('Done')])
PatternExpr_13 = da.pat.TuplePattern([da.pat.ConstantPattern('Prepare'), da.pat.FreePattern('tid')])
PatternExpr_14 = da.pat.FreePattern('coord')
PatternExpr_15 = da.pat.TuplePattern([da.pat.ConstantPattern('Commit'), da.pat.FreePattern('tid')])
PatternExpr_16 = da.pat.FreePattern('fro')
PatternExpr_17 = da.pat.TuplePattern([da.pat.ConstantPattern('Abort'), da.pat.FreePattern('tid')])
PatternExpr_12 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('Done')])])
import sys
from random import randint

class Coordinator(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._CoordinatorReceivedEvent_0 = []
        self._CoordinatorReceivedEvent_1 = []
        self._CoordinatorReceivedEvent_2 = []
        self._CoordinatorReceivedEvent_3 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_CoordinatorReceivedEvent_0', PatternExpr_1, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CoordinatorReceivedEvent_1', PatternExpr_4, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CoordinatorReceivedEvent_2', PatternExpr_7, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CoordinatorReceivedEvent_3', PatternExpr_9, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def main(self):
        super()._label('start', block=False)
        self._send(('Prepare', self.tid), self.cohorts)
        c = None

        def UniversalOpExpr_0():
            nonlocal c
            for c in self.cohorts:
                if (not PatternExpr_2.match_iter(self._CoordinatorReceivedEvent_0, _BoundPattern15_=self.tid, _BoundPattern16_=c)):
                    return False
            return True
        c = None

        def UniversalOpExpr_2():
            nonlocal c
            for c in self.cohorts:

                def ExistentialOpExpr_3():
                    nonlocal c
                    for (_, _, (_ConstantPattern45_, _, _BoundPattern47_, _FreePattern48_)) in self._CoordinatorReceivedEvent_2:
                        if (_ConstantPattern45_ == 'Vote'):
                            if (_BoundPattern47_ == self.tid):
                                if (_FreePattern48_ == c):
                                    if True:
                                        return True
                    return False
                if (not ExistentialOpExpr_3()):
                    return False
            return True
        _st_label_9 = 0
        while (_st_label_9 == 0):
            _st_label_9 += 1
            if UniversalOpExpr_0():
                self._send(('Commit', self.tid), self.cohorts)
                c = None

                def UniversalOpExpr_1():
                    nonlocal c
                    for c in self.cohorts:
                        if (not PatternExpr_5.match_iter(self._CoordinatorReceivedEvent_1, _BoundPattern30_=self.tid, _BoundPattern31_=c)):
                            return False
                    return True
                _st_label_11 = 0
                while (_st_label_11 == 0):
                    _st_label_11 += 1
                    if UniversalOpExpr_1():
                        _st_label_11 += 1
                    else:
                        super()._label('_st_label_11', block=True)
                        _st_label_11 -= 1
                self.output(('log complete record for' + str(self.tid)))
                _st_label_9 += 1
            elif UniversalOpExpr_2():
                s = {c for (_, _, (_ConstantPattern61_, _ConstantPattern62_, tid, c)) in self._CoordinatorReceivedEvent_3 if (_ConstantPattern61_ == 'Vote') if (_ConstantPattern62_ == 'ready')}
                self._send(('Abort', self.tid), s)
                _st_label_9 += 1
            else:
                super()._label('_st_label_9', block=True)
                _st_label_9 -= 1
        super()._label('end', block=False)
        self.terminate()

    def setup(self, tid, cohorts):
        self.cohorts = cohorts
        self.tid = tid
        pass

    def terminate(self):
        self._send(('Done',), self.cohorts)
        self.output('terminating')

class Cohort(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._CohortReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_CohortReceivedEvent_0', PatternExpr_11, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CohortReceivedEvent_1', PatternExpr_13, sources=[PatternExpr_14], destinations=None, timestamps=None, record_history=None, handlers=[self._Cohort_handler_0]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CohortReceivedEvent_2', PatternExpr_15, sources=[PatternExpr_16], destinations=None, timestamps=None, record_history=None, handlers=[self._Cohort_handler_1]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CohortReceivedEvent_3', PatternExpr_17, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Cohort_handler_2])])

    def main(self):
        _st_label_23 = 0
        while (_st_label_23 == 0):
            _st_label_23 += 1
            if PatternExpr_12.match_iter(self._CohortReceivedEvent_0):
                _st_label_23 += 1
            else:
                super()._label('_st_label_23', block=True)
                _st_label_23 -= 1

    def setup(self, failure_rate):
        self.failure_rate = failure_rate
        pass

    def prepared(self, tid):
        return (randint(0, 100) > self.failure_rate)

    def commit(self, tid):
        self.output(('commit:' + str(tid)))

    def abort(self, tid):
        self.output(('abort:' + str(tid)))

    def _Cohort_handler_0(self, coord, tid):
        if self.prepared(tid):
            self.output(('ready:' + str(tid)))
            self._send(('Vote', 'ready', tid, self.id), coord)
        else:
            self.output(('failed:' + str(tid)))
            self._send(('Vote', 'abort', tid, self.id), coord)
    _Cohort_handler_0._labels = None
    _Cohort_handler_0._notlabels = None

    def _Cohort_handler_1(self, fro, tid):
        self._send(('Done', tid, self.id), fro)
        self.commit(tid)
    _Cohort_handler_1._labels = None
    _Cohort_handler_1._notlabels = None

    def _Cohort_handler_2(self, tid):
        self.abort(tid)
    _Cohort_handler_2._labels = None
    _Cohort_handler_2._notlabels = None

def main():
    nproposers = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
    nacceptors = (int(sys.argv[2]) if (len(sys.argv) > 2) else 10)
    fail_rate = (int(sys.argv[3]) if (len(sys.argv) > 3) else 10)
    da.api.config(channel=('unfifo', 'unreliable'))
    accpts = da.api.new(Cohort, [fail_rate], num=nacceptors)
    propsrs = da.api.new(Coordinator, [nproposers, accpts], num=1)
    da.api.start((accpts | propsrs))
