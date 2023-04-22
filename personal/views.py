from django.shortcuts import render

# Create your views here.

def home_screen_view(request):

	context = {}
	# context['some_string'] = "this is some string that I am passing to the view"
	# context['some_number'] = 543633

	# context = {
	# 	'some_string': "this is some string that I am passing to the view",
	# 	'some_number': 543633,
	# }

	list_of_values = []
	list_of_values.append("first entry")
	list_of_values.append("second entry")
	list_of_values.append("third entry")
	list_of_values.append("fourth entry")
	context['list_of_values'] = list_of_values

	return render(request, "personal/home.html", context)