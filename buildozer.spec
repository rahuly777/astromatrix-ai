[app]
# (str) Source directory where the application files are located
source.dir = .

# (str) Title of your application
title = AstroMatrix AI

# (str) Package name
package.name = astromatrix

# (str) Package domain (needed for android packaging)
package.domain = org.astromatrix

# (str) Source files to include (let it include py, png, etc.)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
# Note: Keep requirements simple to avoid exit code 1 compilation errors
requirements = python3,kivy

# (str) Custom icon (app logo on phone)
icon.filename = logo.png

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android arch to build for
android.archs = arm64-v8a, armeabi-v7a
