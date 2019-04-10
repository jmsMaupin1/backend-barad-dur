#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "jayaimzzz"

import unittest
import routes
import subprocess


class TestRoutes(unittest.TestCase):
    def test_read_distances(self):
        map_file = "sample-map.txt"
        connections = {
            'a': [('b', 5.0), ('c', 8.0)],
            'c': [('a', 8.0), ('d', 2.0)],
            'b': [('a', 5.0), ('d', 6.0)],
            'e': [('d', 12.0), ('g', 3.0)],
            'd':  [('b', 6.0), ('c', 2.0), ('e', 12.0), ('f', 2.0)],
            'g': [('e', 3.0), ('f', 7.0)],
            'f': [('d', 2.0), ('g', 7.0)]
        }
        with open(map_file) as file:
            self.assertEquals(routes.read_distances(file), connections)

    def test_dfs(self):
        map_file = "sample-map.txt"
        place = "a"
        dist_so_far = 0
        distances = {}
        distances_ans = {'a': 10.0, 'c': 8.0, 'b': 5.0, 'e': 22.0, 'd': 10.0, 'g': 19.0, 'f': 12.0}
        with open(map_file) as file:
            roads = routes.read_distances(file)
            routes.dfs(place, dist_so_far, roads, distances)
        self.assertAlmostEquals(distances, distances_ans)

    def test_a_to_g_sample_map(self):
        process = subprocess.Popen(
            ["python", "./routes.py", "a", "g", "sample-map.txt"],
            stdout=subprocess.PIPE
        )
        stdout, _ = process.communicate()
        self.assertEquals(stdout, "Distance from a to g is 19.0\n")

    def test_a_to_x_sample_map(self):
        process = subprocess.Popen(
            ["python", "./routes.py", "a", "x", "sample-map.txt"],
            stdout=subprocess.PIPE
        )
        stdout, _ = process.communicate()
        self.assertEquals(stdout, "Destination x is not on the map\n")

    def test_Hobbiton_to_Minis_Tirith_ME_distances(self):
        process = subprocess.Popen(
            ["python", "./routes.py", "Hobbiton", "Minis Tirith", "ME-distances.txt"],
            stdout=subprocess.PIPE
        )
        stdout, _ = process.communicate()
        self.assertEquals(stdout, "Distance from Hobbiton to Minis Tirith is 1560.0\n")

if __name__ == '__main__':
    unittest.main()
