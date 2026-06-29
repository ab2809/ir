
#Block 1: Function, Uppercase & Mapping
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

#Block 2: Keep First Letter & Convert Letters to Numbers

    first = name[0]
    nums = []
    for ch in name[1:]:
        if ch in code:
            nums.append(code[ch])
        else:
            nums.append("0")

#Block 3: Remove Duplicate Numbers
    result = []
    prev = ""
    for n in nums:
        if n != prev:
            result.append(n)
        prev = n

#Block 4: Remove Zeros & Return First 4 Characters

    result = [x for x in result if x != "0"]
    ans = first + "".join(result)
    return ans[:4].ljust(4, "0")


name = input("Enter Name : ")

print("Soundex Code :", soundex(name))