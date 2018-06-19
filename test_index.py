import unittest
import sys
import os
import logging
import filecmp
import shutil

import vcf_filter
import vcftools
import ruffus
import itertools
from itertools import combinations



class filterTest(unittest.TestCase): 
      newpath = ['/home/staff/asukeshkall/Downloads/Test/Run/test1','/home/staff/asukeshkall/Downloads/Test/Run/test2','/home/staff/asukeshkall/Downloads/Test/Run/test3']
    
      file_names = ['out.removed.sites', 'out.kept.sites','out.recode.vcf','out.recode.bcf','res.removed.sites','res.kept.sites','res.recode.vcf','res.recode.bcf']

      list_names = ['fnameFilter', 'outKeptSitesFilter', 'resRemSitesFilter', 'resKeptSitesFilter', 'outVcfFilter', 'outBcfFilter', 'resVcfFilter', 'resBcfFilter']

      file1 = [['merged_chr1_1000.vcf.gz'], ['merged_chr1_1000.vcf.gz', '--out-prefix', 'out'], ['merged_chr1_1000.vcf.gz', '--out-prefix', 'res']]

      idx1 = [a for a,x in enumerate(file_names)]
      idx2 = [b for b,x in enumerate(list_names)]


      def testFunc(lname,fn,np):
          for t in lname:
              print t
              #vcf_filter.run(t)
              #self.assertTrue(os.path.isfile(file_names[fn]))
              #self.assertTrue(os.path.isfile(file_names[fn]+'.log'))     
          #shutil.move(file_names[fn], newpath[np])
          #shutil.move(file_names[fn]+'.log', newpath[np])

#===================================================================================#
      testFunc('file1', '0', '0')
        #testFunc('outFilter', 0, 1)

if __name__ == '__main__':
    unittest.main()
