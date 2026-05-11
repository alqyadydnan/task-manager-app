[app]

title = مدير المهام
package.name = taskmanager
package.domain = org.taskapp

requirements = python3,kivy==2.1.0,kivymd==1.1.1,sqlite3

version = 1.0
orientation = portrait

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# 🔥 أهم التغييرات - إصدارات مستقرة ومجربة
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30
android.ndk_api = 21

# إصدار build-tools الصحيح
android.build_tools = 30.0.3

android.archs = arm64-v8a, armeabi-v7a

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

fullscreen = 0
