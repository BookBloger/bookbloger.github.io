import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(REPO_DIR, 'blogger')
os.makedirs(PAGES_DIR, exist_ok=True)
SITE_URL = "https://bookbloger.github.io"
TG_GROUP_URL = "https://t.me/+tReSYWxBreFmYThk"
GOOGLE_META = '<meta name="google-site-verification" content="1bSuT-QoDy7ukGYtf0DVP8jBzHzIhxEqGPHMJVxjD94" />'

with open(os.path.join(REPO_DIR, "all_users_posts_map.json"), 'r', encoding='utf-8') as f:
    posts_by_user = json.load(f)

with open(os.path.join(REPO_DIR, "instagram_book_bloggers_analytics_rich.json"), 'r', encoding='utf-8') as f:
    bloggers_rich = json.load(f)

pricing_dict = {
    '_cherryremi': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها و تعرفه‌های پیشنهادی گیلاس خانم (Cherry Remi)</h3>
            <h3 style="margin-top: 15px;">📱 تعرفه تبلیغات استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>تک‌استوری معرفی / اد استوری:</span> <b>۵۰۰,۰۰۰ تومان</b></li>
                <li><span>دو استوری متوالی (معرفی اثر + لینک خرید):</span> <b>۹۰۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری اختصاصی و روایی:</span> <b>۱,۴۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🎬 تعرفه ریلز و پست فید (دائمی)</h3>
            <ul class="pricing-list">
                <li><span>ریلز ویدیویی با هویت بصری لوکس و مینیمال:</span> <b>۲,۰۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">📦 پکیج‌های پیشنهادی همکاری</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج طلایی (ریلز اختصاصی + ۲ استوری معرفی)</span>
                    <span class="pkg-price">۲,۸۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: تولید و انتشار ریلز اختصاصی فید با هویت مینیمال به همراه ۲ استوری حمایتی و لینک خرید.</p>
            </div>
        </div>
    """,
    'maral__book': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها و تعرفه‌های پیشنهادی مارال (Maral Book)</h3>
            <h3 style="margin-top: 15px;">📱 تعرفه تبلیغات استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>تک‌استوری بنری / اد استوری (Add to Story):</span> <b>۵۰۰,۰۰۰ تومان</b></li>
                <li><span>دو استوری متوالی (عکس کتاب + توضیح متنی صمیمانه):</span> <b>۷۵۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری اختصاصی ۳ تا ۴ قسمتی (آنباکس + گزیده‌خوانی + معرفی کامل):</span> <b>۱,۲۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🎬 تعرفه ریلز و پست فید (دائمی)</h3>
            <ul class="pricing-list">
                <li><span>پست اسلایدی کاروسل (عکاسی از کتاب + متن تجربه مطالعه):</span> <b>۱,۲۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز ویدیویی اختصاصی (معرفی داستانی و تحلیلی اثر):</span> <b>۱,۸۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">📦 پکیج‌های پیشنهادی همکاری</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج اول (ریلز اختصاصی + ۲ استوری معرفی)</span>
                    <span class="pkg-price">۲,۲۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج طلایی (ریلز اختصاصی + رشته‌استوری آنباکس + هایلایت پیج)</span>
                    <span class="pkg-price">۲,۸۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ویدیوی آنباکس در استوری + تولید ریلز اختصاصی فید + قرارگیری در هایلایت ماندگار پیج.</p>
            </div>
        </div>
    """,
    'booksbahar': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها و تعرفه‌های بهار (Booksbahar)</h3>
            <h3 style="margin-top: 15px;">📱 تعرفه تبلیغات استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>بنر تبلیغاتی | اد استوری ریلز یا پست شما:</span> <b>۴۰۰,۰۰۰ تومان</b></li>
                <li><span>استوری آنباکسینگ اختصاصی:</span> <b>۵۰۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری معرفی (۳ تا ۶ استوری):</span> <b>۱,۰۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🎬 تعرفه ریلز و پست فید (دائمی)</h3>
            <ul class="pricing-list">
                <li><span>پست اسلایدی (کاروسل نقد کتاب):</span> <b>۱,۳۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز اختصاصی ویدیویی:</span> <b>۲,۰۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">📦 پکیج‌های پیشنهادی همکاری</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج استوری (آنباکس + عکاسی + بریده متن + رشته‌استوری معرفی)</span>
                    <span class="pkg-price">۲,۰۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج ویژه (ریلز کامل معرفی + آنباکس + عکاسی + بریده متن در استوری)</span>
                    <span class="pkg-price">۳,۰۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ریلز ویدیویی جامع با مخاطبان هدفمند کتاب‌خوان + پوشش کامل استوری و آنباکسینگ اثر.</p>
            </div>
            <p class="note" style="margin-top: 15px; font-size: 13px; color: #94a3b8; line-height: 1.7;">
                📌 <b>شرایط و نکات مهم همکاری:</b><br>
                • ارسال فیزیکی کتاب الزامی است.<br>
                • مطالعه دقیق کتاب پس از واریز تعرفه انجام شده و فرایند ضبط آغاز می‌شود (حداقل ۱۰ روز کاری).<br>
                • حفظ صداقت در معرفی و بیان نظر واقعی جهت اعتماد مخاطبان.
            </p>
        </div>
    """,
    'about_dokhtarjan': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها و تعرفه‌های پیشنهادی دخترجان (About Dokhtarjan)</h3>
            <h3 style="margin-top: 15px;">📱 تعرفه تبلیغات استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>تک‌استوری بنری / اد استوری (Add to Story):</span> <b>۵۰۰,۰۰۰ تومان</b></li>
                <li><span>دو استوری متوالی (عکس کتاب + معرفی متنی صمیمانه):</span> <b>۷۵۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری اختصاصی ۳ تا ۴ قسمتی (آنباکس + گزیده‌خوانی + معرفی کامل):</span> <b>۱,۲۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🎬 تعرفه ریلز و پست فید (دائمی)</h3>
            <ul class="pricing-list">
                <li><span>پست اسلایدی کاروسل (عکاسی از کتاب + متن و حس‌وحال مطالعه):</span> <b>۱,۲۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز ویدیویی اختصاصی (معرفی داستانی اثر با لحن صمیمانه):</span> <b>۱,۸۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">📦 پکیج‌های پیشنهادی همکاری</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج اول (ریلز اختصاصی + ۲ استوری معرفی)</span>
                    <span class="pkg-price">۲,۲۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج طلایی (ریلز اختصاصی + رشته‌استوری آنباکس + هایلایت پیج)</span>
                    <span class="pkg-price">۲,۸۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ویدیوی آنباکس در استوری + تولید ریلز اختصاصی فید + قرارگیری در هایلایت ماندگار پیج.</p>
            </div>
        </div>
    """,
    'greenverse.book': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها و تعرفه‌های پیشنهادی گِرین (Greenverse Book)</h3>
            <h3 style="margin-top: 15px;">📱 تعرفه تبلیغات استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>تک‌استوری بنری / اد استوری (Add to Story):</span> <b>۵۰۰,۰۰۰ تومان</b></li>
                <li><span>دو استوری متوالی (عکس کتاب + توضیح متنی):</span> <b>۸۰۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری اختصاصی ۳ تا ۴ قسمتی (آنباکس + معرفی با لحن صمیمانه):</span> <b>۱,۴۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🎬 تعرفه ریلز و پست فید (دائمی)</h3>
            <ul class="pricing-list">
                <li><span>پست اسلایدی کاروسل (عکاسی + نقد و بررسی متنی):</span> <b>۱,۴۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز ویدیویی اختصاصی (ترند، سناریو و معرفی رمان):</span> <b>۲,۲۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">📦 پکیج‌های پیشنهادی همکاری</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج اول (ریلز اختصاصی + ۲ استوری معرفی)</span>
                    <span class="pkg-price">۲,۷۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج طلایی (ریلز اختصاصی + رشته‌استوری آنباکس + هایلایت ماندگار)</span>
                    <span class="pkg-price">۳,۴۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ریلز ویدیویی در اکسپلور با میانگین ویو ۱۵K+ و پوشش کامل در استوری و هایلایت پیج.</p>
            </div>
        </div>
    """,
    'saman.reads': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها و تعرفه‌های سامان هلمز (Saman Reads / Holmes)</h3>
            <h3 style="margin-top: 15px;">📱 تعرفه تبلیغات استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>تک‌استوری بنری / اد استوری (Add to Story):</span> <b>۵۰۰,۰۰۰ تومان</b></li>
                <li><span>دو استوری متوالی (عکس کتاب + توضیح متنی):</span> <b>۸۰۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری اختصاصی ۳ تا ۴ قسمتی (آنباکس + معرفی با لحن اختصاصی):</span> <b>۱,۴۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🎬 تعرفه ریلز و پست فید (دائمی)</h3>
            <ul class="pricing-list">
                <li><span>پست اسلایدی کاروسل (عکاسی + نقد و بررسی متنی):</span> <b>۱,۵۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز ویدیویی اختصاصی (ترند، سناریو و معرفی با ادیت قوی):</span> <b>۲,۵۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">📦 پکیج‌های پیشنهادی همکاری</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج اول (ریلز اختصاصی + ۲ استوری معرفی)</span>
                    <span class="pkg-price">۳,۰۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج طلایی (ریلز اختصاصی + رشته‌استوری آنباکس + هایلایت ماندگار)</span>
                    <span class="pkg-price">۳,۸۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ریلز ویدیویی وایرال در اکسپلور با میانگین ویو ۵۰K+ و پوشش کامل در استوری و هایلایت پیج.</p>
            </div>
        </div>
    """,
    'rendtopia': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها و تعرفه‌های رسمی رندتوپیا (Rendtopia)</h3>
            <h3 style="margin-top: 15px;">📱 تعرفه تبلیغات استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>اد استوری (Add to Story) یکی از پست‌های شما:</span> <b>۱,۲۰۰,۰۰۰ تومان</b></li>
                <li><span>استوری تیزر تبلیغاتی شما (حداکثر ۱ دقیقه):</span> <b>۱,۲۰۰,۰۰۰ تومان</b></li>
                <li><span>صحبت و معرفی با چهره در مورد محتوای پیج (۱ استوری ۱ دقیقه‌ای):</span> <b>۱,۷۰۰,۰۰۰ تومان</b></li>
                <li><span>ارسال محصول/کتاب و معرفی کامل در ۲ تا ۳ استوری:</span> <b>۲,۲۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🎬 پکیج جامع پست و معرفی چندپلتفرمی</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج طلایی (پست مستقل فید با چهره + استوری + تلگرام)</span>
                    <span class="pkg-price">۷,۵۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: تولید محتوا و معرفی کتاب در یک پست مستقل با تصویر و نقد رضا + استوری آنباکس کتاب و تگ پیج + استوری مجدد کتاب چند روز بعد + معرفی و توصیه مجدد در کانال و سایر پلتفرم‌های رندتوپیا.</p>
            </div>
        </div>
    """,
    'raha_farbodrad': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها و تعرفه‌های پیشنهادی رها فربدراد (Raha Farbodrad)</h3>
            <div class="package-item" style="background: rgba(34, 158, 217, 0.1); border-color: rgba(56, 189, 248, 0.4); margin-bottom: 15px;">
                <div class="pkg-header">
                    <span class="pkg-title" style="color: #38bdf8;">📢 چنل رسمی تلگرام رها:</span>
                    <a href="https://t.me/raha_farbodrad" target="_blank" rel="noopener noreferrer" style="color: #fbbf24; text-decoration: none; font-weight: 800; direction: ltr;">@raha_farbodrad ↗</a>
                </div>
            </div>

            <h3 style="margin-top: 15px;">📱 تعرفه تبلیغات استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>تک‌استوری بنری / اد استوری (Add to Story):</span> <b>۶۰۰,۰۰۰ تومان</b></li>
                <li><span>دو استوری متوالی (عکس و معرفی متنی کتاب):</span> <b>۱,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری اختصاصی ۴ تایی (آنباکس + عکاسی اختصاصی + خوانش گزیده):</span> <b>۱,۸۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🎬 تعرفه پست و ریلز فید (دائمی)</h3>
            <ul class="pricing-list">
                <li><span>پست اسلایدی (کاروسل عکاسی + نقد و بررسی ادبی کامل در کپشن):</span> <b>۲,۲۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز ویدیویی اختصاصی (معرفی تحلیلی کتاب با کیفیت بصری بالا):</span> <b>۳,۲۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">📦 پکیج‌های پیشنهادی همکاری</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج اول (ریلز اختصاصی + ۲ استوری معرفی)</span>
                    <span class="pkg-price">۳,۸۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج طلایی (ریلز اختصاصی + رشته‌استوری آنباکس + هایلایت ماندگار)</span>
                    <span class="pkg-price">۴,۶۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: معرفی عمیق و تخصصی کتاب در فید و استوری با بالاترین نرخ تعامل و ماندگاری در هایلایت پیج.</p>
            </div>
        </div>
    """,
    'asma_vibe': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها و تعرفه‌های پیشنهادی اسما (Asma Vibe)</h3>
            <h3 style="margin-top: 15px;">📱 تعرفه تبلیغات استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>تک‌استوری بنری / اد استوری (Add to Story):</span> <b>۶۰۰,۰۰۰ تومان</b></li>
                <li><span>دو استوری متوالی (عکس و معرفی متنی کتاب):</span> <b>۱,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری اختصاصی ۴ تایی (آنباکس + عکاسی اختصاصی + خوانش گزیده):</span> <b>۱,۸۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🎬 تعرفه پست و ریلز فید (دائمی)</h3>
            <ul class="pricing-list">
                <li><span>پست اسلایدی (کاروسل عکاسی + نقد و بررسی ادبی کامل در کپشن):</span> <b>۲,۲۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز ویدیویی اختصاصی (معرفی تحلیلی کتاب با کیفیت بصری بالا):</span> <b>۳,۲۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">📦 پکیج‌های پیشنهادی همکاری</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج اول (ریلز اختصاصی + ۲ استوری معرفی)</span>
                    <span class="pkg-price">۳,۸۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج طلایی (ریلز اختصاصی + رشته‌استوری آنباکس + هایلایت ماندگار)</span>
                    <span class="pkg-price">۴,۶۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: معرفی عمیق و تخصصی کتاب در فید و استوری با بالاترین نرخ تعامل و ماندگاری در هایلایت پیج.</p>
            </div>
        </div>
    """,
    'ke_mesle_ketab': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها و تعرفه‌های زینب مهرنگ (ک مثل کتاب)</h3>
            <h3 style="margin-top: 15px;">📱 تعرفه تبلیغات استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>تک‌استوری بنری / اد استوری (Add to Story):</span> <b>۵۰۰,۰۰۰ تومان</b></li>
                <li><span>دو استوری متوالی (عکس کتاب + توضیح متنی):</span> <b>۸۰۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری ۳ تا ۴ قسمتی (آنباکس + عکاسی اختصاصی + معرفی):</span> <b>۱,۴۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🎬 تعرفه پست و ریلز فید (دائمی)</h3>
            <ul class="pricing-list">
                <li><span>پست اسلایدی (کاروسل عکاسی + نقد و بررسی کامل در کپشن):</span> <b>۱,۷۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز ویدیویی اختصاصی (BookTok / سناریو و معرفی کتاب):</span> <b>۲,۴۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">📦 پکیج‌های پیشنهادی همکاری</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج اول (ریلز اختصاصی + ۲ استوری معرفی)</span>
                    <span class="pkg-price">۲,۹۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج طلایی (ریلز اختصاصی + رشته‌استوری آنباکس ۴ تایی + هایلایت پیج)</span>
                    <span class="pkg-price">۳,۶۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ویدیوی آنباکس در استوری + عکاسی و ریلز اختصاصی + هایلایت ماندگار برای افزایش اثربخشی و فروش.</p>
            </div>
        </div>
    """,
    'sabasamaadi': """
        <div class="pricing-card">
            <h3>🌿 پکیج‌ها و تعرفه‌های صبا صمدی (Saba Samadi)</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج اول (رشته‌استوری ۴ تا ۶ تایی)</span>
                    <span class="pkg-price">۱,۲۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ویدیوی آنباکس اختصاصی در استوری + عکس باکیفیت از کتاب و تیکه‌کتاب + معرفی کامل در استوری.</p>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج دوم (رشته‌استوری ۵ تا ۷ تایی + ریلز اختصاصی)</span>
                    <span class="pkg-price">۲,۴۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ویدیوی آنباکس در رشته استوری‌ها + عکس از تیکه کتاب + معرفی کامل و تحلیلی کتاب در یک ریلز اختصاصی و کپشن.</p>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج طلایی (رشته‌استوری ۶ تا ۸ تایی + پست اسلایدی Carousel + یادآوری)</span>
                    <span class="pkg-price">۳,۰۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ویدیوی آنباکس + عکس تیکه کتاب + معرفی کامل در پست اسلایدی (عکس و توضیحات جامع کپشن) + استوری مجدد بعد از چند روز برای یادآوری.</p>
            </div>
            <p class="note" style="margin-top: 15px; font-size: 13px; color: #94a3b8; line-height: 1.7;">
                📌 <b>شرایط و ضوابط همکاری:</b><br>
                • ارسال کتاب یا محصول به صورت فیزیکی (نسخه الکترونیکی پذیرفته نمی‌شود).<br>
                • مطالعه دقیق و کامل کتاب طی ۲ تا ۳ هفته قبل از تولید و انتشار محتوا.<br>
                • بیان صادقانه نقاط قوت و نکات قابل توجه کتاب جهت حفظ اعتماد مخاطبان.<br>
                • امکان معرفی کتاب‌فروشی‌های آنلاین و حضوری.
            </p>
        </div>
    """,
    'sarabooks.ir': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها، شرایط و تعرفه‌های جامع سارا هوشمند (SaraBooks)</h3>
            
            <div class="package-item" style="background: rgba(34, 158, 217, 0.1); border-color: rgba(56, 189, 248, 0.4); margin-bottom: 18px;">
                <div class="pkg-header">
                    <span class="pkg-title" style="color: #38bdf8;">📢 کانال رسمی تلگرام سارابوکز:</span>
                    <a href="https://t.me/BookishDays" target="_blank" rel="noopener noreferrer" style="color: #fbbf24; text-decoration: none; font-weight: 800; direction: ltr;">@BookishDays ↗</a>
                </div>
                <p class="pkg-desc">جامعه کتاب‌خوان‌های همراه، انتشار منظم گزیده‌کتاب‌ها و بازنشر معرفی‌ها | ارتباط تلگرام: <a href="https://t.me/SaraHooshmand" target="_blank" rel="noopener noreferrer" style="color: #818cf8; text-decoration: underline; direction: ltr; font-weight: 700;">@SaraHooshmand</a></p>
            </div>

            <!-- بخش ۱: معرفی کتاب -->
            <h3 style="margin-top: 15px; color: #fbbf24;">📚 ۱. تعرفه اختصاصی معرفی کتاب (ناشران و نویسندگان)</h3>
            <div class="package-item" style="margin-bottom: 12px;">
                <div class="pkg-header">
                    <span class="pkg-title">🌻 رشته‌استوری معرفی کتاب (۶ الی ۷ اسلاید ۲۴ ساعته)</span>
                    <span class="pkg-price">۲,۳۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">استوری گویشی با چهره + آن‌باکس بسته + عکس یا خوانش گزیده‌های کتاب + تولید محتوا و بازنشر در کانال تلگرام (@BookishDays).</p>
            </div>

            <ul class="pricing-list" style="margin-bottom: 20px;">
                <li><span>تعرفه اول فید (پست اسلایدی): استوری‌ها (آن‌باکس و رشته‌استوری) + پست اسلایدی عکاسی (Carousel) + کانال تلگرام:</span> <b>۳,۷۵۰,۰۰۰ تومان</b></li>
                <li><span>تعرفه دوم فید (ریلز کوتاه ترند): استوری‌ها + ریلز کوتاه سبک BookTok (~۲۰ ثانیه با موزیک ترند و ادیت) + کپشن:</span> <b>۴,۱۰۰,۰۰۰ تومان</b></li>
                <li><span>تعرفه سوم فید (ریلز گویشی تحلیلی): استوری‌ها + ریلز ۱ دقیقه‌ای یا بیشتر با صحبت و تحلیل عمیق کتاب در ویدیو:</span> <b>۵,۴۰۰,۰۰۰ تومان</b></li>
                <li><span>تعرفه چهارم فید (⭐️ پکیج VIP ⭐️): ریلز تحلیلی ۱ دقیقه‌ای + یادآوری در یک ویدیو یا کاروسل بعدی + رشته‌استوری + هایلایت ماندگار + تلگرام:</span> <b>۸,۱۰۰,۰۰۰ تومان</b></li>
            </ul>

            <!-- بخش ۲: فروشگاه‌ها و آنلاین‌شاپ‌ها -->
            <h3 style="margin-top: 25px; color: #38bdf8;">🛍️ ۲. تعرفه تبلیغات فروشگاه‌ها و آنلاین‌شاپ‌ها</h3>
            <ul class="pricing-list" style="margin-bottom: 15px;">
                <li><span>تک استوری بنری / شات ارسالی (Add to Story):</span> <b>۵۱۰,۰۰۰ تومان</b></li>
                <li><span>تک استوری گویشی با چهره و هم‌فکری:</span> <b>۹۹۰,۰۰۰ تومان</b></li>
                <li><span>رشته استوری شاپ (برای شاپ‌های زیر ۲۰K با ارسال گیفت ۴۵۰ ت کسر می‌گردد):</span> <b>۲,۲۵۰,۰۰۰ تومان</b></li>
                <li><span>پست دائم همراه با گیفت (معرفی محصولات به صورت عکس اسلایدی یا ویدیو کاربردی):</span> <b>۵,۱۰۰,۰۰۰ تومان</b></li>
                <li><span>پست دائم بدون گیفت (معرفی خدمات و ویژگی‌های خاص آنلاین‌شاپ):</span> <b>۶,۲۰۰,۰۰۰ تومان</b></li>
            </ul>

            <!-- بخش ۳: پیج‌های بلاگری و خدمات -->
            <h3 style="margin-top: 25px; color: #f472b6;">📱 ۳. تعرفه تبلیغات پیج‌های بلاگری، پادکست و خدمات</h3>
            <ul class="pricing-list" style="margin-bottom: 20px;">
                <li><span>تک استوری بنری (عکس/ویدیو ارسالی) یا شات و اد استوری:</span> <b>۵۱۰,۰۰۰ تومان</b></li>
                <li><span>تک استوری گویشی با چهره و هماهنگی متن دلخواه:</span> <b>۹۱۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری اختصاصی (۳ الی ۴ اسلاید متناسب با سناریو و داستان پیج):</span> <b>۲,۳۰۰,۰۰۰ تومان</b></li>
                <li><span>پست دائمی فید (معرفی خدمات، پادکست، کتاب صوتی و ویژگی‌های خاص):</span> <b>۶,۶۰۰,۰۰۰ تومان</b></li>
            </ul>

            <p class="note" style="margin-top: 18px; font-size: 13.5px; color: #cbd5e1; line-height: 1.8; background: rgba(15, 23, 42, 0.6); padding: 16px; border-radius: 14px; border: 1px solid rgba(255, 255, 255, 0.08);">
                📌 <b>شرایط و ضوابط عمومی و اجرایی سارا هوشمند:</b><br>
                • <b>تعهد به مطالعه کامل کتاب:</b> به هیچ عنوان بدون مطالعه دقیق، معرفی انجام نمی‌شود؛ بنابراین پس از دریافت کتاب، بین <b>۲۰ تا ۳۰ روز کاری</b> زمان برای مطالعه و تولید محتوا لازم است.<br>
                • <b>ظرفیت محدود:</b> ماهانه صرفاً <b>۲ الی ۳ عنوان کتاب</b> معرفی می‌شوند؛ همچنین روزانه نهایتاً <b>یک تبلیغ</b> در پیج قرار می‌گیرد.<br>
                • <b>اولویت و تسویه:</b> اولویت رزرو تاریخ‌ها بر اساس زمان واریز وجه است و تسویه پیش از شروع پروژه انجام می‌پذیرد.<br>
                • <b>تبلیغات حضوری:</b> به کلیه تعرفه‌های ذکر شده مبلغ <b>۱,۰۰۰,۰۰۰ تومان</b> اضافه می‌شود.<br>
                • <b>تعرفه Collaboration:</b> برای پیج‌های بالای ۳۰K رایگان؛ برای پیج‌های زیر ۳۰K به تعرفه پایه مبلغ <b>۵۰۰,۰۰۰ تومان</b> افزوده می‌شود.<br>
                • <b>ارسال گیفت:</b> هزینه پست و ارسال گیفت بر عهده سفارش‌دهنده است؛ آن‌باکس گیفت در ۱ الی ۲ استوری به صورت رایگان انجام می‌گیرد.<br>
                • <b>کمپین‌های دارای ددلاین:</b> در صورت وجود زمان‌بندی خاص (کمپین فروش، ددلاین دوره، آفر) هماهنگی از قبل الزامی است.
            </p>
        </div>
    """,
    'datoverse': """
        <div class="pricing-card">
            <h3>🪐 تعرفه‌ها و کمپین‌های اختصاصی داتورس (Datoverse)</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">کمپین جامع و ۳ ماهه اختصاصی کتاب</span>
                    <span class="pkg-price">۶۹,۰۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: حداقل ۳ روز استوری و روزی ۱۰ استوری متوالی + ارجاع اختصاصی به کتاب در حداقل ۳ پست و ریلز طی ۲ هفته + ماندگاری مستقیم ۳ روز تا ۱ هفته و ارجاع پیوسته غیرمستقیم تا ۳ ماه.</p>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">اسپانسری در ریلز اختصاصی (Feed Reels)</span>
                    <span class="pkg-price">۴۵,۰۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">تولید محتوای ویدئویی اختصاصی با بالاترین کیفیت و بازدید میلیونی در پیج داتورس.</p>
            </div>
            <h3 style="margin-top: 20px;">📱 پکیج‌های تبلیغات استوری</h3>
            <ul class="pricing-list">
                <li><span>پکیج ۳ استوری متوالی:</span> <b>۵,۹۰۰,۰۰۰ تومان</b></li>
                <li><span>پکیج ۵ استوری متوالی:</span> <b>۷,۹۰۰,۰۰۰ تومان</b></li>
            </ul>
        </div>
    """,
    'lilith.in.wonderland': """
        <div class="pricing-card">
            <h3>📖 تعرفه معرفی کتاب (بر اساس حجم و صفحات)</h3>
            <ul class="pricing-list">
                <li><span>کتاب زیر ۲۰۰ صفحه (استوری کنجکاوسازی + ریلز اختصاصی):</span> <b>۱,۵۰۰,۰۰۰ تومان</b></li>
                <li><span>کتاب ۲۰۰ تا ۵۰۰ صفحه (استوری کنجکاوسازی + ریلز اختصاصی):</span> <b>۳,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>کتاب ۵۰۰ تا ۱۰۰۰ صفحه (استوری کنجکاوسازی + ریلز اختصاصی):</span> <b>۵,۰۰۰,۰۰۰ تومان</b></li>
            </ul>
            <h3 style="margin-top: 20px;">📱 تعرفه تبلیغات پیج و خدمات</h3>
            <ul class="pricing-list">
                <li><span>تک‌استوری معرفی پیج:</span> <b>۱,۵۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز معرفی زیر ۱ دقیقه:</span> <b>۳,۰۰۰,۰۰۰ تومان</b></li>
            </ul>
            <p class="note" style="margin-top: 15px; font-size: 13px; color: #94a3b8;">📌 شیوه اجرا: یک استوری کنجکاوسازی ۲۴ ساعت قبل از پخش ریلز منتشر شده و سپس ریلز اصلی قرار می‌گیرد.</p>
        </div>
    """,
    'baharthebookreviewer': """
        <div class="pricing-card">
            <h3>📦 پکیج‌های جامع تولید محتوا (اینستاگرام + یوتیوب)</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج ۱ (ویدیوی یوتیوب بالای ۱۰ دقیقه + ریلز اینستاگرام + ۸ استوری + Shorts)</span>
                    <span class="pkg-price">۱۵,۰۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">مناسب برای معرفی کامل و جزئی کتاب‌ها، فروشگاه‌های آنلاین و نشرها. در صورت ارائه هدیه یا کد تخفیف ۲۵٪ برای مخاطبان: <b>۱۴ میلیون تومان</b>.</p>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج ۲ (یک ریلز اختصاصی ۱-۲ دقیقه + ۴ استوری + YouTube Shorts)</span>
                    <span class="pkg-price">۱۱,۰۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">مناسب برای معرفی کوتاه و مؤثر. در صورت ارائه هدیه یا کد تخفیف: <b>۱۰ میلیون تومان</b>.</p>
            </div>
            <h3 style="margin-top: 20px;">📱 تعرفه تبلیغات استوری</h3>
            <ul class="pricing-list">
                <li><span>روش ۱: بنر تبلیغاتی یا اد استوری پست شما:</span> <b>۱,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>روش ۲: رشته استوری ۴ قسمتی (عکس و متن):</span> <b>۳,۹۰۰,۰۰۰ تومان</b></li>
                <li><span>روش ۲: رشته استوری ۶ قسمتی (عکس و متن):</span> <b>۴,۲۰۰,۰۰۰ تومان</b></li>
                <li><span>روش ۳: رشته استوری ترکیبی ۴ قسمتی (۳ عکس + ۱ ویدیو با چهره):</span> <b>۴,۷۰۰,۰۰۰ تومان</b></li>
                <li><span>روش ۳: رشته استوری ترکیبی ۶ قسمتی (۴ عکس + ۲ ویدیو با چهره):</span> <b>۵,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>روش ۴: استوری آنباکسینگ اختصاصی (۴ تا ۵ قسمتی با باز کردن بسته):</span> <b>۴,۲۰۰,۰۰۰ تومان</b></li>
            </ul>
            <p class="note" style="margin-top: 15px; font-size: 13px; color: #94a3b8;">📌 <b>شرایط همکاری:</b> در صورت انتشار محتوا به‌صورت مشترک (Collaborate)، ۲۰٪ به هزینه‌ها اضافه می‌شود • شروع تولید محتوا پس از واریز مبلغ آغاز می‌گردد.</p>
        </div>
    """,
    'artemisbook': """
        <div class="pricing-card">
            <h3>✨ پکیج‌ها و تعرفه‌های به‌روزشده آرتمیس‌بوک (گلاره یوسفی)</h3>
            <div class="package-item" style="background: rgba(99, 102, 241, 0.12); border-color: rgba(99, 102, 241, 0.4); margin-bottom: 15px;">
                <div class="pkg-header">
                    <span class="pkg-title" style="color: #38bdf8;">👑 پکیج پرمیوم و همه‌جانبه (بیشترین بازدهی و ماندگاری)</span>
                    <span class="pkg-price">۵,۸۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ۱ ریلز گویشی و تحلیلی اختصاصی (با پتانسیل اکسپلور میلیونی) + رشته‌استوری ۴ قسمتی (آنباکس، گزیده‌خوانی و معرفی) + هایلایت ماندگار در پیج.</p>
            </div>

            <h3 style="margin-top: 15px;">📱 تعرفه تبلیغات استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>تک‌استوری بنری / اد استوری (Add to Story):</span> <b>۶۰۰,۰۰۰ تومان</b></li>
                <li><span>دو استوری متوالی (عکس کتاب + معرفی متنی):</span> <b>۱,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری اختصاصی ۴ تایی (گویشی با چهره + آنباکس + نقد):</span> <b>۱,۸۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🎬 تعرفه پست و ریلز فید (دائمی)</h3>
            <ul class="pricing-list">
                <li><span>پست اسلایدی کاروسل (عکاسی + نقد و تحلیل عمیق در کپشن):</span> <b>۲,۵۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز ویدیویی اختصاصی (گویشی با سناریو و تحلیل کامل اثر):</span> <b>۴,۲۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">🚗 همکاری و پوشش رویداد حضوری (ایونت / کتابفروشی)</h3>
            <ul class="pricing-list">
                <li><span>کرج (حضور + پوشش کامل استوری و ریلز):</span> <b>۴ تا ۵ میلیون تومان</b></li>
                <li><span>تهران (حضور + پوشش کامل استوری و ریلز):</span> <b>۶ تا ۸ میلیون تومان</b></li>
            </ul>
        </div>
    """,
    'tootfarangi._.book': """
        <div class="pricing-card">
            <h3>🍓 پکیج‌ها و تعرفه‌های توت‌فرنگی بوک</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج ۱ (ریلز اختصاصی + ۱ استوری معرفی)</span>
                    <span class="pkg-price">۹۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج ۲ (ریلز اختصاصی + ۲ استوری معرفی)</span>
                    <span class="pkg-price">۱,۰۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج ۳ (ریلز اختصاصی + رشته‌استوری کامل)</span>
                    <span class="pkg-price">۱,۲۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">تبلیغ و پوشش رویداد حضوری (نمایشگاه / کافه)</span>
                    <span class="pkg-price">۲,۰۰۰,۰۰۰ تومان</span>
                </div>
            </div>
            <h3 style="margin-top: 20px;">📱 تعرفه خدمات تکی استوری و ریلز</h3>
            <ul class="pricing-list">
                <li><span>تک استوری معرفی (متنی + حضور چهره):</span> <b>۵۰۰,۰۰۰ تومان</b></li>
                <li><span>دو استوری معرفی متوالی:</span> <b>۶۰۰,۰۰۰ تومان</b></li>
                <li><span>رشته استوری معرفی:</span> <b>۸۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز معرفی اختصاصی:</span> <b>۸۰۰,۰۰۰ تومان</b></li>
            </ul>
        </div>
    """,
    'roxanaabasian': """
        <div class="pricing-card">
            <h3>🎬 خدمات فید و تولید محتوا</h3>
            <ul class="pricing-list">
                <li><span>ریلز اختصاصی (ایده، سناریو، ضبط، تدوین و انتشار):</span> <b>۱۴,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز اختصاصی + ۵ تا ۸ استوری فضاسازی و اعتمادسازی:</span> <b>۱۷,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>پست کاروسل (اسلایدی) اختصاصی:</span> <b>۸,۰۰۰,۰۰۰ تومان</b></li>
            </ul>
            <h3 style="margin-top: 20px;">📱 تبلیغات استوری</h3>
            <ul class="pricing-list">
                <li><span>تک‌استوری بنری / متنی:</span> <b>۱,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>تک‌استوری گفتاری با چهره:</span> <b>۱,۵۰۰,۰۰۰ تومان</b></li>
                <li><span>رشته‌استوری تبلیغاتی (۵ تا ۱۰ استوری):</span> <b>۵,۰۰۰,۰۰۰ تومان</b></li>
            </ul>
            <h3 style="margin-top: 20px;">👑 پکیج طلایی (بیشترین پوشش)</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج طلایی کامل</span>
                    <span class="pkg-price">۲۴,۰۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ۱ ریلز اختصاصی + رشته‌استوری فضاسازی + ۱ پست کاروسل + معرفی در کانال تلگرام + اطلاع‌رسانی در کامیونیتی کتاب‌خوانی (ارزش واقعی: ۲۷ میلیون تومان).</p>
            </div>
        </div>
    """,
    'nooshinaseri': """
        <div class="pricing-card">
            <h3>🔮 پکیج‌ها و تعرفه‌های جادوگر</h3>
            <ul class="pricing-list">
                <li><span>تک استوری:</span> <b>۲,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>رشته استوری:</span> <b>۳,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>پست اسلایدی (کاروسل):</span> <b>۳,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>ریلز اختصاصی:</span> <b>۷,۰۰۰,۰۰۰ تومان</b></li>
                <li><span>پکیج ریلز + تک‌استوری:</span> <b>۸,۵۰۰,۰۰۰ تومان</b></li>
                <li><span>پکیج ریلز + رشته‌استوری:</span> <b>۹,۰۰۰,۰۰۰ تومان</b></li>
            </ul>
            <p class="note" style="margin-top: 15px; font-size: 13px; color: #94a3b8;">📌 ارسال محتوا حداقل ۲۴ تا ۴۸ ساعت قبل از انتشار • ارائه آمار و Insights پس از پایان تبلیغ.</p>
        </div>
    """,
    'saghaaal': """
        <div class="pricing-card">
            <h3>📦 پکیج‌های اختصاصی معرفی کتاب ساقی</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج اول (آنباکس + عکاسی + استوری)</span>
                    <span class="pkg-price">۱,۲۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">ویدیوی آنباکسینگ کتاب + عکاسی اختصاصی + معرفی کامل بعد از مطالعه در استوری.</p>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج دوم (پست + استوری + ثبت در گودریدز و به‌خوان)</span>
                    <span class="pkg-price">۲,۵۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">آنباکس + عکاسی + معرفی در استوری و پست فید + ثبت نقد و نظر رسمی در برنامه‌های به‌خوان و Goodreads.</p>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج سوم (بیشترین بازدهی - اینستاگرام + یوتیوب)</span>
                    <span class="pkg-price">۴,۰۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">آنباکس + فضاسازی کامل استوری + پست فید + ثبت در گودریدز و به‌خوان + ویدیوی معرفی کامل در کانال یوتیوب.</p>
            </div>
        </div>
    """,
    'dreems_book': """
        <div class="pricing-card">
            <h3>📖 پکیج‌ها و تعرفه‌های رسمی زهرا (Dreems Book)</h3>
            <h3 style="margin-top: 15px;">🎬 تعرفه معرفی کتاب و محتوای فید (همراه با استوری)</h3>
            <ul class="pricing-list">
                <li><span>معرفی کتاب به صورت پست تک‌اسلاید همراه با استوری:</span> <b>۱,۱۰۰,۰۰۰ تومان</b></li>
                <li><span>معرفی کتاب به صورت پست اسلایدی (کاروسل) همراه با استوری:</span> <b>۱,۳۰۰,۰۰۰ تومان</b></li>
                <li><span>معرفی کتاب به صورت ریلز اختصاصی همراه با استوری:</span> <b>۱,۵۰۰,۰۰۰ تومان</b></li>
            </ul>

            <h3 style="margin-top: 20px;">📱 تعرفه تبلیغات پیج و خدمات در استوری (۲۴ ساعته)</h3>
            <ul class="pricing-list">
                <li><span>اد استوری (Add to Story):</span> <b>۴۵۰,۰۰۰ تومان</b></li>
                <li><span>استوری بنری ارسالی (ریلز یا عکس آماده):</span> <b>۵۵۰,۰۰۰ تومان</b></li>
                <li><span>تولید محتوای اختصاصی از پیج (عکس/فیلم + توضیحات کامل در ۲ استوری):</span> <b>۸۹۰,۰۰۰ تومان</b></li>
            </ul>

            <p class="note" style="margin-top: 15px; font-size: 13px; color: #94a3b8; line-height: 1.7;">
                📌 <b>شرایط و ضوابط همکاری:</b><br>
                • ارسال فیزیکی کتاب الزامی است؛ حین مطالعه چندین بار در استوری فضاسازی و معرفی انجام شده و در نهایت پست/ریلز کامل منتشر می‌شود.<br>
                • شروع مطالعه و ورود به پروسه تولید محتوا از زمان تحویل کتاب و واریز وجه آغاز می‌گردد.<br>
                • زمان معرفی بسته به حجم اثر بین ۷ تا ۳۰ روز متغیر است (هماهنگی کمپین‌ها و تاریخ‌های خاص از قبل انجام می‌شود).<br>
                • حفظ صداقت در نقد؛ در صورت عدم تطابق محتوایی اثر، همکاری کنسل و ۵۰٪ مبلغ عودت داده می‌شود.
            </p>
        </div>
    """,
    'kiana_am': """
        <div class="pricing-card">
            <h3>🌼 پکیج‌ها و تعرفه‌های کیانا (Kiana Am)</h3>
            <div class="package-item" style="background: rgba(99, 102, 241, 0.1); border-color: rgba(99, 102, 241, 0.35); margin-bottom: 16px;">
                <div class="pkg-header">
                    <span class="pkg-title" style="color: #38bdf8;">📦 قالب کامل همکاری (اینستاگرام + یوتیوب + به‌خوان):</span>
                </div>
                <p class="pkg-desc" style="line-height: 1.8; color: #cbd5e1;">
                    • ۱ استوری آنباکسینگ اختصاصی<br>
                    • حداقل ۲ استوری از کتاب یا بریده‌های جذاب کتاب<br>
                    • ۱ ریلز معرفی اختصاصی کتاب با حضور چهره در پیج اینستاگرام<br>
                    • قرار دادن همان ویدیو به صورت YouTube Shorts (با ۵۰۰ تا ۱۵۰۰ ویو)<br>
                    • ثبت ۲ گزارش و ۱ اتمام مطالعه همراه با امتیاز در پلتفرم به‌خوان (با ۳۰۰ دنبال‌کننده)
                </p>
            </div>

            <h3 style="margin-top: 15px;">💰 تعرفه همکاری (بر اساس حجم صفحات کتاب)</h3>
            <ul class="pricing-list">
                <li><span>کتاب‌های زیر ۲۰۰ صفحه (پکیج کامل):</span> <b>۶۰۰,۰۰۰ تومان</b></li>
                <li><span>کتاب‌های بالای ۲۰۰ صفحه (پکیج کامل):</span> <b>۹۰۰,۰۰۰ تومان</b></li>
            </ul>

            <p class="note" style="margin-top: 15px; font-size: 13px; color: #94a3b8; line-height: 1.7;">
                📌 <b>شرایط و نکات همکاری:</b><br>
                • ارسال یک نسخه فیزیکی از کتاب الزامی است.<br>
                • زمان مطالعه و آماده‌سازی محتوا بین ۱۰ تا ۱۵ روز کاری است (برای کتاب‌های حجیم بیشتر خواهد بود).<br>
                • معرفی به سبک شخصی و صادقانه؛ در صورت وجود نظر منفی، ابتدا با سفارش‌دهنده مطرح شده و در صورت تمایل، از انتشار خودداری می‌شود.<br>
                • روند مطالعه و تولید محتوا پس از دریافت کتاب و واریز وجه آغاز می‌گردد.<br>
                • در صورت کنسل شدن همکاری به دلیل عدم تطابق با استانداردهای پیج، ۵۰٪ هزینه عودت داده می‌شود.
            </p>
        </div>
    """,
    'ziiboox': """
        <div class="pricing-card">
            <h3>📚 پکیج‌های رسمی و نهایی همکاری زیبوکس (Ziiboox)</h3>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج اول (آنباکس + عکاسی + استوری)</span>
                    <span class="pkg-price">۹۹۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ویدیوی آنباکس اختصاصی کتاب، عکاسی حرفه‌ای، معرفی کامل در استوری (بدون انتشار پست فید).</p>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج دوم (آنباکس + عکاسی + استوری + ۱ ریلز اختصاصی)</span>
                    <span class="pkg-price">۱,۲۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ویدیوی آنباکس کتاب، عکاسی اختصاصی، معرفی در استوری + یک ریلز اختصاصی معرفی کامل اثر.</p>
            </div>
            <div class="package-item">
                <div class="pkg-header">
                    <span class="pkg-title">پکیج سوم (بیشترین بازدهی و پوشش کامل)</span>
                    <span class="pkg-price">۱,۵۰۰,۰۰۰ تومان</span>
                </div>
                <p class="pkg-desc">شامل: ویدیوی آنباکس کتاب، عکاسی اختصاصی، جوسازی و فضاسازی در استوری، انتشار بخش‌هایی از کتاب در استوری + ۲ ریلز اختصاصی و ۱ پست کاروسل (اسلایدی).</p>
            </div>
            <p class="note" style="margin-top: 15px; font-size: 13px; color: #94a3b8; line-height: 1.7;">
                📌 <b>شرایط و ضوابط همکاری:</b><br>
                • ارسال نسخه فیزیکی کتاب قبل از شروع همکاری الزامی است؛ تولید محتوا حداکثر طی ۱ تا ۲ هفته پس از دریافت کتاب انجام می‌شود.<br>
                • هزینه همکاری پیش از شروع پروژه دریافت می‌گردد.<br>
                • در صورتی که پس از مطالعه کتاب محتوای آن همسو با پیج و سلیقه مخاطب نباشد، ۵۰٪ هزینه عودت داده شده و معرفی انجام نمی‌شود.
            </p>
        </div>
    """
}

def parse_followers_num(val):
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

sorted_bloggers = sorted(bloggers_rich, key=lambda x: parse_followers_num(x.get('followers')), reverse=True)

for rank, b in enumerate(sorted_bloggers, 1):
    u = b['username']
    slug = u.lower()
    name = b['display_name'] or u
    foll = b.get('followers', '-')
    flwing = b.get('following', '-')
    posts = b.get('posts', '-')
    acc_id = b.get('account_id', '-')
    coco_url = b.get('coco_analytics_url', f"https://coco.gl/dashboard/analytics/INSTAGRAM/{acc_id}?username={u}")
    ig_url = f"https://instagram.com/{u}"
    page_canonical = f"{SITE_URL}/blogger/{slug}.html"
    
    avatar_filename = f"{slug}.jpg"
    if slug == "_cherryremi":
        avatar_filename = "cherryremi.jpg"
    avatar_src = f"../avatars/{avatar_filename}"
    avatar_abs_url = f"{SITE_URL}/avatars/{avatar_filename}"
    
    user_posts = posts_by_user.get(slug, [])
    
    total_likes = sum(p.get('likes', 0) for p in user_posts)
    total_comms = sum(p.get('comments', 0) for p in user_posts)
    plays_posts = [p.get('plays', 0) for p in user_posts if p.get('plays', 0) > 0]
    total_plays = sum(plays_posts)
    
    avg_likes_val = int(total_likes / len(user_posts)) if user_posts else 0
    avg_comms_val = int(total_comms / len(user_posts)) if user_posts else 0
    avg_plays_val = int(total_plays / len(plays_posts)) if plays_posts else 0
    
    avg_likes = f"{avg_likes_val:,}" if avg_likes_val > 0 else '—'
    avg_comments = f"{avg_comms_val:,}" if avg_comms_val > 0 else '—'
    avg_plays = f"{avg_plays_val:,}" if avg_plays_val > 0 else '—'
    
    bio = b.get('bio', '')
    clean_bio = bio.replace('\n', '<br>') if bio else 'مروج و بلاگر فعال کتاب و ادبیات داستانی.'
    plain_bio = bio.replace('\n', ' ').strip() if bio else f"صفحه و شناسنامه تحلیلی {name} (@{u}) بلاگر کتاب و ادبیات در اینستاگرام"
    
    er = b.get('est_engagement_rate', '۶.۵٪')
    story_view = b.get('est_story_view', '—')
    reel_view = b.get('est_reel_view', '—')
    tier = b.get('influencer_tier', 'میکرو بوک‌بلاگر')
    aud_prof = b.get('audience_profile', 'مخاطبان علاقه‌مند به کتاب و ادبیات داستانی.')
    
    pricing_html = pricing_dict.get(slug, """
        <div class="pricing-card empty-pricing">
            <p style="color: #94a3b8; font-size: 14px;">تعرفه رسمی این پیج پس از تایید هماهنگ‌کننده ثبت خواهد شد. برای استعلام مستقیم قیمت، بررسی پکیج‌های موجود و رزرو کمپین با <b>ریک سانچز</b> در ارتباط باشید.</p>
        </div>
    """)
    
    rank_label = f"رتبه #{rank} در میان بوک‌بلاگرهای برتر"
    if rank == 1:
        rank_label = "🥇 رتبه ۱ برترین بوک‌بلاگر"
    elif rank == 2:
        rank_label = "🥈 رتبه ۲ برترین بوک‌بلاگر"
    elif rank == 3:
        rank_label = "🥉 رتبه ۳ برترین بوک‌بلاگر"

    same_as_links = [ig_url, coco_url]
    if slug == 'sarabooks.ir':
        same_as_links.extend(["https://t.me/BookishDays", "https://t.me/SaraHooshmand"])

    schema_person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": name,
        "alternateName": f"@{u}",
        "description": plain_bio[:250],
        "image": avatar_abs_url,
        "url": page_canonical,
        "sameAs": same_as_links,
        "jobTitle": "Book Blogger / Influencer",
        "knowsAbout": ["معرفی کتاب", "رمان", "ادبیات", "بوک‌استاگرام", "نقد کتاب", "تولید محتوا"]
    }
    
    schema_breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "دایرکتوری بوک‌بلاگرها",
                "item": f"{SITE_URL}/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": f"{name} (@{u})",
                "item": page_canonical
            }
        ]
    }
    
    schema_person_json = json.dumps(schema_person, ensure_ascii=False, indent=2)
    schema_breadcrumb_json = json.dumps(schema_breadcrumb, ensure_ascii=False, indent=2)

    media_cards_html = ""
    if user_posts:
        media_rows = []
        for p_idx, p in enumerate(user_posts[:8], 1):
            m_type = p.get('type', 'پست')
            m_likes = f"{p.get('likes', 0):,}"
            m_comms = f"{p.get('comments', 0):,}"
            m_plays = f"{p.get('plays', 0):,}" if p.get('plays', 0) > 0 else '—'
            m_cap = p.get('caption', '')
            clean_m_cap = m_cap.replace('\n', ' ')[:100]
            if len(m_cap) > 100: clean_m_cap += '...'
            if not clean_m_cap: clean_m_cap = 'بدون متن کپشن'
            p_link = p.get('link', f"https://www.instagram.com/{u}/")
            
            row = f"""
            <div class="media-post-item">
                <div class="media-post-top">
                    <span class="media-type-badge">{m_type}</span>
                    <div class="media-counts">
                        <span title="تعداد لایک">❤️ {m_likes}</span>
                        <span title="تعداد کامنت">💬 {m_comms}</span>
                        <span title="تعداد پخش">▶️ {m_plays}</span>
                    </div>
                </div>
                <div class="media-caption">{clean_m_cap}</div>
                <div class="media-action">
                    <a href="{p_link}" target="_blank" rel="noopener noreferrer" class="post-direct-link">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                        مشاهده این پست در اینستاگرام ↗
                    </a>
                </div>
            </div>
            """
            media_rows.append(row)
        media_cards_html = "\n".join(media_rows)
    else:
        media_cards_html = f"""
        <div class="media-post-item">
            <p style='color:#94a3b8; font-size:13.5px;'>پست‌های این پیج مستقیماً رصد شده‌اند. برای مشاهده تمام پست‌ها و ریلزها به پیج اصلی مراجعه کنید:</p>
            <a href="https://instagram.com/{u}" target="_blank" rel="noopener noreferrer" class="post-direct-link" style="margin-top:8px;">
                مشاهده پست‌ها در اینستاگرام @{u} ↗
            </a>
        </div>
        """

    extra_channel_btn = ""
    if slug == 'sarabooks.ir':
        extra_channel_btn = f"""
            <a href="https://t.me/BookishDays" target="_blank" rel="noopener noreferrer" class="btn" style="background: linear-gradient(135deg, #229ED9, #0284c7); color: #fff;" title="کانال تلگرام سارابوکز">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/></svg>
                کانال تلگرام: @BookishDays ↗
            </a>
        """

    page_html = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    {GOOGLE_META}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>آمار تحلیلی {name} (@{u}) | نرخ تعامل، فالوور و تعرفه تبلیغات | BookBloger</title>
    <meta name="description" content="تحلیل زنده و شناسنامه آماری پیج اینستاگرام {name} (@{u}) بوک‌بلاگر کتاب، تعداد فالوور {foll}، میانگین لایک {avg_likes}، ویو ریلز {avg_plays} و تعرفه تبلیغات.">
    <meta name="keywords" content="{name}, {u}, بوک بلاگر, بلاگر کتاب, اینستاگرام کتاب, تبلیغات کتاب, معرفی کتاب, قیمت تبلیغات بوک بلاگر">
    <link rel="canonical" href="{page_canonical}">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">

    <!-- OpenGraph Meta Tags -->
    <meta property="og:locale" content="fa_IR">
    <meta property="og:type" content="profile">
    <meta property="og:title" content="آمار تحلیلی و تعرفه تبلیغات {name} (@{u}) | BookBloger">
    <meta property="og:description" content="شناسنامه آماری هوشمند، نرخ تعامل، تعداد فالوور ({foll}) و بررسی پست‌های {name} در دایرکتوری بوک‌بلاگرها.">
    <meta property="og:url" content="{page_canonical}">
    <meta property="og:site_name" content="BookBloger - دایرکتوری بوک‌بلاگرهای ایران">
    <meta property="og:image" content="{avatar_abs_url}">
    <meta property="og:image:alt" content="{name}">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="آمار تحلیلی و تعرفه {name} (@{u})">
    <meta name="twitter:description" content="تحلیل زنده اینستاگرام {name}، میانگین لایک و ویو و تعرفه رسمی همکاری.">
    <meta name="twitter:image" content="{avatar_abs_url}">

    <!-- JSON-LD Structured Data Schemas -->
    <script type="application/ld+json">
{schema_person_json}
    </script>
    <script type="application/ld+json">
{schema_breadcrumb_json}
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
            max-width: 920px;
            margin: 0 auto;
        }}

        .nav-back {{
            margin-bottom: 25px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }}

        .back-btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: #818cf8;
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            background: var(--card-bg);
            border: 1px solid var(--border);
            padding: 8px 16px;
            border-radius: 10px;
            transition: all 0.2s;
        }}

        .back-btn:hover {{
            background: #1e293b;
            color: #fff;
            transform: translateX(4px);
        }}

        .top-links-group {{
            display: flex;
            gap: 8px;
        }}

        .top-posts-link {{
            color: #38bdf8;
            text-decoration: none;
            font-size: 13px;
            font-weight: 700;
            background: rgba(56, 189, 248, 0.12);
            border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 8px 12px;
            border-radius: 10px;
            transition: all 0.2s;
        }}

        .top-posts-link:hover {{
            background: rgba(56, 189, 248, 0.22);
        }}

        .profile-header {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            margin-bottom: 25px;
            position: relative;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
        }}

        .rank-tag {{
            display: inline-block;
            background: rgba(99, 102, 241, 0.15);
            color: #818cf8;
            border: 1px solid rgba(99, 102, 241, 0.3);
            padding: 4px 14px;
            border-radius: 9999px;
            font-size: 12.5px;
            font-weight: 700;
            margin-bottom: 15px;
        }}

        .avatar-wrap {{
            width: 110px;
            height: 110px;
            margin: 0 auto 18px;
            position: relative;
        }}

        .avatar {{
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #38bdf8;
            background: #0f172a;
            box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
        }}

        h1.profile-name {{
            font-size: clamp(20px, 4.5vw, 28px);
            font-weight: 900;
            margin-bottom: 6px;
            color: #fff;
        }}

        .profile-handle {{
            font-size: 15px;
            color: #818cf8;
            direction: ltr;
            display: inline-block;
            margin-bottom: 14px;
            font-weight: 600;
            text-decoration: none;
        }}

        .profile-handle:hover {{
            text-decoration: underline;
        }}

        .profile-bio-box {{
            background: rgba(11, 15, 25, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 12px 18px;
            border-radius: 12px;
            font-size: 13.5px;
            color: #cbd5e1;
            margin-bottom: 20px;
            line-height: 1.6;
            max-width: 650px;
            margin-left: auto;
            margin-right: auto;
        }}

        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            background: rgba(11, 15, 25, 0.7);
            padding: 18px;
            border-radius: 14px;
            margin-bottom: 24px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }}

        .metric-box .num {{
            font-size: clamp(18px, 4vw, 26px);
            font-weight: 900;
            color: #f1f5f9;
        }}

        .metric-box .num.highlight {{
            color: #fbbf24;
        }}

        .metric-box .lbl {{
            font-size: 12px;
            color: var(--text-secondary);
            margin-top: 4px;
        }}

        .header-actions {{
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .btn {{
            padding: 11px 22px;
            border-radius: 10px;
            font-size: 14px;
            font-weight: 700;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
        }}

        .btn-ig {{
            background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
            color: #fff;
        }}

        .btn-ig:hover {{
            opacity: 0.92;
            transform: translateY(-2px);
        }}

        .btn-coco {{
            background: #1e293b;
            color: #38bdf8;
            border: 1px solid #334155;
        }}

        .btn-coco:hover {{
            background: #334155;
            color: #fff;
            transform: translateY(-2px);
        }}

        .section-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 24px;
            margin-bottom: 25px;
        }}

        .section-title {{
            font-size: 17px;
            font-weight: 800;
            color: #38bdf8;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 12px;
        }}

        .analytics-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-bottom: 16px;
        }}

        .analytics-item {{
            background: rgba(11, 15, 25, 0.5);
            border: 1px solid var(--border);
            padding: 14px;
            border-radius: 12px;
            text-align: center;
        }}

        .analytics-item .a-lbl {{
            font-size: 11.5px;
            color: var(--text-secondary);
            margin-bottom: 4px;
        }}

        .analytics-item .a-val {{
            font-size: 17px;
            font-weight: 900;
            color: #f8fafc;
        }}

        .analytics-item .a-val.green {{
            color: #4ade80;
        }}

        .analytics-item .a-val.gold {{
            color: #fbbf24;
        }}

        .audience-box {{
            background: rgba(11, 15, 25, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.04);
            padding: 14px;
            border-radius: 12px;
            font-size: 13.5px;
            color: #cbd5e1;
            line-height: 1.7;
        }}

        .media-posts-grid {{
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}

        .media-post-item {{
            background: rgba(11, 15, 25, 0.5);
            border: 1px solid var(--border);
            padding: 16px;
            border-radius: 14px;
            transition: all 0.2s;
        }}

        .media-post-item:hover {{
            border-color: #38bdf8;
            background: rgba(11, 15, 25, 0.7);
        }}

        .media-post-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}

        .media-type-badge {{
            background: rgba(99, 102, 241, 0.2);
            color: #818cf8;
            border: 1px solid rgba(99, 102, 241, 0.35);
            padding: 3px 10px;
            border-radius: 6px;
            font-size: 11.5px;
            font-weight: 700;
        }}

        .media-counts {{
            display: flex;
            gap: 14px;
            font-size: 13px;
            font-weight: 700;
            color: #cbd5e1;
            direction: ltr;
        }}

        .media-caption {{
            font-size: 13px;
            color: #e2e8f0;
            line-height: 1.6;
            margin-bottom: 12px;
        }}

        .media-action {{
            display: flex;
            justify-content: flex-end;
        }}

        .post-direct-link {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: #38bdf8;
            text-decoration: none;
            font-size: 12.5px;
            font-weight: 700;
            background: rgba(56, 189, 248, 0.1);
            border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 6px 14px;
            border-radius: 8px;
            transition: all 0.2s;
        }}

        .post-direct-link:hover {{
            background: #38bdf8;
            color: #0b0f19;
            transform: translateY(-2px);
        }}

        .package-item {{
            background: rgba(11, 15, 25, 0.5);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px;
            margin-bottom: 12px;
        }}

        .pkg-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 6px;
        }}

        .pkg-title {{
            font-weight: 700;
            font-size: 14px;
            color: #e2e8f0;
        }}

        .pkg-price {{
            font-weight: 900;
            color: #fbbf24;
            font-size: 14.5px;
        }}

        .pkg-desc {{
            font-size: 12.5px;
            color: #94a3b8;
            line-height: 1.6;
        }}

        .pricing-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        .pricing-list li {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(11, 15, 25, 0.4);
            padding: 10px 14px;
            border-radius: 8px;
            font-size: 13.5px;
            border: 1px solid rgba(255, 255, 255, 0.03);
        }}

        .pricing-list li b {{
            color: #38bdf8;
            font-size: 14px;
        }}

        .campaign-section {{
            background: var(--campaign-gradient);
            border: 1px solid rgba(168, 85, 247, 0.35);
            border-radius: 18px;
            padding: 24px;
            text-align: center;
            margin-bottom: 25px;
        }}

        .campaign-badge {{
            display: inline-block;
            background: rgba(236, 72, 153, 0.2);
            color: #f472b6;
            border: 1px solid rgba(236, 72, 153, 0.4);
            padding: 3px 12px;
            border-radius: 9999px;
            font-size: 12px;
            font-weight: 700;
            margin-bottom: 10px;
        }}

        .campaign-title {{
            font-size: 18px;
            font-weight: 800;
            color: #fff;
            margin-bottom: 8px;
        }}

        .campaign-desc {{
            font-size: 13.5px;
            color: #cbd5e1;
            margin-bottom: 16px;
            line-height: 1.6;
        }}

        .contact-buttons {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .contact-btn {{
            padding: 9px 16px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 700;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }}

        .contact-btn-group {{
            background: linear-gradient(135deg, #229ED9 0%, #0284c7 100%);
            color: #fff;
        }}

        .contact-btn-tg {{
            background: #1e293b;
            color: #38bdf8;
            border: 1px solid #334155;
        }}

        .contact-btn-ig {{
            background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
            color: #fff;
        }}

        footer {{
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid var(--border);
            color: var(--text-secondary);
            font-size: 12.5px;
        }}

        .footer-links {{
            margin-top: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .footer-links a {{
            color: #94a3b8;
            text-decoration: none;
            font-size: 12px;
        }}

        .footer-links a:hover {{
            color: #38bdf8;
        }}

        @media (max-width: 640px) {{
            body {{
                padding: 16px 10px 40px;
            }}
            .profile-header {{
                padding: 20px 14px;
            }}
            .avatar-wrap {{
                width: 90px;
                height: 90px;
            }}
            .metrics-grid {{
                padding: 12px 6px;
                gap: 6px;
            }}
            .analytics-grid {{
                grid-template-columns: 1fr;
                gap: 10px;
            }}
            .header-actions {{
                flex-direction: column;
            }}
            .btn {{
                width: 100%;
                justify-content: center;
            }}
            .contact-buttons {{
                flex-direction: column;
                width: 100%;
            }}
            .contact-btn {{
                width: 100%;
                justify-content: center;
            }}
            .pkg-header {{
                flex-direction: column;
                align-items: flex-start;
            }}
        }}
    </style>
</head>
<body>
<div class="container">
    <div class="nav-back">
        <a href="../index.html" class="back-btn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            بازگشت به دایرکتوری اصلی
        </a>
        <div class="top-links-group">
            <a href="{TG_GROUP_URL}" target="_blank" rel="noopener noreferrer" class="top-posts-link" style="color:#38bdf8; border-color:#229ED9;">
                👥 گروه تلگرام (بلاگران کتاب)
            </a>
            <a href="../top-posts.html" class="top-posts-link">
                🔥 ۱۰ پست برتر
            </a>
            <a href="../top-100-posts.html" class="top-posts-link">
                🏆 ۱۰۰ پست برتر
            </a>
        </div>
    </div>

    <div class="profile-header">
        <div class="rank-tag">{rank_label}</div>
        <div class="avatar-wrap">
            <img src="{avatar_src}" alt="{name} - بلاگر کتاب اینستاگرام" class="avatar" onerror="this.src='https://ui-avatars.com/api/?name={u}&background=random'">
        </div>
        <h1 class="profile-name">{name}</h1>
        <a href="{ig_url}" target="_blank" rel="noopener noreferrer" class="profile-handle" title="مشاهده پروفایل اینستاگرام {u}">@{u}</a>

        <div class="profile-bio-box">
            <b>بیوگرافی:</b> {clean_bio}
        </div>

        <div class="metrics-grid">
            <div class="metric-box">
                <div class="num highlight">{foll}</div>
                <div class="lbl">تعداد فالوورها</div>
            </div>
            <div class="metric-box">
                <div class="num">{flwing}</div>
                <div class="lbl">فالویینگ‌ها</div>
            </div>
            <div class="metric-box">
                <div class="num">{posts}</div>
                <div class="lbl">تعداد پست‌ها</div>
            </div>
        </div>

        <div class="header-actions">
            <a href="{ig_url}" target="_blank" rel="noopener noreferrer" class="btn btn-ig" title="پیج اینستاگرام {name}">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                مشاهده پیج اینستاگرام
            </a>
            <a href="{coco_url}" target="_blank" rel="noopener noreferrer" class="btn btn-coco" title="داشبورد تحلیلی کوکو">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
                داشبورد آنالیز اختصاصی
            </a>
            {extra_channel_btn}
        </div>
    </div>

    <!-- Analytics KPIs Section -->
    <div class="section-card">
        <div class="section-title">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.21 15.89A10 10 0 1 1 8 2.83"/><path d="M22 12A10 10 0 0 0 12 2v10z"/></svg>
            تحلیل هوشمند و شاخص‌های آماری BoxAPI
        </div>
        <div class="analytics-grid">
            <div class="analytics-item">
                <div class="a-lbl">میانگین لایک پست‌ها</div>
                <div class="a-val green">{avg_likes}</div>
            </div>
            <div class="analytics-item">
                <div class="a-lbl">میانگین کامنت‌ها</div>
                <div class="a-val gold">{avg_comments}</div>
            </div>
            <div class="analytics-item">
                <div class="a-lbl">میانگین ویو و پخش ریلز</div>
                <div class="a-val">{avg_plays}</div>
            </div>
            <div class="analytics-item">
                <div class="a-lbl">نرخ تعامل (ER)</div>
                <div class="a-val green">{er}</div>
            </div>
            <div class="analytics-item">
                <div class="a-lbl">تخمین بازدید هر استوری</div>
                <div class="a-val gold">{story_view}</div>
            </div>
            <div class="analytics-item">
                <div class="a-lbl">سطح اینفلوئنسری</div>
                <div class="a-val" style="font-size:14px;">{tier}</div>
            </div>
        </div>
        <div class="audience-box">
            <b>🎯 پرسونای مخاطبان و تارگت کمپین:</b> {aud_prof}
        </div>
    </div>

    <!-- Recent Media Analytics with direct post links -->
    <div class="section-card">
        <div class="section-title">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>
            تحلیل آخرین پست‌ها و ریلزها به همراه لینک مستقیم
        </div>
        <div class="media-posts-grid">
            {media_cards_html}
        </div>
    </div>

    <!-- Pricing Section -->
    <div class="section-card">
        <div class="section-title">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" width="20" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>
            تعرفه تبلیغات و شرایط همکاری
        </div>
        {pricing_html}
    </div>

    <!-- Campaign CTA -->
    <div class="campaign-section">
        <div class="campaign-badge">🚀 اجرای کمپین و روابط عمومی</div>
        <h2 class="campaign-title">هماهنگی و اجرای کمپین با {name}</h2>
        <p class="campaign-desc">برای هماهنگی تبلیغات، ارسال کتاب، نقد و بررسی و اجرای کمپین‌های هدفمند با این بلاگر با مدیریت <b>ریک سانچز</b> در ارتباط باشید یا در گروه بوک‌بلاگرها مطرح کنید.</p>
        <div class="contact-buttons">
            <a href="{TG_GROUP_URL}" target="_blank" rel="noopener noreferrer" class="contact-btn contact-btn-group">👥 گروه تلگرام: بلاگران کتاب</a>
            <a href="https://t.me/m4tinbeigipv" target="_blank" rel="noopener noreferrer" class="contact-btn contact-btn-tg">تلگرام: @m4tinbeigipv</a>
            <a href="https://instagram.com/m4tinbeigi" target="_blank" rel="noopener noreferrer" class="contact-btn contact-btn-ig">اینستاگرام: @m4tinbeigi</a>
        </div>
    </div>

    <footer>
        <p>گردآوری، تحلیل داده و مدیریت: <b>ریک سانچز (Rick Sanchez)</b> | دایرکتوری بوک‌بلاگرها</p>
        <div class="footer-links">
            <a href="{TG_GROUP_URL}" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; font-weight:700;">👥 گروه تلگرام (بلاگران کتاب)</a>
            <span>•</span>
            <a href="../3d.html">🌌 کهکشان سه‌بعدی</a>
            <span>•</span>
            <a href="../top-posts.html">🔥 ۱۰ پست برتر</a>
            <span>•</span>
            <a href="../top-100-posts.html">🏆 ۱۰۰ پست برتر</a>
            <span>•</span>
            <a href="../sitemap.xml">نقشه سایت</a>
        </div>
    </footer>
</div>
</body>
</html>
"""

    out_file = os.path.join(PAGES_DIR, f"{slug}.html")
    with open(out_file, 'w', encoding='utf-8') as pf:
        pf.write(page_html)

print(f"Successfully rebuilt all {len(sorted_bloggers)} subpages with sarabooks pricing and @BookishDays telegram channel!")
