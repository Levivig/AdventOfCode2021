#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    print('part1:')
    x, y = 0, 0
    for line in data:
        direction = line.split()[0]
        amount = int(line.split()[1])

        if direction == "forward":
            x += amount
        elif direction == "down":
            y += amount
        elif direction == "up":
            y -= amount
    print(x * y)


def part2(data):
    print('part2:')
    x, y, aim = 0, 0, 0
    for line in data:
        direction = line.split()[0]
        amount = int(line.split()[1])

        if direction == "forward":
            x += amount
            y += (aim * amount)
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
    print(x * y)


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        part1(data)
        part2(data)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
