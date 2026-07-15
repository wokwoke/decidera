import os
import re
import subprocess
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
        diff_isi = jalankan("git diff HEAD~1 HEAD -- PROGRESS.md")
        if not diff_isi:
            diff_isi = jalankan("git diff HEAD~1 HEAD")
    else:
        diff_stat = jalankan("git show --stat HEAD")
        diff_isi = jalankan("git show HEAD")

    return pesan, hash_commit, diff_stat, diff_isi[:6000]


def minta_ringkasan_llm(pesan, diff_stat, diff_isi):
    prompt = f"""Ini adalah commit di repo "{SOURCE_REPO}".

Pesan commit:
{pesan}

Ringkasan file yang berubah:
{diff_stat}

Cuplikan perubahan:
{diff_isi}

Tugas: buat RINGKASAN METADATA singkat (bukan narasi panjang) soal apa yang dilakukan di commit ini. Ini untuk jurnal pengingat pribadi developer - tujuannya supaya developer sendiri atau penerusnya nanti cepat paham apa yang pernah dikerjakan dan kenapa, tanpa baca ulang seluruh kode.

Jawab PERSIS format ini (2 baris saja):
Judul: <3-6 kata ringkas aksi utama, huruf kecil, tanpa tanda baca>
Ringkasan: <2-4 kalimat bahasa Indonesia, jelaskan APA yang dilakukan dan KENAPA kalau tersirat>"""

    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
        json={
            "model": "llama-3.3-70b-versatile",
            "max_tokens": 300,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=30,
    )
    r.raise_for_status()
    teks = r.json()["choices"][0]["message"]["content"]

    judul_match = re.search(r"Judul:\s*(.+)", teks)
    ringkasan_match = re.search(r"Ringkasan:\s*(.+)", teks, re.DOTALL)

    judul = judul_match.group(1).strip() if judul_match else "aktivitas tanpa judul"
    ringkasan = ringkasan_match.group(1).strip() if ringkasan_match else pesan

    return judul, ringkasan


def slugify(teks: str) -> str:
    teks = teks.lower().strip()
    teks = re.sub(r"[^a-z0-9\s-]", "", teks)
    teks = re.sub(r"\s+", "-", teks)
    return teks[:60].strip("-")


def main():
    pesan, hash_commit, diff_stat, diff_isi = ambil_konteks_commit()
    judul, ringkasan = minta_ringkasan_llm(pesan, diff_stat, diff_isi)

    waktu = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    nama_repo_asal = SOURCE_REPO.split("/")[-1]
    aksi_slug = slugify(judul)
    nama_file = f"{waktu}-{nama_repo_asal}-{aksi_slug}.md"

    isi_file = f"""# {judul.capitalize()}

- **Tanggal:** {waktu}
- **Proyek:** {SOURCE_REPO}
- **Commit:** [{hash_commit[:8]}](https://github.com/{SOURCE_REPO}/commit/{hash_commit})

## Ringkasan
{ringkasan}

## Pesan commit asli
{pesan}
"""

    jalankan("rm -rf /tmp/target_repo")
    clone_url = f"https://x-access-token:{CROSS_REPO_TOKEN}@github.com/{TARGET_REPO}.git"
    hasil_clone = subprocess.run(f"git clone {clone_url} /tmp/targ
…(dipotong)
