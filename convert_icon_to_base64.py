# convert_icon_to_base64.py
import base64
import sys


def icon_to_base64(icon_path):
    with open(icon_path, "rb") as f:
        b64_str = base64.b64encode(f.read()).decode('utf-8')

    # 每76个字符换行，方便粘贴到代码中
    lines = [b64_str[i:i + 76] for i in range(0, len(b64_str), 76)]
    formatted = 'ICON_BASE64 = (\n' + '\n'.join(f'    "{line}"' for line in lines) + '\n)'

    print(formatted)
    print(f"\n# 总长度: {len(b64_str)} 字符")


if __name__ == "__main__":
    icon_to_base64("yz.ico")