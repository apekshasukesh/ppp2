import sys
from ruffus import *
import logging
#from logging_module import individualFunctionLogger, pipeSwitchLogger
#from dir_test import test_filter_run_1
#from dir_test import test_freq
from dir_test import * 

#start_list = open(str(sys.argv[1:]),'r')
#starting_files = [line.strip() for line in start_list]
#formatLogger()
starting_files = ['merged_chr1_1000.vcf.gz']

#fmt_def = "%(asctime)s - %(levelname)s: %(message)s"
#fmtr = logging.Formatter(fmt=fmt_def)
#logging.basicConfig(filename='example/chr11.pipe.log',filemode="w",level=logging.INFO,format=fmt_def)

#def exp_handler(type,val,tb):
    #logging.exception("Error: %s" % (str(val)))

#sys.excepthook = exp_handler

@transform(starting_files,
           suffix(".vcf.gz"),
           ".recode.bcf")
def run_vcf_to_filter(vcf_in,seq_out):
    #args = ['merged_chr1_1000.vcf.gz']
    test_filter_run_1()


@transform(run_vcf_to_filter,
           suffix(".recode.bcf"),
           ".frq")
def run_vcf_to_calc(vcf_in,seq_out):
    #args = ['merged_chr1_1000.vcf.gz',
                     # '--calc-statistic', 'freq',
                     # '--out', 'out']
    test_freq()

def mainpipe():
    pipeline_run()


if __name__ == '__main__':
    mainpipe()
