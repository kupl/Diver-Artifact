;; solver : CVC5
;; version : git bf53190 on branch main
;; option : --check-models --produce-models --sygus-inst
;; Generated Bug Type : Invalid-model Bug (ex1_bug/cvc5_invalid_model_5.smt2)
(set-logic QF_SLIA)
(declare-fun s () String)
(assert (not (= (str.len (str.substr s (+ 1 1) (- (+ (+ 1 1) (+ 1 1)) (+ 1 1)))) 1)))
(assert (= (str.len (str.substr s 1 (- (+ 1 1) 1))) 1))
(assert (= (str.len (str.substr s 0 (- 1 0))) 1))
(assert (<= (- (- (- (str.len s) 1) 1) (+ 1 1)) 3))
(assert (> (- (- (- (str.len s) 1) 1) (+ 1 1)) 0))
(assert (= (str.at (str.substr s (+ (+ 1 1) 1) (- (str.len s) (+ (+ 1 1) 1))) 0) "0"))
(assert (not (= (str.len (str.substr s (+ (+ 1 1) 1) (- (str.len s) (+ (+ 1 1) 1)))) 1)))
(assert (= (str.len (str.substr s (+ 1 1) (- (+ (+ 1 1) 1) (+ 1 1)))) 1))
(assert (= (str.len (str.substr s 1 (- (+ 1 1) 1))) 1))
(assert (= (str.len (str.substr s 0 (- 1 0))) 1))
(assert (<= (- (- (- (str.len s) 1) 1) 1) 3))
(assert (> (- (- (- (str.len s) 1) 1) 1) 0))
(assert (str.in_re s (re.+ (re.range "0" "9"))))
(assert (not (> (str.len s) 12)))
(assert (not (= (str.len s) 0)))
(assert (= (str.at (str.substr s (+ 1 1) (- (+ (+ 1 1) (+ 1 1)) (+ 1 1))) 0) "0"))
(check-sat)
(get-model)