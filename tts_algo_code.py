import numpy as np
import matplotlib.pyplot as plt



def synthetic_data(num_instances, num_runs, success_prob):
    # Generate synthetic data for testing
    return np.random.binomial(1, success_prob, (num_instances, num_runs))




def estimate_theta(r, y, alpha=0.5, beta=0.5):
    # samples a probability from a posterior distribution for a given instance solved over "r" runs with "y" successes
    return np.random.beta(alpha + y, beta + r - y)


def calculate_r99(theta):
    # calculates R_99 for a given probability theta
    if theta != 1:
        r99 = np.log(1-0.99)/np.log(1-theta)
    else:
        # avoids dividing by zero
        r99 = 1.0
    return r99


    

def bootstrap(Instance_data, B=500, q=0.6):
    q_percentile=[] 
    
    for b in range(B):
    # bootstrap to gather statistics for the R_99 values    
    
        # randomly select a number of instances from the instance set with replacement
        sampled_instances = []
        for i in range(len(Instance_data)):
            random_index = np.random.randint(0, len(Instance_data))
            sampled_instances.append(Instance_data[random_index])
      
    
        r99_values = [] 
        
        # calculate R_99 for each instance    
        for j, instance in enumerate(sampled_instances):
            r = len(instance)
            y = sum(instance)
            theta = estimate_theta(r,y)
            r99 = calculate_r99(theta)
            r99_values.append(r99)
        
    
        q_percentile.append(np.percentile(r99_values,q))
    
    return q_percentile # returns a distribution of TTS values for the given set of instances

    
def main():
    # Sample synthetic data
    generated_instances = synthetic_data(num_instances = 10, num_runs = 100, success_prob = 0.05)

    # Time for the Monte Carlo algorithm to run once, assuming it's the same for every run
    tau = 1
    
    # Bootstrap to estimate the TTS distribution
    tts_distribution = bootstrap(generated_instances, B = 500, q = 0.1)*tau


    ### Below is for the purposes of testing the code
    plt.hist(tts_distribution_tst,100)
    plt.show()
        
    return tts_distribution

tts_distribution = main()
