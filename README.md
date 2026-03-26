# Perceptron Logic Gate Trainer

A single-layer Perceptron built **from scratch** using only Python and NumPy — no ML libraries like scikit-learn or TensorFlow. Train it to learn classic logic gates and observe how the perceptron learning rule works in action.

## What it does

You choose a logic gate (AND, OR, NAND, NOR, or XOR), set a learning rate and number of epochs, and watch the perceptron train itself using the **perceptron learning rule**. It will tell you when it converges and report the final weights, bias, and accuracy.

> **Note:** XOR is not linearly separable, so a single perceptron cannot learn it perfectly — the project handles this case gracefully and informs the user.

## Project Structure

```
Project/
├── main.py          # Entry point — ties everything together
├── perceptron.py    # Perceptron class (fit, predict, accuracy)
├── gates.py         # Truth tables for all supported logic gates
└── helper.py        # Input helper functions (gate, learning rate, epochs)
```

## How to Run

**Requirements:** Python 3.x and NumPy

```bash
pip install numpy
python main.py
```

**Example interaction:**
```
========================================
   Perceptron Logic Gate Trainer
========================================
Enter the Gate you want to train on: AND
Enter the Learning Rate: 0.1
Enter the number of Epocs: 100

Training a Perceptron on the AND gate
----------------------------------------
  Converged at epoch 6
Training Complete!
  Weights : [0.2 0.1]
  Bias    : -0.2
  Accuracy: 100.0%
```

## Supported Gates

| Gate | Linearly Separable | Learnable by Perceptron |
|------|--------------------|-------------------------|
| AND  | ✅ Yes             | ✅ Yes                  |
| OR   | ✅ Yes             | ✅ Yes                  |
| NAND | ✅ Yes             | ✅ Yes                  |
| NOR  | ✅ Yes             | ✅ Yes                  |
| XOR  | ❌ No              | ❌ No                   |

## How the Perceptron Works

1. Weights and bias are initialized to zero.
2. For each training sample, it computes: `output = step(X · W + b)`
3. If the prediction is wrong, it updates using the **perceptron learning rule**:
   - `Δw = lr × (y_true - y_pred) × x`
   - `Δb = lr × (y_true - y_pred)`
4. Training stops early if the perceptron achieves zero errors in an epoch.
