# MoneyforwardAbsence
Code for automatically filling out absences in the money forward system using _selenium_ in _python_.


## Setup

- A driver for the browser being used is necessary for the code to run. For the case of Chrome, you can download your version from: https://chromedriver.chromium.org/downloads ;
- The version of the driver and the browser need to be the same. This can be checked in the "About Google Chrome" section of the help tab avalilable from the dropdown menu in the top right corner of the browser window;
- Change "PATH" to the path of the downloaded driver;
- For this implementation, we used Google Chrome Beta (Google Chrome 103 had several bugs within selenium), so we set the binary location as the path to the Chrome Beta browser. Some browsers will require this, some will not, check documentation for webdriver.BROWSER for setup.
- Change "id" field to the id of company;
- Change "mail" field to account email;
- Change "pw" field to account password;
- The code has a threshold value for a function called _checkmonth()_. This is so that even if you run the program on the beginning of the following month, the program will still correctly fill out information on the previous month. In the current implementation, this can be done until theb 7th day of the subsequent month. After that, the code will not switch month and will fill absences in the current month.

