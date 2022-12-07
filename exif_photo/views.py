from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ExifPhoto
from django.conf import settings
from django.http import HttpResponseRedirect
from .forms import ExifPhotoForm
from PIL import Image

class HomePageView(TemplateView):
    template_name = 'home.html'

def ExifPageView(request):
    submitted = False
    photo_list = ExifPhoto.objects.all()
    if request.method == 'POST':
        form = ExifPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = ExifPhotoForm()
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request, 'exif.html', {'form': form, 'photo_list': photo_list, 'submitted': submitted, 'media_url': settings.MEDIA_URL}) 

def success(request):
    return HttpResponse('successfully uploaded')

'''
class ExifPageView(TemplateView):
    template_name = 'exif.html'
    word = 'If you see this it worked'
    words = {'test': word,
            }
    context = {'words': words}
'''

#class DotMethodPageView(TemplateView):
#    template_name = 'dotmethod.html'


from .models import DotMethodModel
from .forms import DotMethodForm

def DotMethodPageView(request):
    # Set variables and seperate user, @, domain
    
    email_list = []

    if request.method == 'POST':
        form = DotMethodForm(request.POST)
        form.save()
    form = DotMethodForm()



    '''
    email = input('Enter your email: ')
    email_list = [email]
    domain = r'$@.+\.com^'
    at = email.find('@')
    domain = email[at:]
    user = email[:at]

    new_email = ''
    counter = 0

    dotpos = 0
    dotpos_over = 0

    for i in range(len(user) - 1):
        # Create second list of user chars, insert '.' and add 
        # new email to the main email list until chars run out
        user_list = list(user)
        dotpos += 1
        user_list.insert(dotpos, '.')
        new_email = ''.join(user_list) + domain
        if dotpos > len(user_list) - 1:
            print('Full')
        else:
            email_list.append(new_email)
    
    #return email_list
        #dotpos_over += 1
        #dotpos = dotpos - (len(user_list) + dotpos_over)
        #user_list = user_list.insert(dotpos_over, '.')

    '''

    return render(request, 'dotmethodview.html')
