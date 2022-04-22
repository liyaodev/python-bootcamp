
## Python 插件技术
* 

## 程序运行
```shell
# 根路径
python3 server.py
```

```shell
# 输出
OrderedDict([('ctype', <widget.ctype.infer.C_Type object at 0x7fa7ad64ef90>), ('demo', <widget.demo.infer.Demo object at 0x7fa7ad651350>), ('digit_recognition', <widget.digit_recognition.infer.DigitRecognition object at 0x7fa7ad656290>)])
INFO: this is demo infer, req_dict={"plugin": "demo"}
INFO: this is ctype infer, req_dict={"plugin": "ctype"}
INFO: so.sum(50) = 1275
INFO: so.add(50, 100) = 150
INFO: this is demo infer, req_dict={"plugin": "demo"}
INFO: this is digit recognition infer, req_dict={"plugin": "digit_recognition"}
```

## C_lib 包编译
```shell
cd widget/ctype
gcc -c -fPIC -o lib/sum.o sum.c
gcc -shared -o lib/sum.so lib/sum.o
```
