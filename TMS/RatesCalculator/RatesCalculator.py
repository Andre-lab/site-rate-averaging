import pickle
import os

def RatesCalculator(filepath,score_style,offset=0,N=10**2.2):

    if score_style=='Rosetta':
        s = 0.86
        #s = 1/(300*0.00199*4.98682169)
    elif score_style=='Experimental':
        s = 1/(300*0.00199)

    input = [filepath,score_style,offset,s,N]

    filename1 = 'RatesCalculator/input'

    outfile = open(filename1,'wb')

    pickle.dump(input,outfile)

    outfile.close()

    os.system('python RatesCalculator/My_version.py')

    infile = open('RatesCalculator/rates', 'rb')
    rates = pickle.load(infile)
    infile.close()

    return rates
