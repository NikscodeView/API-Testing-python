# API Testing
The projects includes API testing on different set of API testing achieved through different python libraries. The tests folder contains tests on unit tests, API tests, contract tests and security tests as essential testing areas of API testing.

## Getting started :
The repository uses pytest as the test writing library for different scenarios using vscode as the IDE
Set up pytest in VS code.

## Prerequisites
Before we set up Pytest in VS Code, you need to install the below prerequisites in your operating system-
  * VS Code 
  * Python

## Setting Up Pytest In VS Code
To set up Pytest in VS Code, follow the steps described below-
Check the pip version installed and use the set up version to work with pytest - 
  * Pip3 install pytest
  * Pip3 show pytest : To check the version

## Installing Python Extension in VS Code
Open your VS Code and search for Python on the extensions. You’ll find the Python extension at the top of the search result. Select and click install.
This allows to work with python interact within VSCode and utilize Github copilot as an agent.

## Configure pytest
Now the Python extension installation will automatically install Pytest on your environment. All you need to do is just configure Pytest. Follow the below steps to configure Pytest.
Click the flask icon on the left tool bar. You can find this once you open a repository that contains Python unit tests.
Now click on “Configure Python Tests”, select pytest and the test code library. After configuring Pytest, VS Code will automatically discover your Unit Tests. 

## Installing requests
  * To download and install requests, run this command from the terminal : pip install requests
  
## Settting up virtual environment
Pytest is particularly effective in virtual environments when VSCode is utilized. A virtual environment is a way to create an environment that is built-in. A folder is created by a virtual environment that contains a copy to a specific interpreter. Installing packages in a virtual environment will result in a new folder that is isolated from other packages used by other workspaces.
Working in virtual environments-
Pyenv is a library to work with different python environments-
  * brew install pyenv
  * pyenv install 3.13

## Add libraries to be used in the package to requirements.txt :
**Set up requirements.txt for required packages** 

  * [pydantic](https://docs.pydantic.dev/latest/)  - Data validation library for python
  * requests - To get data from APIs
  * [pytest](https://docs.pytest.org/en/stable/) - python testing library
  * jsonschema : to enable json structure for python
  * [pytest-html](https://pypi.org/project/pytest-html/) : plugin for pytest to generate HTML report for results
  * [pytest-cov](https://pypi.org/project/pytest-cov/) : pytest plugin to render coverage reports.
  * pre-commit : maange pre commit hooks

  To install the set up: pip install -r requirements.txt

## Report view in VScode console TEST RESULTS :
The report view provides report after execution of tests in TEST RESULTS tab in VScode. The results are in html format using pytest-html format of report structure woth pytest-cov that gives stats on test execution and code coverage at the end of each run.



