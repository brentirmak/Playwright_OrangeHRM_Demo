<b>(9/26) Background: </b>
1) Utilizes pytest to test https://opensource-demo.orangehrmlive.com/web/index.php/auth/login <br>
2) For stepthrough test, uses a fixture to login once and maintain that throughout the tests <br>
3) The admin test, which is made up of 6 sub-tests, explores the admin functionality of the site (i.e. ~ 20 pages/sections) <br>
4) The leave test, which is made up of 17 sub-tests, explores the leave section of the site <br>
5) The pim test, which is made up of 8 sub-tests, explores the pim section of the site <br>
6) The time test, which is made up of 13 sub-tests, explores the time section of the site <br>
7) The recruitment test, which is made up 9 sub-tests, explored the recruitment section of the site <br>
8) The myinfo test, which is made up 13 sub-tests, explored the myinfo section of the site <br>
9) The performance test, which is made up 12 sub-tests, explored the performance section of the site <br>
10) The recruitment test, which is made up 8 sub-tests, explored the recruitment section of the site <br>
11) Test results are stored in MySQL where tests are identified by test name and script name <br>
12) Dev Environment is on Windows (Visual Studio Code) <br>
13) Jenkins Instance is running on Ubuntu 24.04 - Jenkins(2) <br> 