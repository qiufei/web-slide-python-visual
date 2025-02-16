import os

def create_qmd_files():
    for i in range(1, 9):
        filename = f"chapter{i}.qmd"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Chapter {i}\n\n")  # 添加一个简单的标题作为初始内容
        print(f"Created {filename}")

if __name__ == "__main__":
    create_qmd_files()
