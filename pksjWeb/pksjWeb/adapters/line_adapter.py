from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect
from django.urls import reverse

class NoPromptSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # คุณสามารถเพิ่ม debug log เพื่อตรวจสอบว่าเรียกใช้งานหรือไม่
        print("pre_social_login called - skipping confirmation")

        # ไม่ต้องทำอะไรเพื่อข้ามหน้า confirm

    def get_connect_redirect_url(self, request, socialaccount):
        return reverse('account_profile')  # เปลี่ยนเป็น URL หลังล็อกอินที่คุณต้องการ

    def get_login_redirect_url(self, request):
        return reverse('account_profile')  # เปลี่ยนเป็น URL หลังล็อกอินที่คุณต้องการ

