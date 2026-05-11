[app]

title = مدير المهام
package.name = taskmanager
package.domain = org.taskapp

requirements = python3,kivy==2.1.0,kivymd==1.1.1,sqlite3

version = 1.0
orientation = portrait

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a, armeabi-v7a

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

fullscreen = 0
