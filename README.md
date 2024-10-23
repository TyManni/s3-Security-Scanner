# Automated S3 Security Scanner

## Description
The Automated S3 Security Scanner helps AWS users proactively assess their S3 bucket configurations, ensuring compliance with best practices and minimizing the risk of data exposure or breaches.

## Features
- Bucket Permissions Check
- Public Access Detection
- Versioning Verification
- Encryption Verification
- Notification System

## Branches
- **main**: This branch contains the latest updates of the scanner.
- **master**: This branch contains the source code for the S3 Security Scanner project. The main file is `lambda_function.py`, which contains the logic to assess the S3 bucket configurations.


## How to Use
1. **Setup AWS Credentials:** Configure your AWS credentials and permissions to allow access to S3 and SNS.
2. **Run the Scanner:** Execute the scanner script to initiate a comprehensive security check.
3. **Review Findings:** Analyze the generated report and take necessary actions based on the identified vulnerabilities.

## Installation and Requirements
- **Python 3.x**
- **Boto3 Library:** Install with `pip install boto3`
- **AWS Account:** Access to S3 and SNS services is required.
----------------------------------------------------------------
1. Clone the repository:
   ```bash
   git clone https://github.com/<TyManni>/s3-security-scanner.git
