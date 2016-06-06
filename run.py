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

    print("Chosen " + chosen)

def read_list(path):
    with open(path, 'r') as f:
        return f.readlines()
    
if __name__ == "__main__":
    main()

