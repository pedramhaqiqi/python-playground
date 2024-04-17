import numpy as np
import time
import os

def animate_spiral():
    while True:
        matrix = np.full((3, 3), 'x')
        #set center to 0
        sequence = [0,0,1,2,2,2,1,0]
        seq2 = [1,2,2,2,1,0,0,0]
        clear_seq1 = [1,0,0,0,0,1,2,2,2]
        clear_seq2 = [0,0,0,1,2,2,2,1,0]
        counter = 0
        for i, j, x, k in zip(sequence, seq2, clear_seq1, clear_seq2):
            print(f"i: {i}, j: {j}, x: {x}, k: {k}")
            matrix[i, j] = 'o'
            counter += 1
            if counter > 0:
                matrix[x, k] = 'x'
                counter = 0
            print(matrix, flush = True)
            time.sleep(0.5)
            os.system('clear')


    
    
animate_spiral()


