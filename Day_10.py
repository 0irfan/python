# ========= Input function ===============.
name = input("Check Your Family Member Name: ")
family_list = ['Azlaan','Muhsin','irfan','shoaib']
if name in family_list:
    print(f"{name} is in the family list")
else:
    print(f"{name} Not in the list")