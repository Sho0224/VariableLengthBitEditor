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
        self.assertEqual(0b1,bitEditor.bytes[0])
        bitEditor.Push(2,0b10)
        self.assertEqual(0b110,bitEditor.bytes[0])
        bitEditor.Push(3,0b101)
        self.assertEqual(0b110101,bitEditor.bytes[0])
        bitEditor.Push(4,0b1001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b01,bitEditor.bytes[1])
        bitEditor.Push(5,0b10001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b0110001,bitEditor.bytes[1])
        bitEditor.Push(6,0b100001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b01100011,bitEditor.bytes[1])
        self.assertEqual(0b00001,bitEditor.bytes[2])
        bitEditor.Push(7,0b1000001)
        self.assertEqual(0b11010110,bitEditor.bytes[0])
        self.assertEqual(0b01100011,bitEditor.bytes[1])
        self.assertEqual(0b00001100,bitEditor.bytes[2])
        self.assertEqual(0b0001,bitEditor.bytes[3])

    def test_push2(self):
        bitEditor = be.BitEditor(size=2)

        bitEditor.Push(9,0b101010101)
        self.assertEqual(0b10101010,bitEditor.bytes[0])
        self.assertEqual(0b1,bitEditor.bytes[1])

    def test_push3(self):
        bitEditor = be.BitEditor(size=1)

        bitEditor.Push(8,0b10101010)
        self.assertEqual(0b10101010,bitEditor.bytes[0])
        bitEditor.Push(2,0b1)
        self.assertEqual(0b10101010,bitEditor.bytes[0])

    def test_push4(self):
        bitEditor = be.BitEditor(size=1)

        bitEditor.Push(1,0b1)
        self.assertEqual(0b1,bitEditor.bytes[0])
        bitEditor.Push(1,0b0)
        self.assertEqual(0b1,bitEditor.bytes[0])

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
        byte = bitEditor.Pop(1)
        self.assertEqual(0b1, byte)
        byte = bitEditor.Pop(1)
        self.assertEqual(0b0, byte)
        byte = bitEditor.Pop(1)
        self.assertEqual(0b1, byte)

    def test_pop3(self):
        bitEditor = be.BitEditor(size=2, is_debug_log = True)
        bitEditor.Push(9,0b101010101)

        byte = bitEditor.Pop(6)
        self.assertEqual(0b101010, byte)
        byte = bitEditor.Pop(1)
        self.assertEqual(0b1, byte)
        byte = bitEditor.Pop(1)
        self.assertEqual(0b0, byte)
        byte = bitEditor.Pop(1)
        self.assertEqual(0b1, byte)
 
if __name__ == "__main__":
    unittest.main()
