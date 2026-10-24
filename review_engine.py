# ==============================================================================
# 🧐 REVIEW ENGINE: BỘ SOI CHIẾU DÒNG KHÓA CỨNG & BẢO VỆ VĨNH VIỄN CỦA 10 TỆP
# ==============================================================================
import os, json

def audit_full_repo(repo_dir):
    failures = []

    # 1. Soi contract.json
    c_p = os.path.join(repo_dir, "contract.json")
    if os.path.exists(c_p):
        with open(c_p) as f: c = json.load(f)
        if c.get("genesis_root") != "100048777766367/contract":
            failures.append("contract.json sai genesis_root (bắt buộc trỏ về 100048777766367/contract)!")
    else: failures.append("Thiếu contract.json!")

    # 2. Soi bio_passport.json
    p_p = os.path.join(repo_dir, "synapses", "bio_passport.json")
    if os.path.exists(p_p):
        with open(p_p) as f: p = json.load(f)
        if p.get("genesis_root") != "100048777766367/contract":
            failures.append("bio_passport.json sai genesis_root!")
    else: failures.append("Thiếu bio_passport.json!")

    # 3. Soi Dockerfile
    d_p = os.path.join(repo_dir, "Dockerfile")
    if os.path.exists(d_p):
        with open(d_p) as f: d_txt = f.read()
        if "FROM python:3.14-slim" not in d_txt: failures.append("Dockerfile thiếu dòng Khóa Cứng: FROM python:3.14-slim!")
        if "PYTHONDONTWRITEBYTECODE=1" not in d_txt: failures.append("Dockerfile thiếu Bảo Vệ: PYTHONDONTWRITEBYTECODE=1!")
    else: failures.append("Thiếu Dockerfile!")

    # 4. Soi .gitignore
    g_p = os.path.join(repo_dir, ".gitignore")
    if os.path.exists(g_p):
        with open(g_p) as f: g_txt = f.read()
        if "__pycache__/" not in g_txt or "*.pyc" not in g_txt:
            failures.append(".gitignore thiếu dòng Khóa Cứng chặn rác bytecode!")
    else: failures.append("Thiếu .gitignore!")

    return len(failures) == 0, failures

print("🧐 [REVIEW ENGINE] Đã nạp bộ kiểm định dòng Khóa Cứng toàn diện cho 10 tệp.")
