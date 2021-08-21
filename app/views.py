from django.shortcuts import redirect, render
from .models import Network, Show

# Create your views here.

def start(request):
    return redirect("/shows")

def shows(request):
    context = {
        "shows" : Show.objects.all()
    }
    return render(request,"show.html",context)

def new_show(request):
    context = {
        "networks" : Network.objects.all()
    }
    return render(request,"show_add.html",context)

def create_show(request):
    if request.method == "POST":
        print(request.POST)
        #Fecha llega en YY-MM-DD

        #Cuando se crea un network se obtiene un parametro str desde el request con el nombre ingresado por usuario en form
        if request.POST["new_network"] == "True":
            add_network = Network.objects.create(nombre = request.POST["network"])       
        #Cuando se selecciona una network creada se obtiene el id desde el request   
        elif request.POST["new_network"] == "False":
            add_network = Network.objects.get(id=int(request.POST["network"]))

        nuevo_show = Show.objects.create(
            titulo = request.POST["titulo"],
            network = add_network,
            release_date = request.POST["date"],
            descripcion = request.POST["descripcion"]
        )

    return redirect("/shows")

def mostrar_show(request,id_show):
    context = {

        "show" : Show.objects.get(id=id_show)          
    }
    return render (request, "show_id.html",context)

def edit_show(request,id_show):
    context = {
        "show" : Show.objects.get(id=id_show),
        "networks" : Network.objects.all()
    }
    return render(request, "show_edit.html",context)



def update_show(request,id_show):
    if request.method == "POST":
        print(request.POST)

        #Cuando se crea un network se obtiene un parametro str desde el request con el nombre ingresado por usuario en form
        if request.POST["new_network"] == "True":
            add_network = Network.objects.create(nombre = request.POST["network"])       
        #Cuando se selecciona una network creada se obtiene el id desde el request   
        elif request.POST["new_network"] == "False":
            add_network = Network.objects.get(id=int(request.POST["network"]))

        show = Show.objects.get(id=id_show)
        show.titulo = request.POST["titulo"],
        show.network = add_network,
        show.release_date = request.POST["date"],
        show.descripcion = request.POST["descripcion"]
        show.save()
    return redirect(f"/shows/{id_show}")



def destroy_show(request,id_show):
    show = Show.objects.get(id=id_show)
    show.delete()
    return redirect("/shows")