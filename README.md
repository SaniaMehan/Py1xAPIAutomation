Python API Automation Framework
Hybrid Custom Framework to Test the REST APIs

![image](https://github.com/SaniaMehan/Py1xAPIAutomation/assets/147236996/0fe8fa33-c892-497d-af22-cfc379c20957)
















README file is nothing but it is Python API Authomation Framework or
documentation

It is Hybrid Custom Framework to test the REST APIs

## Tech Stack

1.Python 3.11
2.Requests used to make our HTTP Requests
3.Pytest = It is testing framework
4.Reporting = Allure Report, Pytest HTML
5.Test Data = which we keep in Excel file, CSV file or JSON file also
6.Parallel Execution = this will use xdsitribute dependency


How to Install Packages
pip install requests pytest pytest-html faker allure-pytest jsonschema

To Freeze your Package version
pip freeze > requirements.txt

To Install te Freeze Version
pip install -r requirements.txt

How to run your Testcase Parallel
pip install pytest-xdist

pytest -n auto tests/integration_test/test_create_booking.py -s -v 
