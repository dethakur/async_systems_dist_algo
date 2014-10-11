
import da
PatternExpr_0 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.BoundPattern('_BoundPattern1_'), da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern('a')])
PatternExpr_2 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.BoundPattern('_BoundPattern19_'), da.pat.FreePattern('n'), da.pat.FreePattern('v'), da.pat.FreePattern(None)])
PatternExpr_4 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.BoundPattern('_BoundPattern37_'), da.pat.FreePattern('n'), da.pat.FreePattern('v'), da.pat.FreePattern('a')])
PatternExpr_6 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoAv'), da.pat.BoundPattern('_BoundPattern55_'), da.pat.BoundPattern('_BoundPattern56_'), da.pat.FreePattern('a')])
PatternExpr_8 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoAV'), da.pat.FreePattern('n'), da.pat.FreePattern('v'), da.pat.FreePattern(None)])
PatternExpr_10 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoAV'), da.pat.FreePattern('n'), da.pat.FreePattern('v'), da.pat.FreePattern('a')])
PatternExpr_12 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoB'), da.pat.BoundPattern('_BoundPattern103_'), da.pat.BoundPattern('_BoundPattern104_')])
PatternExpr_15 = da.pat.TuplePattern([da.pat.ConstantPattern('Done')])
PatternExpr_16 = da.pat.BoundPattern('_BoundPattern119_')
PatternExpr_18 = da.pat.TuplePattern([da.pat.ConstantPattern('Prepare'), da.pat.FreePattern('n'), da.pat.FreePattern('p')])
PatternExpr_19 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoAv'), da.pat.FreePattern('vpn'), da.pat.FreePattern('vv'), da.pat.BoundPattern('_BoundPattern135_')])
PatternExpr_21 = da.pat.TuplePattern([da.pat.ConstantPattern('OneC'), da.pat.FreePattern('n'), da.pat.FreePattern('v'), da.pat.FreePattern('p')])
PatternExpr_22 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoAv'), da.pat.BoundPattern('_BoundPattern154_'), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern156_')])
PatternExpr_24 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.FreePattern('n'), da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)])
PatternExpr_26 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.BoundPattern('_BoundPattern188_'), da.pat.FreePattern('vn'), da.pat.FreePattern('vv'), da.pat.FreePattern(None)])
PatternExpr_28 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.BoundPattern('_BoundPattern206_'), da.pat.FreePattern('vn'), da.pat.FreePattern('vv'), da.pat.FreePattern('a')])
PatternExpr_13 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('TwoB'), da.pat.BoundPattern('_BoundPattern114_'), da.pat.BoundPattern('_BoundPattern115_')])])
PatternExpr_17 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern125_')]), da.pat.TuplePattern([da.pat.ConstantPattern('Done')])])
import sys

