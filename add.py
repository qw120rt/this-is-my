import turtle

def draw_petal():
    """
    绘制一个花瓣形状。
    
    Args:
        无参数。
    
    Returns:
        无返回值。
    
    """
    turtle.circle(100, 60)
    turtle.left(120)
    turtle.circle(100, 60)
    turtle.left(120)

for _ in range(6):
    draw_petal()
    turtle.right(60)


turtle.done()