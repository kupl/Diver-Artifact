;; solver : CVC5
;; version : CVC5 - v 1.0.0
;; option : --check-models --produce-models
;; Generated Bug Type : Invalid-model Bug (ex1_bug/cvc5_invalid_model_7.smt2)
(set-logic QF_LIA)
(declare-fun x () Int)
(declare-fun y () Int)
(assert (and (= x 1) (= x (abs y))))
(check-sat)