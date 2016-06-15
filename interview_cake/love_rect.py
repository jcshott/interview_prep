def find_x_overlap(rect1, rect2):
    """find horizontal overlap"""
    # if our second rectangle bottom corner starts to the right of first
    if rect2['left_x'] > rect1['left_x']:
        # find bottom_right, which is bottom right of rect1
        bottom_right_x = rect1['left_x'] + rect1['width'] # 11
        # if the bottom left of our 2nd rect is less than bottom_right of 1st rect, then return the width
        if rect2['left_x'] < bottom_right_x:
            width_of_overlap = bottom_right_x - rect2['left_x'] # 4
        # if 2nd rect bottom left is outside our 1st rect then they don't overlap
        else:
            width_of_overlap = None
    else:
        # same logic if the 2nd rect jutes to the left
        bottom_right_x = rect2['left_x'] + rect2['width']
        if rect1['left_x'] < bottom_right_x:
            width_of_overlap = bottom_right_x - rect1['left_x']
        else:
            width_of_overlap = None
    return width_of_overlap

def find_y_overlap(rect1, rect2):
    """find vertical overlap"""
    if rect1['bottom_y'] < rect2['bottom_y']:
        top_y = rect1['bottom_y'] + rect1['height'] #9
        height_of_overlap = top_y - rect2['bottom_y'] #3
    else:
        top_y = rect2['bottom_y'] + rect2['height']
        height_of_overlap = top_y - rect1['bottom_y']
    if height_of_overlap <= 0:
        return None
    else:
        return height_of_overlap

def find_intersection_rect(rect1, rect2):
    intersect_rect = {}
    intersect_rect['width'] = find_x_overlap(rect1, rect2)
    intersect_rect['height'] = find_y_overlap(rect1, rect2)

    # if we get no intersection for width or height, then return none.
    if not intersect_rect['width'] or not intersect_rect['height']:
        print "no intersection"
        return None

    if rect1['left_x'] < rect2['left_x']:
        intersect_rect['left_x'] = rect2['left_x']
    else:
        intersect_rect['left_x'] = rect1['left_x']

    if rect1['bottom_y'] < rect2['bottom_y']:
        intersect_rect['bottom_y'] = rect2['bottom_y']
    else:
        intersect_rect['bottom_y'] = rect1['bottom_y']

    # find where the the x-i
    return intersect_rect

if __name__ == '__main__':

    my_rectangle = {

        # coordinates of bottom-left corner
        'left_x': 1,
        'bottom_y': 5,

        # width and height
        'width': 10,
        'height': 4,

    }

    other_rectangle = {

        # coordinates of bottom-left corner
        'left_x': 7,
        'bottom_y': 6,

        # width and height
        'width': 5,
        'height': 10,

    }
    third_rectangle = {

            # coordinates of bottom-left corner
            'left_x': 2,
            'bottom_y': 7,

            # width and height
            'width': 2,
            'height': 1,

    }
    print find_intersection_rect(my_rectangle, third_rectangle)

    # expect:
    # intersection_rectangle = {
    #
    #     # coordinates of bottom-left corner
    #     'left_x': 7,
    #     'bottom_y': 6,
    #
    #     # width and height
    #     'width': 4,
    #     'height': 3,
    #
    # }
