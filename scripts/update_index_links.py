import os
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import json
import os
import re

with open(os.path.join(REPO_DIR, "instagram_book_bloggers_analytics_rich.json"), 'r', encoding='utf-8') as f:
    bloggers = json.load(f)

SITE_URL = "https://bookbloger.github.io"
TG_GROUP_URL = "https://t.me/+tReSYWxBreFmYThk"

def parse_num(val):
    if not val or val == '-':
        return 0
    clean = str(val).strip().replace(',', '')
    if 'k' in clean.lower():
        num_str = re.sub(r'[^\d\.]', '', clean)
        return float(num_str) * 1000
    if 'm' in clean.lower():
        num_str = re.sub(r'[^\d\.]', '', clean)
        return float(num_str) * 1000000
    try:
        return float(re.sub(r'[^\d\.]', '', clean))
    except:
        return 0

hidden_usernames = {'mina.bookk', 'sinmoruk', 'ketabiyaaa'}
visible_bloggers = [b for b in bloggers if b['username'].lower() not in hidden_usernames]

# Sort bloggers descending by follower count first
bloggers_sorted = sorted(visible_bloggers, key=lambda x: parse_num(x.get('followers')), reverse=True)

# Exact calculated dynamic stats for visible bloggers
total_followers_num = sum(parse_num(b.get('followers')) for b in visible_bloggers)
total_posts_num = sum(parse_num(b.get('posts')) for b in visible_bloggers)

top_blogger = bloggers_sorted[0] if bloggers_sorted else {}
top_blogger_username = top_blogger.get('username', '')
top_blogger_name = top_blogger.get('display_name', top_blogger_username).split('|')[0].strip()
top_blogger_foll_str = top_blogger.get('followers', '')

total_foll_str = f"{int(total_followers_num):,}"
total_foll_badge = f"+{total_followers_num/1000000:.2f}M" if total_followers_num >= 1000000 else f"+{total_followers_num/1000:.0f}K"
total_pages_count = len(visible_bloggers)
total_posts_str = f"{int(total_posts_num):,}"

item_list_elements = []
for rank, b in enumerate(bloggers_sorted, 1):
    u = b['username']
    slug = u.lower()
    name = b['display_name'] or u
    page_url = f"{SITE_URL}/blogger/{slug}.html"
    item_list_elements.append({
        "@type": "ListItem",
        "position": rank,
        "name": f"{name} (@{u})",
        "url": page_url
    })

schema_website = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "BookBloger - دایرکتوری و رتبه‌بندی بوک‌بلاگرهای اینستاگرام",
    "url": f"{SITE_URL}/",
    "description": f"دایرکتوری جامع، رتبه‌بندی و شناسنامه تحلیلی {total_pages_count} بوک‌بلاگر برتر اینستاگرام با مجموع بیش از {total_foll_badge} مخاطب فعال کتاب.",
    "publisher": {
        "@type": "Person",
        "name": "Rick Sanchez",
        "alternateName": "ریک سانچز",
        "url": "https://t.me/m4tinbeigipv"
    },
    "inLanguage": "fa-IR"
}

schema_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "رتبه‌بندی برترین بوک‌بلاگرهای اینستاگرام ایران",
    "description": "لیست رتبه‌بندی‌شده بوک‌بلاگرها بر اساس تعداد فالوور، تعامل و عملکرد در شبکه‌های اجتماعی",
    "numberOfItems": len(item_list_elements),
    "itemListElement": item_list_elements
}

schema_website_json = json.dumps(schema_website, ensure_ascii=False, indent=2)
schema_itemlist_json = json.dumps(schema_itemlist, ensure_ascii=False, indent=2)

