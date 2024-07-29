#!/usr/bin/python3
'''ALX Interview LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not.
    
    Args:
        boxes (list of lists): A list where each element is a
        list of keys for each box.
        
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''
    total_boxes = len(boxes)
    available_keys = set()
    unlocked_boxes = []
    current_box = 0

    while current_box < total_boxes:
        previous_box = current_box
        unlocked_boxes.append(current_box)
        available_keys.update(boxes[current_box])
        for key in available_keys:
            if key != 0 and key < total_boxes and key not in unlocked_boxes:
                current_box = key
                break
        if previous_box != current_box:
            continue
        else:
            break

    for box_index in range(total_boxes):
        if box_index not in unlocked_boxes and box_index != 0:
            return False
    return True
