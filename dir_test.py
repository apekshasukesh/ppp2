import unittest
import sys
import os
import logging
import filecmp
import shutil
import vcf_filter
import vcftools
import vcf_calc
from ruffus import *


class filterTest(unittest.TestCase):
    
    runpath= "/home/staff/asukeshkall/Downloads/Test/Run"
    if not os.path.exists(runpath):
       os.makedirs(runpath)
    

    def test_filter_run_1(self):
        newpath= "/home/staff/asukeshkall/Downloads/Test/Run/test_1"
        if not os.path.exists(newpath):
           os.makedirs(newpath)

        vcf_filter.run(['merged_chr1_1000.vcf.gz', '--out-format', 'vcf'])

        # Confirm that the output is what is expected      
        self.assertTrue(os.path.isfile('out.filter.log'))
        self.assertTrue(os.path.isfile('out.recode.vcf'))

        # Move the files to the new test folder
        shutil.move('out.filter.log', newpath)
        shutil.move('out.recode.vcf', newpath)
         
        # Remove the ouput and log files created by the function
        #self.addCleanup(os.remove, 'out.filter.log')
        #self.addCleanup(os.remove, 'out.recode.bcf')
 
        
    #def test_filter_run_2(self):
        #newpath= "/home/staff/asukeshkall/Downloads/Test/Run/test_2"
        #if not os.path.exists(newpath):
         #  os.makedirs(newpath)

        #vcf_filter.run(['merged_chr1_1000.vcf.gz',
                   # '--out', 'res'])

        # Confirm that the output is what is expected      
        #self.assertTrue(os.path.isfile('res.filter.log'))
        #self.assertTrue(os.path.isfile('res.recode.bcf'))

        #shutil.move('res.filter.log', newpath)
        #shutil.move('res.recode.bcf', newpath)

         
        # Remove the ouput and log files created by the function
        #self.addCleanup(os.remove, 'res.filter.log')
        #self.addCleanup(os.remove, 'res.recode.bcf')
   # Check that the allele frequency function is operating correctly
    
    def test_freq (self):
        # Run the function with the following arguments
        vcf_calc.run(['merged_chr1_1000.vcf.gz',
                      '--calc-statistic', 'freq',
                      '--out', 'out'])

        # Confirm that the output is what is expected
        #self.assertTrue(file_comp('out.frq', 'example/merged_chr1_10000.frq'))

        
        # Confirm that the output is what is expected      
        self.assertTrue(os.path.isfile('out.frq'))
        self.assertTrue(os.path.isfile('out.frq.log'))
         
        # Move the files to the new test folder
        #shutil.move('out.frq', newpath)
        #shutil.move('out.frq.log', newpath)


        # Remove the ouput and log files created by the function
        #self.addCleanup(os.remove, 'out.frq')
        #self.addCleanup(os.remove, 'out.frq.log')


    

if __name__ == "__main__":
    unittest.main()
