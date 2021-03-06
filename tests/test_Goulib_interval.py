from nose.tools import assert_equal, assert_true, assert_false
from nose import SkipTest

from Goulib.interval import *

class TestInInterval:
    def test_in_interval(self):
        assert_equal(in_interval([1,2], 1),True)
        assert_equal(in_interval([2,1], 1),True) #interval might be unordered
        assert_equal(in_interval((2,1), 1),True) #or defined by a tuple
        assert_equal(in_interval([1,2], 2,closed=True),True)
        assert_equal(in_interval([1,2], 2,closed=False),False)

class TestIntersect:
    def test_intersect(self):
        assert_equal(intersect([1,3],[2,4]),True)
        assert_equal(intersect([3,1],(4,2)),True)
        assert_equal(intersect((1,2),[2,4]),False)
        assert_equal(intersect((5,1),(2,3)),True)

class TestIntersection:
    def test_intersection(self):
        assert_equal(intersection([1,3],(4,2)),(2,3))
        assert_equal(intersection([1,5],(3,2)),(2,3))

class TestIntersectlen:
    def test_intersectlen(self):
        assert_equal(intersectlen([1,5],(3,2)),1)
        assert_equal(intersectlen((1,2),[2,4]),0)

class TestInterval:
    @classmethod
    def setup_class(self):
        self.i12 = Interval(1,2)
        self.i13 = Interval(1,3)
        self.i24 = Interval(2,4)
        self.i33 = Interval(3,3) #empty
        
    def test___init__(self):
        pass #tested above
    
    def test___repr__(self):
        assert_equal(repr(self.i12),'[1,2)')
                     
    def test___str__(self):
        assert_equal(str(self.i12),'[1,2)')
        
    def test___hash__(self):
        """test that we can use an Interval as key in a dict and retrieve it with a different Interval with same values"""
        dict={}
        dict[self.i12]=self.i12
        assert_equal(dict[Interval(2,1)],self.i12)
        
    def test___cmp__(self):
        assert_equal(self.i12<self.i24,True)
        assert_equal(self.i12>self.i24,False)

    def test___contains__(self):
        assert_true(2 in self.i13)
        assert_false(3 in self.i13)
        
    def test_contains(self):
        assert_true(self.i13.contains(2))
        assert_false(self.i13.contains(3))

    def test_empty(self):
        assert_true(self.i33.empty())
        assert_false(self.i13.empty())

    def test_hull(self):
        assert_equal(Interval(1,2).hull(Interval(3,4)),Interval(1,4))

    def test_intersection(self):
        assert_equal(Interval(1,2).intersection(Interval(3,4)),None)
        assert_equal(Interval(1,3).intersection(Interval(2,5)),Interval(2,3))

    def test_overlap(self):
        assert_false(Interval(1,2).overlap(Interval(3,4)))
        assert_true(Interval(1,3).overlap(Interval(2,5)))
        
    def test_separation(self):
        assert_equal(Interval(1,2).separation(Interval(3,5)),3-2)
    
    def test_subset(self):
        assert_true(Interval(1,3).subset(Interval(1,3)))
        assert_false(Interval(1,3).subset(Interval(1,2)))
        assert_false(Interval(2,3).subset(Interval(1,2)))

    def test_proper_subset(self):
        assert_false(Interval(1,3).proper_subset(Interval(1,3)))
        eps=1E-12
        assert_true(Interval(1,3).proper_subset(Interval(1-eps,3+eps)))

    def test_singleton(self):
        assert_true(Interval(1,2).singleton())
        assert_false(Interval(1,3).singleton())


class TestIntervals:
    @classmethod
    def setup_class(self):
        i12 = Interval(1,2)
        i13 = Interval(1,3)
        i24 = Interval(2,4)
        self.intervals=Intervals([i24,i13,i12])
        assert_equal(str(self.intervals),'[[1,2), [1,3), [2,4)]')
    
    def test___init__(self):
        pass #tested above
        
    def test___call__(self):
        # intervals = Intervals(init)
        # assert_equal(expected, intervals.__call__(x))
        raise SkipTest # TODO: implement your test here

    def test_append(self):
        # intervals = Intervals(init)
        # assert_equal(expected, intervals.append(item))
        raise SkipTest # TODO: implement your test here

    def test_extend(self):
        # intervals = Intervals(init)
        # assert_equal(expected, intervals.extend(iterable))
        raise SkipTest # TODO: implement your test here

if __name__ == "__main__":
    import nose
    nose.runmodule()
