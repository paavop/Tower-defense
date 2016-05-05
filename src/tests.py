import unittest

import math
from tower import Tower
from spot import Spot
from road import Road
from enemy import Enemy


class UnitTests(unittest.TestCase):
    
    def test_1_distance(self):
        spot1=Road(5,5)
        tower1=Tower(0,0,2,7,7,0,0,"a","b")
        vihu=Enemy("c",2,2,spot1,0,"d",0)
        self.assertEqual(tower1.distance(vihu),math.sqrt(8))
    def test_2_finding_enemy(self):
        spot1=Road(5,5)
        tower1=Tower(0,0,3,7,7,0,0,"a","b")
        vihu=Enemy("c",2,2,spot1,0,"d",0)
        vihut={}
        vihut[0]=vihu
        tower1.shoot(vihut,0)
        self.assertEqual(tower1.target,vihu)
    def test_3_range_to_enemy(self):
        spot1=Road(5,5)
        tower1=Tower(0,0,2,7,7,0,0,"a","b")
        vihu=Enemy("c",2,2,spot1,0,"d",0)
        vihut={}
        vihut[0]=vihu
        tower1.shoot(vihut,0)
        self.assertEqual(tower1.target,None)
    def test_4_damage(self):
        spot1=Road(5,5)
        tower1=Tower(0,3,3,7,7,0,0,"a","b")
        vihu=Enemy("c",2,2,spot1,0,"d",0)
        vihut={}
        vihut[0]=vihu
        tower1.shoot(vihut,1)
        vihu.gotshot(2000, 1)
        self.assertEqual(vihu.is_alive(),False)

        


if __name__ == '__main__':
    unittest.main()
