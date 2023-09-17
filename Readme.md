Use Case #06

TL;DR
Time = 4H
Results - none. I didn't get the working code.


Log:
Create volumes and snapshots ~ 10 min.
Create Role (EBS-usecase06) and attach correct policies ~ 5 min.
The next time, I spent understanding how to get the working code.
The role is correct. 
hello.py - create the folders. Screenshot - S3-files.png

get_ebs_snap_info.py - shows info about EBS and volumes. Screenshot - showsinfo.png

info_to_s3bucket.py and info_to_s3bucket_with_function.py - doesn't work— this code from ChatGPT.

Using boto3.client for s3 and ec2 in one Lambda function - doesn't work in this code.
I have no experience with Python Lambda and ran out of time to resolve it.
