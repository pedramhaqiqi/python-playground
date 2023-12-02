import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.special import xlogy



def entropy_binary():
    # Define a function to calculate the negative entropy for a binary distribution
    def binary_negative_entropy(p):
        # Handle the case when p is 0 or 1, since log(0) is undefined
        if p == 0 or p == 1:
            return 0
        else:
            return -(p * np.log(p) + (1 - p) * np.log(1 - p))

    # Create a range of p values from 0 to 1
    p_values = np.linspace(0, 1, 500)
    # Calculate negative entropy for each p value
    neg_entropy_values = [binary_negative_entropy(p) for p in p_values]

    # Plot the negative entropy function
    plt.figure(figsize=(10, 6))
    plt.plot(p_values, neg_entropy_values, label='Negative Entropy')

    # Mark the point of maximum negative entropy, which is the vertex of the convex function
    max_neg_entropy = max(neg_entropy_values)
    max_p = p_values[neg_entropy_values.index(max_neg_entropy)]
    plt.plot(max_p, max_neg_entropy, 'ro')  # 'ro' means red dot

    plt.xlabel('Probability p')
    plt.ylabel('Negative Entropy -H(p)')
    plt.title('Negative Entropy of a Binary Probability Distribution')
    plt.legend()
    plt.grid(True)
    plt.show()

def entropy_binomial():
    def binomial_entropy(n, p):
        """
        Calculate the entropy of a binomial distribution with parameters n and p.

        Parameters:
        n (int): number of trials.
        p (float): probability of success on each trial.

        Returns:
        float: The entropy of the binomial distribution.
        """
        # Range of all possible number of successes
        k = np.arange(0, n+1)
        
        # Probability mass function for all k
        pmf = binom.pmf(k, n, p)
        
        # Calculate the entropy using the definition
        entropy = -np.sum(xlogy(pmf, pmf)) # xlogy returns 0 for 0 * log(0)
        return entropy

    # Set number of trials
    n = 10

    # Generate a range of p from 0 to 1
    p_values = np.linspace(0, 1, 100)

    # Calculate entropy for each p value
    entropies = [binomial_entropy(n, p) for p in p_values]

    # Plot the entropy function
    plt.figure(figsize=(10, 6))
    plt.plot(p_values, entropies, label=f'Entropy of Binomial Distribution n={n}')

    plt.xlabel('Probability of Success p')
    plt.ylabel('Entropy H(X)')
    plt.title('Entropy of a Binomial Distribution with Varying p')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    entropy_binary()
    entropy_binomial()