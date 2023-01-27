;; solver : CVC5
;; version : git bf53190 on branch main
;; option : --check-models --produce-models --sygus-inst
;; Generated Bug Type : Invalid-model Bug
(set-logic QF_SLIA)
(declare-fun s () String)
(declare-fun yTnGqY () Int)
(assert (and (<= yTnGqY 32) (<= (- 4) yTnGqY)))
(assert (not (= (str.len (str.substr s (+ 1 1) (- (+ (+ 1 1) (+ 1 1)) (+ 1 1)))) 1)))
(assert (= (str.len (str.substr s 1 (- (+ 1 1) 1))) 1))
(assert (= (str.len (str.substr s 0 (- 1 0))) 1))
(assert (str.in_re (str.replace (str.at s (str.to_int "0")) (str.replace (str.from_int yTnGqY) "00000" (str.++ s "00000")) (str.replace_all (str.replace s "0" s) (str.at "0" 0) (str.replace "9" "00000" "9"))) (re.opt re.all)))
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
(assert (not (str.is_digit (str.rev (str.replace_all (str.from_code yTnGqY) (str.replace "9" "0" s) (str.replace s "9" "9"))))))
(assert (= (str.at (str.substr s (+ 1 1) (- (+ (+ 1 1) (+ 1 1)) (+ 1 1))) 0) "0"))
(check-sat)
(get-model)