import os, sys, subprocess, platform

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pdfkit

from .models import Profile


# if platform.system() == "Windows":
#         pdfkit_config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
# else:
#         os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable)
#         WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')], 
#             stdout=subprocess.PIPE).communicate()[0].strip()
#         pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)


def input(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        summary = request.POST.get('summary', "")
        degree = request.POST.get('degree', "")
        school = request.POST.get('school', "")
        university = request.POST.get('university', "")
        previous_work = request.POST.get('previous_work', "")
        skills = request.POST.get('skills', "")

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work, skills=skills)
        profile.save()

    return render(request, 'pdf/input.html')

def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({"user_profile": user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options=options) # , configuration=pdfkit_config)
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = f'resume_{user_profile.name}.pdf'
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response

def list(request):
    profile_list = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profile_list': profile_list})