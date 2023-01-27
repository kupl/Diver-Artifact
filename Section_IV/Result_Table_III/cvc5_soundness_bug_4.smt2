;; solver : CVC5
;; version : CVC5 - v 1.0.0  
;; option : --check-models --produce-models
;; Generated Bug Type : Soundness Bug
(set-logic QF_NRA)
(declare-fun y () Real)
(declare-fun p () Real)
(declare-fun c () Real)
(assert (< 1.0 c))
(assert (< 0.0 (/ (+ y (+ p 1.0)) c)))
(assert (and (> (* y y y y) 0) (> (* y y y p) 0)))
(check-sat)
(get-model)
