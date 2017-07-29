
'''
This function get a string as input if input is one digit add a zero
:param input_string: input digit az string
:type input_string:str
:return: modified output as str
>>> from pyrgg import *
>>> zero_insert("22")
'22'
>>> zero_insert("320")
'320'
>>> zero_insert("2")
'02'
>>> time_convert('33')
'00 days, 00 hour, 00 minutes, 33 seconds'
>>> time_convert("15000")
'00 days, 04 hour, 10 minutes, 00 seconds'
>>> import random
>>> random.seed(2)
>>> sign_gen()
1
>>> random.seed(11)
>>> sign_gen()
-1
>>> random.seed(2)
>>> branch_gen(10,40,1,20,1)
[[4, 24, 17, 3, 41, 18, 25, 11, 15, 21], [3, 10, 20, 14, -17, 1, -17, 8, 6, 5]]
>>> random.seed(20)
>>> branch_gen(4,40,1,20,2)
[[10, 41, 21, 11], [9, 4, 19, 1]]
>>> random.seed(2)
>>> edge_gen(20,0,400,2,10,1)
[{1: [3, 6], 2: [20, 6, 13, 15, 1], 3: [13, 6, 8, 11, 17, 18, 14], 4: [12, 13, 17, 9, 15, 19, 8], 5: [20, 16, 17, 7], 6: [20, 1, 4, 21, 19, 8, 14], 7: [12, 1, 3, 5, 6, 19, 11], 8: [15, 13, 8, 11, 19, 17], 9: [9, 14, 18, 2, 5, 4, 8], 10: [15, 3, 20, 14, 1], 11: [14, 17, 4, 6, 7, 15, 18, 19], 12: [19, 16, 17, 12, 14, 10, 1, 7, 15, 9], 13: [20, 13, 4], 14: [2, 12, 17, 14, 10, 6, 9, 3, 5], 15: [21, 10, 11], 16: [10, 18, 11, 17, 6, 8, 19, 15, 13, 9], 17: [21, 18, 3, 20, 13, 15, 6, 19], 18: [13, 19, 20], 19: [16, 19, 7, 1, 3, 11, 17, 13], 20: [2, 13, 10, 12]}, {1: [184, -128], 2: [297, -326, -278, -18, -238], 3: [-269, 120, 90, 69, -263, 228, -303], 4: [-82, -335, 250, -256, -179, -249, -358], 5: [-395, -155, -159, -262], 6: [174, 381, 294, 139, 349, 30, 29], 7: [127, 58, 20, 376, 197, 126, -15], 8: [135, 242, 338, 12, -249, -73], 9: [-310, 358, 343, -17, 87, -325, 126], 10: [128, 319, -131, -269, 18], 11: [56, 123, 10, 53, 266, -158, -108, 214], 12: [48, -9, 312, -353, 53, 396, -30, 2, 385, 62], 13: [-328, 354, 316], 14: [-148, -72, -368, -348, -118, -305, -356, 36, -34], 15: [65, -118, -88], 16: [79, -49, 366, -86, -360, -183, 238, 304, 201, -129], 17: [-184, -365, 272, 206, 160, -332, 8, -110], 18: [140, 250, 4], 19: [-262, 239, 179, -272, -345, -136, -14, -345], 20: [255, -345, 5, 275]}, 123]
>>> random.seed(11)
>>> edge_gen(20,0,100,2,10,2)
[{1: [18, 15, 17, 7, 21, 6, 5, 20, 1], 2: [2, 7, 20], 3: [11, 19, 17, 21, 16, 3, 14, 9, 8], 4: [1, 19, 4, 13, 7, 16], 5: [14, 19, 7, 9, 3, 11, 4, 8], 6: [1, 15, 6], 7: [7, 17, 5, 21, 4, 14, 1, 19, 6, 20], 8: [2, 7, 9], 9: [10, 3, 19, 8, 20, 12, 15], 10: [19, 13, 21, 10, 20, 7, 14, 4, 2], 11: [8, 13, 14, 16, 17, 3], 12: [16, 21, 20, 9, 7], 13: [3, 14], 14: [2, 6, 12, 19, 3], 15: [15, 17, 5, 2], 16: [12, 10, 1, 21, 16, 5, 3, 18, 2], 17: [11, 3, 16, 14], 18: [19, 20, 13, 3, 21, 9, 11, 15, 18], 19: [17, 10, 3, 1, 4, 20, 16, 11, 15, 8], 20: [9, 21, 7, 13, 19, 5, 12, 3]}, {1: [99, 57, 75, 23, 78, 12, 11, 50, 67], 2: [4, 30, 3], 3: [56, 25, 29, 37, 0, 58, 70, 40, 65], 4: [8, 98, 51, 8, 6, 48], 5: [9, 80, 99, 43, 39, 1, 17, 90], 6: [7, 62, 87], 7: [57, 24, 53, 49, 50, 27, 34, 38, 50, 82], 8: [18, 56, 1], 9: [49, 9, 81, 1, 47, 79, 16], 10: [17, 23, 19, 29, 31, 20, 6, 13, 65], 11: [94, 32, 76, 37, 22, 16], 12: [71, 78, 9, 27, 95], 13: [34, 57], 14: [5, 36, 67, 16, 46], 15: [42, 74, 75, 2], 16: [89, 4, 76, 9, 8, 9, 57, 47, 94], 17: [45, 87, 9, 3], 18: [1, 84, 48, 11, 14, 53, 49, 59, 10], 19: [3, 76, 61, 29, 63, 84, 32, 84, 63, 41], 20: [25, 55, 27, 28, 40, 63, 5, 35]}, 129]

'''