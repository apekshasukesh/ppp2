import sys
from ruffus import *
import logging
import vcf_calc
import vcf_filter
import vcf_sampler


starting_files = ['merged_chr1_1000.vcf.gz']


def exp_handler(type,val,tb):
    logging.exception("Error: %s" % (str(val)))

sys.excepthook = exp_handler

@transform(starting_files,
           suffix(".vcf.gz"),
           ".recode.bcf")
def run_vcf_to_filter(vcf_in,seq_out):
    args = [vcf_in,
            '--out-format', 'bcf',
            '--out-prefix', 'merged_chr1_1000']
    vcf_filter.run(args)


@transform(run_vcf_to_filter,

           suffix(".recode.bcf"),
           ".windowed.weir.fst")
def run_vcf_to_calc(f_in,f_out):
    args = [f_in,  
            '--calc-statistic', 'windowed-weir-fst',  
            '--out-prefix', 'merged_chr1_1000',
            '--model-file','input.model',
            '--model', '2Pop']
    vcf_calc.run(args)

@transform(run_vcf_to_calc,
           suffix(".vcf.gz"),
           ".tsv")
def run_vcf_to_sampler(f_in,f_out):
    args = ['merged_chr1_1000.vcf.gz',
                         '--statistic-file', 'merged_chr1_1000.windowed.weir.fst',
                         '--out-prefix', 'merged_chr1_1000',
                         '--sample-size', '20',
                         '--random-seed', '1000',
                         '--overwrite']
    vcf_sampler.run(args)


def mainpipe():
    pipeline_run()


if __name__ == '__main__':
    mainpipe()
