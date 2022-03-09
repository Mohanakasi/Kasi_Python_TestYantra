"string"
"string is a collection of characters"
"immutable data type"
"bounded between quotes "" "
"using len function we can find the length of the string"
"to fetch the individual characters and to fetch the group of characters indexing and slicing is available in string data type"
"default value of the string is "" "
# a = str('kasi')
# print(a)
# a = 'kasi'
# print(a)
# print(len(a))
# print(bool("")) # default vlue of string

"""raw strings"""
"when the string contains special meanings like \t and \n to trat normally those in string we use raw strings"
"this raw strings are nothing but r or R is place before the string"
"ex"
# string_ = "python\the language of the \new begining"
# print(string_)
# string_ = r"python\the language of the \new begining"
# print(string_)
"mainly raw strings are used when file path is mentioned in strings"


"indexing"
string_ = "kasi is from guntur"
# print(string_[0]) # to fetch starting of the string
# print(string_[-1]) # to fetch the last element of the string
# middle = len(string_)//2
# print(string_[middle]) # middle elements

"slicing"
"first two elements"
# print(string_[:2])
"last two elemts"
# print(string_[-2:])
"middle two elements"
# middle = len(string_)//2
# print(string_[middle-1:middle+1])

"""string formating"""
"to infuse data dynamically into the string we us string formatig"
"format with format()"
# print("{} is from {}".format('kasi','guntur')) # positional arguments
# print("{1} is in {0}".format('bangalore','kasi')) # infusing arguments based on indexes
# print("{name} know {language} little bit".format(name='kasi', language='english')) # keword arguments

"f strings"
# a = 'kasi'
# b = '25'
# print(f"his name is {a} and he was {b} years old")

"inbuilt methods "

"lower():"
"converts the character or string into lower and returns the o/p without modifying the original string"
"returns modified string"
string_ = 'Hello Python123'
# print(string_.lower()) # if string has special characters it will keep them as it is
char_ = 'H' # single character
# print(char_.lower())

"upper()"
"converts the character or string into upper and returns the o/p without modifying the original string"
"returns modified string"
string_ = 'hello PYTHON'
# print(string_.upper())
char_ = 'i' # single character
# print(char_.upper())

"count()"
"it will count the no of occurrences of a particular sub-string/character present in a sub string"
"input argument is substring OR character"
"returns count as integer"
string_ = 'continuity of presence of democracy'
# print(string_.count('continuity'))
# print(string_.count('of'))
# print(string_.count('c'))
# print(string_.count(' '))

"find()"
"it will gives the index no of first occurence of a particular charactersub-string present in a string"
"have to pass character/sub-string as an argument and starting index and ending index are optional arguments"
"returns first occurence index no as integer"
"it will returns  -1 as output if the substring not found in string instead of raising error"
string_ = 'hello bangalore and hello kasi how is python'
# print(string_.find('l'))
# print(string_.find('hello'))
# print(string_.find('hello',5))
# print(string_.find('hello',5,30)) # we can ending index more then the lengtrh of the string it wont raise error

"rfind()"
"it will gives the index no of first occurence of a particular charactersub-string from end of the string"
"have to pass character/sub-string as an argument and starting index and ending index are optional arguments"
"returns first occurence index no as integer"
# print(string_.rfind('l'))
# print(string_.rfind('hello'))
# print(string_.rfind('hello',5))
# print(string_.rfind('hello',5,30))

"replace"
"replace characte/sub string ad returns modified string"
"have to pass old sub string and new substring as an arguments"
string_ = 'the king of india is raja vikramarka'
# print(string_.replace('raja vikramarka','kasi'))
# print(string_.replace('k','s'))

"starts with()"
"checks whether the string is starting with the proveded char/substring or not and returns true or false"
"arguments char/sub-string"
string_ = 'king of cobra is always python it is more dangerous'
# print(string_.startswith('k'))
# print(string_.startswith('kasi'))
# print(string_.startswith('king'))
# print(string_.startswith('i'))

"endswith()"
"checks whether the string is ending with the proveded char/substring or not and returns true or false"
"arguments char/sub-string"
string_ = 'king of cobra is always python it is more dangerous'
# print(string_.endswith('s'))
# print(string_.endswith('dangerous'))
# print(string_.endswith('kasi'))
# print(string_.endswith('i'))