class Proposer(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._ProposerReceivedEvent_0 = []
        self._ProposerReceivedEvent_1 = []
        self._ProposerReceivedEvent_2 = []
        self._ProposerReceivedEvent_3 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_0', PatternExpr_0, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_1', PatternExpr_2, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_2', PatternExpr_4, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_3', PatternExpr_6, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def main(self):
        count = 0
        while (count < self.nrounds):
            self.work()
            super()._label('prepare', block=False)
            self._send(('Prepare', self.propNum, self.id), self.acceptors)
            _st_label_12 = 0
            self._timer_start()
            while (_st_label_12 == 0):
                _st_label_12 += 1
                if (len({a for (_, _, (_ConstantPattern13_, _BoundPattern14_, _, _, a)) in self._ProposerReceivedEvent_0 if (_ConstantPattern13_ == 'Promise') if (_BoundPattern14_ == self.propNum)}) > self.quorumsize):
                    super()._label('propose', block=False)
                    voted = max(({(n, v) for (_, _, (_ConstantPattern31_, _BoundPattern32_, n, v, _)) in self._ProposerReceivedEvent_1 if (len({a for (_, _, (_ConstantPattern49_, _BoundPattern50_, _FreePattern51_, _FreePattern52_, a)) in self._ProposerReceivedEvent_2 if (_ConstantPattern49_ == 'Promise') if (_BoundPattern50_ == self.propNum) if (_FreePattern51_ == n) if (_FreePattern52_ == v)}) > self.f)} | {(((- 1), self.id), self.propVal)}))[1]
                    self._send(('OneC', self.propNum, voted, self.id), self.acceptors)
                    _st_label_15 = 0
                    self._timer_start()
                    while (_st_label_15 == 0):
                        _st_label_15 += 1
                        if (len({a for (_, _, (_ConstantPattern66_, _BoundPattern67_, _BoundPattern68_, a)) in self._ProposerReceivedEvent_3 if (_ConstantPattern66_ == 'TwoAv') if (_BoundPattern67_ == self.propNum) if (_BoundPattern68_ == voted)}) > self.quorumsize):
                            super()._label('end', block=False)
                            self.output(('Succeeded proposing %r' % voted))
                            count += 1
                            continue
                            _st_label_15 += 1
                        elif self._timer_expired:
                            self.output('Failed to Propose in time, retrying.')
                            _st_label_15 += 1
                        else:
                            super()._label('_st_label_15', block=True, timeout=self.timeout)
                            _st_label_15 -= 1
                    else:
                        if (_st_label_15 != 2):
                            continue
                    if (_st_label_15 != 2):
                        break
                    _st_label_12 += 1
                elif self._timer_expired:
                    self.output('Failed to Prepare in time, retrying.')
                    _st_label_12 += 1
                else:
                    super()._label('_st_label_12', block=True, timeout=self.timeout)
                    _st_label_12 -= 1
            else:
                if (_st_label_12 != 2):
                    continue
            if (_st_label_12 != 2):
                break
            self.propNum = ((self.propNum[0] + 1), self.id)
        self._send(('Done',), self.acceptors)

    def setup(self, acceptors, quorumsize, f, nrounds, timeout):
        self.acceptors = acceptors
        self.quorumsize = quorumsize
        self.f = f
        self.nrounds = nrounds
        self.timeout = timeout
        self.propNum = (0, self.id)
        self.propVal = self.id

class Acceptor(da.DistProcess):

    def __init__(self, parent, initq, channel, props):
        super().__init__(parent, initq, channel, props)
        self._AcceptorReceivedEvent_0 = []
        self._AcceptorReceivedEvent_1 = []
        self._AcceptorSentEvent_2 = []
        self._AcceptorReceivedEvent_3 = []
        self._AcceptorSentEvent_5 = []
        self._AcceptorSentEvent_7 = []
        self._AcceptorSentEvent_8 = []
        self._AcceptorReceivedEvent_9 = []
        self._AcceptorReceivedEvent_10 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_0', PatternExpr_8, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_1', PatternExpr_10, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_2', PatternExpr_12, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_3', PatternExpr_15, sources=[PatternExpr_16], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_4', PatternExpr_18, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Acceptor_handler_0]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_5', PatternExpr_19, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_6', PatternExpr_21, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Acceptor_handler_1]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_7', PatternExpr_22, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_8', PatternExpr_24, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_9', PatternExpr_26, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_10', PatternExpr_28, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def main(self):
        while True:
            a = v = n = None

            def ExistentialOpExpr_0():
                nonlocal a, v, n
                for (_, _, (_ConstantPattern82_, n, v, _)) in self._AcceptorReceivedEvent_0:
                    if (_ConstantPattern82_ == 'TwoAV'):
                        if ((len({a for (_, _, (_ConstantPattern98_, _FreePattern99_, _FreePattern100_, a)) in self._AcceptorReceivedEvent_1 if (_ConstantPattern98_ == 'TwoAV') if (_FreePattern99_ == n) if (_FreePattern100_ == v)}) > self.quorumsize) and (not PatternExpr_13.match_iter(self._AcceptorSentEvent_2, _BoundPattern114_=n, _BoundPattern115_=v))):
                            return True
                return False
            p = None

            def UniversalOpExpr_1():
                nonlocal p
                for p in self.proposers:
                    if (not PatternExpr_17.match_iter(self._AcceptorReceivedEvent_3, _BoundPattern125_=p)):
                        return False
                return True
            _st_label_28 = 0
            while (_st_label_28 == 0):
                _st_label_28 += 1
                if ExistentialOpExpr_0():
                    self._send(('TwoB', n, v), self.peers)
                    _st_label_28 += 1
                elif UniversalOpExpr_1():
                    break
                    _st_label_28 += 1
                else:
                    super()._label('_st_label_28', block=True)
                    _st_label_28 -= 1
            else:
                if (_st_label_28 != 2):
                    continue
            if (_st_label_28 != 2):
                break

    def setup(self, acceptors, proposers, quorumsize, f):
        self.acceptors = acceptors
        self.quorumsize = quorumsize
        self.f = f
        self.proposers = proposers
        self.peers = (acceptors | proposers)

    def maxpromised(self):
        return max(({n for (_, _, (_ConstantPattern182_, n, _, _, _)) in self._AcceptorSentEvent_8 if (_ConstantPattern182_ == 'Promise')} | {((- 2), self.id)}))

    def islegal(self, n, v):
        voted = {(vn, vv) for (_, _, (_ConstantPattern200_, _BoundPattern201_, vn, vv, _)) in self._AcceptorReceivedEvent_9 if (len({a for (_, _, (_ConstantPattern218_, _BoundPattern219_, _FreePattern220_, _FreePattern221_, a)) in self._AcceptorReceivedEvent_10 if (_ConstantPattern218_ == 'Promise') if (_BoundPattern219_ == n) if (_FreePattern220_ == vn) if (_FreePattern221_ == vv)}) > self.f)}
        if (voted and (not (max(voted)[1] is None))):
            return (v == max(voted)[1])
        else:
            return True

    def _Acceptor_handler_0(self, p, n):
        if (n > self.maxpromised()):
            (vn, vv) = max(({(vpn, vv) for (_, _, (_ConstantPattern144_, vpn, vv, _BoundPattern147_)) in self._AcceptorSentEvent_5 if (_ConstantPattern144_ == 'TwoAv') if (_BoundPattern147_ == self.id)} | {(((- 1), self.id), None)}))
            self._send(('Promise', n, vn, vv, self.id), self.peers)
    _Acceptor_handler_0._labels = None
    _Acceptor_handler_0._notlabels = None

    def _Acceptor_handler_1(self, p, v, n):

        def ExistentialOpExpr_2():
            for (_, _, (_ConstantPattern165_, _BoundPattern166_, _, _BoundPattern168_)) in self._AcceptorSentEvent_7:
                if (_ConstantPattern165_ == 'TwoAv'):
                    if (_BoundPattern166_ == n):
                        if (_BoundPattern168_ == self.id):
                            if True:
                                return True
            return False
        if ((n >= self.maxpromised()) and self.islegal(n, v) and (not ExistentialOpExpr_2())):
            self._send(('TwoAv', n, v, self.id), self.peers)
    _Acceptor_handler_1._labels = None
    _Acceptor_handler_1._notlabels = None

def main():
    nproposers = (int(sys.argv[1]) if (len(sys.argv) > 1) else 5)
    nacceptors = (int(sys.argv[2]) if (len(sys.argv) > 2) else 10)
    nrounds = (int(sys.argv[3]) if (len(sys.argv) > 3) else 1)
    timeout = (int(sys.argv[4]) if (len(sys.argv) > 4) else 5)
    f = int(((nacceptors - 1) / 3))
    quorum = int(((nacceptors / 2) + f))
    acceptors = da.api.new(Acceptor, num=nacceptors)
    proposers = da.api.new(Proposer, num=nproposers)
    da.api.setup(acceptors, (acceptors, proposers, quorum, f))
    da.api.setup(proposers, (acceptors, quorum, f, nrounds, timeout))
    da.api.start(acceptors)
    da.api.start(proposers)
