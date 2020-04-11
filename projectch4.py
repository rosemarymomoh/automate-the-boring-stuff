# def commaCode(listname):
#     result = ''
#     for i in listname:
#         if listname.index(i) != (len(listname) - 1):
#             result += str(i) + ', '
#         else:
#             result += 'and ' + str(i)
#     return result
#
#
# spam = [1, 4, 6, 7]
# print(commaCode(spam))



def pictureGrid(grid):
    for i in range(0, len(grid[0])):
        imageStr = ''
        for j in range(0, len(grid)):
            imageStr += grid[j][i]
        print(imageStr)

gridImage = [['.', '.', '.','.', '.', '.'],
        ['.', '0', '0','.', '.', '.'],
        ['0', '0', '0','0', '.', '.'],
        ['0', '0', '0','0', '0', '.'],
        ['.', '0', '0','0', '0', '0'],
        ['0', '0', '0','0', '0', '.'],
        ['0', '0', '0','0', '.', '.'],
        ['.', '0', '0','.', '.', '.'],
        ['.', '.', '.','.', '.', '.']]

pictureGrid(gridImage)
