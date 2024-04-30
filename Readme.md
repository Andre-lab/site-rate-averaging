# Mansucript repo
This a repository for data from the manuscript "Improved prediction of site-specific evolutionary rates from structure by averaging across homologs"

The repo contains:
1. The python script to calculate site-rates from ddG values, and an example command line
2. Example command line for calculating ddG values from a protein structure
3. Data from the manuscript

# Site-rates from TMS
TMS calculations requires the script calc_rates.py, which calls RateCalculator/RateCalculator.py

```console

scripts/calc_rates.py --ranks ranks_xtal/1pga.txt --fasta fasta/1pga.fasta --score_style Rosetta

```
```--ranks``` specifies the ddG values in a list with the format

pos | amino acid type | ddG relative to wildtype | wt yes no?

1 A -4.033 0

1 D 0.2 1

1 E -4.502 0

.
.
.

```--fasta``` specifies a path to a fasta file for the sequence (the script will use this and not the seqeuence in the rank file)

```--score_style``` specfies the type of data that is provided. 'Rosetta' is ddGs predicted by Rosetta (or other software) while 'Experimental' is experimental data.
if other sofware and energy functions are used for ddG calculations are used, the slope parameter (R*T factor in the Boltzmann equation) may need to be adjusted. 

# Rosetta ddG calculations
In this study we used a version of the Rosetta ddG prediction protocol to calculate the effect of mutations on the stability of proteins. The method is accessible through Rosetta Scripts as part of RosettaEvolve.
More documentation on RosettaEvolve is found in the article [Atomistic simulation of protein evolution reveals sequence covariation and time-dependent fluctuations of site-specific substitution rates](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010262) and the corresponding [repo](https://github.com/Andre-lab/RosettaEvolve). An example command line is provided below for calculation of rank files used in this study is shown below, with the input files found in the repo. 

```rosetta_scripts.default.linuxgccrelease -s $pdb -parser:protocol protocols/measure_ranks.xml @flags```

# RosettaEvolve simulations
Evolutionary trajectories were simulated using RosettaEvolve, which is distributed as part of the [Rosetta macromolecular modeling package](https://github.com/RosettaCommons/rosetta). Instructions on how to run RosettaEvolve can be found at the repo for the [RosettaEvolve](https://github.com/Andre-lab/RosettaEvolve) manuscript describing the method [Atomistic simulation of protein evolution reveals sequence covariation and time-dependent fluctuations of site-specific substitution rates](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010262).









