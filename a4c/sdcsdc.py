import numpy as np

arr = np.array([[1, 2],
                [2, 3],
                [5, 6],
                [7, 9]])

subset_arr = np.array([[1, 2], 
                       [7, 9]])

len_a = len(arr)
len_s = len(subset_arr)

# build two separate array that align, for comparison
broad_arr    = (
  np
  .tile(arr, (len_s, 1))
  .reshape(-1, len_a, 2)
)
# [
#   [
#     [1, 2],
#     [2, 3],
#     [5, 6],
#     [7, 9],
#   ],
#   [
#     [1, 2],
#     [2, 3],
#     [5, 6],
#     [7, 9],
#   ]
# ]

# and
broad_subset = (
  np
  .tile(subset_arr, len_a)
  .reshape(-1, len_a, 2)
)
# [
#   [
#     [1, 2],
#     [1, 2],
#     [1, 2],
#     [1, 2],
#   ],
#   [
#     [7, 9],
#     [7, 9],
#     [7, 9],
#     [7, 9],
#   ]
# ]

# do element wise comparison
result = broad_arr == broad_subset
# [
#   [
#     [True,  True ],
#     [False, False],
#     [False, False],
#     [False, False],
#   ],
#   [
#     [False, False],
#     [False, False],
#     [False, False],
#     [True,  True ],
#   ]
# ]


# then an .all on the deepest axis
result = result.all(axis=-1)
# [
#   [
#     True,
#     False,
#     False,
#     False,
#   ],
#   [
#     False,
#     False,
#     False,
#     True,
#   ]
# ]

# then a transposition
result = result.T
# [
#   [True,  False],
#   [False, False],
#   [False, False],
#   [False, True],
# ]

# then .any on the deepest axis
result = result.any(axis=-1)
# [
#   True,
#   False,
#   False,
#   True,
# ]


# get the indices
np.where(result)[0]
# [0, 3]