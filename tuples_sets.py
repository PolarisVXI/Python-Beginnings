# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
fruits = ('Apples', 'Oranges', 'Grapes')

fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

 # Single value tuples need a trailing comma.
fruits3 = ('Bananas',)

# Can't re-declare value
 ##-- fruits[0] = 'Pineapple'

# Delete tuple
del fruits2

# Get length
print(len(fruits3))


print(fruits[2],fruits2,fruits3,type(fruits3))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

# Delete set
del fruits_set

print(fruits_set)
