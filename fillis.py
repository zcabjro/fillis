#!/usr/bin/env python
"""Fuzzy.py: Small collection of fuzzy string functions."""

# https://en.wikipedia.org/wiki/Levenshtein_distance
def levenshtein_distance(str1, str2):
    """
        Return the minimum number of character deletions,
        insertions and/or substitutions between two strings.
        :param str1: first string
        :param str2: second string
        :type str1: string
        :type str2: string
        :returns: levenshtein distance between the two strings
        :rtype: int
    """
    cols, rows = len(str1), len(str2)
    matrix = [[0 for col in range(cols + 1)] for row in range(rows + 1)]

    # Distances from empty string
    for col in range(1, cols + 1):
        matrix[0][col] = col
    for row in range(1, rows + 1):
        matrix[row][0] = row

    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            cost = 0 if str1[col - 1] == str2[row - 1] else 1
            matrix[row][col] = min(
                matrix[row][col - 1] + 1,  # deletion
                matrix[row - 1][col] + 1,  # insertion
                matrix[row - 1][col - 1] + cost)  # substitution

    return matrix[rows][cols]


def levenshtein_sorted(source, elems, truncate=False):
    """
      Sort string iterable by levenshtein distance to source
      (optionally truncating elements for comparison).
      :param source: source used for sorting
      :param elems: strings to sort
      :param truncate: whether or not to truncate elements for comparison
      :type source: string
      :type elems: string iterable
      :type truncate: boolean
      :returns: new iterable sorted by levenshtein distance to the source string
      :rtype: string iterable
    """
    return sorted(elems, key=levenshtein_sort_key(source, truncate))


def levenshtein_sort(source, elems, truncate=False):
    """
      Sort string list by levenshtein distance to source
      (optionally truncating elements for comparison).
      :param source: source used for sorting
      :param elems: strings to sort
      :param truncate: whether or not to truncate elements for comparison
      :type source: string
      :type elems: string list
      :type truncate: boolean
      :returns: same list sorted by levenshtein distance to the source string
      :rtype: string iterable
    """
    elems.sort(key=levenshtein_sort_key(source, truncate))
    return elems


def levenshtein_sort_key(source, truncate):
    """
        Get a key function used for calculating levenshtein distance from source.
        :param source: source used for sorting
        :param truncate: whether or not truncate to source length
        :type source: string
        :type truncate: boolean
        :returns: key function used for calculating levenshtein distance from source
        :rtype: function
    """
    if truncate:
        return lambda elem: levenshtein_distance(source, elem[:len(source)])
    else:
        return lambda elem: levenshtein_distance(source, elem)
    