def floodFill(image, sr, sc, color):
    if image == None or image[sr][sc] == color:
        return image

    fill(image, sr, sc, image[sr][sc], color)
    return image


def fill(image, sr, sc, initialColor, color):
    if (
        sr < 0
        or sr >= len(image)
        or sc < 0
        or sc >= len(image[0])
        or image[sr][sc] != initialColor
    ):
        return
    image[sr][sc] = color

    fill(image, sr + 1, sc, initialColor, color)
    fill(image, sr - 1, sc, initialColor, color)
    fill(image, sr, sc + 1, initialColor, color)
    fill(image, sr, sc - 1, initialColor, color)


print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
