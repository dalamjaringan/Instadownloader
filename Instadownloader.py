#!/usr/bin/env python
# -*-coding:utf-8 -*-

'''
@File    :   Instadownloader.py
@Time    :   2022/12/06 15:22:13
@Author  :   @menjelangpadam 
@Version :   1.0
@Contact :   abdul.hanif@students.untidar.ac.id
@License :   (C)Copyright 2022-2023, Abdul Hanif
@Desc    :   None
'''

#memuat instaloader
import instaloader

#setting nama profile sebagai nama folder
target_dl = input('Masukkan Username IG: ')

#Download Semua Post Instagramc
print('Downloading Media.......')
instaloader.Instaloader().download_profile(target_dl, profile_pic_only=False)
print('Download Selesai!')
print('Foto tersimpan di folder: '+ target_dl)