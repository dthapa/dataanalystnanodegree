import sys
from datetime import datetime

def reducer():
    '''
    For every single unit, write a reducer that will return the busiest datetime (e.g.,
    the entry that had the most entries).  Ties should go to datetimes that are later on in the 
    Month of May.  You can assume that the contents of the reducer will be sorted by UNIT, such that
    all entries corresponding to a given UNIT will be sorted together. The output should be the UNIT
    name, the datetime (which is a concatenation of date and time), and ridership separated by tabs.

    For example, the output of the reducer may look like this:
    R001    2011-05-11 17:00:00    31213.0
    R002    2011-05-12 21:00:00    4295.0
    R003    2011-05-05 12:00:00    995.0
    R004    2011-05-12 12:00:00    2318.0
    R005    2011-05-10 12:00:00    2705.0
    R006    2011-05-25 12:00:00    2784.0
    R007    2011-05-10 12:00:00    1763.0
    R008    2011-05-12 12:00:00    1724.0
    R009    2011-05-05 12:00:00    1230.0
    R010    2011-05-09 18:00:00    30916.0
    ...
    ...
    
    '''
    # this problem isn't as difficult because the datetime is ordered too
    max_entries = 0
    old_key = None
    best_datetime = ''
    pos = 0
    
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 4:
            continue

        unit, entries, date, time = data
        current_datetime = datetime.strptime(date+' '+time, '%Y-%m-%d %H:%M:%S')
            
        if pos == 0:
            best_datetime = current_datetime
            pos += 1
            
        if old_key and old_key != unit:
            print "{0}\t{1}\t{2}".format(old_key, best_datetime, max_entries)
            max_entries = 0
            best_datetime = current_datetime
        old_key = unit
        
        if float(entries) >= max_entries:
            best_datetime = current_datetime
            max_entries = float(entries)
        elif float(entries) == max_entries:
            if best_datetime == '' or best_datetime < current_datetime:
                best_datetime = current_datetime
                max_entries = float(entries)
    
    if old_key != None:
        print "{0}\t{1}\t{2}".format(old_key, best_datetime, max_entries)
                                
reducer()
