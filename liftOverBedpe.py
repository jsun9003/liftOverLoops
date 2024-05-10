#!/usr/bin/env python3

import argparse
import os
import subprocess

def split_bedpe(bedpe_file, output_tmp1="tmp1.bed", output_tmp2="tmp2.bed", has_header=False):
    with open(output_tmp1, 'w') as t1, open(output_tmp2, 'w') as t2, open(bedpe_file, 'r') as bedpein:
        if has_header:
            headerline = bedpein.readline()
        name = 0
        for line in bedpein:
            name += 1
            fields = line.strip().split("\t")
            print("\t".join(fields[0:3] + ['name' + str(name)] + [fields[6]]), file=t1)
            print("\t".join(fields[3:6] + ['name' + str(name)] + [fields[6]]), file=t2)

def run_lift_over(lift_over_path, chain_file, input_file, verbose=False):
    cmd = [lift_over_path, input_file, chain_file, input_file + ".success", input_file + ".failure"]
    print("liftOver".join(cmd))
    if verbose:
        print(" ".join(cmd))
    subprocess.run(cmd, check=True)

def merge_lift_overed_files(tmp1_success, tmp2_success, output_file, verbose=False):
    data_dict = {}
    with open(tmp1_success, 'r') as f1:
        for line in f1:
            fields = line.strip().split('\t')
            data_dict[fields[3]] = fields[:6]

    with open(output_file, 'w') as output:
        with open(tmp2_success, 'r') as f2:
            for line in f2:
                fields = line.strip().split('\t')
                if fields[3] in data_dict:
                    r1 = data_dict[fields[3]]
                    r2 = fields
                    print("\t".join(r1[:3] + r2[:3] + [r2[4]]), file=output)

def main():
    parser = argparse.ArgumentParser(description='wrapper for liftOver to accommodate bedpe files',
                                     epilog='''Example:
liftOverBedpe.py --lift /usr/bin/liftOver --chain ~/mm9ToMm10.over.chain.gz --i input.bedpe --o output.bed --v --h
''')
    parser.add_argument('--lift', dest='lift_over', help='path to liftOver', required=True)
    parser.add_argument('--chain', dest='chain_file', help='path to chain file', required=True)
    parser.add_argument('--i', dest='input_file', help='input file in BEDPE format', required=True)
    parser.add_argument('--o', dest='output_file', help='output file', required=True)
    parser.add_argument('--v', dest='verbose', help='verbose mode', action='store_true')
    parser.add_argument('--h', dest='has_header', help='set if input file has header line', action='store_true')

    args = parser.parse_args()

    lift_over_path = args.lift_over
    chain_file = args.chain_file
    input_file = args.input_file
    output_file = args.output_file
    verbose = args.verbose
    has_header = args.has_header

    tmp1 = "tmp1.bed"
    tmp2 = "tmp2.bed"

    split_bedpe(input_file, tmp1, tmp2, has_header)

    run_lift_over(lift_over_path, chain_file, tmp1, verbose)
    run_lift_over(lift_over_path, chain_file, tmp2, verbose)

    merge_lift_overed_files(tmp1 + ".success", tmp2 + ".success", output_file, verbose)

    # remove tmp files
    os.remove(tmp1)
    os.remove(tmp2)
    os.remove(tmp1 + ".success")
    os.remove(tmp1 + ".failure")
    os.remove(tmp2 + ".success")
    os.remove(tmp2 + ".failure")

if __name__ == "__main__":
    main()
