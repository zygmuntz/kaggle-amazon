'Convert Amazon2-specific CSV file to vw format. Headers are skipped by default.'

import sys
import csv

def construct_line( label, line ):
	new_line = []
	if float( label ) == 0.0:
		label = "-1"
	new_line.append( "%s " % ( label ))
	
	namespaces = [ 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7' ]
	
	#for i, item in enumerate( line ):
	for n in namespaces:
		item = line.pop( 0 )
		new_item = "|%s %s" % ( n, item )
		new_line.append( new_item )
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line

# ---

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
	label_index = int( sys.argv[3] )
except IndexError:
	label_index = 0
	
try:
	skip_headers = sys.argv[4]
except IndexError:
	skip_headers = 1	

i = open( input_file )
o = open( output_file, 'w' )

reader = csv.reader( i )
if skip_headers:
	headers = reader.next()

for line in reader:
	if label_index == -1:
		label = 1
	else:
		label = line.pop( label_index )
		
	new_line = construct_line( label, line )
	o.write( new_line )