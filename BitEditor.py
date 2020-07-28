#!/usr/bin/env python

def main():
    pass

def Write(bit_count,value,target,index,empty_bits):
    for i in reversed(range(bit_count)):
        print("i:{}".format(i))
        print("index:{}".format(index))
        print("empty_bits:{}".format(empty_bits))
        mask = 1 << i
        one_bit = (value & mask) >> i
        print("one_bit << (empty_bits - 1):{}".format(bin(one_bit << (empty_bits - 1))))
        target[index] += one_bit << (empty_bits - 1) 
        empty_bits-=1
        print("value:{}".format(bin(value)))
        print("one_bit:{}".format(bin(one_bit)))
        print("target[{}]:{}".format(index,bin(target[index])))

        if empty_bits == 0:
            index+=1
            empty_bits = 8
            target[index] = 0
    
    return target,index,empty_bits

if __name__ == '__main__': main()
