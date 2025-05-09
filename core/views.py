from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from core.forms import DoctorForm  # Asegúrate de que forms.py contiene la definición de DoctorForm
from core.models import Doctor

def home(request):
    data = {
        'title': 'App Medica',
        'description': 'Gesion de citas medicas',
        'author': 'Daniel Vera',
        'year': 2025,
    }
    # doctores = Doctor.objects.all()
    # data["doctores"]=doctores
    #return HttpResponse("<h1>Hello,Mi primer pagina con django</h1>")
    #return JsonResponse(data)  
    return render(request, 'home.html', data)

def doctor_list(request):
    doctors = Doctor.objects.all()

    print(request.method)
    print(request.GET)
    # return JsonResponse(list(doctors.values()), safe=False)

    query = request.GET.get('q', None)
    print(query)

    if query:
        doctors = Doctor.objects.filter(name__icontains=query)
    else:
        doctors = Doctor.objects.all()

    context = {
        'doctors': doctors,
        'title': 'Listado de doctores'
    }

    return render(request, 'doctor/list.html', context)


def doctor_create(request):
    context={'title':'Ingresar Doctor'}
    print("metodo: ",request.method)
    if request.method == "GET":
        # print("entro por get")
        
        form = DoctorForm()# instancia el formulario con los campos vacios
        context['form'] = form
        return render(request, 'doctor/create.html', context)
    else:
        #  print("entro por post")
        form = DoctorForm(request.POST) # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            # doctor = form.save(commit=False)# lo tiene en memoria
            # doctor.user = request.user
            # doctor.save() # lo guarda en la BD
            return redirect('core:doctor_list')
        else:
            context['form'] = form
            return render(request, 'doctor/create.html',context) 
        #return JsonResponse({"message": "voy a crear un doctor"})



def doctor_update(request, id):
    context = {'title': 'Actualizar Doctor'}
    doctor = Doctor.objects.get(pk=id)

    if request.method == "GET":
        form = DoctorForm(instance=doctor)  # Instancia el formulario con los datos del doctor
        context['form'] = form
        return render(request, 'doctor/create.html', context)

    else:
        form = DoctorForm(request.POST, instance=doctor)

        if form.is_valid():
            form.save()
            return redirect('core:doctor_list')
        else:
            context['form'] = form
            return render(request, 'doctor/create.html', context)
        


def doctor_delete(request,id):
    doctor=None
    try:
        doctor = Doctor.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Doctor a Eliminar','doctor':doctor,'error':''}
            return render(request, 'doctor/delete.html',context)  
        else: 
            doctor.delete()
            return redirect('core:doctor_list')
    except:
        context = {'title':'Datos del Doctor','doctor':doctor,'error':'Error al eliminar al doctor'}
        return render(request, 'doctor/delete.html',context)
    
