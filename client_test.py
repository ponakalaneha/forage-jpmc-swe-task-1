import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      expected_stock = quote['stock']
      expected_top_ask = quote['top_ask']['price']
      expected_top_bid = quote['top_bid']['price']
      expected_price = (expected_top_ask+expected_top_bid)/2

      real_stock, real_bid, real_ask, real_price = getDataPoint(quote)
      self.assertEqual(expected_price, real_price)
      self.assertEqual(expected_stock, real_stock)
      self.assertEqual(expected_top_ask, real_ask)
      self.assertEqual(expected_top_bid, real_bid)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      expected_stock = quote['stock']
      expected_top_ask = quote['top_ask']['price']
      expected_top_bid = quote['top_bid']['price']
      expected_price = (expected_top_ask+expected_top_bid)/2

      real_stock, real_bid, real_ask, real_price = getDataPoint(quote)
      self.assertEqual(expected_price, real_price)
      self.assertEqual(expected_stock, real_stock)
      self.assertEqual(expected_top_ask, real_ask)
      self.assertEqual(expected_top_bid, real_bid)

  """ ------------ Add more unit tests ------------ """

  def test_getRatio(self):
    value_a = 2.3
    value_b = 2.3
    """ ------------ Add the assertion below ------------ """
    expected_ratio = value_a/value_b

    real_ratio = getRatio(value_a, value_b)
    self.assertEqual(expected_ratio, real_ratio)

  def test_getRation_zero(self):
    value_a = 0
    value_b = 0
    """ ------------ Add the assertion below ------------ """
    getRatio(value_a, value_b)
if __name__ == '__main__':
    unittest.main()
