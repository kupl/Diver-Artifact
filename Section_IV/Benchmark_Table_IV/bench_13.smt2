;; solver : CVC5
;; version : git 8311316 on branch main
;; option : --check-models --produce-models --strings-deq-ext
;; Generated Bug Type : Invalid-model Bug (ex1_bug/cvc5_invalid_model_1.smt2)
(set-logic QF_SLIA)
(declare-fun word () String)
(declare-fun abbr () String)
(assert (and (and (and (and (and (not (not (not (= (ite (<= (str.len word) 2) 1 0) 0)))) (not (not (= (ite (not (= (str.at word 1) (str.at abbr 1))) 1 0) 0)))) (not (not (= (ite (<= (str.len word) 1) 1 0) 0)))) (not (not (= (ite (not (= (str.at word 0) (str.at abbr 0))) 1 0) 0)))) (not (not (= (ite (<= (str.len word) 0) 1 0) 0)))) (not (not (= (ite (<= (str.len abbr) 0) 1 0) 0)))))
(check-sat)
(get-model)
