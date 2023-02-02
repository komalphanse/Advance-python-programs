#python code to show how to raise an exception in pyton
num=[3,4,5,7]
if len(num)>3:
    raise Exception(f"length of given list must be less than or equal to 3 but is {len(num)}")