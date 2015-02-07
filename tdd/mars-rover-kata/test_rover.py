
import rover
import unittest

class TestRover(unittest.TestCase):
    
    def setUp(self):
        self.rover = rover.Rover(0, 0, 'N')
        
    
    def testConstructor(self):
        r = rover.Rover(10, 12, 'N')
        self.assertEqual(10, r.x)
        self.assertEqual(12, r.y)
        self.assertEqual('N', r.orientation)
    
    def testMoveTwoInDiagonal(self):
        r = self.rover
        r.receiveCommands("ffrff")
        self.assertEqual(2, r.x)
        self.assertEqual(2, r.y)
        self.assertEqual('E', r.orientation)
        
    def testComplexPath(self):
        r = self.rover
        r.receiveCommands("rffflfflfffrffrfff")
        self.assertEqual(3, r.x)
        self.assertEqual(4, r.y)
        self.assertEqual('E', r.orientation)
    
    def testComplexPathBackwards(self):
        r = self.rover
        r.receiveCommands("rffflfflfffrffrfff") ## starting point
        r.receiveCommands("bbblbblbbbrbbrbbbl")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('N', r.orientation)    
    
    def testUnknownCommandsDoNothing(self):
        r = self.rover
        r.receiveCommands("acdeghijkmnopqstuvwxyz0123456789")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('N', r.orientation)
    
    def testMoveOneForward(self):
        r = self.rover
        r.receiveCommands("f")
        self.assertEqual(0, r.x)
        self.assertEqual(1, r.y)
        self.assertEqual('N', r.orientation)
    
    def testMoveTwoForward(self):
        r = self.rover
        r.receiveCommands("ff")
        self.assertEqual(0, r.x)
        self.assertEqual(2, r.y)
        self.assertEqual('N', r.orientation)  
        
    def testTurnLeftWhenNorth(self):
        r = self.rover
        r.receiveCommands("l")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('W', r.orientation)
    
    def testTurnLeftWhenWest(self):
        r = self.rover
        r.receiveCommands("ll")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('S', r.orientation)
    
    def testTurnLeftWhenSouth(self):
        r = self.rover
        r.receiveCommands("lll")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('E', r.orientation)
    
    def testTurnLeftWhenEast(self):
        r = self.rover
        r.receiveCommands("rl")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('N', r.orientation)
        
    def testTurnRightWhenNorth(self):
        r = self.rover
        r.receiveCommands("r")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('E', r.orientation)
    
    def testTurnRightWhenEast(self):
        r = self.rover
        r.receiveCommands("rr")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('S', r.orientation)
        
    def testTurnRightWhenSouth(self):
        r = self.rover
        r.receiveCommands("rrr")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('W', r.orientation)
    
    def testTurnRightWhenWest(self):
        r = self.rover
        r.receiveCommands("lr")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('N', r.orientation)

    def testForwardToEast(self):
        r = self.rover
        r.receiveCommands("rf")
        self.assertEqual(1, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('E', r.orientation)
    
    def testForwardToSouth(self):
        r = self.rover
        r.receiveCommands("frrf")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('S', r.orientation)
    
    def testForwardToWest(self):
        r = self.rover
        r.receiveCommands("rfllf")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('W', r.orientation)

    def testBackwardWhenSouth(self):
        r = self.rover
        r.receiveCommands("llb")
        self.assertEqual(0, r.x)
        self.assertEqual(1, r.y)
        self.assertEqual('S', r.orientation)
    
    def testBackwardWhenNorth(self):
        r = self.rover
        r.receiveCommands("fb")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('N', r.orientation)
    
    def testBackwardWhenEast(self):
        r = self.rover
        r.receiveCommands("rfb")
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('E', r.orientation)
    
    def testBackwardWhenWest(self):
        r = self.rover
        r.receiveCommands("lb")
        self.assertEqual(1, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual('W', r.orientation)
    
if __name__ == '__main__':
    unittest.main()
