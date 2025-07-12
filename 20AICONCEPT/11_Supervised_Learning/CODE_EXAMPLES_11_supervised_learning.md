# 💻 Code Examples - 11 Supervised Learning

## 🎯 Tổng Quan

Các ví dụ code thực tế cho 11 supervised learning.

## 📚 Basic Examples

### Example 1: Simple Implementation

    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    def simple_11_supervised_learning(X, y):
        """
        Simple implementation of 11 supervised learning
        Parameters:
        X: Input features (numpy array or pandas DataFrame)
        y: Target variable (numpy array or pandas Series)
        Returns:
        model: Trained model
        """
        # Implementation here
        pass

    # Usage example
    if __name__ == "__main__":
        # Load sample data
        from sklearn.datasets import make_classification
        X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # Train model
        model = simple_11_supervised_learning(X_train, y_train)
        # Make predictions
        predictions = model.predict(X_test)
        # Evaluate
        accuracy = accuracy_score(y_test, predictions)
        print(f"Accuracy: {accuracy:.4f}")

## 🔧 Advanced Examples

### Example 2: Custom Implementation

    class Custom11SupervisedLearning:
        """
        Custom implementation of 11 supervised learning
        """
        def __init__(self, learning_rate=0.01, max_iterations=1000):
            self.learning_rate = learning_rate
            self.max_iterations = max_iterations
            self.weights = None
            self.bias = None
            self.history = []
        def fit(self, X, y):
            n_samples, n_features = X.shape
            self.weights = np.zeros(n_features)
            self.bias = 0
            for iteration in range(self.max_iterations):
                predictions = self.predict(X)
                dw = (1/n_samples) * np.dot(X.T, (predictions - y))
                db = np.mean(predictions - y)
                self.weights -= self.learning_rate * dw
                self.bias -= self.learning_rate * db
                loss = np.mean((predictions - y) ** 2)
                self.history.append(loss)
                if len(self.history) > 10 and abs(self.history[-1] - self.history[-10]) < 1e-6:
                    break
        def predict(self, X):
            return np.dot(X, self.weights) + self.bias
        def plot_training_history(self):
            import matplotlib.pyplot as plt
            plt.figure(figsize=(10, 6))
            plt.plot(self.history)
            plt.title('Training History')
            plt.xlabel('Iteration')
            plt.ylabel('Loss')
            plt.grid(True)
            plt.show()

## 📚 References

1. **Official Documentation**: Link to official docs
2. **GitHub Examples**: Link to GitHub examples
3. **Online Tutorials**: Link to tutorials
4. **Research Papers**: Link to relevant papers
5. **Books**: Link to recommended books

## 🔗 Liên Kết Liên Quan

- [Theory](./THEORY_11_supervised_learning.md)
- [Implementation](./IMPLEMENTATION_11_supervised_learning.md)
- [Best Practices](./BEST_PRACTICES_11_supervised_learning.md)
- [Complex Problems](./COMPLEX_PROBLEMS.md)
