import unittest
import BitEditor as be 

class BitEditorTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_push(self):
        bitEditor = be.BitEditor(size=4)

        bitEditor.Push(1,0b1)
        self.assertEqual(0b10000000,bitEditor.bytes[0])
        bitEditor.Push(2,0b10)
        self.assertEqual(0b11000000,bitEditor.bytes[0])
        bitEditor.Push(3,0b101)
        self.assertEqual(0b11010100,bitEditor.bytes[0])
        bitEditor.Push(4,0b1001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b01000000,bitEditor.bytes[1])
        bitEditor.Push(5,0b10001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b01100010,bitEditor.bytes[1])
        bitEditor.Push(6,0b100001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b01100011,bitEditor.bytes[1])
        self.assertEqual(0b00001000,bitEditor.bytes[2])
        bitEditor.Push(7,0b1000001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b01100011,bitEditor.bytes[1])
        self.assertEqual(0b00001100,bitEditor.bytes[2])
        self.assertEqual(0b00010000,bitEditor.bytes[3])
    def test_push2(self):
        bitEditor = be.BitEditor(size=2)

        bitEditor.Push(9,0b101010101)
        self.assertEqual(0b10101010,bitEditor.bytes[0])
        self.assertEqual(0b10000000,bitEditor.bytes[1])

    def test_pop1(self):
        bitEditor = be.BitEditor(size=1)
        bitEditor.Push(5,0b10101)

        byte = bitEditor.Pop(5)
        self.assertEqual(0b10101, byte)
    def test_pop2(self):
        bitEditor = be.BitEditor(size=1)
        bitEditor.Push(5,0b10101)

        byte = bitEditor.Pop(1)
        self.assertEqual(0b1, byte)

        byte = bitEditor.Pop(1)
        self.assertEqual(0b0, byte)
if __name__ == "__main__":
    unittest.main()
