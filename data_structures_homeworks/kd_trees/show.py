from point_set import *

ps = Point_Set()
ps.insert(Point(7, 2))
ps.insert(Point(5, 4))
ps.insert(Point(2, 3))
ps.insert(Point(4, 7))
ps.insert(Point(9, 6))


ps.draw()
ps.draw_range(Rectangle(3, 6, 3, 8))
plt.show()

