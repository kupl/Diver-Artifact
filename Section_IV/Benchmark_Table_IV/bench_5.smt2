;; solver : Z3
;; version : Z3 - v 4.11.0  
;; option : model_validate=true smt.string_solver=z3str3
;; Generated Bug Type : Soundness Bug (ex1_bug/z3_soundness_bug_1.smt2)
(set-info :smt-lib-version 2.6)
(set-logic QF_SLIA)
(set-info :source |
Generated by: Andrew Reynolds
Generated on: 2018-04-25
Generator: Kudzu, converted to v2.6 by CVC4
Application: Symbolic Execution of Javascript
Target solver: Kaluza
Publications: "A symbolic execution framework for JavaScript" by P. Saxena, D. Akhawe, S. Hanna, F. Mao, S. McCamant, and D. Song, 2010.
|)
(set-info :license "https://creativecommons.org/licenses/by/4.0/")
(set-info :category "industrial")
(set-info :status unknown)



(declare-fun T_1 () Bool)
(declare-fun var_0xINPUT_94964 () String)
(assert (= T_1 (not (= "file:" var_0xINPUT_94964))))
(assert T_1)
(check-sat)

(exit)
