;; solver : CVC5
;; version : CVC5 - v 1.0.0  
;; option : --check-models --produce-models
;; Generated Bug Type : Soundness Bug
(set-logic QF_SLIA)
(declare-fun tstr () String)
(assert (>= (+ (+ 0 2) 1) (str.len tstr)))
(assert (ite (str.prefixof "-" (str.substr tstr 0 (- (+ 0 2) 0))) (and (ite (xor (str.< (str.update "-0" 0 tstr) "-0") false) false true) (> (str.len (str.substr tstr 0 (- (+ 0 2) 0))) 1)) (ite (= (- 1) (str.to_int (str.substr tstr 0 (- (+ 0 2) 0)))) false true)))
(assert (not (< (- (str.len tstr) 0) 2)))
(assert (str.suffixof (str.replace_all tstr "-0" "-") (str.replace_re "-" re.all "-0")))
(check-sat)
(get-model)


