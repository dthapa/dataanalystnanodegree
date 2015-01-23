from pandas import *
from ggplot import *
import pandasql as pds

def plot_weather_data(turnstile_weather):
    ''' 
    Use ggplot to make another data visualization focused on the MTA and weather
    data we used in assignment #3. You should make a type of visualization different
    than you did in exercise #1, and try to use the data in a different way (e.g., if you
    made a lineplot concerning ridership and time of day in exercise #1, maybe look at weather
    and try to make a histogram in exercise #2). 
    
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement 
    something more advanced if you'd like.  Here are some suggestions for things
    to investigate and illustrate:
    * Ridership by time of day or day of week
    * How ridership varies based on Subway station
    * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
    
    You can check out: 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
    
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''

    df = turnstile_weather
    df_new = df[['UNIT', 'ENTRIESn_hourly']]
    df_new.columns = ['UNIT', 'ENTRIES']

    q = '''
    select UNIT, ENTRIES
    from df_new 
    group by UNIT
    '''
    
    df_new = pds.sqldf(q.lower(), locals())
    df_new['UNIT'] = df_new['UNIT'].apply(lambda x: int(x[1:]))
    print df_new
    
    plot = ggplot(df_new, aes(x='UNIT', y='ENTRIES')) + geom_point() + \
            ggtitle('Ridership by Subway Station') + xlab('Station') + ylab('Entries per hour')
    
    
    return plot

if __name__ == "__main__":
    image = "plot.png"
    with open(image, "wb") as f:
        turnstile_weather = pd.read_csv(input_filename)
        turnstile_weather['datetime'] = turnstile_weather['DATEn'] + ' ' + turnstile_weather['TIMEn']
        gg =  plot_weather_data(turnstile_weather)
        ggsave(f, gg)