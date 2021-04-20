"""
Variable Assignment 
"""

# # add "Jordan" (value) to the variable (name)
# name = "Jordan"
# print(name)

# ====================================

# assign same value to mutiple variables on the same lime
# a = b = c = "cat"
# print(a)
# print(b)
# print(c)

# ====================================

# reuse variable names, the last assingmentis printed 
# colour = "red"
# colour = "blue"
# print(colour)

# ====================================

#legal names
# firstname ="John"
# first_name = "John"
# _firs_tname = "John"
# firstName = "John"
# firstname2 = "John"
# FIRSTNAME = "John"

# # illegal variable names 
# 2firtsname = "John"
# first-name = "John"
# first name = "John"

# ====================================

"""
Reserved Keywords
"""
# help("keywords")

# from = "London"
# print(from)

# ====================================

# # variable types 
# var = 23
# print(type(var))




"""
Object Identity
"""

# score = 400
# identity = id(score)
# print(identity)

# ====================================

# score variable is saved into the pb by refereence 

# score = 400
# pb = score
# print(id(score))
# print(id(pb))

"""
Object reference
"""

# # both pb and score point to the samee into object
# # score ----------> int 100---------------< pb


# score = 100
# pb = score 
# print(type(score))
# print(type(pb))
# print(score)
# print(pb)


# ====================================
# pb --------------> int 20
# score ------------> into 100


# pb = 20
# score = 100
# print(type(score))
# print(type(pb))
# print(score)
# print(pb)


# ====================================
# garbage colllection

# pb -------------> int 20
# score -------------> str "Completed"
#   ------------------> int 100

# pb = 20
# score = 100
# score = "Completed"
# print(type(score))
# print(type(pb))
# print(score)
# print(pb)

