# Let's create a function wrap_text that wraps text in symbols of our choice. For example:
#
# wrap_text('hello', '===')
# should return:
#
# ===hello===
#
# Now that this function works, how can we use it (without modifying the function) to generate the following string?
#
# ---===###new message###===---
#
# Note that wrap_text needs to return a value rather than print one.
#
# Hints:
#
# You'll have to call the same function multiple times.
# Try breaking down the problem into smaller pieces that you know wrap_text can solve.

def wrap_text(text,wrapper): #Take in two text parameters
    return '{}{}{}'.format(wrapper,text,wrapper) #Return the text as defined above

print(wrap_text('hello','===')) #Try it out with the sample, should print '===hello===
print(wrap_text(wrap_text(wrap_text('new message','###'),'==='),'---')) #Try out the second example, should print '---===###new message###===---'
