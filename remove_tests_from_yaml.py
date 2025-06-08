#!/usr/bin/env python3
import os
import yaml
import argparse
from pathlib import Path

def remove_tests_from_yaml_content(content):
    """YAML 내용에서 tests 섹션을 제거합니다."""
    def remove_tests_recursive(obj):
        if isinstance(obj, dict):
            # tests 키가 있으면 제거
            if 'tests' in obj:
                del obj['tests']
            # 모든 값에 대해 재귀적으로 적용
            for key, value in obj.items():
                remove_tests_recursive(value)
        elif isinstance(obj, list):
            # 리스트의 각 요소에 대해 재귀적으로 적용
            for item in obj:
                remove_tests_recursive(item)
    
    try:
        # YAML 파싱
        data = yaml.safe_load(content)
        if data:
            # tests 섹션 제거
            remove_tests_recursive(data)
            # YAML로 다시 변환
            return yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
        return content
    except Exception as e:
        print(f"YAML 파싱 오류: {e}")
        return content

def process_yaml_file(file_path):
    """단일 YAML 파일을 처리합니다."""
    try:
        print(f"처리 중: {file_path}")
        
        # 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # tests 섹션 제거
        modified_content = remove_tests_from_yaml_content(original_content)
        
        # 변경사항이 있는 경우에만 파일 쓰기
        if original_content != modified_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            print(f"✓ 수정됨: {file_path}")
            return True
        else:
            print(f"○ 변경사항 없음: {file_path}")
            return False
            
    except Exception as e:
        print(f"✗ 오류 발생 {file_path}: {e}")
        return False

def find_yaml_files(directory):
    """디렉토리에서 모든 YAML 파일을 찾습니다."""
    yaml_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                yaml_files.append(os.path.join(root, file))
    return yaml_files

def main():
    parser = argparse.ArgumentParser(description='YAML 파일들에서 tests 섹션을 제거합니다.')
    parser.add_argument('directory', nargs='?', default='generated_yaml', 
                       help='처리할 디렉토리 (기본값: generated_yaml)')
    parser.add_argument('--dry-run', action='store_true', 
                       help='실제로 파일을 수정하지 않고 미리보기만 실행')
    
    args = parser.parse_args()
    
    # 디렉토리 존재 확인
    if not os.path.exists(args.directory):
        print(f"디렉토리가 존재하지 않습니다: {args.directory}")
        return
    
    # YAML 파일 찾기
    yaml_files = find_yaml_files(args.directory)
    
    if not yaml_files:
        print(f"디렉토리에서 YAML 파일을 찾을 수 없습니다: {args.directory}")
        return
    
    print(f"총 {len(yaml_files)}개의 YAML 파일을 찾았습니다.")
    
    if args.dry_run:
        print("DRY RUN 모드 - 파일은 실제로 수정되지 않습니다.")
        for file_path in yaml_files:
            print(f"처리 예정: {file_path}")
        return
    
    # 각 파일 처리
    modified_count = 0
    for file_path in yaml_files:
        if process_yaml_file(file_path):
            modified_count += 1
    
    print(f"\n완료: {modified_count}개 파일이 수정되었습니다.")

if __name__ == "__main__":
    main() 