'''
utils tests
===========
'''

import unittest

from kivy.utils import (boundary, escape_markup, format_bytes_to_human,
        is_color_transparent, SafeList, get_random_color, get_hex_from_color,
        get_color_from_hex, strtotuple, QueryDict, intersection, difference,
        interpolate, Platform)


class UtilsTest(unittest.TestCase):
    
    def test_escape_markup(self):
        escaped = escape_markup('Sun [1] & Moon [2].')
        self.assertEqual(escaped, 'Sun &bl;1&br; &amp; Moon &bl;2&br;.')
        
    def test_format_bytes_to_human(self): 
        a = format_bytes_to_human(6463)
        self.assertEqual(a, '6.31 KB')
        b = format_bytes_to_human(6463, precision=4)
        self.assertEqual(b, '6.3115 KB')
        c = format_bytes_to_human(646368746541)
        self.assertEqual(c, '601.98 GB')
        
    def test_boundary(self):
        x = boundary(-1000, 0, 100)
        self.assertEqual(x, 0)
        x = boundary(1000, 0, 100)
        self.assertEqual(x, 100)
        x = boundary(50, 0, 100)
        self.assertEqual(x, 50)
        
    def test_is_color_transparent(self):
        c = [1,1,1]
        self.assertFalse(is_color_transparent(c))
        c = [1,1,1,1]
        self.assertFalse(is_color_transparent(c))
        c = [1,1,1,0]
        self.assertTrue(is_color_transparent(c))

    def test_SafeList_iterate(self): # deprecated
        sl = SafeList(['1', 2, 3.])
        self.assertTrue(isinstance(sl, list))
        it = sl.iterate()
        self.assertEqual(it.next(), '1')
        self.assertEqual(it.next(), 2)
        self.assertEqual(it.next(), 3.)
        
    def test_SafeList_iterate_reverse(self): # deprecated
        sl = SafeList(['1', 2, 3.])
        self.assertTrue(isinstance(sl, list))
        it = sl.iterate(reverse=True)
        self.assertEqual(it.next(), 3.)
        self.assertEqual(it.next(), 2)
        self.assertEqual(it.next(), '1')
        
    def test_SafeList_clear(self):
        sl = SafeList(['1', 2, 3.])
        self.assertTrue(isinstance(sl, list))
        sl.clear()
        self.assertEqual(len(sl), 0)
        
    def test_get_random_color_fixed_alpha(self):
        actual = get_random_color()
        self.assertEqual(len(actual), 4)
        self.assertEqual(actual[3], 1.)
        
        actual = get_random_color(alpha=.5)
        self.assertEqual(len(actual), 4)
        self.assertEqual(actual[3], .5)
        
    def test_get_random_color_random_alpha(self):
        actual = get_random_color(alpha='random')
        self.assertEqual(len(actual), 4)
        
    def test_get_hex_from_color_noalpha(self):
        actual = get_hex_from_color([0, 1, 0])
        expected = '#00ff00'
        self.assertEqual(actual, expected)
        
    def test_get_hex_from_color_alpha(self):
        actual = get_hex_from_color([.25, .77, .90, .5])
        expected = '#3fc4e57f'
        self.assertEqual(actual, expected)
        
    def test_get_color_from_hex_noalpha(self):
        actual = get_color_from_hex('#d1a9c4')
        expected = [0.81960784, 0.66274509, 0.76862745, 1.]
        for i in range(4):
            self.assertAlmostEqual(actual[i], expected[i])
            
    def test_get_color_from_hex_alpha(self):
        actual = get_color_from_hex('#00FF7F7F')
        expected = [0., 1., 0.49803921, 0.49803921] # can't get .5 from hex
        for i in range(4):
            self.assertAlmostEqual(actual[i], expected[i])
            
    def test_strtotuple(self):
        self.assertRaises(Exception, strtotuple, 'adis!_m%*+-=|')
        self.assertRaises(Exception, strtotuple, '((12, 8, 473)')
        self.assertRaises(Exception, strtotuple, '[12, 8, 473]]')
        self.assertRaises(Exception, strtotuple, '128473')
        actual = strtotuple('(12, 8, 473)')
        expected = (12, 8, 473)
        self.assertEqual(actual, expected)
     
    def test_QueryDict(self):
        qd = QueryDict()
        self.assertTrue(isinstance(qd, dict))
        # __setattr__
        qd.toto = 1
        self.assertEqual(qd.get('toto'), 1)
        # __getattr__
        toto = qd.toto 
        self.assertEqual(toto, 1)
        
    def test_intersection(self):
        abcd = ['a', 'b', 'c', 'd']
        efgh = ['e', 'f', 'g', 'h']
        fedc = ['c', 'd', 'e', 'f'] # cdef is cython keyword O_o
        self.assertEqual(intersection(abcd, efgh), [])
        self.assertEqual(intersection(abcd, fedc), ['c', 'd'])
     
    def test_difference(self):
        abcd = ['a', 'b', 'c', 'd']
        efgh = ['e', 'f', 'g', 'h']
        fedc = ['c', 'd', 'e', 'f'] # cdef is cython keyword O_o
        self.assertEqual(difference(abcd, efgh), ['a', 'b', 'c', 'd'])
        self.assertEqual(difference(efgh, fedc), ['g', 'h'])
        
    def test_interpolate_solo(self):
        values = [10., 19., 27.1]
        a = 0.
        for i in range (0, 3):
            a = interpolate(a, 100)
            self.assertEqual(a, values[i])
        
    def test_interpolate_multi(self):
        x = [10., 19., 27.1]
        y = [-10., -19., -27.1]
        p = 0., 0.
        for i in range (0, 3):
            p = interpolate(p, [100, -100])
            self.assertEqual(p, [x[i], y[i]])
        
    def test_Platform(self):
        strPlat = str(Platform())
        self.assertTrue(strPlat in ['android', 'ios', 'win', 'macosx',
                'linux', 'unknown'])
