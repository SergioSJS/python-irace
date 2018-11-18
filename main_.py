import argparse
import logging
#import matplotlib.pyplot as plt
#import multiprocessing
import numpy as np
#import pandas as pd
import random
import sys

def main(POP, CXPB, MUTPB, DATFILE):
	score = MUTPB*POP/100
	score = float(score)
	score = score - float(CXPB)
	if score < 0:
		score = 0
	# random.seed(64)

	with open(DATFILE, 'w') as f:
		f.write(str(score*100))

if __name__ == "__main__":
	ap = argparse.ArgumentParser(description='Feature Selection using GA with DecisionTreeClassifier')
	ap.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
	ap.add_argument('--pop', dest='pop', type=int, required=True, help='Population size')
	ap.add_argument('--cros', dest='cros', type=float, required=True, help='Crossover probability')
	ap.add_argument('--mut', dest='mut', type=float, required=True, help='Mutation probability')
	ap.add_argument('--datfile', dest='datfile', type=str, required=True, help='File where it will be save the score (result)')

	args = ap.parse_args()
	logging.debug(args)

	main(args.pop, args.cros, args.mut, args.datfile)