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
           ".tsv")
def run_vcf_to_sampler(f_in,f_out):
    args = ['merged_chr1_10000.vcf.gz',
                         '--statistic-file', 'merged_chr1_10000.Tajima.D',
                         '--out-prefix', 'merged_chr1_10000',
                         '--sample-size', '10',
                         '--random-seed', '1000',
                         '--overwrite']
    vcf_sampler.run(args)

def mainpipe():
    pipeline_run()


if __name__ == '__main__':
    mainpipe()
