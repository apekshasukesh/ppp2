import sys
from ruffus import *
import logging
import vcf_calc
import vcf_filter
import vcf_sampler


starting_files = ['merged_chr1_10000.vcf.gz']


def exp_handler(type,val,tb):
    logging.exception("Error: %s" % (str(val)))

sys.excepthook = exp_handler

@transform(starting_files,
           suffix(".vcf.gz"),
           ".recode.bcf")
def run_vcf_to_filter(vcf_in,seq_out):
    args = [vcf_in,
            '--out-format', 'bcf',
            '--out-prefix', 'merged_chr1_10000']
    vcf_filter.run(args)

def mainpipe():
    pipeline_run()


if __name__ == '__main__':
    mainpipe()
