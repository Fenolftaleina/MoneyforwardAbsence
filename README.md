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

