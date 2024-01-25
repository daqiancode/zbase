from zbase.env import getEnv
import unittest





class EnvTest(unittest.TestCase):

    
    def test_s3_main(self):
        print(getEnv('a'))
        print(getEnv('b'))
        print(getEnv('c'))



if __name__ == '__main__':
    unittest.main()