
# 8-Puzzle Solver 🚀

## 📌 Overview

This project implements multiple search algorithms to solve the classic **8-Puzzle Problem**, a 3×3 sliding puzzle containing tiles numbered 1–8 and one empty space.
The objective is to reach a predefined goal configuration by sliding tiles into the empty space.

---

## 🎯 Goals of the Project

* Implement several AI search algorithms.
* Evaluate each algorithm on the same puzzle instances.
* Identify which algorithm performs best and why.
---

## 🧠 Implemented Algorithms

### **1. Breadth-First Search (BFS)**

* Guarantees the shortest path.
* May consume large memory due to storing many states.

### **2. Depth-First Search (DFS)**

* Very memory efficient.
* Does **not** guarantee an optimal solution.
* May dive deep into unhelpful paths.

### **3. Uniform Cost Search (UCS)**

* Expands nodes based on path cost.
* Guaranteed optimal with uniform move costs.

### **4. Iterative Deepening Search (IDS)**

* Combines memory efficiency of DFS with the optimality of BFS.
* Can be slower due to repeated deepening.

### **5. A* Search (with Manhattan Distance Heuristic)**

* Uses heuristic guidance for fast and optimal solutions.
* Expected to be the top-performing algorithm in this project.

### **6. Hill Climbing**

* Heuristic-based local search.
* Fast but can get stuck in local optima.

---
