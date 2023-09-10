def accumulate(collection, operation):
  """
  Given a collection and an operation to perform on each element of the collection,
  returns a new collection containing the result of applying that operation to each element of the input collection.

  Args:
    collection: A collection of elements.
    operation: A function that takes an element of the collection and returns a new value.

  Returns:
    A new collection containing the result of applying the operation to each element of the input collection.
  """

  # Initialize an empty collection to store the results.
  results = []

  # Iterate over the input collection.
  for element in collection:
    # Apply the operation to the element and add the result to the results collection.
    results.append(operation(element))

  # Return the results collection.
  return results
