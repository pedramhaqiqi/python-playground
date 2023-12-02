# Recalculating the probability for 2^30 hosts
total_addresses = 2**48
# Total number of hosts across all networks
total_hosts = 2**30  # 2^30 hosts

# Calculating the probability that all 2^30 hosts have unique addresses
# Due to the large number of iterations, we'll calculate this in a more computationally efficient manner
prob_unique_all_hosts = 1
for i in range(total_hosts):
    prob_unique_all_hosts *= (total_addresses - i) / total_addresses
    # Adding a break condition to avoid excessive computation
   

# Probability that at least two of these 2^30 hosts have the same address
prob_collision_any_two_hosts = 1 - prob_unique_all_hosts
print(prob_collision_any_two_hosts)
