import logging
import unittest

from api.api import function_from_api

logger = logging.getLogger(__name__)


class TestUnits(unittest.TestCase):
    def test_api(self):
        x = function_from_api()
        self.assertEqual(x, 'I am the return value from api.api!')
        logger.info('Passed test')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
