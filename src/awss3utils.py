'''
Created on Oct 31, 2012

@author: peng
'''
import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key


class S3():

    def __init__(self, access_key_id, secret_access_key, bucket):
        self.conn = S3Connection(access_key_id, secret_access_key)
        self.bucket = bucket

    def get_files(self, path):
        bucket = self.conn.get_bucket(self.bucket)
        bucket_list = bucket.list(path)
        files = []
        for b in bucket_list:
            files.append(b.name)
        return files

    def download_file(self, s3_key, local_folder):
        '''
        parameters:
            s3_key: input/test/xxx.log-20111117
            local_folder:/home/peng/test
        '''
        bucket = self.conn.get_bucket(self.bucket)
        key = bucket.get_key(s3_key)
        local_file = os.path.join(local_folder, os.path.basename(key.name))
        if os.path.exists(local_file):
            return local_file
        local_folder = os.path.dirname(local_file)
        if not os.path.exists(local_folder):
            os.makedirs(local_folder)
        key.get_contents_to_filename(local_file)
        return local_file

    def download_file2(self, s3_key, local_file):
        '''
        parameters:
            s3_key: input/test/xxx
            local_folder:/home/peng/test.log
        '''
        local_folder = os.path.dirname(local_file)
        if not os.path.exists(local_folder):
            os.makedirs(local_folder)
        bucket = self.conn.get_bucket(self.bucket)
        key = bucket.get_key(s3_key)
        key.get_contents_to_filename(local_file)
        return local_file

    def upload_file(self, local_file, s3_file):
        '''
        parameters:
            local_file: /home/peng/test.log
            s3_path:input/test/
        '''
        bucket = self.conn.get_bucket(self.bucket)
        key = Key(bucket, s3_file)
        key.set_contents_from_filename(local_file)

    def delete_file(self, s3_key):
        '''
        parameters:
            s3_key: input/test/xxx
        '''
        bucket = self.conn.get_bucket(self.bucket)
        for key in bucket.list(s3_key):
            key.delete()
