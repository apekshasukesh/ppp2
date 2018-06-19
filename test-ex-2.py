import unittest
import sys
import os
import logging
import filecmp
import shutil
import vcftools
import ruffus
import itertools
import model
import model_creator
import vcf_filter
import vcf_calc
import vcf_sampler
from itertools import combinations
from ruffus import *


#================================================# Generate all combinations  #=======================================================================#
   

filter_list=[['merged_chr1_10000.vcf.gz'],['--out-prefix','merged_chr1_10000'],['--out-prefix','res'],['--out-format','removed_sites'],['--out-format','kept_sites'],['--out-format','vcf'],['--out-format','bcf'],['--filter-min-alleles', '2'],['--filter-max-alleles', '4']]

calc_list=[['--out-prefix','merged_chr1_10000'],['--pop-file', 'Paniscus.txt'],['--pop-file', 'Troglodytes.txt'],['--model-file','input.model'],['--model','2Pop'],['--calc-statistic', 'weir-fst'],['--calc-statistic', 'windowed-weir-fst'],['--calc-statistic', 'TajimaD'],['--calc-statistic', 'pi'],['--calc-statistic', 'freq'],['--calc-statistic', 'het'], ['--statistic-window-size', '2'],['--statistic-window-step', '2']]

sampler_list=[['merged_chr1_10000.vcf.gz'],['--model-file','input.model'],['--model','2Pop'],['--statistic-file','merged_chr1_10000.windowed.weir.fst'],['--sample-file','sampled_data.tsv'],['--out-dir','Sample_Files'],['--out-prefix','Sample'],['--out-format','vcf.gz'],['--overwrite'],['--calc-statistic','windowed-weir-fst'], ['--statistic-window-size','10000'],['--sampling-scheme','random'],['--uniform-bins','10'],['--sample-size','10'],['--random-seed','456']]


comb = []
whole_list = []
retList = []

def combFunc(a):
    for i in range(len(a)):
        b = list(combinations(a, i+1))
        c = map(list, b)
        comb.append(c)

    for x in comb:
        for y in x:
             b = list(itertools.chain.from_iterable(y))
             whole_list.append(b)
                #print b
    retList = whole_list
    return retList

 

#=============================================# Filter level 1 function #========================================================================#

filList1 = []
filList2 = []
filList3 = []
filList4 = []
filList5 = []
filList6 = []

def filFunc(name, lol, listname):
    for x in lol:
        for y in x:
            if y== name:
               listname.append(x) 

#============================= input =====================#

filter_comb = combFunc(filter_list)
filFunc('merged_chr1_10000.vcf.gz', filter_comb, filList1)
fnameFilter = filList1
#for t in fnameFilter:
    #print t
    #print "--------------"

#============================= input =====================#

calc_comb = combFunc(calc_list)
filFunc('merged_chr1_10000.vcf.gz', calc_comb, filList2)
fnameCalc = filList2
#for t in fnameCalc:
    #print t
    #print "--------------"

filFunc('Paniscus.txt', fnameCalc, filList3)
panFilter = filList3
#for t in panFilter:
    #print t
    #print "--------------"

filFunc('Troglodytes.txt', panFilter, filList4)
trogFilter = filList4
#for t in trogFilter:
    #print t
    #print "--------------"

#=============================input=======================#

sampler_comb = combFunc(sampler_list)
filFunc('merged_chr1_10000.vcf.gz', sampler_comb, filList5)
fnameSampler = filList5
#for t in fnameSampler:
    #print t
    #print "--------------"

filFunc('merged_chr1_10000.windowed.weir.fst', fnameSampler, filList6)
statFilter = filList6
#for t in statFilter:
    #print t
    #print "--------------"

#======================# Filter level 2 - to filter the redundant options #===================================#

app = []
for m in fnameFilter:  
    for x,y in itertools.combinations(m, 2):  
        if x == y:
           app.append(m) 
        
filter_final_list = [d for d in fnameFilter if d not in app]
#for t in filter_final_list:
    #print t

#======================# Filter level 2 - to filter the redundant options #===================================#

calc_unmatched = []
for e in trogFilter:
    if e.count('--calc-statistic')>1 or e.count('--out-prefix')>1:
       calc_unmatched.append(e)
        #print unmatched
               
calc_final_list = [d for d in trogFilter if d not in calc_unmatched]  

for t in calc_final_list:
    print t


#=============================================================================================================#

starting_files = ['merged_chr1_10000.vcf.gz']

def exp_handler(type,val,tb):
    logging.exception("Error: %s" % (str(val)))

sys.excepthook = exp_handler

@transform(starting_files,
           suffix(".vcf.gz"),
           ".recode.bcf")
def run_vcf_to_filter(vcf_in,seq_out):
    args = filter_final_list[12]
    vcf_filter.run(args)


@transform(run_vcf_to_filter,

           suffix(".recode.bcf"),
           ".windowed.weir.fst")
def run_vcf_to_calc(f_in,f_out):
    #args = [f_in]+calc_final_list[
    #print f_in
    #print args
    #vcf_calc.run(args)

def mainpipe():
    pipeline_run()


if __name__ == '__main__':
    mainpipe()




