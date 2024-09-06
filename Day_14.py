my_list = ['mangoes.hpp','string.hpp','linked.hpp','stdio.hp']  # assume this is your list of file names or strings

new_list = [item.replace('.hpp', '.com') for item in my_list]

print(new_list)

new_list = []
for item in my_list:
    new_item = item.replace('.hpp','.com')
    new_list.append(new_item)
print(new_list)

# Replace old domain name of email to new
def replace_domain_name(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@"+old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
    
print(replace_domain_name("irfanali66693@gmail.com","gmail.com",'bnr360.net'))