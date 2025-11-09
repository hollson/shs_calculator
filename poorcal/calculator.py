class Calculator:
    """简单计算器类，支持加减乘除运算"""
    
    def add(self, a: float, b: float) -> float:
        """加法运算"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """减法运算"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """乘法运算"""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """除法运算"""
        if b == 0:
            raise ValueError("The divisor cannot be zero")
        return a / b