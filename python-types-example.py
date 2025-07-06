def full_name (firstName:str, lastName:str)-> str:
    return firstName.title() +' '  + lastName.title()


name = full_name('tom', 'okware')
print(name)