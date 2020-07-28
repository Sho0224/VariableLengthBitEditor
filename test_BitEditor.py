import unittest
import BitEditor as be

class BitEditorTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_normal(self):
        bytes = bytearray(range(4))
        index = 0
        empty_bits = 8

        bytes,index,empty_bits = be.Write(1,0b1,bytes,index,empty_bits)
        self.assertEqual(0b10000000,bytes[0])
        bytes,index,empty_bits = be.Write(2,0b10,bytes,index,empty_bits)
        self.assertEqual(0b11000000,bytes[0])
        bytes,index,empty_bits = be.Write(3,0b101,bytes,index,empty_bits)
        self.assertEqual(0b11010100,bytes[0])
        bytes,index,empty_bits = be.Write(4,0b1001,bytes,index,empty_bits)
        self.assertEqual(0b11010110,bytes[0])
        self.assertEqual(0b01000000,bytes[1])
        bytes,index,empty_bits = be.Write(5,0b10001,bytes,index,empty_bits)
        self.assertEqual(0b11010110,bytes[0])
        self.assertEqual(0b01100010,bytes[1])
        bytes,index,empty_bits = be.Write(6,0b100001,bytes,index,empty_bits)
        self.assertEqual(0b11010110,bytes[0])
        self.assertEqual(0b01100011,bytes[1])
        self.assertEqual(0b00001000,bytes[2])
        bytes,index,empty_bits = be.Write(7,0b1000001,bytes,index,empty_bits)
        self.assertEqual(0b11010110,bytes[0])
        self.assertEqual(0b01100011,bytes[1])
        self.assertEqual(0b00001100,bytes[2])
        self.assertEqual(0b00010000,bytes[3])
if __name__ == "__main__":
    unittest.main()
