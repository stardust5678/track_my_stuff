from django.shortcuts import render

def home(request):
    return render(request, 'my_stuff/dashboard.html')

def package_detail(request, package_id):
    context = {'package_id': package_id}
    return render(request, 'my_stuff/package_detail.html', context)