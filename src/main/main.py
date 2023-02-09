# libraries
import os
import sys
import time
from pathlib import Path

# root path
path = Path('C:/Users/llorenc.buil/github/Game-Of-Life')
os.chdir(path)
if path not in sys.path:
    sys.path.append(path)

# local libraries
from src.objects import functions as f


def main(matrix_size, initial_probability_of_life, steps):
    '''
    Runs the entire simulation.

    Parameters
    ----------
    matrix_size : int
        Size of the matrix.
    initial_probability_of_life : float
        Initial probability of life for the matrix creatio, between 0 and 1.
    steps : int
        Number of iterations to perform.

    Returns
    -------
    matrix : numpy array
        Final matrix configuration.

    '''

    matrix = f.init_matrix(
        matrix_size=matrix_size,
        initial_probability_of_life=initial_probability_of_life
    )

    for _ in range(steps):
        matrix = f.update_matrix(matrix=matrix)

        f.plot_matrix(matrix)

        # sleep 0.5s to see evolution
        time.sleep(0.5)

    return matrix


if __name__ == '__main__':
    main(matrix_size=20, initial_probability_of_life=0.2, steps=100)
