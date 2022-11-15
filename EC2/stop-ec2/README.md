# Stop Non-Standard AWS EC2 Instances With Tag Checking

## Requirements
Check the EC2 tags and if "Application" tag not found, then stop the EC2 instance.

1. Input - All EC2 Instance IDs
2. Data Parsing -
   Get the list of tag keys and check if the key is in the list or not
   Wait until the server is in stop state
3. Task - Check tags and stop the server if no tag key found
4. Validation - Verify/make sure the non compliant servers are stoppped
