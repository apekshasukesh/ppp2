import unittest
import sys
import os
import logging
import filecmp
import shutil

import vcf_calc
import vcf_filter
import vcftools
import ruffus
import itertools
from itertools import combinations



class calcTest(unittest.TestCase):
 
#=================================function to make dir and sub -dir #================================#


    def test_calc_run_1(self):
        for i in range(1,2):
            os.makedirs(os.path.join('/home/staff/asukeshkall/Downloads/Test-3/Run/withoutPrefix', 'withoutCalcStat'))
        for i in range(1,7):
            os.makedirs(os.path.join('/home/staff/asukeshkall/Downloads/Test-3/Run/withoutPrefix', 'withoutPrefixCalcStat' + str(i)))
        for i in range(1,7):
            os.makedirs(os.path.join('/home/staff/asukeshkall/Downloads/Test-3/Run/outPrefix', 'outPrefixCalcStat' + str(i)))
        for i in range(1,7):
            os.makedirs(os.path.join('/home/staff/asukeshkall/Downloads/Test-3/Run/resPrefix', 'resPrefixCalcStat' + str(i)))

#============================# Create path names to move the generated o/p files #===================#
        defaultPath = []
        outWinWeirPath = []
        outWeirPath = []
        outTajimaPath = []
        outPiPath = []
        outFreqPath = []
        outHetPath = []
        filenamee = 'test'
        counter1 = 1
        counter2 = 2
        list1 = []
        list2 = range(20)    #random number, given len needed
        for x in list2:
            counter1 = str(counter1)
            full_name = (filenamee+counter1)
            list1.append(full_name)
            counter1 = counter2
            counter2+=1

        for x in list1[:4]:
            y = "/home/staff/asukeshkall/Downloads/Test-3/Run/test1"+ x
            defaultPath.append(y)
            z = "/home/staff/asukeshkall/Downloads/Test-3/Run/test2"+ x
            outWinWeirPath.append(y)


        #for x in list1[8:12]:
            #y = "/home/staff/asukeshkall/Downloads/Test/Run/test2"+ x
            #outWeirPath.append(y)


if __name__ == '__main__':
    unittest.main()



