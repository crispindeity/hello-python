class UnexpectedRSPValue(Exception):
    """가위 바위 보 가운데 하나가 아닌값인 경우 발생하는 에러"""
    def __init__(self, message):
        super().__init__(message)
