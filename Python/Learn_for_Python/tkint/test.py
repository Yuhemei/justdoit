from tkinter import *

root=Tk()

cv=Canvas(root,bg='white')
rt1=cv.create_rectangle(10,10,110,110,tags=('r1','r2','r3'))
rt2=cv.create_rectangle(20,20,80,80,tags=('s1','s2','s3'))
rt3=cv.create_rectangle(30,30,70,70,tags=('y1','y2','y3'))

cv.tag_lower(rt3)
cv.tag_raise(rt1)
cv.itemconfig(cv.find_above(rt2),outline='red')
cv.itemconfig(cv.find_below(rt2),outline='green')
cv.pack()

root.mainloop()