cards_html = []
for rank, b in enumerate(bloggers_sorted, 1):
    u = b['username']
    slug = u.lower()
    name = b['display_name'] or u
    foll = b['followers']
    flwing = b['following']
    posts = b['posts']
    avatar = b.get('local_avatar', f"avatars/{u.lower()}.jpg")
    if u.lower() == "_cherryremi":
        avatar = "avatars/cherryremi.jpg"
    coco_url = b['coco_analytics_url']
    ig_url = f"https://instagram.com/{u}"
    detail_page_url = f"blogger/{slug}.html"
    
    rank_class = "rank-badge"
    if rank == 1:
        rank_class += " rank-1"
        rank_label = "🥇 رتبه ۱"
    elif rank == 2:
        rank_class += " rank-2"
        rank_label = "🥈 رتبه ۲"
    elif rank == 3:
        rank_class += " rank-3"
        rank_label = "🥉 رتبه ۳"
    else:
        rank_label = f"#{rank}"

    card = f"""        <div class="card" data-name="{name} {u}" data-followers="{parse_num(foll)}">
            <div class="{rank_class}">{rank_label}</div>
            <div class="card-main-content">
                <div class="card-top">
                    <a href="{detail_page_url}" class="avatar-wrap" title="صفحه تحلیلی و تعرفه {name}">
                        <img src="{avatar}" alt="{name} - بلاگر کتاب" class="avatar" loading="lazy" onerror="this.src='https://ui-avatars.com/api/?name={u}&background=random'">
                    </a>
                    <div class="info">
                        <h3 title="{name}"><a href="{detail_page_url}" class="name-link">{name}</a></h3>
                        <a href="{ig_url}" target="_blank" rel="noopener noreferrer" class="handle" title="اینستاگرام {u}">@{u}</a>
                    </div>
                </div>

                <div class="metrics">
                    <div class="metric-item">
                        <div class="val highlight">{foll}</div>
                        <div class="lbl">فالوور</div>
                    </div>
                    <div class="metric-item">
                        <div class="val">{flwing}</div>
                        <div class="lbl">فالویینگ</div>
                    </div>
                    <div class="metric-item">
                        <div class="val">{posts}</div>
                        <div class="lbl">پست‌ها</div>
                    </div>
                </div>
            </div>

            <div class="card-actions">
                <a href="{detail_page_url}" class="btn btn-detail" title="مشاهده آمار BoxAPI و تعرفه {name}">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
                    صفحه اختصاصی و تعرفه
                </a>
                <a href="{ig_url}" target="_blank" rel="noopener noreferrer" class="btn btn-ig" title="پیج اینستاگرام {u}">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                    اینستاگرام
                </a>
            </div>
        </div>"""
    cards_html.append(card)

all_cards = "\n".join(cards_html)

