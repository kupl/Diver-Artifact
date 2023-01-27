;; solver : Z3
;; version : Z3 - v 4.11.0  
;; option : model_validate=true nlsat.shuffle_vars=true
;; Generated Bug Type : Soundness Bug
(set-logic QF_NRA)
(declare-fun skoS2 () Real)
(declare-fun skoSP () Real)
(declare-fun skoSM () Real)
(declare-fun skoX () Real)
(declare-fun AJOntN () Real)
(declare-fun i0vABO () Real)
(declare-fun LpLYU4 () Real)
(declare-fun WeThA7 () Real)
(assert (<= (- 40.27480555072409) WeThA7))
(assert (<= WeThA7 46.0420390104799))
(assert (<= (- 2.5024609913331304) AJOntN))
(assert (<= AJOntN 34.46083052901105))
(assert (<= (- 30.853680748995018) i0vABO))
(assert (<= i0vABO 50.4531874701719))
(assert (<= (- 39.29498486561446) LpLYU4))
(assert (<= LpLYU4 4.177370647838188))
(assert (and (not (= skoX (+ 1 (* skoSM (* skoSM (- 1)))))) 
        (and (= (+ (- 1) (* skoSP skoSP)) skoX) (and (= (* skoS2 skoS2) 2)
        (and (not (<= skoX 0)) (and (not (<= (- (- WeThA7) LpLYU4) 0)) 
        (and (not (<= skoSM 0))
        (and (and (>= skoS2 skoSP) 
        (= (- (- AJOntN) i0vABO) (- LpLYU4 skoS2))) (not (<= 1 skoX))))))))))
(check-sat)
(get-model)
(exit)


