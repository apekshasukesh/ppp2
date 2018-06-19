import sys
from ruffus import *
import logging
#from logging_module import individualFunctionLogger, pipeSwitchLogger
#from vcf_ref_to_seq import vcf_to_seq
#import vcf_calc
#import vcf_filter
#from dir_test import test_filter_run_1
#from dir_test import test_freq
from dir_test import *


start_list = open(str(sys.argv[1]),'r')
starting_files = [line.strip() for line in start_list]
#formatLogger()
#starting_files = ['merged_chr1_1000.vcf.gz']

#fmt_def = "%(asctime)s - %(levelname)s: %(message)s"
#fmtr = logging.Formatter(fmt=fmt_def)
#logging.basicConfig(filename='example/chr11.pipe.log',filemode="w",level=logging.INFO,format=fmt_def)



@transform(starting_files,
           suffix(".vcf.gz"),
           ".recode.bcf")
def run_vcf_to_filter(vcf_in,seq_out):
    #pref = vcf_in[0:-1*len(".vcf.gz")]
    #pipeSwitchLogger(pref)
    args = ['merged_chr1_1000.vcf.gz']
    filter1= filterTest()
    filter1.test_filter_run_1(args)


@transform(run_vcf_to_filter,
           suffix(".recode.bcf"),
           ".frq")
def run_vcf_to_calc(f_in,f_out):
    args = ['merged_chr1_1000.vcf.gz',
             '--calc-statistic', 'freq',
                      '--out', 'out']
    freq1=filterTest()
    freq1.test_freq(args)



def mainpipe(sysargs):
    pipeline_run()


if __name__ == '__main__':
    mainpipe(sys.argv[1])
