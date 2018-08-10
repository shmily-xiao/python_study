#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    给定平面上的点，这些点在x和y轴都不重复，找出最大的点
    最大的点的定义是 在这个点的右上方不存在其他的点，那么这个点就叫做最大的点
       y^                       
        |      *    
        |           *     
        |        o
        |               *
        | o       
        |                   *
        ------------------------------->
                                        x
        如图所示 *  就是 我们要找寻的最大的点的集合
        (2,6)  (4,5)  (5,3)  (6,1)
        
        1. 对点集合的集合按照 X 的从大到小排序
        2. 取栈顶元素，没有元素的时候就在栈中存放第一个 x 轴最大的那个元素 记为 P0
        3. 找到下一个 在 y 轴方向上第一个大于 P0 的元素，放入栈中
        4. 取栈顶元素重复 第 2 步骤
"""

def search_point(points):
    points_x = sorted(points, key=lambda x:x[0], reverse=True)
    result = []
    for item in points_x:
        if not result:
            result.append(item)
            continue
        p0 = result[len(result)-1]
        x0 = p0[0]
        y0 = p0[1]

        x1 = item[0]
        y1 = item[1]

        if y1 > y0:
            result.append(item)


    return result


if __name__ == '__main__':

    point = [(0,1), (2,6), (3,4), (4,5), (5,3), (6,1)]

    print search_point(point)


