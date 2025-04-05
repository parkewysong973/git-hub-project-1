import numpy as np

def calculate_area(shape):
    """
    Calculate the area of a shape given its dimensions.
    
    Args:
        shape (tuple): A tuple representing the dimensions of the shape.
        
    Returns:
        float: The area of the shape.
    """
    if not shape:
        raise ValueError("Shape cannot be empty")
    
    length, width = shape
    return length * width

# Example usage:
shape1 = (5, 3)
area1 = calculate_area(shape1)
print(f"The area of shape with dimensions {shape1} is: {area1}")
