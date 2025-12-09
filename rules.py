# ##...Here's a **comprehensive cheat sheet** of Python functions and methods organized by category:

# ## **1. LISTS** - `my_list = []`
# ```python
# .append(x)          # Add item to end
# .extend(iterable)   # Add multiple items
# .insert(i, x)       # Insert at index i
# .remove(x)          # Remove first occurrence
# .pop([i])           # Remove at index (or last)
# .clear()            # Remove all items
# .index(x)           # Find index of value
# .count(x)           # Count occurrences
# .sort()             # Sort in place
# .reverse()          # Reverse in place
# .copy()             # Shallow copy
# len(my_list)        # Get length
# ```

# ## **2. SETS** - `my_set = {1, 2}` or `set()`
# ```python
# .add(x)             # Add single element
# .update(iterable)   # Add multiple elements
# .remove(x)          # Remove element (raises error)
# .discard(x)         # Remove element (no error)
# .pop()              # Remove random element
# .clear()            # Remove all elements
# .copy()             # Shallow copy
# .union(other_set)   # |
# .intersection()     # &
# .difference()       # -
# .symmetric_difference()  # ^
# .issubset()         # <=
# .issuperset()       # >=
# ```

# ## **3. TUPLES** - `my_tuple = (1, 2)`
# ```python
# .index(x)           # Find index of value
# .count(x)           # Count occurrences
# # Note: Tuples are immutable - no add/remove methods!
# ```

# ## **4. DICTIONARIES** - `my_dict = {}`
# ```python
# [key] = value       # Add/update
# .get(key, default)  # Get with default
# .pop(key)           # Remove key
# .popitem()          # Remove last item
# .update(other_dict) # Merge dictionaries
# .clear()            # Remove all items
# .copy()             # Shallow copy
# .keys()             # View of keys
# .values()           # View of values
# .items()            # View of key-value pairs
# .setdefault(k, v)   # Get value, set default if missing
# ```

# ## **5. STRINGS** - `my_str = "hello"`
# ```python
# .lower()/.upper()           # Case conversion
# .strip()/.lstrip()/.rstrip()  # Remove whitespace
# .split(sep)                 # Split into list
# .join(iterable)             # Join elements
# .replace(old, new)          # Replace substring
# .find(sub) /.rfind()        # Find substring
# .index(sub) /.rindex()      # Find (raises error)
# .count(sub)                 # Count occurrences
# .startswith()/.endswith()   # Check prefix/suffix
# .isalpha()/.isdigit()/.isalnum()  # Character checks
# .format()                   # Format string
# f"{}"                       # f-string (Python 3.6+)
# ```

# ## **6. COMMON BUILT-IN FUNCTIONS**
# ```python
# len(x)              # Length
# type(x)             # Type
# str(x)              # Convert to string
# int(x)              # Convert to integer
# float(x)            # Convert to float
# list(x)             # Convert to list
# tuple(x)            # Convert to tuple
# set(x)              # Convert to set
# dict(x)             # Convert to dictionary
# bool(x)             # Convert to boolean
# range(start, stop, step)  # Generate range
# enumerate(iterable)        # Add counter
# zip(*iterables)     # Combine iterables
# sorted(iterable)    # Return sorted list
# reversed(iterable)  # Return reversed iterator
# sum(iterable)       # Sum of elements
# min() / max()       # Minimum/Maximum
# abs(x)              # Absolute value
# round(x, digits)    # Round number
# ```

# ## **7. FILE OPERATIONS**
# ```python
# open(file, mode)    # Open file
# .read()             # Read entire file
# .readline()         # Read one line
# .readlines()        # Read all lines as list
# .write(string)      # Write string
# .writelines(list)   # Write list of strings
# .close()            # Close file
# .seek(offset)       # Move file pointer
# .tell()             # Get current position
# ```

# ## **8. USEFUL METHODS BY CATEGORY**

# ### **Adding elements:**
# - Lists: `.append()`, `.insert()`, `.extend()`
# - Sets: `.add()`, `.update()`
# - Dicts: `[key] = value`, `.update()`

# ### **Removing elements:**
# - Lists: `.remove()`, `.pop()`, `.clear()`
# - Sets: `.remove()`, `.discard()`, `.pop()`, `.clear()`
# - Dicts: `.pop()`, `.popitem()`, `.clear()`

# ### **Searching/Checking:**
# - Lists/Tuples: `.index()`, `.count()`, `in` operator
# - Sets: `in` operator, `.issubset()`, `.issuperset()`
# - Dicts: `.get()`, `in` operator (checks keys)

# ### **Converting types:**
# ```python
# list(my_set)        # Set to list
# tuple(my_list)      # List to tuple
# set(my_list)        # List to set
# dict(list_of_tuples)# List of (key,value) to dict
# str(my_num)         # Number to string
# int(my_str)         # String to int (if possible)
# ```

# ## **9. QUICK MEMORY AID**

# | Data Type | Add Single | Add Multiple | Remove | Check Membership |
# |-----------|------------|--------------|---------|------------------|
# | **List**  | `.append()` | `.extend()` | `.pop()` | `in` |
# | **Set**   | `.add()`   | `.update()` | `.pop()` | `in` |
# | **Dict**  | `[key]=val`| `.update()` | `.pop()` | `in` (keys) |
# | **Tuple** | ✗ (immutable) | ✗ | ✗ | `in` |

# ## **Practice Example:**
# ```python
# # List
# nums = [1, 2, 3]
# nums.append(4)          # [1, 2, 3, 4]
# nums.insert(0, 0)       # [0, 1, 2, 3, 4]

# # Set
# unique = {1, 2, 3}
# unique.add(4)           # {1, 2, 3, 4}
# unique.update([5, 6])   # {1, 2, 3, 4, 5, 6}

# # Dict
# person = {"name": "Alice"}
# person["age"] = 25      # {"name": "Alice", "age": 25}
# person.update({"city": "NY"})  # Adds city

# # String
# text = "hello"
# new_text = text.upper()  # "HELLO"
# words = text.split()     # ["hello"]
# ```

# **Tip:** Use `dir(object)` to see all available methods for any object!










