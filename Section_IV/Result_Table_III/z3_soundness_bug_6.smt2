;; solver : Z3
;; version : Z3 - v 4.11.0  
;; option : model_validate=true rewriter.flat=false
;; Generated Bug Type : Soundness Bug
(set-logic QF_NRA)
(set-option :pp.decimal true)
(declare-fun m () Real)
(declare-fun v10 () Real)
(declare-fun v11 () Real)
(declare-fun v12 () Real)
(declare-fun v13 () Real)
(declare-fun SGeomF () Real)
(declare-fun vC8rAa () Real)
(assert (and (<= SGeomF 25.0) (<= (- 7.0) SGeomF) (<= vC8rAa 26.0) (<= 22.0 vC8rAa)))
(assert (and 
            (< 0 m) (< 0 v13) (< 0 v11) (< 0 v12) 
            (= (+ (* (* v10 v10) (- 4)) (- (+ 1.0 SGeomF) (- vC8rAa (- 1.0)))) 0) 
            (= (+ (* (* v10 v10) 4) (* (* v11 v11) (- 4)) 1) 0) 
            (= (+ (* (* v10 v10) 4) (* (* v13 v13) (- 4)) 1) 0) 
            (= (+ (* v12 (- 1)) 1) 0) 
            (= 
                (+ (* 1.0 (- 1)) (* (* v11 v11 v11) (- 1)) (* (* v11 v11) v13) 
                (* v11 (* v13 v13)) (* (* v13 v13 v13) (- 1)) (* v11 v11) (* (* v11 v13) (- 2)) 
                (* v13 v13) v11 v13 (- 1)) 
                0)
            ))
(check-sat)
(get-model)
