import unittest

import pandas as pd


class TestPractical(unittest.TestCase):

    original_file_q1 = './specs/markB_question.csv'

    def setUp(self):
        self.df_mcq1 = pd.read_csv('./output/question_mcq1.csv')
        self.df_mcq2 = pd.read_csv('./output/question_full.csv')

    def tearDown(self):
        self.df_mcq1 = None
        self.df_mcq2 = None

    def test_mcq1_columns_ok(self):
        cols = list(self.df_mcq1.columns)

        self.assertIn('MCQ1', cols)
        self.assertIn('MCQ2', cols)
        self.assertIn('final', cols)
        self.assertIn('final_linear', cols)
        self.assertIn('final_poly2', cols)
        self.assertIn('final_poly3', cols)
        self.assertIn('final_poly4', cols)
        self.assertIn('final_poly8', cols)
        self.assertIn('final_poly10', cols)

    def test_mcq1_rows_ok(self):
        self.assertEqual(16, self.df_mcq1.shape[0])

    def test_mcq1_prediction_ok(self):
        rows = self.df_mcq1[self.df_mcq1['MCQ1'] == 90]

        for i in range(rows.shape[0]):
            v = round(rows.iloc[i].final_linear, 0)
            self.assertAlmostEqual(80, v, 2)
            
    def test_full_columns_ok(self):
        cols = list(self.df_mcq2.columns)

        self.assertIn('MCQ1', cols)
        self.assertIn('MCQ2', cols)
        self.assertIn('final', cols)
        self.assertIn('final_linear', cols)
        self.assertIn('final_quadratic', cols)
       

    def test_mcq2_rows_ok(self):
        self.assertEqual(16, self.df_mcq1.shape[0])

    def test_mcq2_prediction_ok(self):
        rows = self.df_mcq2[(self.df_mcq2['MCQ1'] == 90) & (self.df_mcq2['MCQ2'] == 85)]

        for i in range(rows.shape[0]):
            v = round(rows.iloc[i].final_linear, 1)
            self.assertAlmostEqual(81.6, v, 2)
        
        for i in range(rows.shape[0]):
            v = round(rows.iloc[i].final_quadratic, 1)
            self.assertAlmostEqual(81.4, v, 2)
            break;

    
if __name__ == '__main__':
    unittest.main()
