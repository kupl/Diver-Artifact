;; solver : CVC5
;; version : git 8311316 on branch main
;; option : --check-models --produce-models --strings-deq-ext
;; Generated Bug Type : Invalid-model Bug
(set-logic QF_SLIA)
(declare-fun word () String)
(declare-fun abbr () String)
(assert (and (and (and (and (and (xor (str.<= (str.from_int 1) abbr) (= (str.++ abbr abbr) (str.to_lower abbr)) false (= (str.rev word) "B")) (not (not (= (ite (not (= (str.at abbr 1) (str.at abbr 1))) 1 0) 0)))) (not (not (= (ite (<= (str.len word) 1) 1 0) 0)))) (not (not (= (ite (not (= (str.at word 0) (str.at abbr 0))) 1 0) 0)))) (not (not (= (ite (<= (str.len word) 0) 1 0) 0)))) (not (not (= (ite (<= (str.len abbr) 0) 1 0) 0)))))
(check-sat)
(get-model)