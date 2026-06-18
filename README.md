# Shortest Paths with Positive and Negative Weights

## Team Members
- [cite_start]Nikolaos Katsikavalis
- [cite_start]Georgios Papamikroulis 

## Description
[cite_start]This project focuses on finding shortest paths in networks with altitude variations, where moving uphill incurs a positive fuel cost (+1) and moving downhill results in a negative cost (-1)[cite: 1265, 1294, 1295, 1296]. [cite_start]The study implements and compares **Dijkstra's Algorithm** and the **Bellman-Ford Algorithm** using a simulation over 10,000 random graphs to analyze performance and constraints under negative edge weights and negative cycles[cite: 1475].

## Key Findings
- [cite_start]**Dijkstra's Limitations:** Dijkstra's algorithm fails to guarantee correct results in the presence of negative edge weights due to its greedy nature, as it does not re-evaluate already visited nodes[cite: 1299, 1300, 1302, 1357].
- [cite_start]**Negative Cycles Impact:** In graphs containing negative cycles, shortest paths become ill-posed (tending to negative infinity)[cite: 1346, 1352]. [cite_start]In this simulation, negative cycles appeared in **74.70%** of the generated random graphs[cite: 1481, 1487].
- [cite_start]**Dijkstra vs Bellman-Ford:** There is a 100% correlation between the presence of negative cycles and Dijkstra's failure[cite: 1490]. [cite_start]Dijkstra produced incorrect, finite distances in 74.70% of the cases [cite: 1483, 1492][cite_start], while succeeding only in the 25.30% of graphs that lacked negative cycles[cite: 1482, 1493]. [cite_start]Therefore, Bellman-Ford is mandatory for reliable pathfinding in such topologies[cite: 1496].

## Repository Contents
- `Dijktracode.py`: Python simulation script that generates random graphs, executes both algorithms, and compiles comparison metrics.
- [cite_start]`δεύτερη_απαλλακτικη_εργασια_αλγόριθμοι (1).pdf`: Detailed theoretical report containing step-by-step trace analysis, graph illustrations, and experiment conclusions[cite: 1265, 1305, 1484].
