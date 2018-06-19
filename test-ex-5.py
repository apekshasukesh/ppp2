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


#=================================function to make dir and sub -dir #================================#

  
for i in range(1,61):
    os.makedirs(os.path.join('Run', 'test' + str(i))) 

#============================# Create path names to move the generated o/p files #===================#
newpath = []
filenamee = 'test'
counter1 = 1
counter2 = 2
list1 = []
list2 = range(61)    #random number, given len needed
for x in list2:
    counter1 = str(counter1)
    full_name = (filenamee+counter1)
    list1.append(full_name)
    counter1 = counter2
    counter2+=1

for x in list1:
    y = "/home/staff/asukeshkall/Downloads/Test-3/Run/"+ x
    newpath.append(y)        

#================================================# Generate all combinations  #=======================================================================#

filter_list=[['merged_chr1_10000.vcf.gz'],['--out-prefix','merged_chr1_10000'],['--out-format','removed_sites'],['--out-format','kept_sites'],['--out-format','vcf'],['--out-format','bcf'],['--filter-min-alleles', '2'],['--filter-max-alleles', '4']]

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

filFunc('merged_chr1_10000', fnameFilter, filList2)
prefixFilter = filList2
#for t in prefixFilter:
    #print t
    #print "--------------"

#============================= input =====================#

calc_comb = combFunc(calc_list)

filFunc('Paniscus.txt', calc_comb, filList3)
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
#for t in range(0,200):
    #print t, statFilter[t]
    #print "--------------"

#======================# Filter level 2 - to filter the redundant options #===================================#

app = []
for m in fnameFilter:  
    for x,y in itertools.combinations(m, 2):  
        if x == y:
           app.append(m) 
        
filter_final_list = [d for d in prefixFilter if d not in app]
#for t in filter_final_list:
    #print t

#================================================================================================#

list1 = []

for x in filter_final_list:
    for y in x:
        if y == 'bcf':
           list1.append(x)

for t in list1:
    print t


list2 = [['--out-prefix', 'merged_chr1_10000', '--pop-file', 'Paniscus.txt', '--pop-file', 'Troglodytes.txt', '--model-file', 'input.model', '--model', '2Pop', '--calc-statistic', 'windowed-weir-fst'],
       ['--out-prefix', 'merged_chr1_10000', '--pop-file', 'Paniscus.txt', '--pop-file', 'Troglodytes.txt', '--model-file', 'input.model', '--model', '2Pop', '--calc-statistic', 'windowed-weir-fst','--statistic-window-size','2'],
       ['--out-prefix', 'merged_chr1_10000', '--pop-file', 'Paniscus.txt', '--pop-file', 'Troglodytes.txt', '--model-file', 'input.model', '--model', '2Pop', '--calc-statistic', 'windowed-weir-fst','--statistic-window-step','2'],
       ['--out-prefix', 'merged_chr1_10000', '--pop-file', 'Paniscus.txt', '--pop-file', 'Troglodytes.txt', '--model-file', 'input.model', '--model', '2Pop', '--calc-statistic', 'windowed-weir-fst','--statistic-window-size','2','--statistic-window-step','2']]



list3 = [['merged_chr1_10000.vcf.gz',
                         '--statistic-file', 'merged_chr1_10000.windowed.weir.fst',
                         '--out-prefix', 'merged_chr1_10000',
                         '--sample-size', '20',
                         '--random-seed', '1000',
                         '--overwrite'],
         ['merged_chr1_10000.vcf.gz',
                         '--statistic-file', 'merged_chr1_10000.windowed.weir.fst',
                         '--out-prefix', 'merged_chr1_10000',
                         '--sample-size', '10',
                         '--random-seed', '1000',
                         '--uniform-bins','10',
                         '--overwrite'],
         ['merged_chr1_10000.vcf.gz',
                         '--statistic-file', 'merged_chr1_10000.windowed.weir.fst',
                         '--out-prefix', 'merged_chr1_10000',
                         '--sample-size', '20',
                         '--random-seed','254',
                         '--overwrite'],
         ['merged_chr1_10000.vcf.gz',
                         '--statistic-file', 'merged_chr1_10000.windowed.weir.fst',
                         '--out-prefix', 'merged_chr1_10000',
                         '--sample-size', '20',
                         '--random-seed', '1000',
                         '--statistic-window-size','10000',
                         '--overwrite']]

#======================# Filter level 2 - to filter the redundant options #===================================#

