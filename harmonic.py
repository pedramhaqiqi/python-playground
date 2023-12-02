import decimal

def set_precision(prec):
    decimal.getcontext().prec = prec

def harmonic_sum_normal(n, prec):
    set_precision(prec)
    sum = decimal.Decimal(0)
    for i in range(1, n + 1):
        sum += decimal.Decimal(1) / decimal.Decimal(i)
        print(sum, end="")
        print(" | adding " +str(decimal.Decimal(1) / decimal.Decimal(i)))
    return sum

def harmonic_sum_reverse(n, prec):
    set_precision(prec)
    sum = decimal.Decimal(0)
    for i in range(n, 0, -1):
        sum += decimal.Decimal(1) / decimal.Decimal(i)
        print(sum, end="")
        print(" | adding " + str(decimal.Decimal(1) / decimal.Decimal(i)))
    return sum

n = 20
precision = 3  # Setting a low precision

print("Normal Sum")
normal_sum = harmonic_sum_normal(n, precision)
print("Normal Sum: ", normal_sum)
print("------------------------------------------------")
print("Reverse Sum")
reverse_sum = harmonic_sum_reverse(n, precision)
print("Reverse Sum: ", reverse_sum)

