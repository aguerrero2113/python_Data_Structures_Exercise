def list_manipulation(lst, command, location, value=None):

    if command == "remove":
        if location == "end":
            return lst.pop()

        elif location == "beginning":
            return lst.pop(0)

    elif command == "add":
        if location == "end":
            lst == lst.append(value)
            return lst
        elif location == "beginning":
            lst == lst.insert(0, value)
            return lst

print(list_manipulation([1,2,3],'remove','end',None))
print(list_manipulation([1,2,3],'remove','beginning',None))
print(list_manipulation([1,2,3],'add','beginning',20))
print(list_manipulation([1,2,3],'add','end',30))
print(list_manipulation([1,2,3],'foo','end',None))
print(list_manipulation([1,2,3],'add','dunno',None))