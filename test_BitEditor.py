import unittest
import BitEditor as be

class BitEditorTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_normal(self):
        bytes = bytearray(b'\x00')
        index = 0
        empty_bits = 8

        bytes,index,empty_bits = be.Write(1,0b1,bytes,index,empty_bits)
        self.assertEqual(0b10000000,int.from_bytes(bytes,'big'))
        bytes,index,empty_bits = be.Write(2,0b10,bytes,index,empty_bits)
        self.assertEqual(0b11000000,int.from_bytes(bytes,'big'))
        bytes,index,empty_bits = be.Write(3,0b101,bytes,index,empty_bits)
        self.assertEqual(0b11010100,int.from_bytes(bytes,'big'))
#        bytes,index,empty_bits = be.Write(4,0b1001,bytes,index,empty_bits)
#        bytes,index,empty_bits = be.Write(5,0b10001,bytes,index,empty_bits)
#        bytes,index,empty_bits = be.Write(6,0b100001,bytes,index,empty_bits)
#        bytes,index,empty_bits = be.Write(7,0b1000001,bytes,index,empty_bits)
if __name__ == "__main__":
    unittest.main()
