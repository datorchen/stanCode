"""
File: best_photoshop_award.py
Name: Sean Chen
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""


from simpleimage import SimpleImage


THRESHOLD = 20
BLACK_PIXEL = 280
ADJ = 20


def main():
    """
    創作理念：選擇一個不是明顯紅綠藍的背景並穿著反差沒有那麼大的衣服作為挑戰。
    """
    bg = SimpleImage('image_contest/avatar.jpg')
    img = SimpleImage('image_contest/Sean.png')
    bg.make_as_big_as(img)
    bg.show()
    img.show()
    # for x in range(img.width):
    #     for y in range(img.height):
    #         img_p = img.get_pixel(x, y)
    #         bg_p = bg.get_pixel(x, y)
    #         avg = (img_p.red + img_p.green + img_p.blue) // 3
    #         total = img_p.red + img_p.green + img_p.blue
    #         if img_p.red - ADJ < img_p.green and img_p.red - ADJ < img_p.blue and -THRESHOLD < img_p.green - img_p.blue < THRESHOLD and total > BLACK_PIXEL:
    #             img_p.red = bg_p.red
    #             img_p.green = bg_p.green
    #             img_p.blue = bg_p.blue
    # img.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
