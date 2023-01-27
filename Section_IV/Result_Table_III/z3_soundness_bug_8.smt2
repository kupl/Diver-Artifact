;; solver : Z3
;; version : Z3 - v 4.11.0  
;; option : model_validate=true rewriter.eq2ineq=true
;; Generated Bug Type : Soundness Bug
(set-logic QF_NRA)
(declare-fun skoX () Real)
(declare-fun skoS2 () Real)
(declare-fun skoSP () Real)
(declare-fun skoSM () Real)
(declare-fun dMTirl () Real)
(declare-fun PhIzua () Real)
(declare-fun TNqzmB () Real)
(declare-fun D7SDXI () Real)
(assert (<= (- 46.61972823198872) D7SDXI))
(assert (<= D7SDXI 15.545322465767612))
(assert (<= (- 28.526706955939172) dMTirl))
(assert (<= dMTirl (- 21.39626972292963)))
(assert (<= (- 26.87227863497087) (+ skoS2 (- D7SDXI))))
(assert (<= PhIzua 17.99810905704075))
(assert (<= (- 38.13758853124696) TNqzmB))
(assert (<= TNqzmB (- 33.63155972927738)))
(assert (and (not (<= (* skoX skoX) 0)) (and (= skoX (+ 1 (* skoSM (* skoSM (- 1))))) 
            (and (= (+ (- 1) (* skoSP skoSP)) skoX) (and (= (* skoS2 skoS2) 2) 
            (and (not (<= skoX 0)) (and (not (<= skoSP 0)) 
            (and (not (<= skoSM 0)) 
            (or false (= (- dMTirl) PhIzua) (> (/ skoX (- (- TNqzmB))) skoX) (<= (- skoSP) skoS2))))))))))
(check-sat)
(get-model)
(exit)
