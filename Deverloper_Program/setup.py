from cx_Freeze import setup, Executable

setup(
    name="App",
    version="1.0",
    description="My Application",
    executables=[Executable("App.py", base="Win32GUI")],
    options={
        "build_exe": {
            "packages": ["cv2"],  # เพิ่ม OpenCV
            "include_files": ["./image","./download",'setting.txt']  # ไฟล์หรือโฟลเดอร์เพิ่มเติมที่ต้องการ
        }
    },
)

# python setup.py build