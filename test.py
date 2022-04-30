#!/usr/bin/env python3
import datetime
import time
from multiprocessing import Pool

from numpy import mean


def f(x):
    i = 0
    for j in range(x ** 8):
        i += j
    return i


def process_time():
    clock_t0 = time.time()
    t0 = time.process_time()
    result = f(9)
    print('Result:', result, end='\t')
    t1 = time.process_time()
    clock_t1 = time.time()
    print('CPU time: ', t1 - t0, end='\t')
    print('Clock time: ', clock_t1 - clock_t0)
    return t1 - t0


def multiprocessing_process_time():
    clock_t0 = time.time()
    t0 = time.process_time()
    with Pool(10) as pool:
        result = pool.map(f, [9])
    print('Result:', result[0], end='\t')
    t1 = time.process_time()
    clock_t1 = time.time()
    print('CPU time: ', t1 - t0, end='\t')
    print('Clock time: ', clock_t1 - clock_t0)
    return t1 - t0


if __name__ == '__main__':
    print('Processing in Parent Process\n')
    print('Mean CPU processing time:', mean([process_time() for _ in range(5)]))

    print('\nProcessing in Child Process')
    print('Mean CPU processing time:', mean([multiprocessing_process_time() for _ in range(5)]))