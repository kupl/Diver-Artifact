;; solver : dReal
;; version : dReal - v 4.21.06.2  
;; option : None
;; Generated Bug Type : Soundness Bug
(set-logic QF_NRA)
(declare-fun x_0 () Real)
(declare-fun x_1 () Real)
(declare-fun x_2 () Real)
(assert (= x_0 2))
(assert (<= x_1 (atan2 x_1 x_2)))
(assert (= 2 x_1))
(check-sat)
(get-model)
(exit)

