from django.shortcuts import render, get_object_or_404
from .forms import pdfForm
from .models import pdfs
from django.http import FileResponse
# Create your views here.

def index(request):
    if request.method == 'POST':
        fm=pdfForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm=pdfForm()
    fp=pdfs.objects.all()
    return render(request,'pp/index.html',{'fp':fp,'fm':fm})

def pindex(request,pdfs_id):  
    pdf = get_object_or_404(pdfs, pk=pdfs_id)
    response = FileResponse(pdf.pdf,content_type='application/pdf')
    return response



