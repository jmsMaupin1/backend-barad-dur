#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa

__author__ = "jayaimzzz, madarp"

import unittest
# To test solution code, replace next line with `import soln.routes as routes`
import routes


class TestRoutes(unittest.TestCase):

    def test_read_skip_map(self):
        result = routes.read_distances('skip-map.txt')
        expected = {
            'a': [('d', 1000.0), ('b', 1.0)],
            'b': [('d', 200.0), ('a', 1.0), ('c', 1.0)],
            'c': [('b', 1.0), ('d', 1.0)],
            'd': [('a', 1000.0), ('b', 200.0), ('c', 1.0)]
        }
        self.assertDictEqual(result, expected)

    def test_read_sample_map(self):
        result = routes.read_distances('sample-map.txt')
        expected = {
            'a': [('b', 5.0), ('c', 8.0)],
            'c': [('a', 8.0), ('d', 2.0)],
            'b': [('a', 5.0), ('d', 6.0)],
            'e': [('d', 12.0), ('g', 3.0)],
            'd': [('b', 6.0), ('c', 2.0), ('e', 12.0), ('f', 2.0)],
            'g': [('e', 3.0), ('f', 7.0)],
            'f': [('d', 2.0), ('g', 7.0)]
        }
        self.assertDictEqual(result, expected)

    def test_read_sample_noreach(self):
        result = routes.read_distances('sample-map-noreach.txt')
        expected = {
            'a': [('b', 5.0), ('c', 8.0)],
            'b': [('a', 5.0), ('d', 6.0)],
            'c': [('a', 8.0), ('d', 2.0)],
            'd': [('b', 6.0), ('c', 2.0), ('e', 12.0), ('f', 2.0)],
            'e': [('d', 12.0), ('g', 3.0)],
            'f': [('d', 2.0), ('g', 7.0)],
            'g': [('e', 3.0), ('f', 7.0)],
            'x': [('y', 6.0)],
            'y': [('x', 6.0)]
        }
        self.assertDictEqual(result, expected)

    def test_read_me_distances(self):
        result = routes.read_distances('ME-distances.txt')
        expected = {
            'Angle': [('Mitheithel', 36.0)],
            'Tharbad': [('Bree', 384.0), ('Gap of Rohan', 624.0)],
            'Buckland': [('Bree', 50.0)],
            'Grey Havens': [('Forlond', 72.0), ('Tower Hills', 7.0)],
            'Palargir': [('Minis Tirith', 36.0)],
            'Mitheithel': [('Angle', 36.0)],
            'Brandy Hall': [('Hobbiton', 5.0), ('Tuckborough', 5.5)],
            'Truckborough': [('Hobbiton', 5.5), ('Michel Delving', 5.0)],
            'Michel Delving': [('Hobbiton', 5.5), ('Truckborough', 5.0), ('Greenholm', 4.0)],
            'Entwash': [('Edoras', 36.0), ('Limlight', 36.0)],
            'Emen Arnen': [('Ithilian Crossroads', 4.5)],
            'Galadhan': [('Celebrant', 0.75)],
            'Crossings of Poros': [('Ithilian Crossroads', 48.0)],
            'Bree': [('Buckland', 50.0), ('Hobbiton', 192.0), ('Tharbad', 384.0)],
            'Cair Andros': [('Minis Tirith', 5.0)],
            'Barad-Dur': [('Minis Tirith', 36.0)],
            'Rivendell': [('Delta of Greyflood', 96.0)],
            'Tookbank': [('Tuckborough', 0.75)],
            'Ithilian Crossroads': [('Crossings of Poros', 48.0), ('North Border Ithilien', 24.0), ('Emen Arnen', 4.5)],
            'Emyn Arnen': [('Minis Tirith', 2.0)], 'Forlond': [('Grey Havens', 72.0)],
            'Gap of Rohan': [('Tharbad', 624.0), ('Edoras', 264.0)],
            'Minis Tirith': [('Cair Andros', 5.0), ('Edoras', 96.0), ('Barad-Dur', 36.0), ('Emyn Arnen', 2.0), ('Henneth Annun', 6.0), ('Palargir', 36.0), ('Edoras', 673.0)],
            'Isengard': [('Edoras', 48.0)], 'Limlight': [('Entwash', 36.0), ('Celebrant', 24.0)],
            'Lothlorien': [('Edoras', 120.0)],
            'Hobbiton': [('Brandy Hall', 5.0), ('Michel Delving', 5.5), ('Truckborough', 5.5), ('Bree', 192.0)],
            'Greenholm': [('Michel Delving', 4.0), ('Tower Hills', 5.0)], 'Celebrant': [('Limlight', 24.0), ('Galadhan', 0.75)],
            'Tower Hills': [('Greenholm', 5.0), ('Grey Havens', 7.0)],
            'Edoras': [('Isengard', 48.0), ('Minis Tirith', 96.0), ('Gap of Rohan', 264.0), ('Minis Tirith', 673.0), ('Great West Road', 120.0), ('Entwash', 36.0), ('Lothlorien', 120.0)],
            'North Border Ithilien': [('Ithilian Crossroads', 24.0)], 'Tuckborough': [('Brandy Hall', 5.5), ('Tookbank', 0.75)],
            'Delta of Greyflood': [('Rivendell', 96.0)],
            'Henneth Annun': [('Minis Tirith', 6.0)],
            'Great West Road': [('Edoras', 120.0)]
        }
        self.assertDictEqual(result, expected)

    def test_dfs_sample_map(self):
        roads = routes.read_distances('sample-map.txt')
        expected = {
            'a': {'a': 0, 'c': 8.0, 'b': 5.0, 'e': 22.0, 'd': 10.0, 'g': 19.0, 'f': 12.0},
            'b': {'a': 5.0, 'b': 0, 'c': 8.0, 'd': 6.0, 'e': 18.0, 'f': 8.0, 'g': 15.0},
            'c': {'a': 8.0, 'b': 8.0, 'c': 0, 'd': 2.0, 'e': 14.0, 'f': 4.0, 'g': 11.0},
            'd': {'a': 10.0, 'b': 6.0, 'c': 2.0, 'd': 0, 'e': 12.0, 'f': 2.0, 'g': 9.0},
            'e': {'a': 22.0, 'b': 18.0, 'c': 14.0, 'd': 12.0, 'e': 0, 'f': 10.0, 'g': 3.0},
            'f': {'a': 12.0, 'b': 8.0, 'c': 4.0, 'd': 2.0, 'e': 10.0, 'f': 0, 'g': 7.0},
            'g': {'a': 19.0, 'b': 15.0, 'c': 11.0, 'd': 9.0, 'e': 3.0, 'f': 7.0, 'g': 0}
        }
        for starting_pt in expected.keys():
            result = {}
            routes.dfs(starting_pt, 0, roads, result)
            self.assertDictEqual(result, expected[starting_pt])

    def test_dfs_skip_map(self):
        roads = routes.read_distances('skip-map.txt')
        expected = {
            'a': {'a': 0,   'b': 1.0, 'c': 2.0, 'd': 3.0},
            'b': {'a': 1.0, 'b': 0,   'c': 1.0, 'd': 2.0},
            'c': {'a': 2.0, 'b': 1.0, 'c': 0,   'd': 1.0},
            'd': {'a': 3.0, 'b': 2.0, 'c': 1.0, 'd': 0}
        }
        for starting_pt in expected.keys():
            result = {}
            routes.dfs(starting_pt, 0, roads, result)
            self.assertDictEqual(result, expected[starting_pt])

    def test_dfs_noreach(self):
        roads = routes.read_distances('sample-map-noreach.txt')
        expected = {
            'a': {'a': 0, 'b': 5.0, 'c': 8.0, 'd': 10.0, 'e': 22.0, 'f': 12.0, 'g': 19.0},
            'b': {'a': 5.0, 'b': 0, 'c': 8.0, 'd': 6.0, 'e': 18.0, 'f': 8.0, 'g': 15.0},
            'c': {'a': 8.0, 'b': 8.0, 'c': 0, 'd': 2.0, 'e': 14.0, 'f': 4.0, 'g': 11.0},
            'd': {'a': 10.0, 'b': 6.0, 'c': 2.0, 'd': 0, 'e': 12.0, 'f': 2.0, 'g': 9.0},
            'e': {'a': 22.0, 'b': 18.0, 'c': 14.0, 'd': 12.0, 'e': 0, 'f': 10.0, 'g': 3.0},
            'f': {'a': 12.0, 'b': 8.0, 'c': 4.0, 'd': 2.0, 'e': 10.0, 'f': 0, 'g': 7.0},
            'g': {'a': 19.0, 'b': 15.0, 'c': 11.0, 'd': 9.0, 'e': 3.0, 'f': 7.0, 'g': 0},
            'x': {'x': 0, 'y': 6.0},
            'y': {'x': 6.0, 'y': 0}
        }
        for starting_pt in expected.keys():
            result = {}
            routes.dfs(starting_pt, 0, roads, result)
            self.assertDictEqual(result, expected[starting_pt])

    def test_dfs_me_distances(self):
        roads = routes.read_distances('ME-distances.txt')
        # Not testing all possible routes
        expected = {
            'Ithilian Crossroads': {
                'Crossings of Poros': 48.0,
                'Emen Arnen': 4.5,
                'Ithilian Crossroads': 0,
                'North Border Ithilien': 24.0
            },
            'Minis Tirith': {
                'Buckland': 1418.0, 'Grey Havens': 1581.5, 'Palargir': 36.0,
                'Brandy Hall': 1565.0, 'Truckborough': 1565.5,
                'Michel Delving': 1565.5, 'Entwash': 132.0, 'Tharbad': 984.0,
                'Galadhan': 192.75, 'Cair Andros': 5.0, 'Barad-Dur': 36.0,
                'Bree': 1368.0, 'Tookbank': 1571.25, 'Limlight': 168.0,
                'Forlond': 1653.5, 'Gap of Rohan': 360.0, 'Minis Tirith': 0,
                'Isengard': 144.0, 'Lothlorien': 216.0, 'Henneth Annun': 6.0,
                'Greenholm': 1569.5, 'Celebrant': 192.0, 'Tower Hills': 1574.5,
                'Edoras': 96.0, 'Tuckborough': 1570.5, 'Hobbiton': 1560.0,
                'Great West Road': 216.0, 'Emyn Arnen': 2.0},
            'Hobbiton': {
                'Buckland': 242.0, 'Grey Havens': 21.5, 'Palargir': 1596.0,
                'Brandy Hall': 5.0, 'Truckborough': 5.5, 'Michel Delving': 5.5,
                'Entwash': 1500.0, 'Tharbad': 576.0, 'Galadhan': 1560.75,
                'Cair Andros': 1565.0, 'Barad-Dur': 1596.0, 'Bree': 192.0,
                'Tookbank': 11.25, 'Emyn Arnen': 1562.0, 'Forlond': 93.5,
                'Gap of Rohan': 1200.0, 'Minis Tirith': 1560.0,
                'Isengard': 1512.0, 'Limlight': 1536.0, 'Lothlorien': 1584.0,
                'Hobbiton': 0, 'Greenholm': 9.5, 'Celebrant': 1560.0,
                'Tower Hills': 14.5, 'Edoras': 1464.0, 'Tuckborough': 10.5,
                'Henneth Annun': 1566.0, 'Great West Road': 1584.0},
        }
        for starting_pt in expected.keys():
            result = {}
            routes.dfs(starting_pt, 0, roads, result)
            self.assertDictEqual(result, expected[starting_pt])

    def test_sample_map_a_g(self):
        self.assertEqual(
            routes.main(['a', 'g', 'sample-map.txt']),
            "Distance from a to g is 19.0"
        )

    def test_sample_map_a_x(self):
        self.assertEqual(
            routes.main(['a', 'x', 'sample-map.txt']),
            "Destination x is not on the map"
        )

    def test_me_distance_Hobbiton_to_Minis_Tirith(self):
        self.assertEqual(
            routes.main(['Hobbiton', 'Minis Tirith', 'ME-distances.txt']),
            "Distance from Hobbiton to Minis Tirith is 1560.0"
        )

    def test_noreach_a_x(self):
        self.assertEqual(
            routes.main(['a', 'x', 'sample-map-noreach.txt']),
            "You can't get from a to x"
        )


if __name__ == '__main__':
    unittest.main()
