from django.shortcuts import render

def Terms(request):
    header = 'Terms and Conditions'
    return render(request, 'terms.html',{'header': header})

def FAQ(request): 
    header ="Frequently Asked Questions"
    return render(request, 'FAQ.html',{'header': header})

def help(request): 
    header ="help"
    return render(request, 'help.html',{'header': header})  

