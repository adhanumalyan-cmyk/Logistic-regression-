## 3. Advanced NumPy Concepts

### 3.1 Indexing

Indexing accesses an individual element using its position.

```python
numbers = np.array([10, 20, 30, 40])
print(numbers[0])
```

Python indexing starts from zero.

### 3.2 Slicing

Slicing extracts a range of elements.

Syntax:

```python
array[start:stop:step]
```

Example:

```python
numbers[1:3]
```

The stop index is excluded.

### 3.3 Reshaping

Reshaping changes the dimensions of an array without changing its total number of elements.

```python
numbers = np.array([1, 2, 3, 4, 5, 6])
matrix = numbers.reshape(2, 3)
```

### 3.4 Broadcasting

Broadcasting allows NumPy to perform operations on arrays with compatible shapes.

```python
numbers = np.array([10, 20, 30])
result = numbers + 5
```

Output:

```text
[15 25 35]
```

### 3.5 Matrix Operations

Matrix addition:

```python
A + B
```

Matrix multiplication:

```python
A @ B
```

Matrix operations are fundamental to neural network calculations.

### Learning status

- [x] NumPy introduction
- [x] Array creation
- [x] Dimensions and shape
- [x] Mathematical and statistical operations
- [x] Indexing and slicing
- [x] Reshaping
- [x] Broadcasting
- [x] Matrix operations
- [ ] Practical exercises
- [ ] NumPy with the actual Iris dataset

### Engineering note

NumPy provides the numerical foundation for data processing and mathematical computations in Machine Learning and Deep Learning.