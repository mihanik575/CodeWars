# https://www.codewars.com/kata/56121f3312baa28c8500005b/train/python
# Write a function that given an array of numbers >= 0, will arrange them such that they form the biggest number.
#
# For example:
#
# [1, 2, 3] --> "321" (3-2-1)
# [3, 30, 34, 5, 9] --> "9534330" (9-5-34-3-30)
# The results will be large so make sure to return a string.

def biggest(nums):
    biggest = []
    for i in nums:
        if i >biggest[0]:
            biggest.insert(0, i)

    return biggest

print(biggest([1,22,3]))
# print(str(biggest[1])[0])

# import codewars_test as test
# from solution import biggest
#
# @test.describe("biggest")
# def test_group():
#     @test.it("Basic tests")
#     def test_case():
#         test.assert_equals(biggest([0, 0, 0, 0]),'0')
#         test.assert_equals(biggest([1,2,3]),'321')
#         test.assert_equals(biggest([121,12]),'12121')
#         test.assert_equals(biggest([12,128]),'12812')
#         test.assert_equals(biggest([5051,50]),'505150')
#         test.assert_equals(biggest([10,101]),'10110')
#         test.assert_equals(biggest([3, 30, 34, 5, 9]),'9534330')
#         test.assert_equals(biggest([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247]),'9609938824824769735703560743981399')
#         test.assert_equals(biggest([830,8308]),'8308830')
#         test.assert_equals(biggest([3803,38,380]),'383803803')