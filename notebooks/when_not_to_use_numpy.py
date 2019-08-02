# %% [markdown]
# # You don't always need numpy
# ## Or Scipy or tensor flow or pandas
# ### (right tool for the right job)
#
# * Easy to get tunnel vision on numerical/data problems
# * Might have to interact with other systems i.e. APIs
# * This can create some friction (i.e. conda vs pip for a small example)
# * "Numerical python is a different idiom from other python implementations"
# * Foundation of Numpy is arrays and vectorised expressions on those arrays.
# ### Bag of words
# * Can represent bag of words as a dict, or a numpy array (however that requires a lookup array)
# ## Suggestions
# ### Make the most of pythons core data structions
# #### Lists
# Use lists sets dictionaries and tuples (default data structures)
#
# Lists in python are general purpose O(N) for most operations.
# For numerically heavy operations lists are probably not a good choice
# #### Dicts + Tuples
# These are good too eh?. Tuples are good for metadata (immutable)
#
# Cannot have a set of lists, but can have a set of tuples
# ### Use Composition!
# Sets of tuples + Dicts of Lists
#
# Use the collections module (batteries included eh?). Defaultdict + Counter are good
#
# (lookup) `heapq` (priority queue implementation) and `bisect` (standard bisection search in the std lib)
# ### Generators and Streaming
# Eventually you run out of memory
# Use context managers `with` to iterate through a large file without loading into RAM
# ```python
# import pandas as pd
# with open('really_big_file', 'r') as f:
#    # eager - holds result set in RAM
#    results = [do_something(line) for line in f]
#
#    # lazy - puts results into generator using a generator constructor expression
#    results = (do_something(line) for line in f)
#
# ### Use Databases you nimrod
# Cause SQL is still cool yo. (SQLite is in the stdlib)
# ### Domain specific databases exists
# * Graphs
# * Full text search
# * GIS
# * Relationsal models
# * Analytics databases
