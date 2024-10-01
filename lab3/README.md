[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/dNCDt2bi)
# CSCI360 (2023Fall) Lab3

## Installation
In addition to lab 1 or 2 installed libraries, we use `pandas`, `matplotlib` and `sklearn` in lab 3. If you want to create a brand new environment for lab 3, use commands:
```
conda create -n csci360_lab3 python=3.8
conda activate csci360_lab3
pip install -r requirements.txt
```
Or, you can install new libraries to previous environment with commands:
```
conda activate [PREVIOUS_ENV_NAME]
pip install -U scikit-learn
pip install pandas
pip install matplotlib
```

## Instructions
- Both main part and extra credit of Lab 3 are in `main.ipynb`. You should have Jupyter Notebook installed back to Lab 0. If not, please run command in your current environment `conda install -c anaconda jupyter`.
- We provide skeleton code in `main.ipynb`. You are required to fill blanks in between `# ===== XXX ===== #` and `# ===== End of XXX ===== #`. If the next block starts with `# TEST ...`, your program should pass all assertions.
- For problem 1 (c-e), you need to find optimal k (and p), make sure you fill in `{}` in pre-defined comment blocks.

## FAQ
### Rules of helper function/class
Write inside `# ===== XXX ===== #` blocks where you will use. When grading, we will call each block once from top. If we encounter an error because you place functions in a later block, we are not going to give points back during regrading (even major point deduction due to syntax error). Note that some compiled functions are saved in memory temporarily so you never get error if you once called the block later.

### Can/should we report optimal k (and p) in README?
We will check `main.ipynb` and find the numbers there. It does not matter whether you report these numbers again in anywhere else. It is ineligible to require regrading if you misplaced these numbers.

### How we will grade
Please check instruction PDF for point assignment. We will not disclose further detailed rubrics.
