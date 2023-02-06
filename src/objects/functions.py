# libraries
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def init_matrix(matrix_size, initial_probability_of_life):
    '''
    Initializes a square matrix of size matrix_size, with random 0s and 1s.

    Parameters
    ----------
    matrix_size : int
        Size of the matrix.
    initial_probability_of_life : float
        Initial probability of life for the matrix creatio, between 0 and 1.

    Returns
    -------
    matrix : numpy array
        Matrix.

    '''

    matrix = np.zeros((matrix_size, matrix_size))

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if random.uniform(0, 1) < initial_probability_of_life:
                matrix[i][j] = 1

    return matrix


def indexes_inside_bounds(max_index, i, j):
    '''
    Checks if a pair of indices i, j is inside or outside of the bounds of the
    matrix.

    Parameters
    ----------
    max_index : int
        Maximum index matrix.
    i : int
        Index i to verify.
    j : int
        Index j to verify.

    Returns
    -------
    bool
        True = inside of bounds, False = outside of bounds.

    '''

    if i < 0 or j < 0 or i > max_index or j > max_index:
        return False
    else:
        return True


def calculate_alive_neighbours(matrix, i, j):
    '''
    Calculates the number of alive neighbours for a specific cell.

    Parameters
    ----------
    matrix : numpy array
        Matrix.
    i : int
        Cell index i.
    j : int
        Cell index j.

    Returns
    -------
    alive_neighbours : int
        Number of alive neighbours.

    '''

    up = i - 1
    down = i + 1
    left = j - 1
    right = j + 1

    max_index = len(matrix) - 1
    alive_neighbours = 0

    neighbours_indices = [
        [up, left], [up, j], [up, right], [i, left], [i, right], [down, left],
        [down, j], [down, right]
    ]

    for i, j in neighbours_indices:
        if indexes_inside_bounds(max_index=max_index, i=i, j=j):
            alive_neighbours += matrix[i][j]

    return alive_neighbours


def update_matrix(matrix):
    '''
    Update entire matrix once, based on every cell neighbours.

    Parameters
    ----------
    matrix : numpy array
        Matrix.

    Returns
    -------
    matrix : numpy array
        Updated matrix.

    '''

    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            alive_neighbours = calculate_alive_neighbours(
                matrix=matrix, i=i, j=j
            )

            # kill, revive, or do nothing (based on alive_neighbours)
            if alive_neighbours < 2 or 3 < alive_neighbours:
                new_matrix[i][j] = 0
            if alive_neighbours == 3:
                new_matrix[i][j] = 1

    matrix = new_matrix

    return matrix


def plot_matrix(matrix):
    '''
    Plot matrix.

    Parameters
    ----------
    matrix : numpy array
        Matrix.

    Returns
    -------
    None.

    '''

    values = [0, 1]
    im = plt.imshow(matrix, interpolation='none')
    colors = [im.cmap(im.norm(value)) for value in values]
    patches = [
        mpatches.Patch(color=colors[0], label='Dead'),
        mpatches.Patch(color=colors[1], label='Alive')
    ]
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2)
    plt.show()