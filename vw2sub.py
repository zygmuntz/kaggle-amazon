'convert VWs predictions into format suitable for submission'

import sys, csv

input_file = sys.argv[1]
output_file = sys.argv[2]

reader = csv.reader( open( input_file ))
writer = csv.writer( open( output_file, 'wb' ))

writer.writerow( [ 'id', 'ACTION' ] )

i = 1
for line in reader:
	p = float( line[0] )
	
	writer.writerow( [ i, p ] )
	i += 1
	
	
	

