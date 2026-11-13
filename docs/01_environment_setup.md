:::writing{variant="document" id="63821"}
# 01 — Development Environment Setup

## 1. Project Overview

**Project:** Iris Flower Classification  
**Domain:** Machine Learning  
**Programming Language:** Python 3.12  
**Operating Environment:** Ubuntu 26.04 LTS (WSL2)  
**Environment Manager:** Miniconda  
**IDE:** Visual Studio Code  
**Environment Name:** `ml_learning`

### Objective

To create an isolated, reliable Python development environment for machine learning experimentation, model development and data analysis.

---

## 2. Why Did We Choose Ubuntu WSL2?

Initially, Python development was attempted using Windows and Miniconda.

However, Windows Smart App Control blocked certain compiled scientific Python extension files, including Pandas and SciPy components.

To avoid changing Windows security settings, we selected Ubuntu through Windows Subsystem for Linux (WSL2).

### What is WSL2?

WSL2 stands for Windows Subsystem for Linux 2.

It allows developers to run a genuine Linux environment alongside Windows without requiring a separate physical computer or traditional dual boot.

### Why use WSL2 for AI development?

- Access to Linux development tools.
- Compatibility with many Python and ML libraries.
- Linux-based development workflow.
- Integration with Visual Studio Code.
- Ability to use Windows and Linux side by side.

**Engineering decision:** Use Ubuntu WSL2 as the development environment while keeping Windows security settings enabled.

---

## 3. Why Did We Choose Miniconda?

Miniconda is a lightweight distribution that provides Conda, Python environment management and package management.

### What is Conda?

Conda is an environment and package manager.

It helps developers:
- Create isolated environments.
- Install different Python versions.
- Install compatible packages.
- Manage project dependencies.
- Avoid conflicts between projects.

### Why not use only the system Python?

Ubuntu has its own system Python, which is used by operating-system tools.

Changing or modifying system Python packages unnecessarily can create compatibility problems.

Therefore, we use a separate Conda environment for our ML project.

---

## 4. Creating the ML Environment

### Command

```bash
conda create -n ml_learning python=3.12 -y
```

### Command explanation

| Component | Purpose |
|---|---|
| `conda` | Calls the Conda manager |
| `create` | Creates a new environment |
| `-n` | Specifies the environment name |
| `ml_learning` | Name of our environment |
| `python=3.12` | Installs Python 3.12 |
| `-y` | Automatically confirms installation prompts |

### Activating the environment

```bash
conda activate ml_learning
```

This activates our isolated Python environment.

### Verifying the Python version

```bash
python --version
```

Expected major and minor version:

```text
Python 3.12
```

---

## 5. Installing Machine Learning Libraries

The following libraries were installed:

```bash
conda install numpy pandas matplotlib seaborn scikit-learn jupyter ipykernel -y
```

| Library | Purpose |
|---|---|
| NumPy | Numerical computing and multidimensional arrays |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning algorithms |
| Jupyter | Interactive computational notebooks |
| IPykernel | Connects a Python environment to Jupyter |

### Testing the installation

```bash
python -c 'import numpy, pandas, matplotlib, seaborn, sklearn; print("Everything working!")'
```

**Observed result:** All libraries imported successfully.

---

## 6. Why Did We Use Jupyter Kernel Registration?

Command:

```bash
python -m ipykernel install --user --name ml_learning --display-name "Python 3.12 (ML Learning)"
```

This registers our Conda environment as a selectable Jupyter kernel.

A kernel is the execution engine that runs code inside a Jupyter notebook.

This allows us to select our `ml_learning` Python environment when executing notebook cells.

---

## 7. Visual Studio Code Integration

We use Visual Studio Code as our primary development environment.

### Required extensions

1. WSL — Connects VS Code to Ubuntu.
2. Python — Provides Python language support.
3. Jupyter — Provides notebook support.

### Opening the project

```bash
cd ~/projects/Iris_Flower_Classification
code .
```

The `code .` command opens the current project directory in Visual Studio Code.

### Selecting the Python interpreter

Selected interpreter:

```text
/home/mercy_dona_s/miniconda3/envs/ml_learning/bin/python
```

This ensures that VS Code uses our Conda environment rather than Windows Python.

---

## 8. Important Troubleshooting

### Issue 1 — Conda command not found

**Cause:** Miniconda installed in Windows is separate from Ubuntu.

**Solution:** Install Miniconda independently inside Ubuntu and initialize the shell.

### Issue 2 — Python venv creation failed

**Cause:** Ubuntu did not have the corresponding Python virtual-environment support package.

**Solution:** We chose Conda instead of installing the missing venv package.

### Issue 3 — Conda Terms of Service error

**Cause:** Anaconda required acceptance of the Terms of Service for its configured package channels.

**Solution:** Review and accept the applicable terms before using those channels.

### Issue 4 — Python 3.13 appeared in VS Code

**Cause:** VS Code terminal was running Windows PowerShell instead of Ubuntu Bash.

**Solution:** Connect VS Code to WSL Ubuntu and select the `ml_learning` interpreter.

### Issue 5 — Bash history expansion error

**Cause:** Bash interpreted the exclamation mark in a double-quoted command.

**Solution:** Use single quotes around the Python command.

---

## 9. Final Environment Architecture

```text
Windows 11
    |
    └── WSL2
          |
          └── Ubuntu Linux
                |
                └── Miniconda
                      |
                      └── ml_learning
                            |
                            ├── Python 3.12
                            ├── NumPy
                            ├── Pandas
                            ├── Matplotlib
                            ├── Seaborn
                            ├── Scikit-learn
                            └── Jupyter
                                  |
                                  └── VS Code
```

---

## 10. Learning Outcomes

After completing this setup, I understand:

- The difference between Windows and Linux development environments.
- The purpose of WSL2.
- Why Conda is useful in machine learning projects.
- How Python environments isolate dependencies.
- Why machine learning libraries are required.
- How Jupyter kernels execute notebook code.
- How VS Code connects to Ubuntu through WSL.
- How to identify and troubleshoot environment-related errors.

**Status:** Development environment configured and library imports verified.

**Next milestone:** Python libraries and Iris dataset exploration.
:::