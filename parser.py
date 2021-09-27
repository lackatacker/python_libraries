import argparse
#create a parser + the description is shown when passing -h or --help
parser = argparse.ArgumentParser(description='Sum of two ints + displaying the user')
#adding arguments long from, short form, default value, nargs=? means we can skip the arg, choices limite the pool
#of entries
parser.add_argument('--user','-u',nargs='?',default='guest',choices=['salah','moncef','root','guest'])
parser.add_argument('--first','-f',type=int, default=0)
parser.add_argument('--second', '-s', type=int, default=0)
#we call the
args = parser.parse_args()

print('hey mr ' + args.user + ' the sum of the provided numbers is : '+f'{(args.first+args.second)}')