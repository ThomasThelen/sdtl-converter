#  This example reads a Deposit amount and an interest Rate
#  It computes the amount of Interest
#  The Rate variable is dropped

setwd("~/ICPSR/Project development/metadata_capture/Prov")
library(tidyverse)
Deposits1 <- read_csv("Deposits.csv")
Deposits1 <- mutate(Deposits1, Interest = Deposit * Rate)
Account <- select(Deposits1, -Rate  )
write.csv(Account, 'account.csv')