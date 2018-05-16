# pyadb3

自用，仅支持python3。

## 安装
```
pip install pyadb3
```

## 使用
```python
import pyadb3

adb = pyadb3.ADB()
adb.run_shell_cmd('ls -l /')
print(adb.get_output().decode())
```
