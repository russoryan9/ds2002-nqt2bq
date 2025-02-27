#!/bin/bash

filename="$1"
bucketname="$2"
expire=604800

if [ "$#" -eq 3 ]; then
	expire="$3"
fi

aws s3 cp "$filename" s3://"$bucketname"

aws s3 presign --expires-in "$expire" s3://"$bucketname"/"$filename"
