#!/usr/bin/python

import random

def main():
    # Load the lists
    done = read_list("done.txt")
    total = read_list("static/all.txt")

    # Get the undone countries
    undone = [c for c in total if c not in done]

    # Pick a random one
    chosen = random.choice(undone)
    chosen_split = chosen.split("|")
    chosen_code = chosen_split[0]
    chosen_name = chosen_split[1]

    print("Chosen " + chosen_code + " - " + chosen_name)

def read_list(path):
    with open(path, 'r') as f:
        return f.readlines()
    
if __name__ == "__main__":
    main()

