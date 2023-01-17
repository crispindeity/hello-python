def return_false():
    print("함수 return_false")
    return False


def return_true():
    print("함수 return_true")
    return True


print("테스트 1")
a = return_false()
b = return_true()

if a and b:
    print(True)
else:
    print(False)

print("테스트 2")
if return_false() and return_true():
    print("True")
else:
    print("False")

dic = {
    "Key2": "Value"
}

if "Key" in dic and dic["Key1"] == "Value1":
    print("Key1 도 있고, 그 값은 Value1 이다.")
else:
    print("아니네")
