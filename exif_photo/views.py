from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ExifPageView(TemplateView):
    template_name = 'exif.html'
    word = 'If you see this it worked'
    words = {'test': word,
            }
    context = {'words': words}

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
