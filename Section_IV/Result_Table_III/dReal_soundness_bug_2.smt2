;; solver : dReal
;; version : dReal - v 4.21.06.2  
;; option : None
;; Generated Bug Type : Soundness Bug
(set-logic QF_NRA)
(declare-fun x () Real)
(declare-fun free_variable_0 () Real)
(declare-fun free_variable_1 () Real)
(assert (<= -10 free_variable_0))
(assert (<= free_variable_0 10))
(assert (<= -10 free_variable_1))
(assert (<= free_variable_1 10))
(assert (< 2.0 x))
(assert (< x 3.0))
(assert (>= (^ (^ x (- (- x free_variable_0) free_variable_1)) 3) 7))
(check-sat)
(get-model)
(exit)
