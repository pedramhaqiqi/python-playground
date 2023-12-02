import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.special import xlogy
from mpl_toolkits.mplot3d import Axes3D

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

def binary_negative_entropy(p):
    # Handle the case when p is 0 or 1, since log(0) is undefined
    if p == 0 or p == 1:
        return 0
    else:
        return -(p * np.log(p) + (1 - p) * np.log(1 - p))

def entropy_binary():
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

def simplex_negative_entropy(p1, p2, p3):
    # Calculate the negative entropy for the given probabilities
    return -(xlogy(p1, p1) + xlogy(p2, p2) + xlogy(p3, p3))

def entropy_binomial():
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

def entropy_3D_uniform():
    # Create a grid of p1 and p2 values
    p1 = np.linspace(0.01, 0.99, 50)
    p2 = np.linspace(0.01, 0.99, 50)
    P1, P2 = np.meshgrid(p1, p2)
    P3 = 1 - P1 - P2

    # Mask invalid probabilities where p1 + p2 > 1
    mask = P3 >= 0.01
    P1 = P1[mask]
    P2 = P2[mask]
    P3 = P3[mask]

    # Calculate negative entropy for each (p1, p2) pair
    Neg_Entropy = np.array([simplex_negative_entropy(p1, p2, p3) for p1, p2, p3 in zip(P1, P2, P3)])

    # Create a plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Create a scatter plot
    scatter = ax.scatter(P1, P2, Neg_Entropy, c=Neg_Entropy, cmap='viridis')

    # Add labels and title
    ax.set_xlabel('Probability p1')
    ax.set_ylabel('Probability p2')
    ax.set_zlabel('Negative Entropy -H(p)')
    ax.set_title('Negative Entropy over a 3D Probability Simplex')

    # Add a color bar
    cbar = fig.colorbar(scatter, shrink=0.5, aspect=5)
    cbar.set_label('Negative Entropy')

    plt.show()



if __name__ == "__main__":
    entropy_binary()
    entropy_binomial()
    entropy_3D_uniform()