;; solver : CVC5
;; version : CVC5 version 1.0.1
;; option : --check-models --produce-models --strings-deq-ext
;; Generated Bug Type : Crash Bug
(set-logic QF_SLIA)
(declare-fun s () String)
(assert (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (or (str.<= (str.to_lower "AAADCCAB") (str.to_lower s)) (str.suffixof (str.to_lower "AAADCCAB") (str.update "AAADCCAB" 3 s)) (str.suffixof (str.rev s) s) false) (not (= (ite (not (= (str.at s 4) (str.at s 6))) 1 0) 0))) (not (= (ite (not (= (str.at s 6) (str.at s 7))) 1 0) 0))) (not (= (ite (<= (str.len s) 8) 1 0) 0))) (not (= (ite (= (str.len s) 8) 1 0) 0))) (not (xor (str.suffixof (str.replace_re "AAADCCAB" re.all "AAADCCAB") (str.replace_all s s s)) true (str.suffixof (str.replace_all s "AAADCCAB" s) (str.replace_all s "AAADCCAB" "AAADCCAB"))))) (not (not (= (ite (= (str.len s) 7) 1 0) 0)))) (not (not (= (ite (<= (str.len s) 6) 1 0) 0)))) (not (not (= (ite (= (str.len s) 6) 1 0) 0)))) (not (not (= (ite (not (= (str.at s 4) (str.at s 5))) 1 0) 0)))) (not (= (ite (not (= (str.at s 5) (str.at s 7))) 1 0) 0))) (not (= (ite (not (= (str.at s 5) (str.at s 6))) 1 0) 0))) (not (= (ite (not (= (str.at s 6) (str.at s 7))) 1 0) 0))) (not (= (ite (<= (str.len s) 8) 1 0) 0))) (not (= (ite (= (str.len s) 8) 1 0) 0))) (not (not (= (ite (<= (str.len s) 7) 1 0) 0)))) (not (not (= (ite (= (str.len s) 7) 1 0) 0)))) (not (not (= (ite (<= (str.len s) 6) 1 0) 0)))) (not (not (= (ite (= (str.len s) 6) 1 0) 0)))) (not (not (= (ite (<= (str.len s) 5) 1 0) 0)))) (not (not (= (ite (= (str.len s) 5) 1 0) 0)))) (not (not (= (ite (<= (str.len s) 4) 1 0) 0)))) (not (not (= (ite (= (str.len s) 4) 1 0) 0)))) (not (not (= (ite (<= (str.len s) 3) 1 0) 0)))) (not (not (= (ite (= (str.len s) 3) 1 0) 0)))) (not (not (= (ite (<= (str.len s) 2) 1 0) 0)))) (not (not (= (ite (= (str.len s) 2) 1 0) 0)))) (not (not (= (ite (<= (str.len s) 1) 1 0) 0)))) (not (not (= (ite (= (str.len s) 1) 1 0) 0)))) (not (not (= (ite (<= (str.len s) 0) 1 0) 0)))) (not (not (= (ite (= (str.len s) 0) 1 0) 0)))))
(check-sat)
(get-model)