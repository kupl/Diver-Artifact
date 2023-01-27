;; solver : Z3
;; version : Z3 - v 4.11.0  
;; option : model_validate=true smt.string_solver=z3str3
;; Generated Bug Type : Soundness Bug
(set-logic QF_SLIA)
(declare-fun T_1 () Bool)
(declare-fun var_0xINPUT_94964 () String)
(declare-fun gqoQt2 () Int)
(declare-fun HItARO () Int)
(assert (and (<= gqoQt2 (- 18)) (<= (- 26) gqoQt2) (<= HItARO 29) (<= (- 38) HItARO)))
(assert (=> (str.prefixof (str.replace (str.replace (str.++ "" var_0xINPUT_94964) (str.substr var_0xINPUT_94964 gqoQt2 (- HItARO)) "file:") (str.replace (str.++ "" var_0xINPUT_94964) (str.at "file:" gqoQt2) (str.replace var_0xINPUT_94964 "file:" "file:")) (str.replace (str.substr "file:" 5 HItARO) (str.replace "file:" "" var_0xINPUT_94964) var_0xINPUT_94964)) "") false))
(assert T_1)
(check-sat)
