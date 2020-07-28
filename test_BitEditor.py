import unittest
import BitEditor as be 

class BitEditorTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_normal(self):
        bytes = bytearray(range(4))
        bitEditor = be.BitEditor()

        bytes = bitEditor.Write(1,0b1,bytes)
        self.assertEqual(0b10000000,bytes[0])
        bytes = bitEditor.Write(2,0b10,bytes)
        self.assertEqual(0b11000000,bytes[0])
        bytes = bitEditor.Write(3,0b101,bytes)
        self.assertEqual(0b11010100,bytes[0])
        bytes = bitEditor.Write(4,0b1001,bytes)
        self.assertEqual(0b11010110,bytes[0])
        self.assertEqual(0b01000000,bytes[1])
        bytes = bitEditor.Write(5,0b10001,bytes)
        self.assertEqual(0b11010110,bytes[0])
        self.assertEqual(0b01100010,bytes[1])
        bytes = bitEditor.Write(6,0b100001,bytes)
        self.assertEqual(0b11010110,bytes[0])
        self.assertEqual(0b01100011,bytes[1])
        self.assertEqual(0b00001000,bytes[2])
        bytes = bitEditor.Write(7,0b1000001,bytes)
        self.assertEqual(0b11010110,bytes[0])
        self.assertEqual(0b01100011,bytes[1])
        self.assertEqual(0b00001100,bytes[2])
        self.assertEqual(0b00010000,bytes[3])
if __name__ == "__main__":
    unittest.main()
