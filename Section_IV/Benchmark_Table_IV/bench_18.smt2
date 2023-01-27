;; solver : CVC5
;; version : git 0bf059f79 on branch main
;; option : --check-models --produce-models --sygus-inst
;; Generated Bug Type : Invalid-model Bug (ex1_bug/cvc5_invalid_model_6.smt2)
(set-logic QF_SLIA)
(declare-fun tstr () String)
(assert (ite (str.prefixof "-" (str.substr tstr 0 (- (+ 0 2) 0))) (and (ite (= (- 1) (str.to_int (str.substr (str.substr tstr 0 (- (+ 0 2) 0)) 1 (- (str.len (str.substr tstr 0 (- (+ 0 2) 0))) 1)))) false true) (> (str.len (str.substr tstr 0 (- (+ 0 2) 0))) 1)) (ite (= (- 1) (str.to_int (str.substr tstr 0 (- (+ 0 2) 0)))) false true)))
(assert (not (< (- (str.len tstr) 0) 2)))
(assert (>= (+ (+ 0 2) 1) (str.len tstr)))
(check-sat)
(get-model)


