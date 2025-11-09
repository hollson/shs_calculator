# 🧮 Python项目全流程指南

这是一个简单的 **Python计算器**示例项目，完整演示了从项目创建、编码、测试、打包发布到 PyPI 的全流程，适合初学者参考。



🌟 **核心特性:**

- 支持基础算术运算：加、减、乘、除
- 清晰的项目结构，便于初学者参考
- 全流程演示（编码 → 测试 → 打包 → 发布）
- 安装简单、使用便捷
- 代码注释完善，适合学习
- 包含异常处理（如除零错误）



<br/>



## 📂 一、创建项目

**项目结构**

```bash
poorcal/
├── poorcal/        	   # 核心代码(与项目名一致）
│   ├── __init__.py        # 包初始化
│   ├── calculator.py      # 计算器实现
│   └── cli.py             # 命令行接口
├── tests/                 # 测试目录
│   ├── __init__.py
│   └── test_calculator.py  # 测试用例
├── README.md               # 项目说明
├── pyproject.toml          # 项目配置(符合PEP621标准)
└── LICENSE                 # 许可证文件
```

**创建命令**

```bash
# 创建目录
mkdir -p poorcal/poorcal poorcal/tests
cd poorcal

# 创建文件
touch poorcal/__init__.py
touch poorcal/calculator.py
touch poorcal/cli.py
touch tests/__init__.py
touch tests/test_calculator.py
touch README.md
touch pyproject.toml
```



<br/>



## ✍️ 二、 项目编码

### 2.1 计算器类

```python
# File: poorcal/calculator.py
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
            raise ValueError("除数不能为零")
        return a / b
```

### 2.2 命令行接口

```python
# File: poorcal/cli.py
import sys
import re
from .calculator import Calculator

def main():
    if len(sys.argv) != 2:
        print("Usage: poorcal \"<number1> <operator> <number2>\"")
        print("Example: poorcal \"1 + 2\"")
        sys.exit(1)

    expr = sys.argv[1].strip()
    match = re.match(r'^\s*(\d*\.?\d+)\s*([+\-*/])\s*(\d*\.?\d+)\s*$', expr)
    if not match:
        print(f"Error: Invalid expression format. Expected '<number> <operator> <number>', you entered: {expr}")
        print("Example: poorcal \"3 + 2\" or poorcal \"10.5 * 2\"")
        sys.exit(1)

    a_str, op, b_str = match.groups()
    calc = Calculator()

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print("Error: Numbers must be valid numeric values")
        sys.exit(1)

    operations = {
        '+': calc.add,
        '-': calc.subtract,
        '*': calc.multiply,
        '/': calc.divide
    }

    if op not in operations:
        print("Error: Operator must be one of +, -, *, /")
        sys.exit(1)

    try:
        result = operations[op](a, b)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### 2.3 包初始化

```python
# File: poorcal/__init__.py
# 从核心模块导入 Calculator 类，方便用户直接导入使用
from .calculator import Calculator

# 定义包的版本号（与 pyproject.toml 中的版本保持一致）
__version__ = "0.1.0"
__all__ = ["Calculator"]
```



<br/>



## 🧪  三、测试验证

### 3.1 测试代码

```python
# File: tests/test_calculator.py
import unittest
from poorcal import Calculator

