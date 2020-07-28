#!/usr/bin/env python

def main():
    bytes = bytearray(b'\x00,\x00,')
    index = 0
    empty_bits = 8

    bytes,index,empty_bits = BinaryWrite(1,0b1,bytes,index,empty_bits)
    bytes,index,empty_bits = BinaryWrite(2,0b10,bytes,index,empty_bits)
    bytes,index,empty_bits = BinaryWrite(3,0b101,bytes,index,empty_bits)
    bytes,index,empty_bits = BinaryWrite(4,0b1001,bytes,index,empty_bits)
    bytes,index,empty_bits = BinaryWrite(5,0b10001,bytes,index,empty_bits)
    bytes,index,empty_bits = BinaryWrite(6,0b100001,bytes,index,empty_bits)
    bytes,index,empty_bits = BinaryWrite(7,0b1000001,bytes,index,empty_bits)

    print(bytes)
    print(bin(int.from_bytes(bytes,'big')))
    # 1 10 101 1001 10001 100001 1000001 0000

def BinaryWrite(bit_count,value,target,index,empty_bits):
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
