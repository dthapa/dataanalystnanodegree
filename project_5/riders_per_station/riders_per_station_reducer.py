import sys

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should return one row
    per unit, along with the total number of ENTRIESn_hourly over the course of may. 
    
    You can assume that the input to the reducer is sorted by UNIT, such that all rows 
    corresponding to a particular UNIT are group together.

    '''
    
    entries = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 2:
            continue
        current_key, count = data
        if old_key and old_key != current_key:
            print "{0}\t{1}".format(old_key, entries)
            entries = 0
        
        old_key = current_key
        entries += float(count)
    
    if old_key != None:
        print "{0}\t{1}".format(old_key, entries)

reducer()