calc_unmatched = []
for e in trogFilter:
    if e.count('--calc-statistic')>1 or e.count('--out-prefix')>1:
       calc_unmatched.append(e)
        #print unmatched
               
calc_final_list = [d for d in trogFilter if d not in calc_unmatched]  

#for t in calc_final_list:
    #print t


#=============================================================================================================#

starting_files = ['merged_chr1_10000.vcf.gz']

#file_names = ['merged_chr1_10000.removed.sites', 'merged_chr1_10000.kept.sites','merged_chr1_10000.recode.vcf','merged_chr1_10000.recode.bcf']

def exp_handler(type,val,tb):
    logging.exception("Error: %s" % (str(val)))

sys.excepthook = exp_handler

def pipe1(name1,name2):
        @transform(starting_files,
           suffix(".vcf.gz"),
           name1)
        def run_vcf_to_filter(vcf_in,seq_out):   
            for i in range(len(list1)):  
                print len(list1)    
           # args = filter_final_list[4]
                args = list1[i]
                print args
                vcf_filter.run(args)
                print 'hello'
                print newpath[i]
                shutil.move('merged_chr1_10000'+name1, newpath[i])
                shutil.move('merged_chr1_10000'+name1+'.log', newpath[i])
        
            shutil.move('/home/staff/asukeshkall/Downloads/Test-3/Run/test1/merged_chr1_10000.recode.bcf','/home/staff/asukeshkall/Downloads/Test-3/')
            #shutil.move('/home/staff/asukeshkall/Downloads/Test-3/Run/'+folder+'/merged_chr1_10000.recode.bcf','/home/staff/asukeshkall/Downloads/Test-3/')
             #shutil.move('merged_chr1_10000'+name1+'.log', newpath[i])        
                #os.remove('merged_chr1_10000.recode.bcf')
                #os.remove('merged_chr1_10000.recode.bcf.log')
                

        @transform(run_vcf_to_filter,
           suffix(name1),
           name2)
        def run_vcf_to_calc(f_in,f_out):
            for i in range(len(list2)):  
                print len(list2) 
                args = ['merged_chr1_10000.recode.bcf']+calc_final_list[123]
            #args = newpath[1]+"/merged_chr1_10000.recode.bcf"+calc_final_list[123]
                print f_in
                print args
                vcf_calc.run(args)
                print 'hello'
                print newpath[i]
                shutil.move('merged_chr1_10000'+name2, newpath[i])
                shutil.move('merged_chr1_10000'+name2+'.log', newpath[i])

            shutil.move('/home/staff/asukeshkall/Downloads/Test-3/Run/test1/merged_chr1_10000.windowed.weir.fst','/home/staff/asukeshkall/Downloads/Test-3/')
            #shutil.move('/home/staff/asukeshkall/Downloads/Test-3/Run/'+folder+'/merged_chr1_10000.windowed.weir.fst','/home/staff/asukeshkall/Downloads/Test-3/')

        @transform(run_vcf_to_calc,
           suffix(name2),
           ".tsv")
        def run_vcf_to_sampler(f_in,f_out):
            for i in range(len(list3)):
                print len(list3)
                args = statFilter[i]
                print args
                vcf_sampler.run(args)
                print 'hello'
                print newpath[i]
                shutil.move('sampled_data.tsv', newpath[i])
                shutil.move('Sample_Files', newpath[i])

        
            shutil.move('/home/staff/asukeshkall/Downloads/Test-3/merged_chr1_10000.recode.bcf','/home/staff/asukeshkall/Downloads/Test-3/Run/test1')
            shutil.move('/home/staff/asukeshkall/Downloads/Test-3/merged_chr1_10000.windowed.weir.fst','/home/staff/asukeshkall/Downloads/Test-3/Run/test1')
            #shutil.move('/home/staff/asukeshkall/Downloads/Test-3/merged_chr1_10000.recode.bcf','/home/staff/asukeshkall/Downloads/Test-3/Run/'+folder)
            #shutil.move('/home/staff/asukeshkall/Downloads/Test-3/merged_chr1_10000.windowed.weir.fst','/home/staff/asukeshkall/Downloads/Test-3/Run/'+folder)
        #pipeline_run()


pipe1(".recode.bcf",".windowed.weir.fst")
#pipe1(".recode.bcf",".windowed.weir.fst","test2")




#pipe1(".recode.vcf",3)
#pipe1(".removed.sites",3)
#pipe1(".kept.sites",4)



def mainpipe():
    pipeline_run()


if __name__ == '__main__':
    mainpipe()


