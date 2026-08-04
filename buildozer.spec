[app]
title = JARVIS
package.name = jarvisapp
package.domain = org.tonystark
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, kivy, kivymd, google-genai, requests, reportlab, openpyxl, python-docx, android
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.permissions = INTERNET, CALL_PHONE, READ_SMS, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
[buildozer]
log_level = 2
warn_on_root = 1
