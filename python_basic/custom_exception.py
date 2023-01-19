from UnexpetedRSPValue import UnexpectedRSPValue

value = "가"
try:
    if value not in ["가위", "바위", "보"]:
        raise UnexpectedRSPValue("가위바위보 중에 하나의 값이어야 합니다.")
except UnexpectedRSPValue as e:
    print(e)


# def sign_up():
#     """회원가입 함수"""
#
# try:
#     sign_up()
# except BadUserName:
#     print("이름으로 사용할 수 없는 입력입니다.")
# except PasswordNotMatched:
#     print("입력한 패스워드가 서로 일치하지 않습니다.")
