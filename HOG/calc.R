# this code takes distances between images as input and calculates accuracy rates of
# euclidean, chi sq, cosine sim.

getwd()
setwd("/Users/boyaronur/Desktop")
rm(list=ls())

euc <- read.csv('euclidean_cuhk_man_ph_denoise.csv', header = F)
#euc <- read.csv('euclidean_ar_women_all_sigma_15_photo_1.5_sketch.csv', header = F)
#euc <- read.csv('/Users/boyaronur/Desktop/FACE/CUHK_FINAL_RESULTS/euclidean_cuhk_man_all.csv', header = F)
#euc <- read.csv('/Users/boyaronur/Desktop/FACE/man_ar/euclidean_ar_man_full_1.5zoom.csv', header = F)
#euc <- read.csv('/Users/boyaronur/Desktop/FACE/man_ar/euclidean_ar_women_full.csv', header = F)
counter <- 0
for (i in 1:70){
  min <- which.min(euc[i,])
  if(min==i){
    print(min)
    counter = counter+1
  }
}

cos <- read.csv('cosine_cuhk_man_ph_denoise.csv', header = F)
#cos <- read.csv('cosine_ar_women_all_sigma_15_photo_1.5_sketch.csv', header = F)
#cos <- read.csv('/Users/boyaronur/Desktop/FACE/CUHK_FINAL_RESULTS/cosine_cuhk_man_all.csv', header = F)
#cos <- read.csv('/Users/boyaronur/Desktop/FACE/man_ar/cosine_ar_man_full_1.5zoom.csv', header = F)
#cos <- read.csv('/Users/boyaronur/Desktop/FACE/man_ar/cosine_ar_women_full.csv', header = F)
counter <- 0
for (i in 1:123){
  min <- which.min(cos[i,])
  if(min==i){
    counter = counter+1
  }
}

chi <- read.csv('chi_sq_cuhk_man_ph_denoise.csv', header = F)
#chi <- read.csv('chi_sq_ar_women_all_sigma_15_photo_1.5_sketch.csv', header = F)
#chi <- read.csv('/Users/boyaronur/Desktop/FACE/CUHK_FINAL_RESULTS/chi_sq_cuhk_man_all.csv', header = F)
#chi <- read.csv('/Users/boyaronur/Desktop/FACE/man_ar/chi_sq_ar_man_full_1.5zoom.csv', header = F)
#chi <- read.csv('/Users/boyaronur/Desktop/FACE/man_ar/chi_sq_ar_women_full.csv', header = F)

counter <- 0
for (i in 1:123){
  min <- which.min(chi[i,])
  if(min==i){
    counter = counter+1
  }
}

male <- chi[1:14,1:14]

counter <- 0
for (i in 1:14){
  min <- which.min(male[i,])
  if(min==i){
    counter = counter+1
  }
}

# 22,23,24,24
which.min(euc[24,])

