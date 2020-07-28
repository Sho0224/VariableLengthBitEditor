#!/usr/bin/env python
import logging
# reference https://qiita.com/__init__/items/91e5841ed53d55a7895e

def main():
    pass

class BitEditor:
    def __init__(self):
        self.index = 0
        self.empty_bits = 8

    def Write(self,bit_count,value,target):
        logging.debug('value:{}'.format(bin(value)))
        for i in reversed(range(bit_count)):
            logging.debug('i:{}'.format(i))
            logging.debug('self.index:{}'.format(self.index))
            logging.debug('self.empty_bits:{}'.format(self.empty_bits))
            mask = 1 << i
            one_bit = (value & mask) >> i
            target[self.index] += one_bit << (self.empty_bits - 1) 
            self.empty_bits-=1
            logging.debug('one_bit:{}'.format(bin(one_bit)))
            logging.debug('target[{}]:{}'.format(self.index,bin(target[self.index])))

            if self.empty_bits == 0:
                self.index+=1
                self.empty_bits = 8
                target[self.index] = 0
    
        return target

if __name__ == '__main__': main()
