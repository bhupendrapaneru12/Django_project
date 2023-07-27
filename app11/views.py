from django.shortcuts import render, HttpResponse
from app11.models import person, user_table

# Create your views here.\

# def addobject(request):
#     obj=person.objects.create(
#         name="ram",
#         age=13,
#         is_student=True,
#         email="ram@gamil.com",
#         message="yes i m a student")
#     obj.save()
#     return HttpResponse("ha ha ha ")


# def contactform(request):
#     if request.method=='POST':
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         email = request.POST.get('email')
#         is_student = request.POST.get('is_student')
#         message = request.POST.get('message')
#         photo =request.FILES.get('photo')
#         # print(name,age,email,is_student,message)

#         obj=person.objects.create(
#             name=name,
#             age=age,
#             email=email,
#             is_student = is_student,
#             message = message,
#             photo = photo)
#         obj.save()
#         return HttpResponse('user created successfully')
#         persons =person.objects.all()
#         return render(request,'person.html',{'person':person})
    
#     return render(request,'person.html')   


def registeruser(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        photo =request.FILES.get('photo')

        obj=user_table.objects.create(
            name=name,
            email=email,
            password = password,
            photo = photo
            )
        obj.save()
        return HttpResponse('user created successfully')
    ob = user_table.objects.all()
    return render(request, 'register.html',{'ob': ob})


def user_delete(request, user_id):
    obj = user_table.objects.get(id=user_id)
    obj.delete()
    return HttpResponse("user deleted succesfully")


def user_update(request, user_id):
    obj = user_table.objects.get(id=user_id)

    if request.method=="POST":
        obj.name= request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.password = request.POST.get('password')
        obj.photo = request.FILES.get('photo')

        obj.save()
        return HttpResponse('value updated succesfully!')
    return render(request, 'register.html')