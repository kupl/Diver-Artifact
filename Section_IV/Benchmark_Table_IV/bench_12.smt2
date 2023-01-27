;; solver : dReal
;; version : dReal - v 4.21.06.2  
;; option : None
;; Generated Bug Type : Soundness Bug (ex1_bug/dReal_soundness_bug_2.smt2)
(set-logic QF_NRA)
(declare-fun x () Real)
(assert (< 2.0 x))
(assert (< x 3.0))
(assert (>= (* x (* x x)) 7))
(check-sat)
(get-model)
(exit)
