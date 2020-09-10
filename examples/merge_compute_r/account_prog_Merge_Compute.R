#  This example merges Deposit amount and an interest Rate from a different files
#  It computes the amount of Interest

setwd("~/ICPSR/Project development/metadata_capture/Prov/Prov_R_examples")
library(tidyverse)
Deposit_only <- read_csv("Deposit_only.csv")
Rate_only <- read_csv("Rate_only.csv")

Accounts_all <- full_join(Deposit_only, Rate_only, by="AcctNo")

Accounts_all <- mutate(Deposits_all, Interest = Deposit * Rate)


write.csv(Accounts_all, 'account_2.csv')
