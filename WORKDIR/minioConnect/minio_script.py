from minio import Minio
from minio.error import ResponseError
import os
#import skimmage

def getKey():
    with open('gitignore/id.txt','r') as id:
        for i in range (1):
            ID = id.read()
            return ID
    with open('gitignore/mp.txt','r') as mp:
        for i in range (1):
            MP = mp.read()
            return MP


def getMinioClient(ID,MP):
    return Minio(
        'localhost:9000',
        access_key=ID,
        secret_key=MP,
        secure=False
    )
if __name__ == "__main__":
    minioClient = getMinioClient('testkey','testsecret')

    if(not minioClient.bucket_exists('testbucket')):
        try:
            minioClient.make_bucket('testbucket')
        except ResponseError as identifier:
            raise


    try:
        with open('file.txt','rb') as testfile:
            statdata = os.stat('file.txt')
            result = minioClient.put_object(
                'testbucket',
                'miniotest.txt',
                testfile,
                statdata.st_size
            )
            print ('result', result)

    except ResponseError as identifier:
        raise



# Get presigned URL string
url = minioClient.presigned_url('GET',"testbucket","miniotest.txt")
print('url', url)

# Uploads data from a file to an object in a bucket
minioClient.fput_object('testbucket','miniotest.txt','file.txt','application octet stream')

# Uploads data from a stream to an object in a bucket
# file_stat = os.getcwd('capture.png')
# with open ('capture.png','r') as data:
#     minioClient.put_object(
#         'testbucket', 
#         'capture.png',
#         data,
#         file_stat.st_size
#         )