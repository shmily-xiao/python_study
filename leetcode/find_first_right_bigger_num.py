#! /usr/bin/python
# -*- coding:utf-8 -*-


"""
    给定一个数组找寻所有元素右边第一个比他大的数字,数组元素不重复

    q = [1, 3, 6, 4, 5, 7]
    输出：
        3 ，6，7, 5, 7
"""

# ---------------------------
# 遍历
# ---------------------------
#

def find_num_v1(a):
    """
        时间复杂度是 O（n^2）
    :param a:
    :return:
    """
    result = {}
    for i in range(len(a)):
        for aj in a[i:]:
            if aj > a[i]:
                result[a[i]] = aj
                break


    return result


def find_num_v2(a):
    """
        栈 第二个元素和栈顶元素进行比较，如果二个元素比栈顶元素大，就弹出栈顶元素，然后将第二个元素入栈


    :param a:
    :return:
    """
    stack = []
    top = -1
    result = {}
    for ai in a:
        if not stack:
            stack.append(ai)
            top += 1
            continue

        if ai > stack[top]:
            while(True):
                result[stack[top]] = ai
                stack.pop(top)
                top -= 1
                if not stack or stack[top] > ai:
                    break
            stack.append(ai)
            top += 1
        else:
            stack.append(ai)
            top += 1

    return result



if __name__ == '__main__':
    q = [1, 3, 6, 4, 5, 7]
    print find_num_v1(q)
    print find_num_v2(q)