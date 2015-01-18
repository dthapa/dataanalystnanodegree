import sys
import string

def mapper():
    for line in sys.stdin: #cycle through lines of standard input
        #  Example execution step in the terminal below
        # $ cat aadhaar_data.csv | python aadhaar_generated_mapper.py | sort |
        #   python aadhaar_generated_mapper.py
    
        #Your mapper code goes here.
        #You will also need to fill out the reducer
        #code as well before test running or else you will get an error.
        #
        #Each line will be
        #a comma-separated list of values.  The
        #header row WILL be included.  Tokenize
        #each row using the commas, and emit a key-
        #value pair containing the district and
        #Aadhaar generated, separated by a tab.
        #Make sure each row has the correct number
        #of tokens and is not the header row!
        #
        #You can see a copy of the the input aadhaar data
        #in the link below:
        #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv
        
        line = line.strip().split(',')
        if len(line) != 12 or line[0] == 'Registrar':
            continue
        print "{0}\t{1}".format(line[3], line[8])
        
mapper()