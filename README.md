# Pathfinding Algorithm Visualisation Tool

A pathfinding algorithm visualisation tool completed in partial fulfilment of the requirements of the AQA A-Level Computer Science Non-Exam Assessment.

Pathfinding has wide-reaching applications from routing packets in packet switching over the Internet to satellite navigation systems. Giving pupils a greater understanding of this field will help them appreciate how computer science influences humanity daily. For this reason, pathdfinding algorithms specifically were chosen.

The project was created to aid A-Level students more concretely understand some common pathfinding algorithms. The three pathfinding algorithms that were selected were: Dijkstra's algorithm; A* search and Breadth-First search. For the maze generation, a less well-known technique called recursive division was used in which recursion is used to repeatedly divide the grid into a maze. To implement these algorithms, stacks, queues and binary minimum heaps were used.

How to use the Tool:

On start, a white interactive grid is displayed along with a toolbar at the top of the window. The program allows the user to select two cells, the first indicating the start node and the second indicating the end node. At this stage, the obstacles (cells in which the path cannot travel) can be chosen in two ways: filling in cells manually or the program using recursive division to automatically create a maze. To fill in the cells manually, the cells which are to be selected need to be pressed. To create the recursively divided maze, the "Recursive Division Maze" should be pressed. The obstacles will be indicated in purple.

A pathfinding algorithm can be selected by pressing the "Algorithms" tab which will open a dropdown menu giving a choice of pathfinding algorithms. Once the algorithm has been selected, the shortest path is now able to be visualised and thus the "Visualise" button will work. This will show the way the chosen algorithm finds the end node.  Note: the "Visualise" button will only work if the dropdown menu is closed.  
