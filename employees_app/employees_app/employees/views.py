from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.

# def home(request):
#     html = f'<h1>{request.method}: This is home.</h1>'
#     # could return --> return HttpResponseNotFound()
#     # which is the same as --> return HttpResponse(status=404)
#     return HttpResponse(
#         html,
#         status=202,
#         # content_type='text/plain',
#         headers={
#             'x-current-header': 'Django',
#         }
#     )

def home(request):
    return render(request, 'index.html')


def not_found(request):
    return HttpResponseNotFound()
    # or --> raise Http404()


def go_to_home(request):
    return redirect(to='/')


def department_details(request, id):
    if not isinstance(id, int):
        pass

    return HttpResponse(f'This is department {id}.')


def list_departments(request):
    return HttpResponse('This is a list of all departments.')
