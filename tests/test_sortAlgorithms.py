import unittest

from sortAlgorithms import sortAlgorithms

class TestStringMethods(unittest.TestCase):

    # tuple of [input_list, expected_list, msg]
    # input_list:    input to the sort algorithm
    # expected_list: expected output of the sort algorithm
    # msg:           short test case description
    
    testdata = [
        ([-10,2,3,4,5,6,7,8,9,1], [-10,1,2,3,4,5,6,7,8,9], "TestCase: input contains one negative number"),
        ([999,2,3,4,5,6,7,8,9,1], [1,2,3,4,5,6,7,8,9,999], "TestCase: input contains greatest number at the beginning"),
        ([0,1,0,0], [0,0,0,1], "TestCase: input contains several times same numbers"),
        ([1,1,1], [1,1,1], "TestCase: input contains only ame numbers"),
        ([5], [5], "TestCase: one number as input"),
        ([], [], "TestCase: empty input")
        ]
     
    # tuple of [input_list, expected_list, start, end, msg]
    # input_list:    input to the sort algorithm
    # expected_list: expected output of the sort algorithm
    # start:         left boarder of list to be sorted
    # end:           right boarder of the list to be sorted
    # msg:           short test case description
    
    testdata_with_arguments = [
        ([5,4,3,2,1], [5,1,2,3,4], 1, 5, "TestCase: start = 1, end = len(input_list)"),
        ([5,4,3,2,1], [2,3,4,5,1], 0, 4, "TestCase: start = 0, end = len(input_list)-1"),
        ([5,4,3,2,1], [2,3,4,5,1], 0, 6, "TestCase: start = 0, end = len(input_list)+1 (out of range)"),
        ([5,4,3,2,1], [2,3,4,5,1], -1, 4, "TestCase: start = -1 (out of range), end = len(input_list)-1")
        ]
        

    def test_qsort1_using_testdata(self):
        
        for input_list, expected_list, msg in self.testdata:
            with self.subTest(input_list=input_list, expected_list=expected_list, msg=msg):
                self.assertEqual(sortAlgorithms.qsort1(input_list), expected_list, msg)

    def test_qsort1_using_testdata_with_arguments(self):
    
        for input_list, expected_list, start, end, msg in self.testdata_with_arguments:
            with self.subTest(input_list=input_list, expected_list=expected_list, start=start, end=end, msg=msg):
                self.assertEqual(sortAlgorithms.qsort1(input_list, start, end), expected_list, msg)


    def test_qsort2_using_testdata(self):
        
        for input_list, expected_list, msg in self.testdata:
            with self.subTest(input_list=input_list, expected_list=expected_list, msg=msg):
                self.assertEqual(sortAlgorithms.qsort2(input_list), expected_list, msg)

    def test_qsort2_using_testdata_with_arguments(self):
    
        for input_list, expected_list, start, end, msg in self.testdata_with_arguments:
            with self.subTest(input_list=input_list, expected_list=expected_list, start=start, end=end, msg=msg):
                self.assertEqual(sortAlgorithms.qsort2(input_list, start, end), expected_list, msg)


    def test_qsort3_using_testdata(self):
        
        for input_list, expected_list, msg in self.testdata:
            with self.subTest(input_list=input_list, expected_list=expected_list, msg=msg):
                self.assertEqual(sortAlgorithms.qsort3(input_list), expected_list, msg)

    def test_qsort3_using_testdata_with_arguments(self):
    
        for input_list, expected_list, start, end, msg in self.testdata_with_arguments:
            with self.subTest(input_list=input_list, expected_list=expected_list, start=start, end=end, msg=msg):
                self.assertEqual(sortAlgorithms.qsort3(input_list, start, end), expected_list, msg)


    def test_qsort4_using_testdata(self):
        
        for input_list, expected_list, msg in self.testdata:
            with self.subTest(input_list=input_list, expected_list=expected_list, msg=msg):
                self.assertEqual(sortAlgorithms.qsort4(input_list), expected_list, msg)

    def test_qsort4_using_testdata_with_arguments(self):
    
        for input_list, expected_list, start, end, msg in self.testdata_with_arguments:
            with self.subTest(input_list=input_list, expected_list=expected_list, start=start, end=end, msg=msg):
                self.assertEqual(sortAlgorithms.qsort4(input_list, start, end), expected_list, msg)


    def test_obviously_wrong_using_testdata(self):
        
        for input_list, expected_list, msg in self.testdata:
            with self.subTest(input_list=input_list, expected_list=expected_list, msg=msg):
                self.assertEqual(sortAlgorithms.obviously_wrong(input_list), expected_list, msg)


if __name__ == '__main__':
    unittest.main()