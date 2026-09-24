import json
import os
import re

SITE_URL = "https://bookbloger.github.io"
TG_GROUP_URL = "https://t.me/+tReSYWxBreFmYThk"
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_HTML = os.path.join(REPO_DIR, "pricing-table.html")
GOOGLE_META = '<meta name="google-site-verification" content="1bSuT-QoDy7ukGYtf0DVP8jBzHzIhxEqGPHMJVxjD94" />'

# Specific explicit verified pricing database
EXPLICIT_RATES = {
    'aqaye.ketab': {
        'story': 'استعلام اختصاصی',
        'reels': 'استعلام اختصاصی',
        'package': 'هماهنگی کمپین کلان',
        'verified': False,
        'note': 'بزرگ‌ترین پیج کتاب ایران (۵۵۸K فالوور)'
    },
    'saraybook': {
        'story': 'استعلام اختصاصی',
        'reels': 'استعلام اختصاصی',
        'package': 'هماهنگی کمپین کلان',
        'verified': False,
        'note': '۳۳۹K فالوور'
    },
    'datoverse': {
        'story': '۵,۹۰۰,۰۰۰ تومان',
        'reels': '۴۵,۰۰۰,۰۰۰ تومان',
        'package': '۶۹,۰۰۰,۰۰۰ تومان (۳ ماهه)',
        'verified': True,
        'note': 'پکیج‌های اسپانسری و کمپین‌های ۳ ماهه'
    },
    'mohammadzaabihi': {
        'story': 'استعلام اختصاصی',
        'reels': 'استعلام اختصاصی',
        'package': 'هماهنگی کمپین',
        'verified': False,
        'note': '۲۲۶K فالوور'
    },
    'pragma_book': {
        'story': 'استعلام اختصاصی',
        'reels': 'استعلام اختصاصی',
        'package': 'هماهنگی کمپین',
        'verified': False,
        'note': '۲۱۶K فالوور'
    },
    'narges.book': {
        'story': 'استعلام اختصاصی',
        'reels': 'استعلام اختصاصی',
        'package': 'هماهنگی کمپین',
        'verified': False,
        'note': '۱۴۱K فالوور'
    },
    'rendtopia': {
        'story': '۱.۲ تا ۲.۲ میلیون',
        'reels': '۷,۵۰۰,۰۰۰ تومان',
        'package': '۷,۵۰۰,۰۰۰ تومان (پست+استوری+تلگرام)',
        'verified': True,
        'note': '۱۰۱K فالوور، تفکر نقاد و معرفی با چهره'
    },
    'baharthebookreviewer': {
        'story': '۱.۵ تا ۲.۵ میلیون',
        'reels': '۱۱,۰۰۰,۰۰۰ تومان',
        'package': '۱۳,۵۰۰,۰۰۰ تومان (ریلز+شورتس+استوری)',
        'verified': True,
        'note': '۸۳K فالوور، نقد آکادمیک و پوشش یوتیوب'
    },
    'acal.madahi': {
        'story': '۸۰۰ ت تا ۱.۵ میلیون',
        'reels': '۶,۰۰۰,۰۰۰ تومان',
        'package': '۸,۰۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۶۶K فالوور، تعامل اکسپلور'
    },
    'book_spook': {
        'story': '۸۰۰ ت تا ۱.۵ میلیون',
        'reels': '۵,۵۰۰,۰۰۰ تومان',
        'package': '۷,۵۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۶۴K فالوور'
    },
    'parham.hami': {
        'story': '۷۰۰ ت تا ۱.۴ میلیون',
        'reels': '۵,۰۰۰,۰۰۰ تومان',
        'package': '۷,۰۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۶۱K فالوور، ادبیات و هنر'
    },
    'maryamaamalii': {
        'story': '۷۰۰ ت تا ۱.۴ میلیون',
        'reels': '۵,۰۰۰,۰۰۰ تومان',
        'package': '۷,۰۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۵۰K فالوور، معرفی کتاب با حس و حال'
    },
    'roxanaabasian': {
        'story': '۱,۵۰۰,۰۰۰ تومان',
        'reels': '۹ تا ۱۴ میلیون',
        'package': '۲۴,۰۰۰,۰۰۰ تومان (پکیج طلایی)',
        'verified': True,
        'note': '۴۸K فالوور، پرستیژ و کامیونیتی فعال کتابخوانی'
    },
    'sarabooks.ir': {
        'story': '۵۱۰ ت تا ۲.۳ میلیون',
        'reels': '۳.۷۵ تا ۶.۶ میلیون',
        'package': '۸,۱۰۰,۰۰۰ تومان (پکیج VIP)',
        'verified': True,
        'note': '۴۳K فالوور، پکیج‌های مجزای کتاب، شاپ و بلاگری'
    },
    'misaghsdiary': {
        'story': '۶۰۰ ت تا ۱.۲ میلیون',
        'reels': '۴,۰۰۰,۰۰۰ تومان',
        'package': '۵,۵۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۳۴K فالوور'
    },
    'tootfarangi._.book': {
        'story': '۹۹۰,۰۰۰ تومان',
        'reels': '۳,۵۰۰,۰۰۰ تومان',
        'package': '۴,۹۰۰,۰۰۰ تومان (پکیج جامع)',
        'verified': True,
        'note': '۲۹K فالوور، ریلزهای جذاب و فضاسازی'
    },
    'artemisbook': {
        'story': '۶۰۰ ت تا ۱.۸ میلیون',
        'reels': '۴,۲۰۰,۰۰۰ تومان',
        'package': '۵,۸۰۰,۰۰۰ تومان (پکیج پرمیوم)',
        'verified': True,
        'note': '۲۸.۵K فالوور، ویوهای میلیونی اکسپلور'
    },
    'dreems_book': {
        'story': '۴۵۰ تا ۸۹۰ هزار تومان',
        'reels': '۱.۱ تا ۱.۵ میلیون',
        'package': '۲,۹۰۰,۰۰۰ تومان (پکیج پیشنهادی)',
        'verified': True,
        'note': '۲۱K فالوور، ۳ تا ۴.۵K ویو استوری'
    },
    'storyteller.shahrzad': {
        'story': '۵۰۰ ت تا ۱ میلیون',
        'reels': '۲,۸۰۰,۰۰۰ تومان',
        'package': '۳,۸۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۲۱K فالوور، داستان‌سرایی و معرفی رمان'
    },
    'asma_vibe': {
        'story': '۶۰۰ ت تا ۱.۸ میلیون',
        'reels': '۳,۲۰۰,۰۰۰ تومان',
        'package': '۴,۶۰۰,۰۰۰ تومان (پکیج طلایی)',
        'verified': True,
        'note': '۱۷.۸K فالوور، امتیاز EQS ۱۰۰ از ۱۰۰'
    },
    'saghaaal': {
        'story': '۶۰۰ ت تا ۱.۲ میلیون',
        'reels': '۲,۵۰۰,۰۰۰ تومان',
        'package': '۴,۰۰۰,۰۰۰ تومان (اینستا+یوتیوب)',
        'verified': True,
        'note': '۱۷K فالوور، میانگین ۲۱۸K ویو ریلز (ارزان‌ترین CPV)'
    },
    'raha_farbodrad': {
        'story': '۶۰۰ ت تا ۱.۸ میلیون',
        'reels': '۳,۲۰۰,۰۰۰ تومان',
        'package': '۴,۶۰۰,۰۰۰ تومان (پکیج طلایی)',
        'verified': True,
        'note': '۱۶.۵K فالوور، ادبیات داستانی + کانال تلگرام'
    },
    'book_zarii': {
        'story': '۵۰۰ ت تا ۱ میلیون',
        'reels': '۲,۴۰۰,۰۰۰ تومان',
        'package': '۳,۵۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۱۶K فالوور'
    },
    'sabasamaadi': {
        'story': '۱,۲۰۰,۰۰۰ تومان',
        'reels': '۲,۴۰۰,۰۰۰ تومان',
        'package': '۳,۰۰۰,۰۰۰ تومان (پکیج طلایی)',
        'verified': True,
        'note': '۱۶K فالوور، میانگین ۱۰۹K ویو ریلز و ۷.۶K لایک'
    },
    'nooshinaseri': {
        'story': '۸۰۰ ت تا ۲ میلیون',
        'reels': '۷,۰۰۰,۰۰۰ تومان',
        'package': '۹,۰۰۰,۰۰۰ تومان (ریلز+استوری)',
        'verified': True,
        'note': '۱۴K فالوور، موتور وایرال اکسپلور و فانتزی'
    },
    'donyaahayati': {
        'story': '۶۰۰ ت تا ۱.۲ میلیون',
        'reels': '۲,۲۰۰,۰۰۰ تومان',
        'package': '۳,۰۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۱۳.۳K فالوور، رمان و روزمرگی کتابخوانی'
    },
    'mahi_bookworld': {
        'story': '۵۰۰ ت تا ۱ میلیون',
        'reels': '۲,۰۰۰,۰۰۰ تومان',
        'package': '۲,۸۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۱۱.۸K فالوور'
    },
    'bookish_melika': {
        'story': '۵۰۰ تا ۹۰۰ هزار تومان',
        'reels': '۱,۸۰۰,۰۰۰ تومان',
        'package': '۲,۵۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۱۰K فالوور'
    },
    'ziiboox': {
        'story': '۹۹۰,۰۰۰ تومان',
        'reels': '۱,۲۰۰,۰۰۰ تومان',
        'package': '۱,۵۰۰,۰۰۰ تومان (پکیج ۳۶۰ درجه)',
        'verified': True,
        'note': '۹.۵K فالوور، آنباکس و تولید محتوای تخصصی'
    },
    'kiana_am': {
        'story': '۴۰۰ تا ۶۰۰ هزار تومان',
        'reels': '۶۰۰ تا ۹۰۰ هزار تومان',
        'package': '۶۰۰ تا ۹۰۰ هزار تومان (اینستا+یوتیوب+به‌خوان)',
        'verified': True,
        'note': '۸.۸K فالوور، بر اساس حجم صفحات کتاب'
    },
    'booksbahar': {
        'story': '۴۰۰ ت تا ۱ میلیون',
        'reels': '۲,۰۰۰,۰۰۰ تومان',
        'package': '۳,۰۰۰,۰۰۰ تومان (پکیج ویژه)',
        'verified': True,
        'note': '۸.۵K فالوور، تعهد مطالعه کامل اثر'
    },
    'negarankarimi': {
        'story': '۵۰۰ ت تا ۱ میلیون',
        'reels': '۱,۸۰۰,۰۰۰ تومان',
        'package': '۲,۵۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۸.۳K فالوور'
    },
    'lilith.in.wonderland': {
        'story': '۴۰۰ تا ۷۰۰ هزار تومان',
        'reels': '۱,۵۰۰,۰۰۰ تومان',
        'package': '۲,۲۰۰,۰۰۰ تومان',
        'verified': True,
        'note': '۷.۴K فالوور، فانتزی و ماجراجویی'
    },
    '_cherryremi': {
        'story': '۵۰۰ تا ۹۰۰ هزار تومان',
        'reels': '۲,۰۰۰,۰۰۰ تومان',
        'package': '۲,۸۰۰,۰۰۰ تومان',
        'verified': True,
        'note': '۷.۲K فالوور، هویت بصری لوکس و مینیمال'
    },
    'ke_mesle_ketab': {
        'story': '۵۰۰ ت تا ۱.۴ میلیون',
        'reels': '۲,۴۰۰,۰۰۰ تومان',
        'package': '۳,۶۰۰,۰۰۰ تومان (پکیج طلایی)',
        'verified': True,
        'note': '۷.۱K فالوور، تعامل صمیمی و معرفی کتاب'
    },
    'ayazreviews': {
        'story': '۴۰۰ تا ۷۰۰ هزار تومان',
        'reels': '۱,۴۰۰,۰۰۰ تومان',
        'package': '۲,۰۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۴.۹K فالوور، پاپ‌کالچر و کمیک'
    },
    'ketabkhan.koochak': {
        'story': '۴۰۰ تا ۷۰۰ هزار تومان',
        'reels': '۱,۳۰۰,۰۰۰ تومان',
        'package': '۱,۸۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۴.۸K فالوور'
    },
    'artadall': {
        'story': '۴۰۰ تا ۷۰۰ هزار تومان',
        'reels': '۱,۳۰۰,۰۰۰ تومان',
        'package': '۱,۸۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۴.۸K فالوور'
    },
    'mozhdeh_booklover': {
        'story': '۳۵۰ تا ۶۵۰ هزار تومان',
        'reels': '۱,۲۰۰,۰۰۰ تومان',
        'package': '۱,۷۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۴.۵K فالوور'
    },
    'coralism': {
        'story': '۳۵۰ تا ۶۵۰ هزار تومان',
        'reels': '۱,۲۰۰,۰۰۰ تومان',
        'package': '۱,۷۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۴.۲K فالوور'
    },
    'negin_books': {
        'story': '۳۵۰ تا ۶۵۰ هزار تومان',
        'reels': '۱,۲۰۰,۰۰۰ تومان',
        'package': '۱,۷۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۴.۱K فالوور'
    },
    'pariaareads': {
        'story': '۳۵۰ تا ۶۰۰ هزار تومان',
        'reels': '۱,۱۰۰,۰۰۰ تومان',
        'package': '۱,۶۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۳.۸K فالوور'
    },
    'ryhn_books': {
        'story': '۳۵۰ تا ۶۰۰ هزار تومان',
        'reels': '۱,۱۰۰,۰۰۰ تومان',
        'package': '۱,۶۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۳.۸K فالوور'
    },
    'ketab_jaann': {
        'story': '۳۵۰ تا ۶۰۰ هزار تومان',
        'reels': '۱,۱۰۰,۰۰۰ تومان',
        'package': '۱,۶۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۳.۵K فالوور'
    },
    'fa_bookworm': {
        'story': '۳۵۰ تا ۶۰۰ هزار تومان',
        'reels': '۱,۱۰۰,۰۰۰ تومان',
        'package': '۱,۶۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۳.۴K فالوور'
    },
    'maral__book': {
        'story': '۵۰۰ تا ۷۵۰ هزار تومان',
        'reels': '۱,۲۰۰,۰۰۰ تا ۱,۸۰۰,۰۰۰ تومان',
        'package': '۲,۲۰۰,۰۰۰ تا ۲,۸۰۰,۰۰۰ تومان',
        'verified': True,
        'note': '۳.۱K فالوور، ۶.۱٪ تعامل و معرفی داستانی'
    },
    'imnon.aa': {
        'story': '۳۵۰ تا ۸۵۰ هزار تومان',
        'reels': '۱.۵ تا ۱.۸ میلیون',
        'package': '۲,۵۰۰,۰۰۰ تومان',
        'verified': True,
        'note': '۲.۷K فالوور، میانگین ۷۳K ویو ریلز اکسپلور'
    },
    'saman.reads': {
        'story': '۵۰۰ ت تا ۱.۴ میلیون',
        'reels': '۲,۵۰۰,۰۰۰ تومان',
        'package': '۳,۸۰۰,۰۰۰ تومان (پکیج طلایی)',
        'verified': True,
        'note': '۲.۳K فالوور، میانگین ۵۲K ویو ریلز اکسپلور'
    },
    'zahrabook_': {
        'story': '۳۰۰ تا ۵۰۰ هزار تومان',
        'reels': '۹۰۰,۰۰۰ تومان',
        'package': '۱,۴۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۱.۶K فالوور'
    },
    'totfarangii_ketab': {
        'story': '۳۰۰ تا ۵۰۰ هزار تومان',
        'reels': '۹۰۰,۰۰۰ تومان',
        'package': '۱,۴۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۱.۵K فالوور'
    },
    'about_dokhtarjan': {
        'story': '۵۰۰ ت تا ۱.۲ میلیون',
        'reels': '۱,۸۰۰,۰۰۰ تومان',
        'package': '۲,۸۰۰,۰۰۰ تومان (پکیج طلایی)',
        'verified': True,
        'note': '۱.۴K فالوور، معرفی صمیمانه کتاب'
    },
    'greenverse.book': {
        'story': '۵۰۰ ت تا ۱.۴ میلیون',
        'reels': '۲,۲۰۰,۰۰۰ تومان',
        'package': '۳,۴۰۰,۰۰۰ تومان (پکیج طلایی)',
        'verified': True,
        'note': '۱.۴K فالوور، میانگین ۱۵.۷K ویو ریلز'
    },
    'joi_boy_art': {
        'story': '۳۵۰,۰۰۰ تومان',
        'reels': '۱,۵۰۰,۰۰۰ تومان',
        'package': '۲,۰۰۰,۰۰۰ تومان (اینستا+یوتیوب)',
        'verified': True,
        'note': '۶۵۰ فالوور، تحلیل عمیق ویدیویی یوتیوب'
    },
    'parnianbook0': {
        'story': '۲۵۰ تا ۴۵۰ هزار تومان',
        'reels': '۷۰۰,۰۰۰ تومان',
        'package': '۱,۰۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۴۴۲ فالوور'
    },
    'negin_book': {
        'story': '۲۰۰,۰۰۰ تومان',
        'reels': '۵۰۰,۰۰۰ تومان',
        'package': '۸۰۰,۰۰۰ تومان',
        'verified': False,
        'note': '۱۳۱ فالوور'
    }
}

