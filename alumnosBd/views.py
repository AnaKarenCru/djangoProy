from django.shortcuts import render
from alumnosBd.models import Alumnos

def mostrarIndex(request):
    return render (request, 'index.html')


def mostrarLista(request):
    alum = Alumnos.objects.all().values()
    datos = {'alum': alum}
    return render (request, 'lista_alumnos.html', datos)

def mostrarFormsRegistrar(request):
    return render (request, 'forms_registrar.html')

def mostrarFormsActualizar(request, id):
    try: 
        alum = Alumnos.objects.get(id = id) #primer id nombre del atributo de la clase Alumnos y segundo id es el parametro 
        datos = {'alum': alum}
        return render (request, 'forms_actualizar.html', datos)
    except: 
        alum = Alumnos.objects.all().values()
        datos = {
            'alum': alum,
            'r2' : 'El ID ('+str(id)+') No existe, imposible actualizar'}
        return render (request, 'lista_alumnos.html', datos)

def insertarAlumno(request):
    if request.method == 'POST':
        nom = request.POST['txtnom']
        ape = request.POST['txtape']
        matri = request.POST['txtmatri']
        camp = request.POST['cbocamp']
        carre = request.POST['cbocarre']
        sem = request.POST['txtsem']
        mate = request.POST['txtmate'] 
        alum = Alumnos(
            nombre=nom, 
            apellido=ape, 
            matricula=matri,
            campus= camp, 
            carrera= carre, 
            semestre=sem, 
            materias=mate)
        alum.save()
        datos = {'r': 'Registro exitoso'} #respuesta de exito
        return render(request, 'forms_registrar.html', datos)
    else: 
        datos = {'r2': 'Error, no se puede procesar solicitud'} #respuesta de error 
        return render(request, 'forms_registrar.html', datos)
    

def actualizarAlumno(request, id):
    if request.method == 'POST':
        nom = request.POST['txtnom']
        ape = request.POST['txtape']
        matri = request.POST['txtmatri']
        camp = request.POST['cbocamp']
        carre = request.POST['cbocarre']
        sem = request.POST['txtsem']
        mate = request.POST['txtmate'] 
        alum = Alumnos.objects.get(id = id)
        alum.nombre = nom
        alum.apellido = ape
        alum.matricula = matri
        alum.campus = camp
        alum.carrera = carre
        alum.semestre = sem
        alum.materias = mate
        alum.save()
        alum = Alumnos.objects.all().values()
        datos = {
            'alum': alum, 
            'r': 'Datos modificados correctamente.'} #respuesta de exito
        return render(request, 'lista_alumnos.html', datos)
    else: 
        datos = {'r2': 'Error, no se puede procesar solicitud'} #respuesta de error 
        return render(request, 'lista_alumnos.html', datos)
    

def eliminarAlumno(request, id): 
    try: 
        alum = Alumnos.objects.get(id = id)
        alum.delete()
        alum = Alumnos.objects.all().values()
        datos = {
            'alum': alum, 
            'r' : 'Registro eliminado correctamente'
            }
        return render(request, 'lista_alumnos.html', datos)
    except: 
        alum = Alumnos.objects.all().values()
        datos = {
            'alum': alum, 
            'r2' : 'El ID ('+str()+') No existe y no se puede eliminar'
            }
        return render(request, 'lista_alumnos.html', datos)