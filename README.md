<b>(8/25) Background: </b>
1) Utilizes pytest to test https://opensource-demo.orangehrmlive.com/web/index.php/auth/login <br>
2) For stepthrough test, uses a fixture to login once and maintain that throughout the tests <br>
3) The admin test, which is made up of 6 sub-tests, explores the admin functionality of the site (i.e. ~ 20 pages/sections) <br>
4) Test results are stored in MySQL where tests are identified by test name and script name <br>
5) Dev Environment is on Windows (Visual Studio Code) <br>
6) Jenkins Instance is running on Ubuntu 24.04 - Jenkins(2) <br> 