#!/usr/bin/env python3
"""
GitHub Action Runner for BookBloggers Coordinator
"""
import os
import sys
import json
import argparse
import urllib.request
import subprocess

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(REPO_DIR, "instagram_book_bloggers_analytics_rich.json")
AVATARS_DIR = os.path.join(REPO_DIR, "avatars")
SCRIPTS_DIR = os.path.join(REPO_DIR, "scripts")

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
GROUP_ID = os.environ.get("TELEGRAM_GROUP_ID", "-1004445327603")
BOXAPI_AUTH = os.environ.get("BOXAPI_AUTH", "Basic MDkxMjcwNDc4MTM6UmljazA5MTJA")


def send_tg_message(text):
    if not BOT_TOKEN:
        print("No TELEGRAM_BOT_TOKEN set, skipping message.")
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = json.dumps({
        "chat_id": GROUP_ID,
        "text": text
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req, timeout=15)
        print("Telegram notification sent.")
    except Exception as e:
        print(f"Telegram notify error: {e}", file=sys.stderr)


def fetch_boxapi(username):
    url = "https://boxapi.ir/api/instagram/user/get_info_by_username"
    clean_user = username.strip().lstrip("@")
    payload = json.dumps({"username": clean_user}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": BOXAPI_AUTH,
        "Content-Type": "application/json"
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            user = data.get("response", {}).get("body", {}).get("user", {})
            return user
    except Exception as e:
        print(f"BoxAPI error: {e}", file=sys.stderr)
        return None


def format_num(n):
    if n >= 1000000:
        return f"{round(n / 1000000, 1)}M"
    if n >= 1000:
        return f"{round(n / 1000, 1)}K"
    return str(n)


def run_builders():
    subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, "build_blogger_pages.py")], check=True)
    subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, "update_index_links.py")], check=True)
    subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, "generate_sitemap.py")], check=True)
    subprocess.run([sys.executable, os.path.join(SCRIPTS_DIR, "build_pricing_table_page.py")], check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", required=True, choices=["add", "update", "sync"])
    parser.add_argument("--handle", default="")
    args = parser.parse_args()

    handle = args.handle.strip().lstrip("@")

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        bloggers = json.load(f)
    blogger_map = {b["username"].lower(): b for b in bloggers}

    if args.action == "add":
        if not handle:
            print("Handle is required for add")
            sys.exit(1)

        user_info = fetch_boxapi(handle)
        folls = user_info.get("follower_count", 1000) if user_info else 1000
        foll_str = format_num(folls)
        fn = user_info.get("full_name") if user_info else handle
        posts = str(user_info.get("media_count", 50)) if user_info else "50"
        pic_url = user_info.get("profile_pic_url", "") if user_info else ""
        
        avatar_file = f"{handle.lower()}.jpg"
        dest = os.path.join(AVATARS_DIR, avatar_file)
        if pic_url:
            try:
                pic_req = urllib.request.Request(pic_url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(pic_req, timeout=15) as r, open(dest, "wb") as out:
                    out.write(r.read())
            except Exception as e:
                print(f"Avatar download failed: {e}")

        entry = {
            "input": handle.lower(),
            "username": handle.lower(),
            "display_name": fn,
            "account_id": f"{handle.lower()}_id",
            "followers": foll_str,
            "following": str(user_info.get("following_count", 200)) if user_info else "200",
            "posts": posts,
            "is_private": False,
            "is_verified": False,
            "coco_analytics_url": f"https://coco.gl/dashboard/analytics/INSTAGRAM/{handle.lower()}?username={handle.lower()}",
            "profile_pic_url": pic_url,
            "local_avatar": f"avatars/{avatar_file}",
            "est_engagement_rate": "۷.۰٪ الی ۱۰.۰٪",
            "est_story_view": f"{int(folls * 0.1)} تا {int(folls * 0.18)} بازدید",
            "est_reel_view": f"{int(folls * 0.3)} تا {int(folls * 0.8)} بازدید",
            "influencer_tier": "بوک‌بلاگر فعال",
            "audience_profile": "دنبال‌کنندگان پیگیر حوزه کتاب و معرفی رمان."
        }

        if handle.lower() not in blogger_map:
            bloggers.append(entry)
        else:
            blogger_map[handle.lower()].update(entry)

        with open(JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(bloggers, f, ensure_ascii=False, indent=2)

        run_builders()
        send_tg_message(f"پیج @{handle} با موفقیت به دایرکتوری اضافه شد 🤍\n\n• نام: {fn}\n• فالوور: {foll_str}\n• تعداد پست: {posts}\n• لینک صفحه اختصاصی: https://bookbloger.github.io/blogger/{handle.lower()}.html")

    elif args.action == "update":
        if not handle:
            print("Handle is required for update")
            sys.exit(1)

        user_info = fetch_boxapi(handle)
        if user_info and handle.lower() in blogger_map:
            folls = user_info.get("follower_count", 0)
            foll_str = format_num(folls)
            posts = str(user_info.get("media_count", 0))
            blogger_map[handle.lower()]["followers"] = foll_str
            blogger_map[handle.lower()]["posts"] = posts
            with open(JSON_PATH, "w", encoding="utf-8") as f:
                json.dump(bloggers, f, ensure_ascii=False, indent=2)

            run_builders()
            send_tg_message(f"آمار پیج @{handle} با موفقیت به‌روزرسانی شد 🤍\n\n• فالوور جدید: {foll_str}\n• تعداد پست: {posts}\n• لینک: https://bookbloger.github.io/blogger/{handle.lower()}.html")
        else:
            send_tg_message(f"خطا: پیج @{handle} یافت نشد یا دریافت آمار ناموفق بود.")

    elif args.action == "sync":
        run_builders()
        send_tg_message(f"دایرکتوری بوک‌بلاگرها با موفقیت همگام‌سازی و منتشر شد 🤍\nتعداد کل بلاگرها: {len(bloggers)}")


if __name__ == "__main__":
    main()
