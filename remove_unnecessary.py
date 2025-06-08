"""
다섯번째 실행되는 파일
백틱 및 random.choice([True, False]) else None 패턴 제거
"""

import os
import glob
import re


def remove_backticks_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 백틱으로 둘러싸인 부분 제거
    if "```" in content:
        # ```python 제거
        content = content.replace("```python", "")
        # 일반 백틱 제거
        content = content.replace("```", "")

    # random.choice([True, False]) else None 패턴 제거
    pattern = r"if\s+random\.choice\(\[True,\s*False\]\)\s+else\s+None"
    content = re.sub(pattern, "", content)

    # 파일 끝의 빈 줄 정리
    content = content.rstrip() + "\n"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"백틱 및 random.choice 패턴 제거됨: {file_path}")


def main():
    # temp_faker_code 디렉토리와 그 하위 디렉토리의 모든 .py 파일 찾기
    py_files = glob.glob("temp_faker_code/**/*.py", recursive=True)

    for file_path in py_files:
        remove_backticks_from_file(file_path)


if __name__ == "__main__":
    main()