"split"
"splits the string at the seperator and returns the list"
"arguments seperator(either special character or number or substring)"
"returns list of string with seperation a the seperator"
string_ = 'the space is a special character'
# print(string_.split()) # the seperator argument is optiopnal inbuiltly it will take space as seperator
# print(string_.split('#')) # if the seperator is not found it will insert string as it is into list and returns the list
# print(string_.split('i'))
# print(string_.split('is')) # we can pass substring as an argument in the split


"join"
"joins the elements of iterable using the string specified"
"arguments joining element and string"
msg = 'the part is of different kind'
# print('@'.join(msg))
# print('***'.join(msg))
# print("".join(msg)) # if no substring is given it will return the string as it is

"strip"
"strip() will removes the leading and tailing edges of string with the specified substring"
"if substring is not found at leading and tailing edges it will return the string as it is"
"if we not providing of any substring it will implicitly takes space as substring"
string_ = '$$$$the king of hindu ocean is kasi$$$'
# print(string_.strip('$'))
# print(string_.strip()) # here it is taking space as substring
# string_ = '@$$$$the king of hindu ocean is kasi$$$'
# print(string_.strip('@$'))
# print(string_.strip('$'))
# print(string_.strip('@'))
"rstrip"
"it will remooves only tailing edge  of the string"
# string_ = '$$$$the king of hindu ocean is kasi$$$'
# print(string_.rstrip('$'))
# print(string_.rstrip())
# string_ = '$$$$the king of hindu ocean is kasi@$$$@@@'
# print(string_.rstrip('$@'))
# print(string_.rstrip('$'))

"lstrip"
"remooves only leading edge of the string"
string_ = '****^$$$$%%%the king of hindu ocean is kasi$$$^^^^***'
# print(string_.lstrip('*'))
# print(string_.lstrip('^'))
# print(string_.lstrip('*^'))
# print(string_.lstrip('^$%'))
# print(string_.lstrip('^$*'))

"""isalpha"""
"returns true if character/all characters in string is of alphabets else returns false"
"even space or any special characters or numbers is present it will return false"
# string_ = 'kasi1ia'
# print(string_.isalpha())
# msg = 'kasi nadh'
# print(msg.isalpha())
# msg = 'kasinadh'
# print(msg.isalpha())
# char_ = 'a'
# print(char_.isalpha())
# char_ = 'A'
# print(char_.isalpha())


"isalnum"
"it will return true if the all characters in string is of either alphabets or numeric only"
"even a single space or special characters is present it will return false"
# string_ = '12456'
# print(string_.isalnum())
# msg = 'hello'
# print(msg.isalnum())
# msg = 'hello123'
# print(msg.isalnum())
# msg = 'hello 412'
# print(msg.isalnum())
# msg = 'kasi@123'
# print(msg.isalnum())


"isdigit()"
"it will return if the character or all characters in the string is of digits"
"even a single space or alphabets or spedcial characters is present it will return false"
# msg = '1224'
# print(msg.isdigit())
# msg = '1223 450'
# print(msg.isdigit())
# msg = 'hello123'
# print(msg.isdigit())
# char_ = '1'
# print(msg.isdigit())


'isnumeric()'
"return true if the character "
# data = '25052'
# print(data.isnumeric())
# char_ = '1'
# print(char_.isnumeric())


"""isupper()"""
"return true if the character or all alphabets in the string is in upper case"
"if the special characters/numbers is there in the string there it will checks alphabets only"

# msg ='KKKKKKK IIII 122 '
# print(msg.isupper())
# msg = 'lllllLLLLIIIII RRRR'
# print(msg.isupper())
# data = 'Python 123'
# print(data.isupper())
# char_ = 'A'
# print(char_.isupper())

"islower()"
"return true if the character or all alphabets in the string is in lower case"
"if the special characters/numbers is there in the string there it will checks alphabets only"
# msg = 'king of jungle15'
# print(msg.islower())
# msg = 'king of Jungle'
# print(msg.islower())
# msg = 'king never fails'
# print(msg.islower())
# msg = '123212'
# print(msg.islower())
# char_ = 'a'
# print(char_.islower())

"ispsce()"
"returns true if the character or string contains only space"
char_ = ' '
print(char_.isspace())
msg = 'kasi 123'
print(msg.isspace())