def AviFunc(name):
    if name == "Avi":
        return "granted"
    return "denied"

print(f"Welcome, {AviFunc('Avi').replace('granted', "access granted")}")