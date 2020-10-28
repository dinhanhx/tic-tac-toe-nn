# Tic tac toe Neural Network

My first project about neural network.

## Installation

You need `tensorflow`, `keras` and `numpy` on Python 3.

or just `pip install -r req.txt`

## Project structure

```
.
├── smort/ # Smort model
├── TEST_training_history.py # Generated from Simulator.py
├── training_history.py # Generated from Simulator.py
├── Simulator.py # Generate random tic-tac-toe games
├── NeuralNetwork.py # Train Smort by fitting training_history.pkl
├── Test.py # Test Smort with TEST_training_history.pkl
└── PlayWithSmort # You are O, Smort is X. O goes first.
```

## Play with Smort

`py PlayWithSmort.py`

Note that: your input is based on indices of matrix.

## About Smort

Because Smort are trained with X goes first. Therefore, it is good at making X wins.

Given the board at any moment of one game, Smort can predict who will win with accuracy up to 0.70%
