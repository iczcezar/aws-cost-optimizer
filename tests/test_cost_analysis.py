import unittest
import src.cost_analysis as ca

class TestCostAnalysis(unittest.TestCase):
    def test_parse_cost_data(self):
        mock_response = {
            'ResultsByTime': [{
                'TimePeriod': {'Start': '2024-02-10'},
                'Groups': [{'Keys': ['Amazon EC2'], 'Metrics': {'UnblendedCost': {'Amount': '12.50'}}}]
            }]
        }
        df = ca.parse_cost_data(mock_response)
        self.assertEqual(df.iloc[0]['Service'], 'Amazon EC2')
        self.assertAlmostEqual(df.iloc[0]['Cost'], 12.50)

if __name__ == '__main__':
    unittest.main()
