#!/home/russoryan/myenv/bin/python3

import boto3
import requests


s3 = boto3.client('s3', region_name="us-east-1")

img_data = requests.get("https://www.google.com/search?sca_esv=6acdd3b722376336&sxsrf=AHTn8zpID0ADb96DbN_lBNhufuZwFA8adQ:1740685193358&q=rotunda&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBsxayPSIAqObp_AgjkUGqekYoUzDaOcDDjQfK4KpR2OI5Qd-8j1TSLAwLVCkgMnrPWaOMZbwx26hbDhQ5sP58pXkBmb6Oje746jHR2P1mgYbG6fnNXaHEEPPIFfN5s2kRN1g2JLdsz0UpKxecWtOw-3vecz2bKZ5T-VRQUnZjQd6B6gggA&sa=X&sqi=2&ved=2ahUKEwiUqvbUzeSLAxW4F1kFHTY5BZYQtKgLegQIGRAB&biw=1536&bih=826&dpr=1.25#vhid=7XhRA-I6e6Ak4M&vssid=mosaic").content

f = open("rotunda.jpg","wb")
f.write(img_data)
f.close()


bucket = 'ds2002-nqt2bq'
object_name="rotunda.jpg"

resp = s3.put_object(
    Body = object_name,
    Bucket = bucket,
    Key = object_name
)

expires_in = 30
response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': object_name},
    ExpiresIn=expires_in
)

#Revision to Submission Below
#Added
print(response)
