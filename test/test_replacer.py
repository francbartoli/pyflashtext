from flashtext.keyword import KeywordProcessor
import logging
import unittest
import json

logger = logging.getLogger(__name__)


class TestKeywordExtractor(unittest.TestCase):
    def setUp(self):
        logger.info("Starting...")
        with open('test/keyword_extractor_test_cases.json') as f:
            self.test_cases = json.load(f)

    def tearDown(self):
        logger.info("Ending.")

    def test_replace_keywords(self):
        """For each of the test case initialize a new KeywordProcessor.
        Add the keywords the test case to KeywordProcessor.
        Replace keywords and check if they match the expected result for the test case.

        """
        for test_id, test_case in enumerate(self.test_cases):
            keyword_replacer = KeywordProcessor()
            keyword_replacer.add_keywords_from_dict(test_case['keyword_dict'])
            new_sentence = keyword_replacer.replace_keywords(test_case['sentence'])

            keyword_extractor = KeywordProcessor(case_sensitive=True)
            keyword_extractor.add_keywords_from_list(list(test_case['keyword_dict'].keys()))
            keywords_extracted = keyword_extractor.extract_keywords(new_sentence)

            self.assertEqual(keywords_extracted, test_case['keywords'],
                             "keywords_extracted don't match the expected results for test case: {}".format(test_id))

if __name__ == '__main__':
    unittest.main()