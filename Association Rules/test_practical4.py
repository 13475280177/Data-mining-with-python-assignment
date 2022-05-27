import unittest

import pandas as pd


class TestPractical(unittest.TestCase):

    original_file_q1 = './specs/gpa_question1.csv'
    original_file_q2 = './specs/bank_data_question2.csv'

    def setUp(self):
        self.df_q1_apriori = pd.read_csv('./output/question1_out_apriori.csv')
        self.df_q1_rules6 = pd.read_csv('./output/question1_out_rules06.csv')
        self.df_q1_rules9 = pd.read_csv('./output/question1_out_rules09.csv')
        self.df_q2_fpg = pd.read_csv('./output/question2_out_fpgrowth.csv')
        self.df_q2_rules = pd.read_csv('./output/question2_out_rules.csv')

    def tearDown(self):
        self.df_q1_apriori = None
        self.df_q1_rules6 = None
        self.df_q1_rules9 = None
        self.df_q2_fpg = None
        self.df_q2_rules = None

    def test_question1_itemset_columns_ok(self):
        self.assertIn('support', list(self.df_q1_apriori.columns))
        self.assertIn('itemsets', list(self.df_q1_apriori.columns))

    def test_question1_itemset_rows_ok(self):
        self.assertEqual(29, self.df_q1_apriori.shape[0])

    def test_question1_support_ok(self):
        self.assertTrue(all(map(
            lambda x: x >= 0.15,
            self.df_q1_apriori.support.values.tolist())))

    def test_question1_rules6_columns_ok(self):
        self.assertIn('support', list(self.df_q1_rules6.columns))
        self.assertIn('confidence', list(self.df_q1_rules6.columns))
        self.assertIn('antecedents', list(self.df_q1_rules6.columns))
        self.assertIn('consequents', list(self.df_q1_rules6.columns))

    def test_question1_rules6_rows_ok(self):
        self.assertEqual(44, self.df_q1_rules6.shape[0])

    def test_question1_rules6_confidence_ok(self):
        self.assertTrue(all(map(
            lambda x: x >= 0.6,
            self.df_q1_rules9.confidence.values.tolist())))

    def test_question1_rules9_columns_ok(self):
        self.assertIn('support', list(self.df_q1_rules9.columns))
        self.assertIn('confidence', list(self.df_q1_rules9.columns))
        self.assertIn('antecedents', list(self.df_q1_rules9.columns))
        self.assertIn('consequents', list(self.df_q1_rules9.columns))

    def test_question1_rules9_rows_ok(self):
        self.assertEqual(22, self.df_q1_rules9.shape[0])

    def test_question1_rules9_confidence_ok(self):
        self.assertTrue(all(map(
            lambda x: x >= 0.9,
            self.df_q1_rules9.confidence.values.tolist())))#

    def test_question2_itemset_columns_ok(self):
        self.assertIn('support', list(self.df_q2_fpg.columns))
        self.assertIn('itemsets', list(self.df_q2_fpg.columns))

    def test_question2_itemset_rows_ok(self):
        self.assertEqual(231, self.df_q2_fpg.shape[0])

    def test_question2_support_ok(self):
        self.assertTrue(all(map(
            lambda x: x >= 0.2,
            self.df_q2_fpg.support.values.tolist())))

    def test_question2_rules_row_ok(self):
        self.assertTrue(self.df_q2_rules.shape[0] >= 10)


if __name__ == '__main__':
    unittest.main()
