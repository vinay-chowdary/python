l = int(input("length "))
w = int(input("breadth "))


def findSquares(length, width):
    if width == 1:
        return length
    if length == 1:
        return width
    if length == 0 or width == 0:
        return 0
    return (length//width)+findSquares(width, length % width)


print(findSquares(l, w))
