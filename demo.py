import os
from pathlib import Path

from src.bucket import create_bucket, download_file, upload_new_file

# CONSTANTS
BUCKET_NAME = "my-studies-test-for-learning"
# us-east-1 is not working
REGION = "us-east-2"
KEY = "hello.txt"

if __name__ == "__main__":
    create_bucket(bucket_name=BUCKET_NAME, region=REGION)
    print(f"Bucket {BUCKET_NAME} created!")

    with open("hello.txt", "w+b") as data:
        data.writelines([b"Hello\n", b"World\n", b"AWS!! =)"])
        data.seek(0)
        print(f"Creating and uploading a dumb file {KEY} ...")
        response = upload_new_file(bucket_name=BUCKET_NAME, data=data, key=KEY)
        print(response)
        os.remove(KEY)
        print(f"{KEY} removed locally!")

    print("---")

    download_file(bucket_name=BUCKET_NAME, key=KEY, filename_path="hi.txt")
