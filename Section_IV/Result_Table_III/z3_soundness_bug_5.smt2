;; solver : Z3
;; version : Z3 - v 4.11.0  
;; option : model_validate=true
;; Generated Bug Type : Soundness Bug
(set-logic QF_NRA)
(declare-fun m () Real)
(declare-fun v10 () Real)
(declare-fun v11 () Real)
(declare-fun v12 () Real)
(declare-fun v13 () Real)
(declare-fun XVL2jt () Real)
(assert (<= (- 11.499900983398014) XVL2jt))
(assert (<= XVL2jt 0.0))
(assert (and 
            (< 0 m) (< (* v12 XVL2jt) v13) (< (- (- v12) v12) v11) (< 0 v12) 
            (= (+ (* (* v10 v10) (- 4)) 1) 0) (= (+ (* (* v10 v10) 4) (* (* v11 v11) (- 4)) 1) 0) 
            (= (+ (* (* v10 v10) 4) (* (* v13 v13) (- 4)) 1) 0) 
            (= (+ (* v12 (- 1)) 1) 0) 
            (= 
                (+ (* (* m (* v11 v11) v13) (- 1)) (* (* m v11 (* v13 v13)) (- 1)) 
                (* (* m (* v11 v11)) (- 1)) (* (* m v11 v13) (- 2)) (* (* m (* v13 v13)) (- 1)) 
                (* v11 v11 v11) (* v13 v13 v13) (* (* m v11) (- 1)) (* (* m v13) (- 1)) 1) 
                0)
        )
)
(check-sat)
(get-model)
;;(exit)
