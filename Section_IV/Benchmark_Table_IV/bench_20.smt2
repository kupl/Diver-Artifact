;; solver : Z3
;; version : Z3 - v 4.11.0
;; option : model_validate=true smt.string_solver=z3str3
;; Generated Bug Type : Invalid-model Bug (ex1_bug/z3_invalid_model_1.smt2)
(set-logic QF_SLIA)
(declare-fun T_1 () Bool)
(declare-fun T_2 () Bool)
(declare-fun var_0xINPUT_107797 () String)
(assert (= T_1 (not (= "file:" var_0xINPUT_107797))))
(assert (= T_2 (not T_1)))
(assert T_2)
(check-sat)
(get-model)
