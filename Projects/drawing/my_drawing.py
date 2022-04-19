"""
File: my_drawing.py
Name: Hui-Chieh Chen
----------------------
This program draws the flag of the Straw Hat Pirates from One Piece.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLine
from campy.graphics.gwindow import GWindow

window = GWindow(560, 510, title='Straw Hat Pirates')


def main():
    """
    Title: Straw Hat Pirates

    This manga, One Piece, occupies my childhood, youth and present.
    """
    background()
    bone()
    circle = GOval(300, 300)
    circle.filled = True
    circle.fill_color = '#428AE4'
    window.add(circle, 129, 90)
    chin = GOval(72, 45)
    chin.filled = True
    chin.fill_color = 'white'
    window.add(chin, 243, 363)
    low_teeth()
    rope()
    up_teeth()
    skull()
    hat()


def background():
    """
    This function draws the background
    """
    bg = GRect(540, 490)
    window.add(bg, x=10, y=10)
    stripe1 = GRect(60, 490)
    stripe1.filled = True
    stripe1.fill_color = '#702222'
    window.add(stripe1, 67, 10)
    stripe2 = GRect(60, 490)
    stripe2.filled = True
    stripe2.fill_color = '#702222'
    window.add(stripe2, 187, 10)
    stripe3 = GRect(60, 490)
    stripe3.filled = True
    stripe3.fill_color = '#702222'
    window.add(stripe3, 307, 10)
    stripe4 = GRect(60, 490)
    stripe4.filled = True
    stripe4.fill_color = '#702222'
    window.add(stripe4, 434, 10)


def bone():
    """
    This function draws two bones
    """
    bone1 = GPolygon()
    bone1.add_vertex((125.89, 98.16))
    bone1.add_vertex((147.63, 77.49))
    bone1.add_vertex((441.79, 387.01))
    bone1.add_vertex((420.05, 407.67))
    bone1.filled = True
    bone1.fill_color = 'white'
    window.add(bone1)
    bone1_ball1 = GOval(40, 40)
    bone1_ball1.filled = True
    bone1_ball1.fill_color = 'white'
    window.add(bone1_ball1, 127, 57)
    bone1_ball2 = GOval(40, 40)
    bone1_ball2.filled = True
    bone1_ball2.fill_color = 'white'
    window.add(bone1_ball2, 106, 77)
    bone1_ball3 = GOval(40, 40)
    bone1_ball3.filled = True
    bone1_ball3.fill_color = 'white'
    window.add(bone1_ball3, 395, 386)
    bone1_ball4 = GOval(40, 40)
    bone1_ball4.filled = True
    bone1_ball4.fill_color = 'white'
    window.add(bone1_ball4, 416, 366)
    bone2 = GPolygon()
    bone2.add_vertex((420.05, 77.79))
    bone2.add_vertex((441.79, 98.46))
    bone2.add_vertex((147.63, 407.97))
    bone2.add_vertex((125.89, 387.3))
    bone2.filled = True
    bone2.fill_color = 'white'
    window.add(bone2)
    bone2_ball1 = GOval(40, 40)
    bone2_ball1.filled = True
    bone2_ball1.fill_color = 'white'
    window.add(bone2_ball1, 395, 57)
    bone2_ball2 = GOval(40, 40)
    bone2_ball2.filled = True
    bone2_ball2.fill_color = 'white'
    window.add(bone2_ball2, 416, 77)
    bone2_ball3 = GOval(40, 40)
    bone2_ball3.filled = True
    bone2_ball3.fill_color = 'white'
    window.add(bone2_ball3, 127, 386)
    bone2_ball4 = GOval(40, 40)
    bone2_ball4.filled = True
    bone2_ball4.fill_color = 'white'
    window.add(bone2_ball4, 106, 366)


def low_teeth():
    """
    This function draws the lower row of teeth
    """
    low_teeth2 = GPolygon()
    low_teeth2.add_vertex((255.8, 355))
    low_teeth2.add_vertex((274.61, 361.8))
    low_teeth2.add_vertex((267.81, 380.61))
    low_teeth2.add_vertex((249, 373.81))
    low_teeth2.filled = True
    low_teeth2.fill_color = 'white'
    window.add(low_teeth2)
    low_teeth3 = GPolygon()
    low_teeth3.add_vertex((282, 362.68))
    low_teeth3.add_vertex((300.47, 355))
    low_teeth3.add_vertex((308.15, 373.47))
    low_teeth3.add_vertex((289.68, 381.15))
    low_teeth3.filled = True
    low_teeth3.fill_color = 'white'
    window.add(low_teeth3)
    low_teeth1 = GRect(20, 20)
    low_teeth1.filled = True
    low_teeth1.fill_color = 'white'
    window.add(low_teeth1, 269, 360)


def rope():
    """
    This function draws the rope
    """
    rope_l = GPolygon()
    rope_l.add_vertex((253.2, 350))
    rope_l.add_vertex((266.76, 361.84))
    rope_l.add_vertex((201, 437.17))
    rope_l.add_vertex((187.44, 425.34))
    rope_l.filled = True
    rope_l.fill_color = '#CC6633'
    window.add(rope_l)
    rope_le1 = GPolygon()
    rope_le1.add_vertex((189.51, 424))
    rope_le1.add_vertex((195.03, 432.34))
    rope_le1.add_vertex((180.86, 441.73))
    rope_le1.add_vertex((175.34, 435.39))
    rope_le1.filled = True
    rope_le1.fill_color = '#CC6633'
    window.add(rope_le1)
    rope_le2 = GPolygon()
    rope_le2.add_vertex((194.27, 430))
    rope_le2.add_vertex((202.98, 434.91))
    rope_le2.add_vertex((194.62, 449.72))
    rope_le2.add_vertex((185.91, 444.81))
    rope_le2.filled = True
    rope_le2.fill_color = '#CC6633'
    window.add(rope_le2)
    l_line1 = GLine(239.37, 366.91, 252.4, 378.55)
    window.add(l_line1)
    l_line2 = GLine(226.07, 381.91, 239.4, 393.55)
    window.add(l_line2)
    l_line3 = GLine(213.07, 396.91, 226.4, 408.55)
    window.add(l_line3)
    l_line4 = GLine(200.07, 410.91, 213.4, 422.55)
    window.add(l_line4)
    rope_r = GPolygon()
    rope_r.add_vertex((293, 362.84))
    rope_r.add_vertex((306.56, 351))
    rope_r.add_vertex((372.32, 426.34))
    rope_r.add_vertex((358.76, 438.17))
    rope_r.filled = True
    rope_r.fill_color = '#CC6633'
    window.add(rope_r)
    rope_r1 = GPolygon()
    rope_r1.add_vertex((357, 436.13))
    rope_r1.add_vertex((366.76, 421))
    rope_r1.add_vertex((386.08, 433.47))
    rope_r1.add_vertex((376.33, 448.59))
    rope_r1.filled = True
    rope_r1.fill_color = '#CC6633'
    window.add(rope_r1)
    rope_r2 = GPolygon()
    rope_r2.add_vertex((375.47, 448.94))
    rope_r2.add_vertex((381, 431.82))
    rope_r2.add_vertex((402.89, 438.89))
    rope_r2.add_vertex((397.35, 456.02))
    rope_r2.filled = True
    rope_r2.fill_color = '#CC6633'
    window.add(rope_r2)
    rope_r3 = GPolygon()
    rope_r3.add_vertex((395.92, 456.18))
    rope_r3.add_vertex((398.36, 438.34))
    rope_r3.add_vertex((421.15, 441.46))
    rope_r3.add_vertex((418.71, 459.29))
    rope_r3.filled = True
    rope_r3.fill_color = '#CC6633'
    window.add(rope_r3)
    rope_r4 = GPolygon()
    rope_r4.add_vertex((416, 458.98))
    rope_r4.add_vertex((416.75, 441))
    rope_r4.add_vertex((439.73, 441.96))
    rope_r4.add_vertex((438.98, 459.95))
    rope_r4.filled = True
    rope_r4.fill_color = '#CC6633'
    window.add(rope_r4)
    rope_r5 = GPolygon()
    rope_r5.add_vertex((432, 443.17))
    rope_r5.add_vertex((453.09, 434))
    rope_r5.add_vertex((460.27, 450.51))
    rope_r5.add_vertex((439.17, 459.68))
    rope_r5.filled = True
    rope_r5.fill_color = '#CC6633'
    window.add(rope_r5)
    rope_re1 = GPolygon()
    rope_re1.add_vertex((449, 436.31))
    rope_re1.add_vertex((460.72, 424))
    rope_re1.add_vertex((467.97, 430.9))
    rope_re1.add_vertex((456.24, 443.21))
    rope_re1.filled = True
    rope_re1.fill_color = '#CC6633'
    window.add(rope_re1)
    rope_re2 = GPolygon()
    rope_re2.add_vertex((456, 442.04))
    rope_re2.add_vertex((472.88, 440))
    rope_re2.add_vertex((474.08, 449.93))
    rope_re2.add_vertex((457.2, 451.97))
    rope_re2.filled = True
    rope_re2.fill_color = '#CC6633'
    window.add(rope_re2)
    r_line1 = GLine(306.67, 377.62, 320, 365.98)
    window.add(r_line1)
    r_line2 = GLine(318.67, 391.62, 332, 379.98)
    window.add(r_line2)
    r_line3 = GLine(331.67, 406.62, 345, 394.98)
    window.add(r_line3)
    r_line4 = GLine(343.67, 420.62, 357, 408.98)
    window.add(r_line4)


def up_teeth():
    """
    This function draws the upper row of teeth
    """
    up_teeth1 = GRect(15, 19)
    up_teeth1.filled = True
    up_teeth1.fill_color = 'white'
    window.add(up_teeth1, 243, 337)
    up_teeth2 = GRect(15, 19)
    up_teeth2.filled = True
    up_teeth2.fill_color = 'white'
    window.add(up_teeth2, 256, 340)
    up_teeth1 = GRect(15, 19)
    up_teeth1.filled = True
    up_teeth1.fill_color = 'white'
    window.add(up_teeth1, 271, 341)
    up_teeth1 = GRect(15, 19)
    up_teeth1.filled = True
    up_teeth1.fill_color = 'white'
    window.add(up_teeth1, 286, 340)
    up_teeth1 = GRect(15, 19)
    up_teeth1.filled = True
    up_teeth1.fill_color = 'white'
    window.add(up_teeth1, 299, 337)


def skull():
    """
    This function draws the skull
    """
    face = GOval(205, 216)
    face.filled = True
    face.fill_color = 'white'
    window.add(face, 177, 130)
    eye_l = GOval(50, 50)
    eye_l.filled = True
    window.add(eye_l, 209, 264)
    eye_r = GOval(50, 50)
    eye_r.filled = True
    window.add(eye_r, 299, 264)
    nose = GOval(20, 20)
    nose.filled = True
    window.add(nose, 269, 310)


def hat():
    """
    This function draws the straw hat
    """
    up_hat = GArc(205, 410, 0, 180)
    up_hat.filled = True
    up_hat.fill_color = '#E0BA65'
    window.add(up_hat, 176, 130)
    dec = GRect(205, 36)
    dec.filled = True
    dec.fill_color = '#BC3131'
    window.add(dec, 176, 206)
    brim = GRect(325, 18)
    brim.filled = True
    brim.fill_color = '#E0BA65'
    window.add(brim, 115, 229)


if __name__ == '__main__':
    main()
