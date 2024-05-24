# django_api_stt

https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
1.) install this file

2.) extraxt to c drive

3.) open "edit the system environment viriable"
4.) click "environment viriables"
5.) under "user variables for " click path
6.) click "new"
7.) then browse the ffmpeg/bin then click ok and ok

in terminal
pip install django django-cors-headers djangorestframework

then ipconfig find the

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : 
   IPv4 Address. . . . . . . . . . . :  <----------------------this Ip address
   Subnet Mask . . . . . . . . . . . : 
   Default Gateway . . . . . . . . . : 
                                       

then in terminal:

python manage.py runserver 192.168.0.0:8000

change the 192.168.0.0 into your real ip addres
