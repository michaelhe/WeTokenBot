# -*- coding=utf-8

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)1.4s|%(threadName)s|%(asctime)s|%(name)s|%(message)s'
)

# logging.getLogger("requests").setLevel(logging.CRITICAL)

logger = logging.getLogger('wetokenbot')