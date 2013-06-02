'convert VWs predictions into format suitable for submission'

import sys, csv, math

input_file = sys.argv[1]
output_file = sys.argv[2]

reader = csv.reader( open( input_file ))
writer = csv.writer( open( output_file, 'wb' ))

writer.writerow( [ 'id', 'ACTION' ] )

i = 1
for line in reader:
	raw_p = float( line[0] )
	p = math.tanh( raw_p )
	
	writer.writerow( [ i, p ] )
	i += 1
	
	
	

