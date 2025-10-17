# Rtivik-pycloud-projects

# 1. EC2 Instance Monitoring Tool

This Python script uses the Boto3 SDK to connect to AWS EC2 and provide a detailed inventory report.

## Key Features:
- Connects securely using local AWS CLI configuration.
- Navigates complex EC2 API data (Reservations, Instances, Tags).
- Extracts human-readable instance Name, ID, and State.
- Uses defensive programming (try/except, .get()) for robust operation.

## Requirements
- Python 3.x
- AWS CLI configured locally
- `pip install boto3`
