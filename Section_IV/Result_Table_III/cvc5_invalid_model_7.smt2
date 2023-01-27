;; solver : CVC5
;; version : CVC5 - v 1.0.0
;; option : --check-models --produce-models
;; Generated Bug Type : Invalid-model Bug
(set-logic QF_LIA)
(declare-fun x () Int)
(declare-fun y () Int)
(assert (= (- x y) (int.pow2 x)))
(check-sat)
(get-model)
