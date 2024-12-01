# from django.utils.deprecation import MiddlewareMixin


# class JWTCookieMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         access_token = request.COOKIES.get('access_token')
#         if access_token:
#             print("TOEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
#             print(access_token)
#             print("TOEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
#             request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
