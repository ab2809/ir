def soundex(name):
    name = name.upper()
    code = {
        "B":"1","F":"1","P":"1","V":"1",
        "C":"2","G":"2","J":"2","K":"2","Q":"2","S":"2","X":"2","Z":"2",
        "D":"3","T":"3",
        "L":"4",
        "M":"5","N":"5",
        "R":"6"
    }

    first = name[0]
    result = []
    prev = ""

    for ch in name[1:]:
        if ch in code:
            num = code[ch]
        else:
            num = "0"
        if num != prev:
            result.append(num)
        prev = num
    result = [x for x in result if x != "0"]
    return (first + "".join(result))[:4].ljust(4, "0")


name = input("Enter Name: ")
print("Soundex Code:", soundex(name))
