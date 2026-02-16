# Artificial Intelligence Fundamentals Lab

## Introduction
This repository contains a collection of Python scripts developed during my academic exchange in **Japan**. The project explores the core pillars of classical Artificial Intelligence, including agent architectures, evolutionary computing, logical inference, and probabilistic modeling. 

These implementations serve as a practical foundation for understanding how intelligent systems perceive environments, reason through logic, and optimize solutions using biologically-inspired algorithms.

---

## Scripts Overview

1. **Table-Driven Decision Agent**

* **File:** `table-driven_decision.py`
* **Description:** An implementation of an intelligent agent that relies on a lookup table to determine its actions.
* **Purpose:** To demonstrate fundamental AI decision-making where the agent stores its entire percept history and maps it to specific actions predefined in a dictionary. This showcases a system with no internal reasoning that depends entirely on prior knowledge.

2. **Simple Reflex Agent**

* **File:** `simple_reflex_agent.py`
* **Description:** A reactive agent that makes decisions based solely on the current percept, ignoring the history of past states.
* **Purpose:** To implement a condition-action rule system (if-then logic). This script simulates an agent reacting immediately to environmental cues (e.g., "if dirty, then suck"), highlighting the efficiency of agents without memory.

3. **Model-Based Vacuum Agent**

* **File:** `model-based_vacuum_agent.py`
* **Description:** A sophisticated agent that maintains an internal state to track parts of the world it cannot currently see.
* **Purpose:** To model a complex environment where the agent uses a transition model to predict movement and a probabilistic sensor model. The sensor includes a 2% error margin for "clean" rooms, demonstrating how AI handles uncertainty and tracks environmental changes.

4. **Genetic Solution Optimizer**

* **File:** `genetic_algorithm_optimizer.py`
* **Description:** A search and optimization tool based on the principles of natural selection and genetics.
* **Purpose:** To find an optimal binary sequence through iterative generations. The script implements fitness evaluation, weighted parent selection, crossover (DNA recombination), and random mutations to evolve a population toward a perfect individual.

5. **Forward Chaining Inference Engine**

* **File:** `forward_chaining_inference.py`
* **Description:** A logical reasoning engine that starts with known facts and applies rules to extract new information.
* **Purpose:** To demonstrate automated deduction by iterating through a rule base. The script identifies when conditions are met to infer new conclusions (e.g., if A and B are true, then C is inferred), illustrating the core logic of expert systems.

6. **Semantic Knowledge Graph Visualizer**

* **File:** `semantic_knowledge_graph.py`
* **Description:** A visual and logical representation of entities and their semantic relationships using the **NetworkX** library.
* **Purpose:** To build an ontology where entities have defined relationships (e.g., "Mary is a MemberOf Female Persons"). The scripts allow for attribute inheritance and direct querying of properties, such as asking for the number of legs an entity has, while providing a graphical visualization.

7. **Probabilistic Hidden Markov Model**

* **File:** `hmm_predictor.py` 
* **Description:** A probabilistic model used to predict hidden states from a sequence of observable events using the `hmmlearn` library.
* **Purpose:** To demonstrate temporal reasoning by predicting hidden states (e.g., "happy" or "sad") based on observable actions like "smile" or "cry". This technique is fundamental to Natural Language Processing (NLP) and speech recognition.

---

## Requirements
To run these scripts, you will need:
* **Python 3.x**
* **NumPy**
* **NetworkX**
* **Matplotlib**
* **hmmlearn**