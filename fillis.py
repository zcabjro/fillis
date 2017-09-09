#!/usr/bin/env python
"""Fuzzy.py: Small collection of fuzzy string functions."""

# https://en.wikipedia.org/wiki/Levenshtein_distance
def levenshtein_distance(a, b):
	"""Return the minimum number of character deletions, insertions and/or substitutions between strings a and b."""
	w, h = len(a), len(b)
	matrix = [[0 for x in range(w + 1)] for y in range(h + 1)]

	# Distances from empty string
	for x in range(1, w + 1):
		matrix[0][x] = x
	for y in range(1, h + 1):
		matrix[y][0] = y
	
	for y in range(1, h + 1):
		for x in range(1, w + 1):
			cost = 0 if a[x - 1] == b[y - 1] else 1			
			matrix[y][x] = min(
				matrix[y][x - 1] + 1, # deletion
				matrix[y - 1][x] + 1, # insertion
				matrix[y -1][x - 1] + cost) # substitution
	
	return matrix[h][w]

def levenshtein_sort(source, li, truncate=False):
	"""Return a new list sorted by levenshtein distance to the source string (optionally truncating elements to source length)."""
	if truncate:
		collection = [elem[:len(source)] for elem in li]
	return sorted(li, key=lambda elem: levenshtein_distance(source, elem))