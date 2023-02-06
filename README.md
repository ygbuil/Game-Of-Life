# Game-Of-Life
A cellular survival simulation.

The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

The universe of the Game of Life is a square matrix, where each cell can be in one of two possible states, live or dead. Every cell interacts with its eight neighbours, and based on their state, the cell lives or dies. The matrix evolves following this crietria:

* Any live cell with two or three live neighbours survives.
* Any dead cell with three live neighbours becomes a live cell.
* All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The two pictures below are an example of how the game evolves. The first picture correpsonds to the inital configuration, and the second picture corresponds to the last one (where equilibrium has been reached and the system no longer evolves) after 24 iterations:

![alt_file](https://github.com/ygbuil/Game-Of-Life/blob/main/images/initial_state.png)

![alt_file](https://github.com/ygbuil/Game-Of-Life/blob/main/images/final_state.png)
