;; solver : CVC5
;; version : CVC5 - v 1.0.1  
;; option : --check-models --produce-models
;; Generated Bug Type : Soundness Bug (ex1_bug/cvc5_soundness_bug_1.smt2)
(set-logic QF_SLIA)
(declare-fun var_0 () String)
(declare-fun var_1 () String)
(declare-fun var_2 () String)
(declare-fun var_3 () String)
(declare-fun var_4 () String)
(declare-fun var_5 () String)
(declare-fun var_6 () String)
(declare-fun var_7 () String)
(declare-fun var_8 () String)
(declare-fun var_9 () String)
(declare-fun var_10 () String)
(declare-fun var_11 () String)
(declare-fun var_12 () String)
(assert (str.in_re (str.++ var_9 "z" var_10) (re.++ (re.* (re.union (re.union (str.to_re "z") (str.to_re "a")) (re.++ (str.to_re "b") (re.++ (re.* (str.to_re "b")) (re.union (str.to_re "z") (str.to_re "a")))))) (re.++ (str.to_re "b") (re.* (str.to_re "b"))))))
(assert (str.in_re (str.++ var_9 "z" var_10) (re.++ (re.* (re.union (str.to_re "a") (re.++ (str.to_re "b") (re.++ (re.* (re.union (str.to_re "b") (str.to_re "a"))) (str.to_re "z"))))) (re.++ (str.to_re "b") (re.* (re.union (str.to_re "b") (str.to_re "a")))))))
(assert (str.in_re (str.++ var_9 "z" var_10) (re.++ (re.* (re.++ (str.to_re "b") (re.++ (re.* (re.union (str.to_re "z") (str.to_re "b"))) (str.to_re "a")))) (re.++ (str.to_re "b") (re.* (re.union (str.to_re "z") (str.to_re "b")))))))
(assert (str.in_re (str.++ var_9 "z" var_10) (re.* (re.++ (str.to_re "b") (re.++ (re.* (str.to_re "z")) (str.to_re "b"))))))
(assert (str.in_re (str.++ var_9 "z" var_10) (re.++ (re.* (re.++ (str.to_re "b") (str.to_re "z"))) (str.to_re "b"))))
(assert (str.in_re (str.++ var_9 "z" var_10) (re.++ (re.* (re.union (str.to_re "z") (re.++ (re.union (str.to_re "b") (str.to_re "a")) (re.union (str.to_re "z") (str.to_re "b"))))) (re.union (str.to_re "b") (str.to_re "a")))))
(assert (str.in_re var_10 (re.* (re.range "a" "u"))))
(assert (str.in_re var_9 (re.* (re.range "a" "u"))))
(assert (not (str.in_re (str.++ "b" var_9 "z" "a" var_10) (re.++ (re.* (re.union (str.to_re "z") (re.++ (re.union (str.to_re "b") (str.to_re "a")) (re.union (str.to_re "z") (str.to_re "b"))))) (re.union (str.to_re "b") (str.to_re "a"))))))
(check-sat)
(get-model)
