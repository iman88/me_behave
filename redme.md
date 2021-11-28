Download and install python 3.9.6 or above
run: pip install -r requirements.txt

Download chrome driver from https://chromedriver.storage.googleapis.com/index.html?path=96.0.4664.45/

-- run all features from folder
behave Features

-- run tag
behave --tags=sanity

-- run multiple tags at once
behave --tags=sanity,abcd

-- run tests that have multiple tags
behave --tags=sanity --tags=smoke 

-- run test and create json results files
behave -f allure_behave.formatter:AllureFormatter -o allure/reports
behave -f allure_behave.formatter:AllureFormatter -o allure/reports --tags=sanity

Download latets allure zip from https://github.com/allure-framework/allure2
Set allure in PATH
run allure--v

-- open results in allure
allure serve C:\git\behave\allure\reports



