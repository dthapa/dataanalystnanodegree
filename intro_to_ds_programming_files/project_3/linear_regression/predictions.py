import pandas as pd
import numpy as np
from datetime import datetime

def normalize_features(array):
   """
   Normalize the features in our data set.
   """
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, and the values for our thetas.
    
    This should be the same code as the compute_cost function in the lesson #3 exercises. But
    feel free to implement your own.
    """ 
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    
    This is the same gradient descent code as in the lesson #3 exercises. But feel free
    to implement your own.
    """
    cost_history = []

    for i in range(num_iterations):
        predicted_values = np.dot(features, theta)
        theta = theta - alpha/len(values) * np.dot((predicted_values - values), features)
        cost_history += [compute_cost(features, values, theta)]
        
    return theta, pd.Series(cost_history)

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pd dataframe called weather_turnstile.
    Using the information stored in the dataframe, lets predict the ridership of
    the NYC subway using linear regression with gradient descent.
    
    You can look at information contained in the turnstile weather dataframe 
    at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv    
    
    Your prediction should have a R^2 value of .40 or better.
    
    Note: due to the memory and CPU limitation of our amazon EC2 instance, we will
    give you a random subet (~15%) of the data contained in turnstile_data_master_with_weather.csv
    
    If you receive a "server has encountered an error" message, that means you are hitting 
    the 30 second  limit that's placed on running your program. Try using a smaller number
    for num_iterations if that's the case.
    
    Or if you are using your own algorithm/model, see if you can optimize your code so it
    runs faster.
    '''
    # best is 0.494721161545

    dummy_units = pd.get_dummies(dataframe['UNIT'], prefix='unit')
    #not having UNIT can hurt predictions
    dataframe['WEEKDAYn'] = dataframe['DATEn'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").weekday())
    dataframe['HOLIDAYn'] = dataframe['WEEKDAYn'].apply(lambda x: 1 if x in [5, 10, 25] else 0)
    dataframe['WEEKDAYn'] = dataframe['WEEKDAYn'].apply(lambda x: 0 if x in [5, 6] else 1)
    dataframe['PEAKn'] = dataframe['Hour'].apply(lambda x: 1 if x in [9, 12, 13, 16, 17, 20, 21, 0] else 0)
    
    features = dataframe[['rain', 'Hour', 'PEAKn', 'WEEKDAYn', 'HOLIDAYn',
                          'maxtempi', 'mintempi']].join(dummy_units)
    values = dataframe[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)

    features['ones'] = np.ones(m)
    features_array = np.array(features)
    values_array = np.array(values).flatten()

    #Set values for alpha, number of iterations.
    alpha = 0.5 # please feel free to play with this value
    num_iterations = 75 # please feel free to play with this value

    #Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, 
                                                            values_array, 
                                                            theta_gradient_descent,
                                                            alpha, num_iterations)
    print theta_gradient_descent
    predictions = np.dot(features_array, theta_gradient_descent)

    return predictions

def compute_r_squared(data, predictions):
    SST = ((data-np.mean(data))**2).sum()
    SSReg = ((predictions-np.mean(data))**2).sum()
    r_squared = SSReg / SST

    return r_squared

if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    predicted_values = predictions(turnstile_master)
    r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predicted_values) 

    print r_squared