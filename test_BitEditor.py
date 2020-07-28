import unittest
import BitEditor as be 

class BitEditorTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_normal(self):
        bitEditor = be.BitEditor(size=4)

        bitEditor.Write(1,0b1)
        self.assertEqual(0b10000000,bitEditor.bytes[0])
        bitEditor.Write(2,0b10)
        self.assertEqual(0b11000000,bitEditor.bytes[0])
        bitEditor.Write(3,0b101)
        self.assertEqual(0b11010100,bitEditor.bytes[0])
        bitEditor.Write(4,0b1001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b01000000,bitEditor.bytes[1])
        bitEditor.Write(5,0b10001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b01100010,bitEditor.bytes[1])
        bitEditor.Write(6,0b100001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b01100011,bitEditor.bytes[1])
        self.assertEqual(0b00001000,bitEditor.bytes[2])
        bitEditor.Write(7,0b1000001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b01100011,bitEditor.bytes[1])
        self.assertEqual(0b00001100,bitEditor.bytes[2])
        self.assertEqual(0b00010000,bitEditor.bytes[3])
if __name__ == "__main__":
    unittest.main()
