;; solver : CVC5
;; version : CVC5 - v 1.0.0
;; option : --check-models --produce-models --sygus-rr-synth-input --incremental
;; Generated Bug Type : Invalid-model Bug
(set-logic QF_SLIA)
(declare-fun T_1 () Bool)
(declare-fun T_2 () Bool)
(declare-fun var_0xINPUT_100868 () String)
(assert (= T_1 (not (= "file:" var_0xINPUT_100868))))
(assert (= T_2 (or (str.prefixof "file:" (str.update "file:" (+ (str.len var_0xINPUT_100868) 3) var_0xINPUT_100868)) (str.is_digit "file:") false)))
(assert T_2)
(check-sat)
(get-model)