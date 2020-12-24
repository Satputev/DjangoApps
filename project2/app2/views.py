from django.http import HttpResponse
def index(request):
	data='''<html>
	<body bgcolor=yellow>
	<h1>Welcome to Django</h1>
	</body>
	</html>'''
	return HttpResponse(data)

