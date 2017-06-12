import unittest

from coala_quickstart.info_extraction.Info import Info
from coala_quickstart.info_extraction.InfoExtractor import InfoExtractor


class InfoTest(unittest.TestCase):

    def setUp(self):

        class DummyInfoExtractor(InfoExtractor):

            def parse_file(self, file_content):
                return file_content

            def find_information(self, fname, parsed_file):
                return [Info(
                    fname,
                    'Dummy information it is!')]

        self.base_info = Info(
            'source_file',
            'base_info_value',
            DummyInfoExtractor(['some_file'], 'some_dir'))

        class InfoA(Info):
            description = 'Information A'

            def __init__(self,
                         source,
                         value,
                         extra_param):
                super().__init__(source, value)
                self.extra_param = extra_param

        self.info_a = InfoA(
            'source_file',
            'info_a_value',
            'extra_param_value')

    def test_main(self):
        self.assertEqual(self.base_info.name, 'Info')
        self.assertEqual(self.base_info.value, 'base_info_value')
        self.assertEqual(self.base_info.source, 'source_file')
        self.assertEqual(self.base_info.description, 'Some information')
        self.assertIsInstance(self.base_info.extractor, InfoExtractor)

    def test_derived_instances(self):
        self.assertEqual(self.info_a.name, 'InfoA')
        self.assertEqual(self.info_a.value, 'info_a_value')
        self.assertEqual(self.info_a.source, 'source_file')
        self.assertEqual(self.info_a.extra_param, 'extra_param_value')
        self.assertEqual(self.info_a.description, 'Information A')