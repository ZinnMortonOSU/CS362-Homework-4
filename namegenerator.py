def nameGenerator(firstName, lastName):
    if(not(isinstance(firstName, str) and isinstance(lastName, str))):
        raise Exception("nameGenerator expects strings only")

    if(firstName == "" or lastName == ""):
        raise Exception("nameGenerator needs non-empty names")

    return firstName + " " + lastName