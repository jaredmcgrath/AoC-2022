#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022
Day 4

Created on 2022-12-03T23:53:17.622677

@author: jaredmcgrath
"""
# %% Data loading


def find_path_to_helpers(target_folder="helpers", quiet=False):
    # Skip path finding if we successfully import the dummy file
    try:
        from helpers.dummy import dummy_func
        dummy_func()
        return
    except ImportError:
        not quiet and print("", "Couldn't find helpers directory!",
                            "Searching for path...", sep="\n")

    import os
    import sys
    # Figure out where this file is located so we can work backwards to find the target folder
    file_directory = os.path.dirname(os.path.abspath(__file__))
    path_check = []

    # Check parent directories to see if we hit the main project directory containing the target folder
    prev_working_path = working_path = file_directory
    while True:

        # If we find the target folder in the given directory, add it to the python path (if it's not already there)
        if target_folder in os.listdir(working_path):
            if working_path not in sys.path:
                tilde_swarm = "~"*(4 + len(working_path))
                not quiet and print("\n{}\nPython path updated:\n  {}\n{}".format(
                    tilde_swarm, working_path, tilde_swarm))
                sys.path.append(working_path)
            break

        # Stop if we hit the filesystem root directory (parent directory isn't changing)
        prev_working_path, working_path = working_path, os.path.dirname(
            working_path)
        path_check.append(prev_working_path)
        if prev_working_path == working_path:
            not quiet and print("\nTried paths:", *path_check, "", sep="\n  ")
            raise ImportError(
                "Can't find '{}' directory!".format(target_folder))


def load_data(quiet=True):
    find_path_to_helpers(quiet=quiet)
    if __package__:
        from ..helpers import get_input, ints, floats, get_input_lines
    else:
        from helpers import get_input, ints, floats, get_input_lines

    # data = get_input()
    data = get_input_lines()
    # data = ints(data)
    # data = floats(data)

    return data

# %% Part 1


def part1(data):
    count = 0
    for line in data:
        pair1, pair2 = line.split(",")
        p1 = [int(x) for x in pair1.split("-")]
        p2 = [int(x) for x in pair2.split("-")]
        min_s = p1 if min(p1[0], p2[0]) == p1[0] else p2
        max_s = p1 if max(p1[0], p2[0]) == p1[0] else p2
        if max_s[1] <= min_s[1]:
            count += 1
    return count

# %% Part 2


def part2(data):
    count = 0
    for line in data:
        pair1, pair2 = line.split(",")
        p1 = [int(x) for x in pair1.split("-")]
        p2 = [int(x) for x in pair2.split("-")]
        min_s = p1 if min(p1[0], p2[0]) == p1[0] else p2
        max_s = p1 if max(p1[0], p2[0]) == p1[0] else p2
        if min_s[1] >= max_s[0]:
            count += 1
    return count


# %% Run all
if __name__ == "__main__":
    data = load_data()

    print(part1(data))
    print(part2(data))

# %%
