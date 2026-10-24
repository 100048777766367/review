# ==============================================================================
# 🧐 REVIEW ENGINE: RÀ SOÁT CÁC DÒNG KHÓA CỨNG & BẮT LỆCH PHA WORKFLOW
# ==============================================================================
import os, re

def audit_workflow(yml_path, engine_file):
    if not os.path.exists(yml_path): return False, "Thiếu tệp workflow CI/CD!"
    with open(yml_path, "r", errors="ignore") as f: content = f.read()

    # 1. Soi các dòng Khóa Cứng bắt buộc
    if "permissions:" not in content or "contents: write" not in content:
        return False, "Thiếu dòng Khóa Cứng: 'permissions: contents: write' (Sẽ lỗi 403)!"
    if "actions/setup-python@v7" not in content:
        return False, "Thiếu dòng Khóa Cứng: 'actions/setup-python@v7'!"
    if "'3.14'" not in content and '"3.14"' not in content:
        return False, "Thiếu dòng Khóa Cứng: python-version: '3.14'!"

    # 2. Soi cơ chế Git bọc thép
    if "[skip ci]" not in content:
        return False, "Thiếu dòng Bảo Vệ: cờ [skip ci] trong commit (Nguy cơ bão lặp)!"
    if "git reset origin/" not in content:
        return False, "Thiếu dòng Bảo Vệ: git reset origin/ chống lỗi 128!"

    # 3. Soi khớp lệnh động cơ
    if engine_file and engine_file not in content and "kernel.py" not in content:
        return False, f"LỆCH PHA: Workflow không chứa lệnh chạy cho tệp '{engine_file}'!"

    return True, "🟢 Workflow đạt chuẩn Bọc Thép 100%!"

print("🧐 [REVIEW ENGINE] Đã nạp bộ kiểm định dòng Khóa Cứng & Chống Lệch Pha.")
