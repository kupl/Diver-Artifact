(set-logic QF_NRA)
(set-option :pp.decimal true)
(declare-fun y () Real)
(declare-fun p () Real)
(declare-fun c () Real)
(assert (< 1.0 c))
(assert (< 0.0 (* p c)))
(assert (and (> (* y y y y) 0) (> (* y y y p) 0)))
(check-sat)
(get-model)