def parse_num(val):
    if not val or val == '-': return 0
    clean = str(val).strip().replace(',', '')
    if 'k' in clean.lower(): return float(clean.lower().replace('k','')) * 1000
    if 'm' in clean.lower(): return float(clean.lower().replace('m','')) * 1000000
    try: return float(clean)
    except: return 0

def build_pricing_table():
    with open(os.path.join(REPO_DIR, "instagram_book_bloggers_analytics_rich.json"), 'r', encoding='utf-8') as f:
        bloggers = json.load(f)

    with open(os.path.join(REPO_DIR, "all_users_posts_map.json"), 'r', encoding='utf-8') as f:
        posts_map = json.load(f)

    hidden = {'mina.bookk', 'sinmoruk', 'ketabiyaaa'}
    visible = [b for b in bloggers if b['username'].lower() not in hidden]
    
    # Sort descending by followers
    sorted_bloggers = sorted(visible, key=lambda x: parse_num(x.get('followers')), reverse=True)
    
    rows_html = []
    
    for rank, b in enumerate(sorted_bloggers, 1):
        u = b['username']
        slug = u.lower()
        name = b.get('display_name', u).split('|')[0].strip()
        foll = b.get('followers', '-')
        avatar = b.get('local_avatar', f'avatars/{u}.jpg')
        tier = b.get('influencer_tier', 'بوک‌بلاگر')
        
        # Calculate average views from posts_map
        posts = posts_map.get(u, [])
        plays = [p.get('plays', 0) for p in posts if p.get('plays', 0) > 0]
        if plays:
            avg_plays_str = f"{int(sum(plays)/len(plays)):,} ویو"
        else:
            avg_plays_str = b.get('est_reel_view', '—')
            
        rate_info = EXPLICIT_RATES.get(slug, {
            'story': '۵۰۰ تا ۸۰۰ هزار تومان',
            'reels': '۱.۵ تا ۲.۵ میلیون',
            'package': '۲.۵ تا ۳.۵ میلیون',
            'verified': False,
            'note': 'نرخ پیشنهادی استاندارد'
        })
        
        story_price = rate_info['story']
        reels_price = rate_info['reels']
        pkg_price = rate_info['package']
        is_verified = rate_info.get('verified', False)
        
        badge_status = '<span class="badge verified">✓ تایید رسمی</span>' if is_verified else '<span class="badge estimated">برآورد عادلانه</span>'
        
        row = f"""
        <tr data-username="{u.lower()}" data-name="{name.lower()}" data-foll="{parse_num(foll)}">
            <td class="col-rank">{rank}</td>
            <td class="col-blogger">
                <div class="blogger-info-box">
                    <img src="{avatar}" alt="{name}" class="table-avatar" onerror="this.src='https://ui-avatars.com/api/?name={u}&background=random'">
                    <div>
                        <a href="blogger/{slug}.html" class="blogger-name-link">{name}</a>
                        <div class="blogger-handle">@{u}</div>
                    </div>
                </div>
            </td>
            <td class="col-foll"><span class="foll-pill">{foll}</span></td>
            <td class="col-views"><span class="view-txt">{avg_plays_str}</span></td>
            <td class="col-price story-price">{story_price}</td>
            <td class="col-price reels-price"><b>{reels_price}</b></td>
            <td class="col-price pkg-price"><span class="pkg-pill">{pkg_price}</span></td>
            <td class="col-status">{badge_status}</td>
            <td class="col-action">
                <a href="blogger/{slug}.html" class="btn-table-view">صفحه ↗</a>
                <a href="https://t.me/m4tinbeigipv?text=درخواست_استعلام_تعرفه_{u}" target="_blank" rel="noopener noreferrer" class="btn-table-tg" title="رزرو و هماهنگی">رزرو</a>
            </td>
        </tr>
        """
        rows_html.append(row)
        
    table_body = "\n".join(rows_html)
    
    html = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    {GOOGLE_META}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>جدول تعرفه تبلیغات بوک‌بلاگرهای اینستاگرام | قیمت استوری، ریلز و پکیج‌ها | BookBloger</title>
    <meta name="description" content="جدول مقایسه‌ای و کامل تعرفه تبلیغات ۵۲ بوک‌بلاگر برتر ایران. قیمت به‌روز و منصفانه استوری، ریلز فید و پکیج‌های اختصاصی معرفی کتاب همراه با میانگین ویو واقعی.">
    <meta name="keywords" content="تعرفه تبلیغات بوک بلاگرها, قیمت استوری معرفی کتاب, هزینه ریلز کتاب, تبلیغ کتاب در اینستاگرام, تعرفه بلاگر کتاب, نرخ تبلیغات نشر, BookBloger">
    <link rel="canonical" href="{SITE_URL}/pricing-table.html">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">

    <!-- OpenGraph Meta Tags -->
    <meta property="og:locale" content="fa_IR">
    <meta property="og:type" content="website">
    <meta property="og:title" content="جدول جامع و شفاف تعرفه تبلیغات بوک‌بلاگرهای ایران | BookBloger">
    <meta property="og:description" content="مشاهده و مقایسه یکجای قیمت استوری، ریلز و پکیج‌های معرفی کتاب در پیج‌های برتر ادبیات.">
    <meta property="og:url" content="{SITE_URL}/pricing-table.html">
    <meta property="og:site_name" content="BookBloger">
    <meta property="og:image" content="{SITE_URL}/story_poster.png">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="جدول تعرفه تبلیغات بوک‌بلاگرها | BookBloger">
    <meta name="twitter:description" content="لیست رسمی قیمت تبلیغات استوری و ریلز برای ناشران و نویسندگان.">
    <meta name="twitter:image" content="{SITE_URL}/story_poster.png">

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
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --border: #23304e;
            --gold: #f59e0b;
            --green: #10b981;
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
            padding: 25px 16px 60px;
        }}

        .container {{
            max-width: 1350px;
            margin: 0 auto;
        }}

        /* Navigation */
        .nav-back {{
            margin-bottom: 25px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }}

        .nav-pill {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: #818cf8;
            text-decoration: none;
            font-size: 13.5px;
            font-weight: 700;
            background: var(--card-bg);
            border: 1px solid var(--border);
            padding: 8px 16px;
            border-radius: 12px;
            transition: all 0.2s;
        }}

        .nav-pill:hover {{
            background: #1e293b;
            color: #fff;
            transform: translateY(-2px);
        }}

        .top-links {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        /* Header */
        header {{
            text-align: center;
            margin-bottom: 30px;
        }}

        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(99, 102, 241, 0.18);
            color: #818cf8;
            border: 1px solid rgba(99, 102, 241, 0.4);
            padding: 6px 20px;
            border-radius: 9999px;
            font-size: 13.5px;
            font-weight: 800;
            margin-bottom: 14px;
        }}

        h1 {{
            font-size: clamp(24px, 4.5vw, 38px);
            font-weight: 900;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
            line-height: 1.3;
        }}

        p.subtitle {{
            color: var(--text-secondary);
            font-size: clamp(14px, 3.2vw, 16px);
            max-width: 820px;
            margin: 0 auto 20px;
            line-height: 1.7;
        }}

        /* Filter & Controls */
        .controls-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 16px 20px;
            margin-bottom: 25px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
        }}

        .search-box {{
            flex: 1;
            min-width: 260px;
            position: relative;
        }}

        .search-input {{
            width: 100%;
            background: #0f172a;
            border: 1.5px solid var(--border);
            color: #fff;
            padding: 10px 16px 10px 38px;
            border-radius: 12px;
            font-size: 14px;
            outline: none;
            transition: all 0.2s;
        }}

        .search-input:focus {{
            border-color: #6366f1;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.25);
        }}

        .search-icon {{
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: #64748b;
            pointer-events: none;
        }}

        .filter-tags {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .filter-btn {{
            background: #1e293b;
            color: #94a3b8;
            border: 1px solid #334155;
            padding: 7px 14px;
            border-radius: 10px;
            font-size: 12.5px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .filter-btn.active, .filter-btn:hover {{
            background: #6366f1;
            color: #fff;
            border-color: #6366f1;
        }}

        .stats-counter {{
            font-size: 13px;
            color: #94a3b8;
            font-weight: 600;
        }}

        /* Table Wrapper */
        .table-responsive {{
            width: 100%;
            overflow-x: auto;
            background: var(--card-bg);
            border: 1.5px solid var(--border);
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
            margin-bottom: 35px;
            -webkit-overflow-scrolling: touch;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: right;
            font-size: 13.5px;
            white-space: nowrap;
        }}

        thead tr {{
            background: rgba(15, 23, 42, 0.85);
            border-bottom: 2px solid var(--border);
        }}

        th {{
            padding: 15px 14px;
            font-weight: 800;
            color: #cbd5e1;
            font-size: 13px;
            user-select: none;
        }}

        tbody tr {{
            border-bottom: 1px solid rgba(35, 48, 78, 0.6);
            transition: background 0.15s ease;
        }}

        tbody tr:hover {{
            background: rgba(30, 41, 59, 0.7);
        }}

        td {{
            padding: 13px 14px;
            vertical-align: middle;
        }}

        /* Columns styling */
        .col-rank {{
            text-align: center;
            font-weight: 900;
            color: #64748b;
            width: 45px;
        }}

        .blogger-info-box {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .table-avatar {{
            width: 38px;
            height: 38px;
            border-radius: 50%;
            object-fit: cover;
            border: 1.5px solid #38bdf8;
            background: #0f172a;
            flex-shrink: 0;
        }}

        .blogger-name-link {{
            color: #ffffff;
            font-weight: 800;
            text-decoration: none;
            display: block;
            line-height: 1.3;
        }}

        .blogger-name-link:hover {{
            color: #38bdf8;
        }}

        .blogger-handle {{
            font-size: 11.5px;
            color: #818cf8;
            direction: ltr;
            text-align: right;
            font-weight: 600;
        }}

        .foll-pill {{
            display: inline-block;
            background: rgba(99, 102, 241, 0.15);
            color: #a5b4fc;
            border: 1px solid rgba(99, 102, 241, 0.3);
            padding: 3px 10px;
            border-radius: 8px;
            font-weight: 800;
            font-size: 13px;
        }}

        .view-txt {{
            color: #cbd5e1;
            font-size: 12.5px;
            font-weight: 600;
        }}

        .col-price {{
            font-size: 13.5px;
        }}

        .story-price {{
            color: #38bdf8;
            font-weight: 600;
        }}

        .reels-price b {{
            color: #fbbf24;
            font-weight: 900;
        }}

        .pkg-pill {{
            display: inline-block;
            background: rgba(16, 185, 129, 0.12);
            border: 1px solid rgba(16, 185, 129, 0.3);
            color: #34d399;
            padding: 3px 10px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 12px;
        }}

        .badge {{
            display: inline-block;
            font-size: 11px;
            font-weight: 800;
            padding: 2px 8px;
            border-radius: 999px;
            white-space: nowrap;
        }}

        .badge.verified {{
            background: rgba(16, 185, 129, 0.2);
            color: #4ade80;
            border: 1px solid rgba(16, 185, 129, 0.4);
        }}

        .badge.estimated {{
            background: rgba(148, 163, 184, 0.12);
            color: #94a3b8;
            border: 1px solid rgba(148, 163, 184, 0.25);
        }}

        .col-action {{
            text-align: center;
        }}

        .btn-table-view {{
            display: inline-block;
            background: #1e293b;
            color: #38bdf8;
            border: 1px solid #334155;
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            text-decoration: none;
            margin-left: 5px;
            transition: all 0.2s;
        }}

        .btn-table-view:hover {{
            background: #334155;
            color: #fff;
        }}

        .btn-table-tg {{
            display: inline-block;
            background: #229ED9;
            color: #fff;
            padding: 4px 11px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.2s;
        }}

        .btn-table-tg:hover {{
            background: #1b86b8;
        }}

        /* Notes Card */
        .notes-card {{
            background: linear-gradient(135deg, #1e1b4b 0%, #172554 100%);
            border: 1.5px solid rgba(99, 102, 241, 0.4);
            border-radius: 18px;
            padding: 22px 25px;
            margin-bottom: 35px;
        }}

        .notes-card h3 {{
            color: #38bdf8;
            font-size: 16px;
            font-weight: 900;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .notes-card p {{
            color: #cbd5e1;
            font-size: 13.5px;
            line-height: 1.8;
        }}

        footer {{
            margin-top: 40px;
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid var(--border);
            color: var(--text-secondary);
            font-size: 13px;
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
    </style>
</head>
<body>
<div class="container">
    <div class="nav-back">
        <a href="index.html" class="nav-pill">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            دایرکتوری اصلی
        </a>
        <div class="top-links">
            <a href="campaign-squad.html" class="nav-pill" style="color:#f472b6; border-color:#ec4899;">🚀 پکیج کمپین ۶ نفره</a>
            <a href="{TG_GROUP_URL}" target="_blank" rel="noopener noreferrer" class="nav-pill" style="color:#38bdf8; border-color:#229ED9;">👥 گروه تلگرام</a>
            <a href="3d.html" class="nav-pill">🌌 کهکشان سه‌بعدی</a>
            <a href="top-posts.html" class="nav-pill">🔥 ۱۰ پست برتر</a>
            <a href="top-100-posts.html" class="nav-pill">🏆 ۱۰۰ پست برتر</a>
        </div>
    </div>

    <header>
        <div class="hero-badge">📊 مرجع رسمی و مقایسه‌ای تعرفه‌های تبلیغات کتاب</div>
        <h1>جدول جامع تعرفه تبلیغات بوک‌بلاگرهای اینستاگرام</h1>
        <p class="subtitle">فهرست شفاف، مرتب و تفکیک‌شده هزینه‌های استوری، ریلز فید و پکیج‌های اختصاصی معرفی کتاب برای ناشران، مترجمان و نویسندگان مستقل</p>
    </header>

    <!-- Controls -->
    <div class="controls-card">
        <div class="search-box">
            <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <input type="text" id="tableSearchInput" class="search-input" placeholder="🔍 جستجوی نام، آیدی اینستاگرام یا قیمت...">
        </div>

        <div class="filter-tags">
            <button class="filter-btn active" data-filter="all">همه پیج‌ها ({len(sorted_bloggers)})</button>
            <button class="filter-btn" data-filter="verified">✓ نرخ‌های رسمی اعلام‌شده</button>
            <button class="filter-btn" data-filter="macro">پیج‌های بالای ۳۰K</button>
            <button class="filter-btn" data-filter="micro">پیج‌های زیر ۳۰K</button>
        </div>

        <div class="stats-counter" id="visibleCounter">
            نمایش {len(sorted_bloggers)} از {len(sorted_bloggers)} بلاگر
        </div>
    </div>

    <!-- Table -->
    <div class="table-responsive">
        <table id="pricingTable">
            <thead>
                <tr>
                    <th class="col-rank">#</th>
                    <th>بوک‌بلاگر</th>
                    <th>فالوور</th>
                    <th>میانگین ویو ریلز</th>
                    <th>تعرفه استوری (۲۴h)</th>
                    <th>تعرفه ریلز / پست فید</th>
                    <th>پکیج جامع / VIP</th>
                    <th>وضعیت</th>
                    <th style="text-align:center;">عملیات</th>
                </tr>
            </thead>
            <tbody>
{table_body}
            </tbody>
        </table>
    </div>

    <!-- Important Notes -->
    <div class="notes-card">
        <h3>💡 راهنمای انتخاب و سفارش کمپین</h3>
        <p>
            • <b>صداقت در نقد و مطالعه کامل:</b> تمامی بوک‌بلاگرهای عضو گروه متعهد به مطالعه دقیق اثر پیش از معرفی هستند؛ زمان آماده‌سازی بین ۷ الی ۲۵ روز کاری است.<br>
            • <b>هماهنگی یکپارچه کمپین‌ها:</b> برای رزرو کمپین‌های چند نفره، رونمایی کتاب و تخفیف‌های ویژه پکیجی، مدیریت اجرا و گزارش‌گیری بازدهی را به <b>ریک سانچز</b> بسپارید.
        </p>
    </div>

    <footer>
        <p>گردآوری، تحلیل داده و مدیریت دایرکتوری: <b>ریک سانچز (Rick Sanchez)</b> | مرجع بوک‌بلاگرهای ایران</p>
        <div class="footer-links">
            <a href="{TG_GROUP_URL}" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; font-weight:700;">👥 گروه تلگرام (بلاگران کتاب)</a>
            <span>•</span>
            <a href="pricing-table.html" style="color:#fbbf24; font-weight:700;">📊 جدول تعرفه‌ها</a>
            <span>•</span>
            <a href="campaign-squad.html" style="color:#f472b6; font-weight:700;">🚀 پکیج کمپین ۶ نفره</a>
            <span>•</span>
            <a href="3d.html">🌌 کهکشان سه‌بعدی</a>
            <span>•</span>
            <a href="top-posts.html">🔥 ۱۰ پست برتر</a>
            <span>•</span>
            <a href="sitemap.xml">نقشه سایت</a>
        </div>
    </footer>
</div>

<script>
    const searchInput = document.getElementById('tableSearchInput');
    const tableBody = document.querySelector('#pricingTable tbody');
    const rows = Array.from(tableBody.querySelectorAll('tr'));
    const counter = document.getElementById('visibleCounter');
    const filterBtns = document.querySelectorAll('.filter-btn');

    let currentFilter = 'all';

    function filterTable() {{
        const q = searchInput.value.trim().toLowerCase();
        let visibleCount = 0;

        rows.forEach(r => {{
            const u = r.getAttribute('data-username') || '';
            const n = r.getAttribute('data-name') || '';
            const textContent = r.textContent.toLowerCase();
            const foll = parseFloat(r.getAttribute('data-foll')) || 0;
            const isVerified = r.querySelector('.badge.verified') !== null;

            let matchesFilter = true;
            if (currentFilter === 'verified' && !isVerified) matchesFilter = false;
            if (currentFilter === 'macro' && foll < 30000) matchesFilter = false;
            if (currentFilter === 'micro' && foll >= 30000) matchesFilter = false;

            const matchesQuery = !q || textContent.includes(q) || u.includes(q) || n.includes(q);

            if (matchesFilter && matchesQuery) {{
                r.style.display = '';
                visibleCount++;
            }} else {{
                r.style.display = 'none';
            }}
        }});

        counter.textContent = `نمایش ${{visibleCount}} از ${{rows.length}} بلاگر`;
    }}

    searchInput.addEventListener('input', filterTable);

    filterBtns.forEach(btn => {{
        btn.addEventListener('click', () => {{
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentFilter = btn.getAttribute('data-filter');
            filterTable();
        }});
    }});
</script>
</body>
</html>
"""

    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Generated {OUTPUT_HTML} successfully with {len(sorted_bloggers)} bloggers!")

if __name__ == "__main__":
    build_pricing_table()
