# Setup
Download [Selenium Grid](https://selenium.dev/downloads/) jar file and place it in same directory
where this README is located.

Install [SeleniumLibrary](https://github.com/robotframework/SeleniumLibrary#installation) and 
[browser drivers](https://github.com/robotframework/SeleniumLibrary#browser-drivers).

Install pabot with: `pip install robotframework-pabot`. Install Java, follow your operating system
instructions for Java installations.

# Running tests
From to root of the repository run: `python run_3_paraller.py`
  
# Result
The `run_3_paraller.py` scripts starts Selenium Grid with 
[hub and node roles](https://selenium.dev/documentation/en/grid/components_of_a_grid/).
The script runs tests from `1-browser-configuration` folder with two parallel executions
by using `pabot`.