use "AgeDeath.dta"
replace age = 5*int(age/5)
save "AgeDeath5"
