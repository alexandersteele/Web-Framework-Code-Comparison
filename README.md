## Requirements
*	Prerequisite libraries
*	Python3 programming language
*	A dataset to analyse/compare
*	A Command-Line Interface (CLI) to execute the software
Recommended:
* Linux-based operating system or Windows with WSL
* Virtual environment (e.g. pipenv)

### Prerequisite Libraries
Using your CLI the following libraries should be installed:

```pip install gitpython```
```pip install requests```


### Python3 Language
To install Python3 on Linux enter the commands:

```sudo apt-get update```
```sudo apt-get install python3.6```
  
### Dataset
This project includes a precompiled collection of repositories designed to demonstrate software functionality. If however, you wish to add your own data then simply copy repositories into the root dataset directory (/cloned_repos/). Alternatively the software provides Git clone functionality. Using the software you can enter a designated GitHub organization (collection of repositories) to clone into the dataset directory.

## Running the Software without Thresholds
To run the software without thresholds, enter the following command into your CLI:

```python3 compare_repos.py```

## Running the Software with Thresholds
The software can be run with threshold values ranging from 0 to 100 (100 being repositories that completely match for that given fundamental feature). The flags are entered into your CLI at execution and are ordered: frameworks, endpoints, model classes, model fields.

```python3 compare_repos.py 40 30 20 10```

The example above shows the CLI instruction to run the software with:
1.	40% matching frameworks
2.	30% matching endpoints
3.	20% matching model classes
4.	10% matching model fields

## Interpreting Results
Every matched repository pair found within the threshold values will output to the CLI, You will be shown a title for each comparison (with the names of the matched repositories). Inside each comparison title will be relevant data on the match percentage of framework and fundamental features, and the matched source code lines for each matching feature.
