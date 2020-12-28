# .libPaths("/home/gribble/work/rPackages")
# install.packages("devtools")
# library(devtools)

# library("zoo", lib.loc="C:/software/Rpackages")
# devtools::install_github("mtoto/ufc.stats")
install.packages("dplyr")
library(dplyr)

stats <- load(file = "ufc_stats.rda", verbose = TRUE)
print(stats)
