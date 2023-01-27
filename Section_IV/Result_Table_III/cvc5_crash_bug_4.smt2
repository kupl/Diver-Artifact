;; solver : CVC5
;; version : git 0bf059f79 on branch main
;; option : --check-models --produce-models --strings-fmf
;; Generated Bug Type : Crash Bug
(set-logic QF_SLIA)
(declare-fun T_1 () Bool)
(declare-fun var_0xINPUT_126612 () String)
(declare-fun XMOqJP () Int)
(declare-fun td9VpI () Int)
(assert (and (<= XMOqJP 6) (<= (- 1) XMOqJP) (<= td9VpI (- 15)) (<= (- 38) td9VpI)))
(assert (not (str.< (str.++ (str.++ (str.from_int XMOqJP) (str.from_int (- td9VpI))) var_0xINPUT_126612) "3lABVjA2UN")))
(assert T_1)
(check-sat)
(get-model)
