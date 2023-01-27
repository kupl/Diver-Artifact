;; solver : CVC5
;; version : git 0bf059f79 on branch main
;; option : --check-models --produce-models --strings-fmf
;; Generated Bug Type : Crash Bug (ex1_bug/cvc5_crash_bug_4.smt2)
(set-logic QF_SLIA)
(declare-fun T_1 () Bool)
(declare-fun var_0xINPUT_126612 () String)
(assert (= T_1 (= var_0xINPUT_126612 "3lABVjA2UN")))
(assert T_1)
(check-sat)
(get-model)

