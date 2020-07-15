# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function 
# takes two rectangles described this way, and returns True if the rectangles 
# overlap at all (even if just at a point), and False otherwise. 
# Note: here we will represent coordinates the way they are usually represented in 
# computer graphics, where (0,0) is at the left-top corner of the screen, and while 
# the x-coordinate goes up while you head right, the y-coordinate goes up while you 
# head down (so we say that "up is down")

def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
    (x1,y1) = left1,top1
    (x2,y2) = left1+width1,top1
    (x3,y3) = left1,top1+height1
    (x4,y4) = left1+width1,top1+height1

    return (x1 >= left2 and x1 <= left2+width2 and y1 >= top2 and y1 <= top2+height2) or (x2 >= left2 and x2 <= left2+width2 and y2 >= top2 and y2 <= top2+height2) or (x3 >= left2 and x3 <= left2+width2 and y3 >= top2 and y3 <= top2+height2) or (x4 >= left2 and x4 <= left2+width2 and y4 >= top2 and y4 <= top2+height2)

        