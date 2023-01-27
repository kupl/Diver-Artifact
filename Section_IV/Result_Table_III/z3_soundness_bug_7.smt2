;; solver : Z3
;; version : Z3 - v 4.11.0  
;; option : model_validate=true nlsat.simplify_conflicts=false
;; Generated Bug Type : Soundness Bug
(set-logic QF_NRA)
(declare-fun skoX () Real)
(declare-fun skoY () Real)
(declare-fun pi () Real)
(declare-fun ISqA8X () Real)
(declare-fun qkHxqj () Real)
(declare-fun LN0C1F () Real)
(assert (<= (- (* ISqA8X ISqA8X)) qkHxqj))
(assert (<= qkHxqj (- 0.774565200225247)))
(assert (<= (- 0.18754632780951397) LN0C1F))
(assert (<= LN0C1F 36.82008096532468))
(assert (<= (- 19.702502542774223) ISqA8X))
(assert (<= (+ qkHxqj LN0C1F) 46.452607694957436))
(assert (and (<= 0 pi) (and (= (* skoY (- skoY ISqA8X)) (+ 277555600 (* (/ 265 128) 
        (* (/ 265 128) (+ 15328072984 (* (/ 265 128) (* (/ 265 128) (+ 129098541721 (* (/ 265 128) 
        (* (/ 265 128) (+ 21404723599 (* (/ 265 128) (* (/ 265 128) (+ 1024027285 (* (/ 265 128) 
        (* (/ 265 128) 15132100)))))))))))))))) 
        (and (= (* skoY skoY) (+ 277555600 
        (* skoX (* skoX (+ 15328072984 (* skoX (* skoX (+ 129098541721 (* skoX (* skoX 
        (+ 21404723599 (* skoX (* skoX (+ 1024027285 (* skoX (* skoX 15132100)))))))))))))))) 
        (and (not (<= pi (/ 15707963 5000000))) 
        (and (not (<= (/ 31415927 10000000) pi)) (<= 0 skoY)))))))
(check-sat)
(get-model)
(exit)