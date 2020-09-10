GET     FILE='deposits.sav'.
compute Interest = Deposit * Rate.
execute.

save outfile='accounts.sav'.
EXECUTE.
