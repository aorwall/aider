def find(search_list, value):
  """
  Finds the index of the given value in the list.

  Args:
    search_list: The list to search.
    value: The value to find.

  Returns:
    The index of the value in the list, or -1 if the value is not found.
  """

  # Check if the list is empty.
  if not search_list:
    return -1

  # Find the middle element of the list.
  middle_index = len(search_list) // 2
  middle_value = search_list[middle_index]

  # Compare the value to the middle element.
  if value == middle_value:
    return middle_index
  elif value < middle_value:
    # The value is less than the middle element, so we can eliminate the right half of the list.
    return find(search_list[:middle_index], value)
  else:
    # The value is greater than the middle element, so we can eliminate the left half of the list.
    return find(search_list[middle_index + 1:], value)

  # The value was not found in the list.
  raise ValueError("value not in array")
