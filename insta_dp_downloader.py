'''
Use below line to install required python module
pip install instaloader
'''
import instaloader

ig = instaloader.Instaloader()

dp = input("Enter instagram username")

ig.download_profile(dp,profile_pic_only=True)
