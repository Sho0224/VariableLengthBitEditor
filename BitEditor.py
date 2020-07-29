#!/usr/bin/env python
import logging
# reference https://qiita.com/__init__/items/91e5841ed53d55a7895e

def main():
    pass

class BitEditor:
    def __init__(self,size):
        self.__BYTE_BIT_SIZE = 8
        self.index = 0
        self.empty_bits = self.__BYTE_BIT_SIZE 
        self.size = size 
        self.bytes = bytearray(range(self.size))

    def Push(self,bit_count,value):
        logging.debug('value:{}'.format(bin(value)))
        for i in reversed(range(bit_count)):
            logging.debug('i:{}'.format(i))
            logging.debug('self.index:{}'.format(self.index))
            logging.debug('self.empty_bits:{}'.format(self.empty_bits))
            mask = 1 << i
            one_bit = (value & mask) >> i
            self.bytes[self.index] += one_bit << (self.empty_bits - 1) 
            self.empty_bits-=1
            logging.debug('one_bit:{}'.format(bin(one_bit)))
            logging.debug('self.bytes[{}]:{}'.format(self.index,bin(self.bytes[self.index])))

            if self.empty_bits == 0:
                self.index+=1
                self.empty_bits = self.__BYTE_BIT_SIZE
                self.bytes[self.index] = 0

    def Pop(self,bit_count):
        self.bytes[0] = self.bytes[0] >> (self.__BYTE_BIT_SIZE - bit_count)
        b = self.bytes[0]
        logging.debug('b:{}'.format(bin(b)))
        return b 
if __name__ == '__main__': main()
