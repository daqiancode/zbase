from zbase.drivers.s3 import S3Client
from zbase.env import getEnv
import unittest
from io import BytesIO



class S3ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = S3Client(bucket="test")
        self.client.ensureBucket()
    
    def test_s3_main(self):
        key = "test/hello"
        r = self.client.put(key, b"hello world","text/plain")
        self.assertEqual(r.object_name, key)
        r = self.client.put(key, BytesIO(b"hello world"),"text/plain")
        self.assertEqual(r.object_name, key)
        bs = self.client.get(key)
        self.assertEqual(bs, b"hello world")

        r = self.client.download(key, "tests/data/hello.txt")
        self.assertEqual(r.content_type, "text/plain")

        srcFile = "tests/drivers/s3_test.py"
        r = self.client.put(srcFile,srcFile , "text/plain")
        self.assertEqual(r.object_name, srcFile)
        self.client.putDir("tests/drivers","tests" ,{"txt":"text/plain"})

if __name__ == '__main__':
    unittest.main()
