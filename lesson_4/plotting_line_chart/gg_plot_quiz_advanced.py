import matplotlib
matplotlib.use('agg')

import pandas as pd
from ggplot import *

def lineplot_compare(hr_by_team_year_sf_la_csv):
    # Write a function, lineplot_compare, that will read a csv file
    # called hr_by_team_year_sf_la_csv and plot it using pandas and ggplot2.
    #
    # This csv file has three columns -- yearID, HR, and teamID, 
    # representing the total number of HR hit each year by the SF Giants 
    # and LA Dodgers. Produce a visualization comparing the total HR by 
    # year of the two teams. 
    # 
    # You can see the data in hr_by_team_year_sf_la_csv
    # at the link below:
    # https://www.dropbox.com/s/wn43cngo2wdle2b/hr_by_team_year_sf_la.csv
    #
    # Note that to differentiate between multiple categories on the 
    # same plot in ggplot, we can pass color in with the other arguments
    # to aes, rather than in our geometry functions.
    # 
    # For example, ggplot(data, aes(xvar, yvar, color=category_var)).  This
    # should help you.
    df = pd.read_csv(hr_by_team_year_sf_la_csv)
    
    gg = ggplot(df, aes(df['yearID'], df['HR'], color='teamID')) + \
            geom_point() + geom_line() + ggtitle('Home Run by Teams') + \
            xlab('Year') + ylab('Home Run')
    return gg

if __name__ == "__main__":
    data = "hr_by_team_year_sf_la.csv"
    image = "plot.png"
    gg =  lineplot_compare(data)
    print gg
    ggsave(image, gg, width=11, height=12)