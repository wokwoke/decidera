import os
import re
import json
import subprocess
import sys
from datetime import datetime, timezone
import requests

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
CROSS_REPO_TOKEN = os.environ["CROSS_REPO_TOKEN"]
TARGET_REPO = os.environ["TARGET_REPO"]  # format: username/nama-repo
SOURCE_REPO = os.environ["SOURCE_REPO"]  # otomatis dari github.repository

def jalankan(cmd, cwd=None):
    hasil = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return hasil.stdout.strip()

def ambil_konteks_commit():
    pesan = jalankan("git log -1 --pretty=%B")
    hash_commit = jalankan("git log -1 --pretty=%H")
    ada_parent = jalankan("git rev-parse HEAD~1 2>/dev/null || true")

    if ada_parent:
        diff_stat = jalankan("git diff --stat HEAD~1 HEAD")
        # Prioritaskan diff PROGRESS.md jika ada, karena sering berisi konteks penting
        diff_isi = jalankan("git diff HEAD~1 HEAD -- PROGRESS.md")
        if not diff_isi:
            diff_isi = jalankan("git diff HEAD~1 HEAD")
    else:
        diff_stat = jalankan("git show --stat HEAD")
        diff_isi = jalankan("git show HEAD")

    return pesan, hash_commit, diff_stat, diff_isi[:6000]

def cek_apakah_trivial():
    """
    LAPISAN 1: Gatekeeper Murah & Cepat
    Mengembalikan True jika commit dianggap sepele (skip), False jika potensial penting (lanjut ke LLM).
    """
    # 1. Ambil daftar file yang berubah
    files_str = jalankan("git diff --name-only HEAD~1 HEAD")
    if not files_str:
        files_str = jalankan("git show --name-only --format='' HEAD")
    
    files = [f.strip() for f in files_str.split('\n') if f.strip()]
    if not files:
        return True  # Tidak ada file yang berubah

    # 2. Ambil statistik perubahan (shortstat)
    stat_str = jalankan("git diff --shortstat HEAD~1 HEAD")
    if not stat_str:
        stat_str = jalankan("git show --shortstat --format='' HEAD")
    
    # Parse jumlah baris yang berubah
    insertions = 0
    deletions = 0
    ins_match = re.search(r'(\d+)\s+insertion', stat_str)
    del_match = re.search(r'(\d+)\s+deletion', stat_str)
    if ins_match: insertions = int(ins_match.group(1))
    if del_match: deletions = int(del_match.group(1))
    
    total_changes = insertions + deletions
    
    # Rule A: Perubahan sangat kecil (kurang dari 5 baris total) -> kemungkinan typo/spasi
    if total_changes < 5:
        print(f"[Gatekeeper] Skip: Perubahan terlalu kecil ({total_changes} baris).")
        return True
