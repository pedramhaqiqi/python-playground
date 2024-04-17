import matplotlib.pyplot as plt

# Values of n and corresponding probabilities
n = 10
prob_1_n = 1 - 1/n**2
prob_n = 1/n**2

# x and y values for the PMF plot
x_values = [1/n, n]
y_values = [prob_1_n, prob_n]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(x_values, y_values, width=0.1, color=['blue', 'orange'])

# Annotating the probability above each bar
for i in range(len(x_values)):
    plt.text(x_values[i], y_values[i] + 0.01, f'{y_values[i]:.2f}', ha = 'center')

# Set the labels and title
plt.xticks(x_values, [f'1/{n}', f'{n}'])
plt.yticks([0, prob_n, prob_1_n], ['0', f'1/{n**2}', f'{15}/{16}'])
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.title('PMF of $X_4$')

# Show the plot
plt.grid(axis='y')
plt.show()
