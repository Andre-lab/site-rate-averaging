from RatesCalculator import RatesCalculator
import glob
import csv
import argparse

def get_native_aa(path):
    aa = []
    with open(path, 'r') as f:
        line = f.readline()
        line = f.readline()
        for a in line:
            if a != '\n':
                aa.append(a)
    return aa

parser = argparse.ArgumentParser(description='site-rates from ddG values')
parser.add_argument('-r', '--ranks', help="Ranks file containing ddG values", default=".", required=True)
parser.add_argument('-f', '--fasta', help="fasta file for sequence", default=".", required=True)
parser.add_argument('-n', '--name', help="site rates", default="site.")
parser.add_argument("-o", '--out_dir',help="Paths to the output dir", default="rosrates")
parser.add_argument("-d", '--dG',help="dG stability", default=5.5,type=float)
parser.add_argument("-s", '--score_style',help="score_style", default="Rosetta")
args = parser.parse_args()

deltaG=args.dG
score_style = args.score_style
path = args.ranks
fasta_path = args.fasta
print(fasta_path)
aas= get_native_aa(args.fasta)
seqname = args.name
outdir = args.out_dir

rates=RatesCalculator.RatesCalculator(path,score_style,deltaG)

with open(outdir + '/' + seqname + 'ros.rate', 'w') as f:
   write = csv.writer(f)
   num_cys = 0
   for i, aa in enumerate(aas):
      if aa == 'C':
         write.writerow( [i+1, aa, 'nan' ])
         num_cys += 1
      else:
         write.writerow( [i+1, aa, rates[i-num_cys] ] )