full_html = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta name="google-site-verification" content="1bSuT-QoDy7ukGYtf0DVP8jBzHzIhxEqGPHMJVxjD94" />
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>معرفی و رتبه‌بندی برترین بوک‌بلاگرهای اینستاگرام | دایرکتوری و تعرفه تبلیغات BookBloger</title>
    <meta name="description" content="دایرکتوری جامع و رتبه‌بندی {total_pages_count} بوک‌بلاگر برتر اینستاگرام در ایران با مجموع بیش از {total_foll_badge} مخاطب فعال کتاب، شناسنامه آماری، نرخ تعامل و تعرفه تبلیغات.">
    <meta name="keywords" content="بوک بلاگر, بلاگر کتاب, بهترین بوک بلاگرهای ایران, اینستاگرام کتاب, تبلیغات کتاب, رتبه‌بندی بوک بلاگرها, معرفی کتاب, قیمت تبلیغات کتاب, بوک‌استاگرام, bookblogger">
    <link rel="canonical" href="{SITE_URL}/">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">

    <!-- OpenGraph Meta Tags -->
    <meta property="og:locale" content="fa_IR">
    <meta property="og:type" content="website">
    <meta property="og:title" content="رتبه‌بندی و دایرکتوری جامع بوک‌بلاگرهای اینستاگرام | BookBloger">
    <meta property="og:description" content="بانک اطلاعاتی و شناسنامه تحلیلی برترین بلاگرهای کتاب ایران با بیش از {total_foll_badge} مخاطب فعال کتاب. گردآوری و تحلیل: ریک سانچز.">
    <meta property="og:url" content="{SITE_URL}/">
    <meta property="og:site_name" content="BookBloger">
    <meta property="og:image" content="{SITE_URL}/story_poster.png">
    <meta property="og:image:width" content="1080">
    <meta property="og:image:height" content="1920">
    <meta property="og:image:alt" content="پوستر رتبه‌بندی بوک‌بلاگرهای ایران">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="رتبه‌بندی جامع بوک‌بلاگرهای اینستاگرام | BookBloger">
    <meta name="twitter:description" content="دایرکتوری و تعرفه تبلیغات {total_pages_count} اینفلوئنسر و بلاگر کتاب در ایران.">
    <meta name="twitter:image" content="{SITE_URL}/story_poster.png">

    <!-- JSON-LD Structured Data Schemas -->
    <script type="application/ld+json">
{schema_website_json}
    </script>
    <script type="application/ld+json">
{schema_itemlist_json}
    </script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0b0f19;
            --card-bg: #151d30;
            --card-hover: #1b2640;
            --accent: #6366f1;
            --accent-gradient: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
            --campaign-gradient: linear-gradient(135deg, #1e1b4b 0%, #311042 50%, #1e293b 100%);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --border: #23304e;
            --gold: #f59e0b;
            --silver: #94a3b8;
            --bronze: #b45309;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Vazirmatn', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }}

        body {{
            background-color: var(--bg-color);
            color: var(--text-primary);
            line-height: 1.6;
            min-height: 100vh;
            padding: 30px 16px 60px;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        header {{
            text-align: center;
            margin-bottom: 35px;
        }}

        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(99, 102, 241, 0.12);
            color: #818cf8;
            border: 1px solid rgba(99, 102, 241, 0.3);
            padding: 6px 16px;
            border-radius: 9999px;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 16px;
        }}

        .nav-banners-row {{
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 18px;
        }}

        .banner-btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 9px 20px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 800;
            text-decoration: none;
            transition: all 0.25s ease;
        }}

        .banner-btn.pricing-tbl {{
            background: linear-gradient(135deg, #059669 0%, #10b981 50%, #06b6d4 100%);
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
            border: 1.5px solid rgba(255, 255, 255, 0.2);
        }}

        .banner-btn.squad-pkg {{
            background: linear-gradient(135deg, #be185d 0%, #ec4899 50%, #8b5cf6 100%);
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4);
            border: 1.5px solid rgba(255, 255, 255, 0.2);
        }}

        .banner-btn.group-tg {{
            background: linear-gradient(135deg, #229ED9 0%, #0284c7 100%);
            border: 1.5px solid #38bdf8;
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(34, 158, 217, 0.3);
        }}

        .banner-btn.group-tg:hover {{
            background: #1b86b8;
            transform: translateY(-2px);
        }}

        .banner-btn.galaxy {{
            background: linear-gradient(135deg, rgba(56, 189, 248, 0.2) 0%, rgba(99, 102, 241, 0.25) 100%);
            border: 1.5px solid rgba(56, 189, 248, 0.5);
            color: #38bdf8;
        }}

        .banner-btn.galaxy:hover {{
            background: rgba(56, 189, 248, 0.3);
            transform: translateY(-2px);
        }}

        .banner-btn.top-posts {{
            background: linear-gradient(135deg, rgba(236, 72, 153, 0.2) 0%, rgba(99, 102, 241, 0.2) 100%);
            border: 1.5px solid rgba(236, 72, 153, 0.4);
            color: #f472b6;
        }}

        .banner-btn.top-posts:hover {{
            background: rgba(236, 72, 153, 0.3);
            transform: translateY(-2px);
        }}

        .banner-btn.top-100 {{
            background: rgba(15, 23, 42, 0.7);
            border: 1.5px solid rgba(255, 255, 255, 0.15);
            color: #e2e8f0;
        }}

        .banner-btn.top-100:hover {{
            background: #1e293b;
            transform: translateY(-2px);
        }}

        h1 {{
            font-size: clamp(22px, 5vw, 36px);
            font-weight: 900;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
            line-height: 1.3;
        }}

        p.subtitle {{
            color: var(--text-secondary);
            font-size: clamp(13px, 3.5vw, 16px);
            max-width: 680px;
            margin: 0 auto 12px;
            padding: 0 10px;
        }}

        .curator-tag {{
            display: inline-block;
            color: #38bdf8;
            font-size: 13.5px;
            font-weight: 600;
            margin-bottom: 24px;
        }}

        /* Campaign Banner */
        .campaign-section {{
            background: var(--campaign-gradient);
            border: 1px solid rgba(168, 85, 247, 0.35);
            border-radius: 20px;
            padding: 28px 24px;
            margin: 0 auto 35px;
            max-width: 900px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
        }}

        .campaign-section::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.08) 0%, transparent 70%);
            pointer-events: none;
        }}

        .campaign-badge {{
            display: inline-block;
            background: rgba(236, 72, 153, 0.2);
            color: #f472b6;
            border: 1px solid rgba(236, 72, 153, 0.4);
            padding: 4px 14px;
            border-radius: 9999px;
            font-size: 12px;
            font-weight: 700;
            margin-bottom: 12px;
        }}

        .campaign-title {{
            font-size: clamp(18px, 4vw, 22px);
            font-weight: 800;
            color: #fff;
            margin-bottom: 10px;
        }}

        .campaign-desc {{
            font-size: clamp(13px, 3.2vw, 14.5px);
            color: #cbd5e1;
            max-width: 720px;
            margin: 0 auto 20px;
            line-height: 1.7;
        }}

        .contact-buttons {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .contact-btn {{
            padding: 10px 18px;
            border-radius: 10px;
            font-size: 13.5px;
            font-weight: 700;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.25s ease;
        }}

        .contact-btn-group {{
            background: linear-gradient(135deg, #229ED9 0%, #0284c7 100%);
            color: #fff;
            box-shadow: 0 4px 12px rgba(34, 158, 217, 0.4);
        }}

        .contact-btn-group:hover {{
            background: #1b86b8;
            transform: translateY(-2px);
        }}

        .contact-btn-tg {{
            background: #1e293b;
            color: #38bdf8;
            border: 1px solid #334155;
        }}

        .contact-btn-tg:hover {{
            background: #334155;
            color: #fff;
            transform: translateY(-2px);
        }}

        .contact-btn-ig {{
            background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
            color: #fff;
        }}

        .contact-btn-ig:hover {{
            opacity: 0.95;
            transform: translateY(-2px);
        }}

        /* Stats Banner */
        .stats-banner {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            max-width: 820px;
            margin: 0 auto 30px;
        }}

        .stat-box {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            padding: 14px 10px;
            border-radius: 14px;
            text-align: center;
            transition: transform 0.2s;
        }}

        .stat-box:hover {{
            transform: translateY(-2px);
            border-color: rgba(99, 102, 241, 0.4);
        }}

        .stat-box .num {{
            font-size: clamp(18px, 4vw, 24px);
            font-weight: 900;
            color: #38bdf8;
        }}

        .stat-box.highlight-box .num {{
            color: #fbbf24;
        }}

        .stat-box .label {{
            font-size: 11.5px;
            color: var(--text-secondary);
            margin-top: 3px;
        }}

        .controls {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 15px;
            margin-bottom: 30px;
        }}

        .search-input {{
            width: 100%;
            max-width: 480px;
            padding: 14px 18px;
            border-radius: 14px;
            border: 1px solid var(--border);
            background: var(--card-bg);
            color: #fff;
            font-size: 15px;
            outline: none;
            transition: all 0.3s;
        }}

        .search-input:focus {{
            border-color: var(--accent);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.25);
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }}

        .card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 20px;
            transition: all 0.25s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
        }}

        .card:hover {{
            transform: translateY(-4px);
            background: var(--card-hover);
            border-color: #3b82f6;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
        }}

        .rank-badge {{
            position: absolute;
            top: 14px;
            left: 14px;
            background: rgba(30, 41, 59, 0.9);
            color: #94a3b8;
            font-size: 12px;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 9999px;
            border: 1px solid #334155;
            direction: ltr;
        }}

        .rank-1 {{
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.25), rgba(217, 119, 6, 0.35));
            color: #fde047;
            border-color: #f59e0b;
        }}

        .rank-2 {{
            background: linear-gradient(135deg, rgba(148, 163, 184, 0.25), rgba(100, 116, 139, 0.35));
            color: #f1f5f9;
            border-color: #94a3b8;
        }}

        .rank-3 {{
            background: linear-gradient(135deg, rgba(180, 83, 9, 0.25), rgba(146, 64, 14, 0.35));
            color: #fdba74;
            border-color: #b45309;
        }}

        .card-top {{
            display: flex;
            align-items: center;
            gap: 14px;
            margin-bottom: 16px;
            padding-left: 55px;
        }}

        .avatar-wrap {{
            position: relative;
            width: 60px;
            height: 60px;
            flex-shrink: 0;
            display: block;
        }}

        .avatar {{
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid #38bdf8;
            background: #0f172a;
            transition: transform 0.2s;
        }}

        .avatar-wrap:hover .avatar {{
            transform: scale(1.05);
        }}

        .info {{
            overflow: hidden;
        }}

        .info h3 {{
            font-size: 15px;
            font-weight: 700;
            color: #f8fafc;
            line-height: 1.4;
            margin-bottom: 3px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .name-link {{
            color: #f8fafc;
            text-decoration: none;
            transition: color 0.2s;
        }}

        .name-link:hover {{
            color: #38bdf8;
        }}

        .info .handle {{
            font-size: 13px;
            color: #818cf8;
            direction: ltr;
            display: inline-block;
            font-weight: 500;
            text-decoration: none;
        }}

        .info .handle:hover {{
            text-decoration: underline;
        }}

        .metrics {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 6px;
            background: rgba(11, 15, 25, 0.6);
            padding: 10px;
            border-radius: 12px;
            margin-bottom: 16px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.04);
        }}

        .metric-item .val {{
            font-size: 14px;
            font-weight: 700;
            color: #f1f5f9;
        }}

        .metric-item .val.highlight {{
            color: #fbbf24;
            font-size: 15px;
            font-weight: 800;
        }}

        .metric-item .lbl {{
            font-size: 11px;
            color: var(--text-secondary);
            margin-top: 2px;
        }}

        .card-actions {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }}

        .btn {{
            padding: 9px 10px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            text-align: center;
            text-decoration: none;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
        }}

        .btn-detail {{
            background: #1e293b;
            color: #38bdf8;
            border: 1px solid #334155;
        }}

        .btn-detail:hover {{
            background: #334155;
            color: #fff;
            transform: scale(1.02);
        }}

        .btn-ig {{
            background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
            color: #fff;
        }}

        .btn-ig:hover {{
            opacity: 0.92;
            transform: scale(1.02);
        }}

        footer {{
            margin-top: 50px;
            text-align: center;
            padding-top: 25px;
            border-top: 1px solid var(--border);
            color: var(--text-secondary);
            font-size: 13px;
        }}

        .footer-curator {{
            color: #f8fafc;
            font-weight: 700;
        }}

        .footer-links {{
            margin-top: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 14px;
            flex-wrap: wrap;
        }}

        .footer-links a {{
            color: #94a3b8;
            text-decoration: none;
            font-size: 12.5px;
        }}

        .footer-links a:hover {{
            color: #38bdf8;
        }}

        /* Mobile Optimization */
        @media (max-width: 768px) {{
            .stats-banner {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}

        @media (max-width: 640px) {{
            body {{
                padding: 20px 12px 40px;
            }}
            .campaign-section {{
                padding: 20px 14px;
            }}
            .contact-buttons {{
                flex-direction: column;
                width: 100%;
            }}
            .contact-btn {{
                width: 100%;
                justify-content: center;
            }}
            .grid {{
                grid-template-columns: 1fr;
                gap: 14px;
            }}
            .card {{
                padding: 16px;
            }}
            .card-top {{
                gap: 12px;
                padding-left: 50px;
                margin-bottom: 12px;
            }}
            .avatar-wrap {{
                width: 52px;
                height: 52px;
            }}
            .info h3 {{
                font-size: 14px;
            }}
            .info .handle {{
                font-size: 12px;
            }}
            .metrics {{
                padding: 8px;
                margin-bottom: 12px;
            }}
            .metric-item .val {{
                font-size: 13px;
            }}
            .metric-item .lbl {{
                font-size: 10px;
            }}
            .btn {{
                padding: 8px;
                font-size: 11.5px;
            }}
            .stats-banner {{
                gap: 8px;
                grid-template-columns: repeat(2, 1fr);
            }}
            .stat-box {{
                padding: 10px 6px;
            }}
        }}
    </style>
</head>
<body>
<div class="container">
    <header>
        <div class="hero-badge">📊 مرتب‌شده بر اساس بیشترین فالوور اینستاگرام</div>
        
        <div class="nav-banners-row">
            <a href="pricing-table.html" class="banner-btn pricing-tbl">
                📊 جدول تعرفه تبلیغات ↗
            </a>
            <a href="campaign-squad.html" class="banner-btn squad-pkg">
                🚀 پکیج ویژه تبلیغ کتاب (اتحاد ۶ بوک‌بلاگر) ↗
            </a>
            <a href="{TG_GROUP_URL}" target="_blank" rel="noopener noreferrer" class="banner-btn group-tg">
                👥 گروه تلگرام (بلاگران کتاب) ↗
            </a>
            <a href="3d.html" class="banner-btn galaxy">
                🌌 کهکشان سه‌بعدی
            </a>
            <a href="top-posts.html" class="banner-btn top-posts">
                🔥 ۱۰ پست برتر
            </a>
            <a href="top-100-posts.html" class="banner-btn top-100">
                🏆 ۱۰۰ پست برتر
            </a>
        </div>

        <h1>رتبه‌بندی جامع بوک‌بلاگرهای اینستاگرام</h1>
        <p class="subtitle">مرجع رسمی دایرکتوری، آمار زنده BoxAPI، نرخ تعامل و تعرفه تبلیغات بلاگرهای برتر کتاب ایران</p>
        <div class="curator-tag">✨ گردآوری، تحلیل داده و مدیریت: <b>ریک سانچز | Rick Sanchez</b></div>
    </header>

    <!-- Campaign & PR Call to Action Section -->
    <div class="campaign-section">
        <div class="campaign-badge">🚀 اجرای کمپین و روابط عمومی کتاب</div>
        <h2 class="campaign-title">طراحی و اجرای کمپین‌های تخصصی با بوک‌بلاگرها</h2>
        <p class="campaign-desc">
            برای اجرای کمپین‌های تبلیغاتی، رونمایی و نقد کتاب، اسپانسرشیپ و همکاری هدفمند با بیش از <b>{total_foll_badge} مخاطب کتاب‌خوان</b> این لیست ({total_pages_count} پیج تخصصی)، هماهنگی و مدیریت اختصاصی کمپین‌ها را می‌توانید به <b>ریک سانچز</b> بسپارید یا در گروه تلگرامی مطرح کنید.
        </p>
        <div class="contact-buttons">
            <a href="{TG_GROUP_URL}" target="_blank" rel="noopener noreferrer" class="contact-btn contact-btn-group">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/></svg>
                گروه تلگرام: بلاگران کتاب
            </a>
            <a href="https://t.me/m4tinbeigipv" target="_blank" rel="noopener noreferrer" class="contact-btn contact-btn-tg">
                ادمین: @m4tinbeigipv
            </a>
            <a href="https://instagram.com/m4tinbeigi" target="_blank" rel="noopener noreferrer" class="contact-btn contact-btn-ig">
                اینستاگرام: @m4tinbeigi
            </a>
        </div>
    </div>

    <!-- Stats Banner -->
    <div class="stats-banner">
        <div class="stat-box highlight-box">
            <div class="num">{total_foll_badge}</div>
            <div class="label">مجموع کل فالوورها ({total_foll_str})</div>
        </div>
        <div class="stat-box">
            <div class="num">{total_pages_count}</div>
            <div class="label">تعداد کل پیج‌ها</div>
        </div>
        <div class="stat-box">
            <div class="num">{top_blogger_foll_str}</div>
            <div class="label">بیشترین فالوور پیج (<a href="blogger/{top_blogger_username.lower()}.html" style="color:#38bdf8; text-decoration:none; font-weight:700;">@{top_blogger_username}</a>)</div>
        </div>
        <div class="stat-box">
            <div class="num">{total_posts_str}</div>
            <div class="label">مجموع محتوا و پست‌ها</div>
        </div>
    </div>

    <div class="controls">
        <input type="text" id="searchInput" class="search-input" placeholder="🔍 جستجو بر اساس نام یا آیدی بلاگر...">
    </div>

    <div class="grid" id="bloggersGrid">
{all_cards}
    </div>

    <footer>
        <p>گردآوری، تحلیل داده و توسعه: <span class="footer-curator">ریک سانچز (Rick Sanchez)</span></p>
        <div class="footer-links">
            <a href="{TG_GROUP_URL}" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; font-weight:700;">👥 گروه تلگرام (بلاگران کتاب)</a>
            <span>•</span>
            <a href="3d.html">🌌 کهکشان سه‌بعدی (3D)</a>
            <span>•</span>
            <a href="top-posts.html">🔥 ۱۰ پست برتر</a>
            <span>•</span>
            <a href="top-100-posts.html">🏆 ۱۰۰ پست برتر</a>
            <span>•</span>
            <a href="sitemap.xml">نقشه سایت</a>
        </div>
    </footer>
</div>

<script>
    const searchInput = document.getElementById('searchInput');
    const cards = document.querySelectorAll('.card');

    searchInput.addEventListener('input', (e) => {{
        const query = e.target.value.toLowerCase().trim();
        cards.forEach(card => {{
            const text = card.getAttribute('data-name').toLowerCase();
            if (text.includes(query)) {{
                card.style.display = 'flex';
            }} else {{
                card.style.display = 'none';
            }}
        }});
    }});
</script>
</body>
</html>
"""

with open(os.path.join(REPO_DIR, "index.html"), 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Updated index.html with direct telegram group link t.me/bookblogersiran!")
