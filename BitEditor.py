#!/usr/bin/env python
import logging

def main():
    pass

def Write(bit_count,value,target,index,empty_bits):
    logging.debug('value:{}'.format(bin(value)))
    for i in reversed(range(bit_count)):
        logging.debug('i:{}'.format(i))
        logging.debug('index:{}'.format(index))
        logging.debug('empty_bits:{}'.format(empty_bits))
        mask = 1 << i
        one_bit = (value & mask) >> i
        target[index] += one_bit << (empty_bits - 1) 
        empty_bits-=1
        logging.debug('one_bit:{}'.format(bin(one_bit)))
        logging.debug('target[{}]:{}'.format(index,bin(target[index])))

        if empty_bits == 0:
            index+=1
            empty_bits = 8
            target[index] = 0
    
    return target,index,empty_bits

if __name__ == '__main__': main()
