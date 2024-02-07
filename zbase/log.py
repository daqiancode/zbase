import logging
from zbase.env import getEnv
import sys

logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s.%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=getEnv("LOG_LEVEL","INFO").upper())
