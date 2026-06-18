# Shortest Paths Analysis: Dijkstra vs Bellman-Ford

## Team Members
- Nikolaos Katsikavalis 
- Georgios Papamikroulis 

---

## What We Did in This Project (Project Overview)
In this assignment, we investigated how routing algorithms behave when dealing with a mix of positive and negative edge weights. 

### 1. The Scenario (Fuel Cost Model)
We modeled a real-world problem involving vehicle fuel consumption across terrain with significant altitude changes:
* **Uphill Movements:** Moving to a higher altitude requires engine work against gravity, resulting in positive fuel consumption (represented as a **+1** weight).
* **Downhill Movements:** Moving downhill allows the vehicle to coast or use gravity, which reduces overall energy expenditure. This is represented as a "reward" or negative cost (represented as a **-1** weight).

### 2. Theoretical Trace
We manually executed and traced Dijkstra's algorithm on a specific 4-node graph ($s$, $A$, $B$, $t$) where the edges followed an antisymmetric rule ($w(u,v) = -w(v,u)$). Through this trace, we analyzed step-by-step why Dijkstra gets trapped by negative weights and fails to find the actual shortest path.

### 3. Experimental Simulation
To back up our theoretical analysis, we wrote a Python simulation that:
* Generated **10,000 random graphs** with high density ($p=0.7$) and random directional distribution of positive/negative weights ($q=0.3$).
* Ran both **Dijkstra's** and **Bellman-Ford's** algorithms on every single graph.
* Compared their final distance outputs to measure Dijkstra's exact failure rate.

---

## Key Findings & Results
* **Dijkstra's Flaw:** Because Dijkstra uses a greedy strategy, once it "closes" a node, it assumes the shortest path to it has been definitively found. When negative edges exist, cheaper paths can appear later, but Dijkstra never goes back to re-evaluate them.
* **The Danger of Negative Cycles:** We discovered that a massive **74.70%** of the generated random graphs formed "negative cycles" (loops where spinning around indefinitely keeps reducing the total cost towards negative infinity). 
* **The Verdict:** In our 10,000 trials, Dijkstra was incorrect in exactly **74.70%** of the cases (every single time a negative cycle existed). It only gave correct answers in the **25.30%** of graphs that happened to have no negative cycles. 
* **Conclusion:** For any network structure where "downhill" rewards (negative weights) are possible, the **Bellman-Ford** algorithm is absolutely mandatory because it is the only one capable of detecting these infinite-loop anomalies.

---

## Repository Contents
* `Dijktracode.py`: Our complete Python implementation containing the graph generator, the customized Dijkstra/Bellman-Ford algorithms, and the simulation loop.
* `δεύτερη_απαλλακτικη_εργασια_αλγόριθμοι (1).pdf`: Our analytical project report, which includes our handwritten graph diagram, mathematical formulations, and detailed answers to all theoretical questions.
