import sys
from ruffus import *
import logging
import vcf_calc
import vcf_filter


starting_files = ['merged_chr1_1000.vcf.gz']


def exp_handler(type,val,tb):
    logging.exception("Error: %s" % (str(val)))

sys.excepthook = exp_handler

@transform(starting_files,
           suffix(".vcf.gz"),
           ".recode.bcf")
def run_vcf_to_filter(vcf_in,seq_out):
    args = [vcf_in]
    vcf_filter.run(args)


@transform(run_vcf_to_filter,
           suffix(".recode.bcf"),
           ".frq")
def run_vcf_to_calc(f_in,f_out):
    args = [f_in,
             '--calc-statistic', 'freq',
                      '--out', 'out']
    vcf_calc.run(args)
    

def mainpipe():
    pipeline_run()


if __name__ == '__main__':
    mainpipe()
