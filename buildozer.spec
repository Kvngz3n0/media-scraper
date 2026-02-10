[app]
title = MediaScraper
package.name = mediascraper
package.domain = org.example
version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv

requirements = python3,kivy,requests,beautifulsoup4

orientation = portrait

# -------- ANDROID SETTINGS (CRITICAL) --------
android.api = 33
android.minapi = 21

# FORCE BUILD-TOOLS (PREVENTS 36.x LICENSE PROMPT)
android.sdk_build_tools = 33.0.2
android.accept_sdk_license = True

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.ndk = 25b
