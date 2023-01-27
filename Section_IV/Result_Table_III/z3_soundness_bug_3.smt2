;; solver : Z3
;; version : Z3 - v 4.11.0  
;; option : model_validate=true smt.string_solver=z3str3
;; Generated Bug Type : Soundness Bug
(set-logic QF_SLIA)
(declare-fun x () String)
(declare-fun y () String)
(assert (= 1 (str.len y)))
(assert (str.in_re x (re.range "-" y)))
(check-sat)
