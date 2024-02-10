## SQL INJECTION SCANNER

## Discription
SQLi Vulnerability Scanner is a Python tool designed to detect potential SQL injection vulnerabilities in web applications. It parses URLs, extracts parameters, and sends requests with modified parameter values to identify SQL injection patterns in the HTTP response. This tool is intended for security testing purposes and should only be used on systems where you have explicit permission to test for vulnerabilities.
 

## Prerequisites

    Python 3.6 or higher
    Requests library

## Installation

    Clone the repository to your local machine
    git clone https://github.com/M0hamedsh0aib/sqli-scanner.git

    Install the required Python packages:
    pip install sqli-scanner

 
## Usage 
-u, --url     URL to scan                                sqli-scanner -u https://target.com  
-h, --help    Help Menu

## Features

    Automated detection of SQL injection vulnerabilities in web applications.
    Parsing of URLs to identify parameters for injection.
    Crafting and sending HTTP requests with modified parameter values.
    Analysis of HTTP responses for SQL injection patterns.

## Run Command
To execute the SQLi Vulnerability Scanner, run the following command:

python sqlitool.py --url http://example.com/



## Disclaimer

This tool is provided for educational and testing purposes only. It should only be used on web applications for which you have explicit permission to test for vulnerabilities. The developers assume no liability for any misuse or damage caused by the tool.

## License

This project is licensed under the MIT License. The MIT License is a permissive open-source license that allows you to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to certain conditions. You can find more details in the [LICENSE](LICENSE) file.
