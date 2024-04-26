def space(nums: int):
    string_ = " "
    text = ' '
    for i in range(nums):
        string_ += text
        text = ' '
    return string_
