#  TDD in Python
## Setup
1. Install python3
2. Install pip3
```
pip3 install -U pytest
```
OR 

```
pip install -U pytest
```
## Running test

#### Plain and simple
```
pytest
```
#### With output from stdout 
```
pytest --show-capture stdout
```

#### Run single test
```
pytest test_21_recent_filelist.py::test_empty_list
```