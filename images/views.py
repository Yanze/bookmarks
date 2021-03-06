from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successsfully')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(request.GET)

    return render(request, 'images/create.html', {'section': 'images', 'form': form})
