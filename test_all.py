import unittest
import sys
import os
import logging
import filecmp
import shutil

import vcf_filter
import vcf_calc
import vcftools
import ruffus
import model
import model_creator
from itertools import combinations
import itertools
from ruffus import *



class calcTest(unittest.TestCase):
   def test_calc_run_1(self):
       comb = []

       a=[['merged_chr1_1000.vcf.gz'],['--out-prefix','merged_chr1_1000'],['--out-format','removed_sites'],['--out-format','kept_sites'],['--model-file', 'input.model'],['--model', '2Pop'],['--out-format','vcf'],['--out-format','bcf'],['--filter-min-alleles', '2'],['--filter-max-alleles', '4']]

       for i in range(len(a)):

           b = list(combinations(a, i+1))
           c = map(list, b)
           comb.append(c)

           whole_list = []

           for x in comb:
               for y in x:
                   b = list(itertools.chain.from_iterable(y))
                   whole_list.append(b)
              #print b
           m = whole_list
      #print m

#========================================================#
       filter1 = []      

       for x in whole_list:
           if not 'merged_chr1_1000.vcf.gz' in x:
              filter1.append(x)
       #for t in filter1:
           #print t



       app = []
       unmatched = []

       for m in filter1:  
           for x,y in itertools.combinations(m, 2):  
               if x == y:
                  app.append(m) 
        
       unmatched = [d for d in filter1 if d not in app]

       #for t in unmatched:
           #print t

#========================================================#



       comb1 = []

       calc=[['merged_chr1_1000.vcf.gz'],['--out-prefix','merged_chr1_1000'],['--model-file', 'input.model'],['--model', '2Pop'],['--calc-statistic', 'weir-fst'],['--calc-statistic', 'windowed-weir-fst'],['--calc-statistic', 'TajimaD'],['--calc-statistic', 'windowed-pi'],['--calc-statistic', 'freq'],['--calc-statistic', 'het-fit'], ['--calc-statistic', 'het-fis'],['--statistic-window-size', '2'],['--statistic-window-step', '2']]

       for i in range(len(calc)):

           b = list(combinations(calc, i+1))
           c = map(list, b)
           comb1.append(c)

       whole_list_calc = []

       for x in comb1:
           for y in x:
               b = list(itertools.chain.from_iterable(y))
               whole_list_calc.append(b)
               #print b
       m = whole_list_calc




       filList1_calc = []
       filList2_calc = []
       filList3_calc = []

 
       final = []
    
       for z,m in enumerate(m):
 
           if all(x in m for x in ['merged_chr1_1000.vcf.gz','--model-file','--model']):
              #print m
              final.append(m)

    

       unmatched_calc = []

       for e in final:
           if e.count('--calc-statistic')>1 or e.count('--out-prefix')>1:
              unmatched_calc.append(e)
       #print unmatched
               

       unmatched1 = [d for d in final if d not in unmatched_calc]  
    
       #for t in unmatched1:
           #print t 


       for sublist in unmatched1:
           del sublist[0]

       #for t in unmatched1:
           #print t 

        
#========================================================#


       starting_files = ['merged_chr1_1000.vcf.gz']


       def exp_handler(type,val,tb):
           logging.exception("Error: %s" % (str(val)))
  
       sys.excepthook = exp_handler

       @transform(starting_files,
           suffix(".vcf.gz"),
           ".recode.vcf")
       def run_vcf_to_filter(vcf_in,seq_out):

           a = [vcf_in]
  
           b = []

           c = []

           for i in range(len(unmatched)):
               b = unmatched[i]
               b.insert(0,a[0])
               c.append(b)

           rem_sites_filter = []

           #rem_sites_filter.append(c[0])
    
           for z,m in enumerate(c):
 
               if all(x in m for x in ['--out-prefix','vcf','--model-file','--model']):                
                  rem_sites_filter.append(m)

           for t in rem_sites_filter:
               print t 

           
           #print "====================================="  
 
 
           vcf_filter.run(rem_sites_filter[0])
           self.assertTrue(os.path.isfile('merged_chr1_1000.recode.vcf'))
           self.assertTrue(os.path.isfile('merged_chr1_1000.recode.vcf.log'))
            
           
       

               #self.addCleanup(os.remove, 'merged_chr1_1000.recode.bcf')
               #self.addCleanup(os.remove, 'merged_chr1_1000.recode.bcf.log')

       @transform(run_vcf_to_filter,
        
           suffix(".recode.vcf"),
           ".windowed.weir.fst")
       def run_vcf_to_calc(f_in,f_out):

           a1 = [f_in]
  
           b1 = []

           c1 = []

           for i in range(len(unmatched1)):
               b1 = unmatched1[i]
               b1.insert(0,a1[0])
               c1.append(b1)
           
           for t in c1:
               print t
         

           vcf_calc.run(c1[11])
           self.assertTrue(os.path.isfile('merged_chr1_1000.windowed.weir.fst'))
           self.assertTrue(os.path.isfile('merged_chr1_1000.windowed.weir.fst.log'))
           #args = [f_in,
           # '--calc-statistic', 'het',
           # '--out-prefix', 'merged_chr1_1000']
           #vcf_calc.run(args)
           #self.assertTrue(os.path.isfile('merged_chr1_1000.het'))
           #self.assertTrue(os.path.isfile('merged_chr1_1000.het.log'))

    

       pipeline_run()

        #vcf_filter.run(t)
            #self.assertTrue(os.path.isfile('merged_chr1_1000.recode.bcf'))
           # self.assertTrue(os.path.isfile('merged_chr1_1000.recode.bcf.log'))
        


if __name__ == "__main__":
    pipeline_run()
    unittest.main()
