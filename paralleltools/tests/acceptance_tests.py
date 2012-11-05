import sys
import unittest
import random

import paralleltools

if sys.version_info >= (3, 0):
    xrange = range


class AcceptanceTestCase(unittest.TestCase):

    ### Map:

    def test_sync_map(self):
        lst = [1, 3, 3, 7]
        exp = [1, 9, 9, 49]

        res = paralleltools.map(lambda x: x * x, lst)
        assert set(res) == set(exp), res

    def test_async_map(self):
        def callback(res):
            assert res in exp, res

        lst = [1, 3, 3, 7]
        exp = [1, 9, 9, 49]
        paralleltools.async_map(lambda x: x * x, lst, callback=callback)

    def test_map_empty(self):
        res = paralleltools.map(lambda x: x, [])

        assert len(res) == 0, res

    def test_map_large_input(self):
        func = lambda x: x / 2
        lst = random.sample(xrange(10 ** 6), 10 ** 5)
        exp = map(func, lst)

        res = paralleltools.map(func, lst)
        assert set(res) == set(exp)

    def test_map_zero_threads(self):
        test_func = lambda: paralleltools.map(lambda x: x, [], threads=0)
        self.assertRaises(ValueError, test_func)

    def test_map_one_thread(self):
        # running one thread shouldn't affect ordering

        lst = [1, 2, 3, 4, 5]
        exp = [2, 3, 4, 5, 6]

        res = paralleltools.map(lambda x: x + 1, lst, threads=1)
        assert res == exp, res

    def test_map_few_threads(self):
        lst = [1, 2, 3, 4, 5]
        exp = [2, 3, 4, 5, 6]

        res = paralleltools.map(lambda x: x + 1, lst, threads=2)
        assert set(res) == set(exp), res

    def test_map_many_threads(self):
        lst = [1, 2, 3, 4, 5]
        exp = [2, 3, 4, 5, 6]

        res = paralleltools.map(lambda x: x + 1, lst, threads=20)
        assert set(res) == set(exp), res

    def test_map_dying_thread(self):
        def dying(el):
            if el == 3:
                raise Exception("This exception shouldn't fail the tests")

            return func(el)

        func = lambda x: x * 2
        lst = [1, 2, 3, 4]
        exp = [2, 4, 8]

        res = paralleltools.map(dying, lst)
        assert set(res) == set(exp), res

    ### Filter:

    def test_sync_filter(self):
        lst = [1, 3, 3, 7]
        exp = [1, 7]

        res = paralleltools.filter(lambda x: x != 3, lst)
        assert set(res) == set(exp), res

    def test_async_filter(self):
        def callback(res):
            assert res in exp, res

        lst = [1, 3, 3, 7]
        exp = [1, 7]

        paralleltools.async_filter(lambda x: x != 3, lst, callback=callback)

    def test_filter_empty(self):
        res = paralleltools.filter(lambda x: True, [])

        assert len(res) == 0, res

    def test_filter_large_input(self):
        func = lambda x: x > 100500
        lst = random.sample(xrange(10 ** 6), 10 ** 5)
        exp = filter(func, lst)

        res = paralleltools.filter(func, lst)
        assert set(res) == set(exp)

    def test_filter_zero_threads(self):
        test_func = lambda: paralleltools.filter(lambda x: x, [], threads=0)
        self.assertRaises(ValueError, test_func)

    def test_filter_one_thread(self):
        # running one thread shouldn't affect ordering
        lst = [1, 3, 3, 7]
        exp = [1, 7]

        res = paralleltools.filter(lambda x: x != 3, lst, threads=1)
        assert res == exp, res

    def test_filter_few_threads(self):
        lst = [1, 3, 3, 7]
        exp = [1, 7]

        res = paralleltools.filter(lambda x: x != 3, lst, threads=2)
        assert set(res) == set(exp), res

    def test_filter_many_threads(self):
        lst = [1, 3, 3, 7]
        exp = [1, 7]

        res = paralleltools.filter(lambda x: x != 3, lst, threads=20)
        assert set(res) == set(exp), res

    def test_filter_dying_thread(self):
        def dying(el):
            if el == 3:
                raise Exception("This exception shouldn't fail the tests")

            return func(el)

        func = lambda x: x != 1
        lst = [1, 2, 3, 4]
        exp = [2, 4]

        res = paralleltools.filter(dying, lst)
        assert set(res) == set(exp), res


if __name__ == '__main__':
    unittest.main()
