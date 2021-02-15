# word = "supercaligrafkjoknsk"
#
# # word = word[0: 5: 1]
# print(word)
# print(word[:7])
# print(word[::-1])
#
# word = word[word.index("cali"):word.index("jok")]
# print(word)
# get user email address
email = input("Please Input your email?: ").strip()

# slice the user name
user = email[:email.index("@")]
print(user)

# slice domain name
domain = email[email.index("@") + 1:]
print(domain)

# format message
output = "Your username is {} and your domain name is {}"

# display message
print(output.format(user, domain))
