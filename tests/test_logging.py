import logging
import unittest


class TestLogging(unittest.TestCase):
    def test_import_does_not_configure_root_logger(self):
        root = logging.getLogger()
        handlers_before = len(root.handlers)

        # Re-importing should not add handlers to root logger
        import importlib
        import gnews
        importlib.reload(gnews)

        # Root logger handlers should not increase due to gnews import
        self.assertEqual(len(root.handlers), handlers_before)

    def test_gnews_has_own_logger(self):
        from gnews.gnews import logger
        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.name, "gnews.gnews")

    def test_gnews_logger_uses_null_handler(self):
        from gnews.gnews import logger
        gnews_logger = logging.getLogger("gnews.gnews")
        handler_types = [type(h) for h in gnews_logger.handlers]
        self.assertIn(logging.NullHandler, handler_types)
        # must not add a StreamHandler (which would pollute user apps)
        self.assertNotIn(logging.StreamHandler, handler_types)
