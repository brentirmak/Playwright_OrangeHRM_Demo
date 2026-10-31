<b>(10/30/26) Background: </b>
1) Utilizes pytest to test https://opensource-demo.orangehrmlive.com/web/index.php/auth/login <br>
2) For stepthrough test, uses a fixture to login once and maintain that throughout the tests <br>
3) The admin tests, which are made up of 60+ sub-tests, explores the admin functionality of the site (i.e. ~ 20 pages/sections) <br>
4) The leave test, which is made up of 17 sub-tests, explores the leave section of the site <br>
5) The pim test, which is made up of 8 sub-tests, explores the pim section of the site <br>
6) The time test, contains 30+ sub-tests, explores the time section of the site <br>
7) The recruitment test, which is made up of 9 sub-tests, explored the recruitment section of the site <br>
8) The myinfo test, which is made up 13 sub-tests, explored the myinfo section of the site <br>
9) The performance test, which is made up 18 of sub-tests, explored the performance section of the site <br>
10) The directory test, which is made up of 8 sub-tests, explored the recruitment section of the site <br>
11) The claim test, which is made up of 13 sub-tests, explored the claim section of the site <br>
12) Test results are stored in MySQL where tests are identified by test name and script name <br>
13) Dev Environment is on Windows (Visual Studio Code) <br>
14) Jenkins Instance is running on Ubuntu 26.04.1 LTS - Jenkins(3)