"inbuilt methods"
"lower() and upper()"
char_ = 'o'
print(char_.lower())
char_ = 0
string_ = '123'
print(string_.lower()) # for lower() and upper() if string having no's also it doesn't hrow any error
string_ = 'kasi 123'
print(string_.lower())
print(string_.upper())

# print(string_.isalnum())
# print(string_.isnumeric())
print(string_.isspace())
print(string_.isupper())
print(string_.islower()) # isupper() and islower() checks only alphabets are in particular case or not these ignore numbers and special

list_ = [1,2,3,'kasi']
list_.append('89')
print(list_)
# print(list_.pop())
# print(list_.pop(79)) # raises error if position not found
# print(list_.pop(2))
