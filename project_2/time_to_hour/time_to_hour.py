import pandas

def time_to_hour(time):
    '''
    Given an input variable time that represents time in the format of:
    00:00:00 (hour:minutes:seconds)
    
    Write a function to extract the hour part from the input variable time
    and return it as an integer. For example:
        1) if hour is 00, your code should return 0
        2) if hour is 01, your code should return 1
        3) if hour is 21, your code should return 21
        
    Please return hour as an integer.
    '''
    # this exercise somehow doesn't fit in the scheme of things
    # besides this could easily be done in the map function as an anonomous fun
    # student_df['Hour'] = student_df['TIMEn'].map(lambda x: int(x[0:2]))
    return int(time[0:2])

if __name__ == "__main__":
    input_filename = "turnstile_data_master_subset_consolidate_rows.csv"
    output_filename = "output.csv"
    turnstile_master = pd.read_csv(input_filename)
    student_df = turnstile_master.copy(deep=True)
    student_df['Hour'] = student_df['TIMEn'].map(lambda x: int(x[0:2]))
    student_df.to_csv(output_filename)