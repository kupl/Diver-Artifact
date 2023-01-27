;; solver : Z3
;; version : Z3 - v 4.11.0  
;; option : model_validate=true nlsat.shuffle_vars=true rewriter.eq2ineq=true
;; Generated Bug Type : Soundness Bug
(set-logic QF_NRA)
(declare-fun skoCP1 () Real)
(declare-fun skoCM1 () Real)
(declare-fun skoC () Real)
(declare-fun skoX () Real)
(declare-fun CMu9ra () Real)
(assert (<= (- (/ skoX skoC)) CMu9ra))
(assert (<= CMu9ra 23.78782684445106))
(assert (and (not (<= (* skoCP1 (+ 2 (* skoCM1 (+ (- 12) (* skoCM1 24))))) 0)) (and (= (+ (- 1) (* skoCP1 (* skoCP1 (/ (- CMu9ra skoCM1) (/ skoCM1 skoC))))) skoX) (and (= (+ 1 (* skoCM1 (* skoCM1 skoCM1))) skoX) (and (= (* skoC (* skoC skoC)) skoX) (and (not (<= skoX 2)) (and (not (<= skoCP1 0)) (and (not (<= skoCM1 0)) (and (not (<= skoC 0)) (not (<= 10 skoX)))))))))))
(check-sat)
(get-model)
(exit)