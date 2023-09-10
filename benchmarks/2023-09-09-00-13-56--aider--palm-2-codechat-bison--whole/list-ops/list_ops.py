def append(list1, list2):
  """
  Appends all items in list2 to the end of list1.

  Args:
    list1: The list to which items will be appended.
    list2: The list of items to be appended.

  Returns:
    The updated list1.
  """

  for item in list2:
    list1.append(item)

  return list1


def concat(lists):
  """
  Concatenates all lists in lists into one flattened list.

  Args:
    lists: A list of lists.

  Returns:
    The flattened list.
  """

  flat_list = []
  for list in lists:
    flat_list.extend(list)

  return flat_list


def filter(function, list):
  """
  Filters the list based on a predicate.

  Args:
    function: A function that takes an item in the list as input and returns a
      boolean value.
    list: The list to be filtered.

  Returns:
    The filtered list.
  """

  filtered_list = []
  for item in list:
    if function(item):
      filtered_list.append(item)

  return filtered_list


def length(list):
  """
  Returns the number of items in the list.

  Args:
    list: The list whose length will be returned.

  Returns:
    The number of items in the list.
  """

  return len(list)


def map(function, list):
  """
  Maps a function over the list.

  Args:
    function: A function that takes an item in the list as input and returns a
      new item.
    list: The list to be mapped.

  Returns:
    The mapped list.
  """

  mapped_list = []
  for item in list:
    mapped_list.append(function(item))

  return mapped