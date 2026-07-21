import marshal
import base64

# خواندن کد رمزگذاری شده از فایل
try:
    with open("kinghacker_protected.py", "rb") as f:
        encoded_data = f.read()
    
    # رمزگشایی و اجرا در حافظه (بدون اینکه در فایل ذخیره شود)
    code_obj = marshal.loads(base64.b64decode(encoded_data))
    exec(code_obj)
    
except FileNotFoundError:
    print("Error: Protected file not found!")
except Exception as e:
    print(f"An error occurred: {e}")

