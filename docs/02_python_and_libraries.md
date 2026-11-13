# 02 — Python Libraries for AI Engineering

## 1. Introduction

Python provides several libraries that simplify AI and Machine Learning development.

In this project, we will use:

| Library | Purpose |
|---|---|
| NumPy | Numerical computation and arrays |
| Pandas | Data analysis and manipulation |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine Learning algorithms and evaluation |

## 2. NumPy — Numerical Python

### What is NumPy?

NumPy is a Python library for efficient numerical computation. Its primary data structure is the N-dimensional array (`ndarray`).

### Why is NumPy used in AI?

- Efficient storage and processing of numerical data.
- Vectorized mathematical operations.
- Matrix and linear algebra operations.
- Statistical calculations.
- Numerical data preparation for ML models.

### Creating an array

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])
print(numbers)
```

### Important array properties

| Property | Description |
|---|---|
| ndim | Number of dimensions |
| shape | Size of each dimension |
| size | Total number of elements |
| dtype | Data type of elements |

### Mathematical operations

```python
numbers + 10
numbers * 2
```

NumPy performs these operations element by element. This is called vectorization.

### Statistical operations

```python
np.mean(numbers)
np.max(numbers)
np.min(numbers)
np.std(numbers)
```

### Array dimensions

- 1D array: A sequence of values.
- 2D array: Rows and columns.
- 3D array: Multiple 2D arrays stacked together.

### Connection to Iris Flower Classification

Each Iris flower has four numerical features:

1. Sepal length
2. Sepal width
3. Petal length
4. Petal width

One flower can be represented as:

```python
flower = np.array([5.1, 3.5, 1.4, 0.2])
```

The complete Iris feature matrix contains 150 rows and 4 columns, giving it a shape of `(150, 4)`.

### Learning status

- [x] NumPy introduction
- [x] Array creation
- [x] Dimensions and shape
- [x] Mathematical operations
- [x] Statistical operations
- [ ] Indexing and slicing
- [ ] Broadcasting
- [ ] Matrix operations
- [ ] NumPy practical exercises

### Engineering note

NumPy is an important foundation for understanding numerical computation in Machine Learning and tensor operations in Deep Learning.