class TestCalculator(unittest.TestCase):
    """Calculator 类的单元测试用例"""

    def setUp(self):
        """每个测试方法执行前初始化计算器实例"""
        self.calc = Calculator()

    def test_add(self):
        """测试加法运算"""
        # 整数加法
        self.assertEqual(self.calc.add(2, 3), 5)
        # 负数加法
        self.assertEqual(self.calc.add(-1, 1), 0)
        # 浮点数加法
        self.assertEqual(self.calc.add(3.5, 2.5), 6.0)
        # 零值加法
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """测试减法运算"""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(5, 8), -3)
        self.assertEqual(self.calc.subtract(7.2, 2.2), 5.0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        """测试乘法运算"""
        self.assertEqual(self.calc.multiply(5, 6), 30)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        """测试除法运算"""
        self.assertEqual(self.calc.divide(8, 2), 4.0)
        self.assertEqual(self.calc.divide(-9, 3), -3.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        # 浮点数除数
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)

    def test_divide_by_zero(self):
        """测试除零异常"""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(5, 0)
        self.assertEqual(str(context.exception), "除数不能为零")        

if __name__ == "__main__":
    # 运行所有测试用例
    unittest.main()
```

### 3.2 运行测试

```bash
# 方式1：直接运行测试文件
python -m tests.test_calculator

# 方式2：发现所有测试用例
python -m unittest discover -s tests -v
```

### 3.3 终端CLI测试

```shell
pip install -e .  # 本地安装(开发模式）
pip list
```

```shell
# 测试命令行
poorcal "1 + 2"
poorcal "3 - 1"
poorcal "2 * 3"
poorcal "8 / 2"
```



<br/>



## 📦 四、打包发布

### 4.1 配置pyproject

```toml
[project]
name = "poorcal"
version = "0.1.0"
authors = [
  { name="Hollson", email="hollson@qq.com" }
]
description = "一个简单的Python计算器项目示例"
license = { file="LICENSE" }
classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  "Intended Audience :: Developers",
  "Topic :: Education",
  "Topic :: Software Development :: Testing",
]
keywords = ["calculator", "python-beginner"]
requires-python = ">=3.12"
dependencies = []

[project.scripts]
poorcal = "poorcal.cli:main"
```



### 2. 构建打包

```bash
# 需要先安装：pip install build
python -m build
```

生成文件：

- `dist/poorcal-0.1.0.tar.gz` (源码包)
- `dist/poorcal-0.1.0-py3-none-any.whl` (Wheel 安装包，推荐）



### 3. 发布到PyPI

- **注册账号 ：**  前往 [https://pypi.org](https://pypi.org/) 注册账号，并验证邮箱。
- **创建API Token :** 登录后进入账号管理，点击生成 [Add API token](https://pypi.org/manage/account/token/) 创建**Token**，复制Token (_只会显示一次_)。

- **上传到PyPI  :** 上传时需要填入上面的Token进行验证。

    ```shell
    # 依赖上传工具: pip install twine
    twine upload dist/*
    ```

    ```shell
    $ twine upload dist/*
    Uploading distributions to https://upload.pypi.org/legacy/
    WARNING  This environment is not supported for trusted publishing                                             
    Enter your API token: 
    Uploading poorcal-0.1.0-py3-none-any.whl
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.7/5.7 kB • 00:00 • ?
    Uploading poorcal-0.1.0.tar.gz
    100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 kB • 00:00 • ?
    
    View at:
    https://pypi.org/project/ccliulator/0.1.0/
    ```

    

<br/>



## 🚀 五、使用示例

### 1. 安装包

```shell
$ pip show poorcal
Name: poorcal
Version: 0.1.0
Summary: 一个简单的加减乘除计算包，完美演绎了Python包的应用过程。
Home-page: https://github.com/hollson/poorcal
Author:
Author-email: Hollson <hollson@qq.com>
License-Expression: MIT
Location: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages
Requires:
Required-by:
```

### 2. 项目中使用

```python
from poorcal import Calculator

calc = Calculator()
print(calc.add(2, 3))      # 5.0
print(calc.divide(10, 2))  # 5.0
```

### 3. 命令行使用

```bash
poorcal "3 * 4"  # 输出: 结果: 12.0
```



<br/>



## 🔄 六、版本更新

1. 修改代码（如新增`power`平方函数）
2. 更新`__init__.py`中的`__version__`（如改为`0.1.1`）
3. 重新构建打包：`python -m build`
4. 重新上传：`twine upload dist/*`（PyPI不允许重复上传同一版本，需升级版本号）

