#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(data):
    print('part1:')
    increases = 0
    for idx, line in enumerate(data):
        if idx == 0:
            continue
        num1 = int(data[idx-1])
        num2 = int(line)
        if num2 > num1:
            increases += 1
    print(increases)


def part2(data):
    print('part2:')
    increases = 0
    for idx,line in enumerate(data):
        if idx + 3 >= len(data):
            continue
        sum1 = int(line) + int(data[idx+1]) + int(data[idx+2])
        sum2 = int(data[idx+1]) + int(data[idx+2]) + int(data[idx+3])
        if sum2 > sum1:
            increases += 1
    print(increases)



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
