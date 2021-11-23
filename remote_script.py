import pandas
import random
import argparse


def read_random_lines(input_path,sample_size:int):
    line_numbers = sum(1 for line in open(input_path))
    skip = sorted(random.sample(range(line_numbers),line_numbers-sample_size))
    df = pandas.read_csv(input_path,skiprows=skip)
    return df



def write_file(output_path,df):
    df.to_csv(output_path)








parser = argparse.ArgumentParser(description='Copy a random sample from a file')
parser.add_argument('-s','--source',metavar='filename')
parser.add_argument('-d','--destination',metavar='filename')
args = parser.parse_args()
input_file = args.source
output_file = args.destination

df = read_random_lines(input_file,100)
write_file(output_file,df)




