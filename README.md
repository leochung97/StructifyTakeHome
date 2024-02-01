# Structify Take-Home Assignment

## Summary

Using Python3, I have created an algorithm that will count the number of intersecting chords in a circle.
I first identify the chords through `find_chords`, which returns a map of lines (key: integer, value: [radian1, radian2]). The values list is always sorted so that the radian1 < radian2. This prevents any errors in the case of the identifiers argument containing non-sorted points (i.e., it won't matter if 'e2' shows up before 's2').

Every pair of chords returned from `find_chords` are then checked for intersections in `count_intersections` by determining whether `(s1 < s2 < e1) and (s2 < e1 < e2)`.

I provided a visual representation of the chords intersecting as well through `matplotlib.pyplot`.

## Usage

My submission requires Python3 to be installed on your device.

In the file directory, type `python3 submission.py` into your console and hit enter. The command line will ask for an input on which test case to show; enter a number between 1 and 5 (you can add your own test cases to the program by replacing the existing examples). A separate pop-up window will provide a sample graph of the intersecting lines assuming a radius of 1.

## Time Complexity

Time complexity: O(n^2) - n represents the number of radians / identifiers in the input. The time complexity of `find_chords` is O(n) as we iterate through each radian / identifier to create a map of existing chords. The time complexity of `count_intersections` is O(n^2) as we iterate through every possible pair of chords using two for loops to determine whether they intersect. Asymptotically, the entire algorithm is O(n^2).

Space complexity: O(n) - n represents the number of radians / identifiers in the input. In `find_chords`, we store the coordinates of chords in a hashmap that scales linearly to the number of inputs.
