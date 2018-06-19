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
           ".recode.vcf.gz")
def run_vcf_to_filter(vcf_in,seq_out):
    args = [vcf_in,
            '--out-format', 'vcf.gz',
            '--out-prefix', 'merged_chr1_10000']
    vcf_filter.run(args)


@transform(run_vcf_to_filter,

           suffix(".recode.vcf.gz"),
           ".windowed.pi")
def run_vcf_to_calc(f_in,f_out):
    args = [f_in,
            '--calc-statistic', 'windowed-pi',
            '--out-prefix', 'merged_chr1_10000',
            '--model-file','input.model',
            '--model', '2Pop',
            '--overwrite']
    print (f_in)
    print (args)
    vcf_calc.run(args)

@transform(run_vcf_to_calc,
           suffix(".windowed.pi"),
           ".tsv")
def run_vcf_to_sampler(f_in,f_out):
    args = [starting_files[0],
                         '--statistic-file',f_in,
                         '--sample-size', '20',
                         '--random-seed', '1000',
                         '--overwrite']
    print (args)
    vcf_sampler.run(args)


def mainpipe():
    pipeline_run()


if __name__ == '__main__':
    mainpipe()
