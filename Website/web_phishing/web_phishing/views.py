from django.shortcuts import render
from .forms import URLForm
from . import phishy_checker_code  # Import your phishing detection code

def check_phishing(request):
    result = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            result = phishy_checker_code.check_url_phishy(url)
            print("Result View:", result)
    else:
        form = URLForm()

    return render(request, 'index.html', {'form': form, 'result': result})
