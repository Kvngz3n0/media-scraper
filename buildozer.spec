[app]
title = MediaScraper
package.name = mediascraper
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0

requirements = python3,kivy,requests,beautifulsoup4

orientation = portrait

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 25b