#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advent of Code 2022
Day 5

Created on 2022-12-04T23:41:17.034086

@author: jaredmcgrath
"""

from typing import Dict, List, Set, Tuple

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

    data = get_input()

    initial_state = [
        ["N", "R", "G", "P"],
        ["J", "T", "B", "L", "F", "G", "D", "C"],
        ["M", "S", "V"],
        ["L", "S", "R", "C", "Z", "P"],
        ["P", "S", "L", "V", "C", "W", "D", "Q"],
        ["C", "T", "N", "W", "D", "M", "S"],
        ["H", "D", "G", "W", "P"],
        ["Z", "L", "P", "H", "S", "C", "M", "V"],
        ["R", "P", "F", "L", "W", "G", "Z"]
    ]
    moves_txt_split = [x.split(" ") for x in data.split("\n")[10:]]
    moves = [{"n": int(x[1]), "src": int(x[3]), "dst": int(x[5])}
             for x in moves_txt_split]

    # data = get_input_lines()
    # data = ints(data)
    # data = floats(data)

    return initial_state, moves

# %% Part 1


def part1(data: Tuple[List[List[str]], List[Dict[str, int]]]):
    state, moves = data
    # Note: added after submission
    state = [[x for x in stack] for stack in state]

    for move in moves:
        n = move["n"]
        src = move["src"]
        dst = move["dst"]

        while n > 0:
            to_move = state[src - 1].pop()
            state[dst - 1].append(to_move)
            n -= 1

    top = [x[len(x) - 1] for x in state]

    return "".join(top)

# %% Part 2


def part2(data: Tuple[List[List[str]], List[Dict[str, int]]]):
    state, moves = data
    # Note: added after submission
    state = [[x for x in stack] for stack in state]

    for move in moves:
        n = move["n"]
        src = move["src"]
        dst = move["dst"]

        to_move = []
        while n > 0:
            to_move.append(state[src - 1].pop())
            n -= 1

        while len(to_move) > 0:
            state[dst - 1].append(to_move.pop())

    top = [x[len(x) - 1] for x in state]

    return "".join(top)


# %% Run all
if __name__ == "__main__":
    data = load_data()

    print(part1(data))
    print(part2(data))

# %%
