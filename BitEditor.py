#!/usr/bin/env python
import logging
# reference https://qiita.com/__init__/items/91e5841ed53d55a7895e

def main():
    bitEditor = BitEditor(size=4,is_debug_log=True)
    bitEditor.Write(5,0b10101)
    print(bin(bitEditor.bytes[1]))

class BitEditor:
    def __init__(self,size=1,is_debug_log=False):
        self.index = 0
        self.__BYTE_BIT_SIZE = 8
        self.empty_bits = self.__BYTE_BIT_SIZE 
        self.size = size 
        self.bytes = bytearray(range(self.size))
        if is_debug_log:
            logging.basicConfig(level=logging.DEBUG)

    def Push(self,bit_count,value):
        self.bytes[self.index] = self.bytes[self.index] << self.empty_bits
        if self.empty_bits == 0:
            return
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

            if self.index < self.size - 1:
                if self.empty_bits == 0:
                    self.index+=1
                    self.empty_bits = self.__BYTE_BIT_SIZE
                    self.bytes[self.index] = 0
        self.bytes[self.index] = self.bytes[self.index] >> self.empty_bits

    def Pop(self,bit_count):
        self.bytes[self.index] = self.bytes[self.index] << self.empty_bits
        if self.size <= 1:
            b = self.bytes[0] >> (self.__BYTE_BIT_SIZE - bit_count)
            self.bytes[0] = 0b11111111 & (self.bytes[0] << bit_count)

        for i in reversed(range(self.size - 1)):
            print('self.bytes[{}]:{}'.format(i+1, bin(self.bytes[i+1])))
            print('self.bytes[{}]:{}'.format(i, bin(self.bytes[i])))
            top = self.bytes[i+1] >> (self.__BYTE_BIT_SIZE - bit_count)
            b = self.bytes[i] >> (self.__BYTE_BIT_SIZE - bit_count)
            self.bytes[i+1] = 0b11111111 & (self.bytes[i+1] << bit_count)
            self.bytes[i] = 0b11111111 & (self.bytes[i] << bit_count) + top
            print('top:{}'.format(bin(top)))
            print('b:{}'.format(bin(b)))

        self.bytes[self.index] = self.bytes[self.index] >> self.empty_bits
        return b 
if __name__ == '__main__': main()
