"""
perceptron.py
-------------
A single-layer Perceptron built from scratch using only Python and NumPy.
Activation function: Step function 
Learning rule:  Perceptron learning rule (weight update on misclassification)
"""

import numpy as np


class Perceptron:

    def __init__(self, learning_rate: float = 0.1, epochs: int = 100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None   
        self.bias = None      
        self.errors_per_epoch = []  # track misclassifications per epoch

    @staticmethod
    def step_function(x):
        return np.where(x >= 0, 1, 0)

    def fit(self, X, y):
        """
        Train the perceptron on input data X and binary labels y.

        Parameters
        ----------
        X , shape (n_samples, n_features)
        y , shape (n_samples,) — values must be 0 or 1

        Returns
        -------
        self
        """
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for epoch in range(self.epochs):
            errors = 0
            for xi, yi in zip(X, y):
                linear_output = np.dot(xi, self.weights) + self.bias
                y_pred = self.step_function(linear_output)

                # Perceptron update rule: Δw = lr * (y_true - y_pred) * x
                delta = self.learning_rate * (yi - y_pred)
                self.weights += delta * xi
                self.bias    += delta

                if delta != 0:
                    errors += 1

            self.errors_per_epoch.append(errors)

            # Early stopping if perfect classification
            if errors == 0:
                print(f"  Converged at epoch {epoch + 1}")
                break

        return self

    def predict(self, X) :
        """
        Predict class labels for samples in X.

        Parameters
        ----------
        X , shape (n_samples, n_features)

        Returns
        -------
        np.ndarray of predicted labels (0 or 1)
        """
        linear_output = np.dot(X, self.weights) + self.bias
        return self.step_function(linear_output)

    def accuracy(self, X, y):
        """Returns percentage of correctly classified samples."""
        predictions = self.predict(X)
        return (np.sum(predictions == y)/np.size(predictions))*100
