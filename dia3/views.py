from django.shortcuts import render, redirect

# Create your views here.

def counter(req):
    #para guardar en sesión
    veces = req.session.get('veces',None)
    if veces is None:
        veces = 0
    veces += 1
    req.session['veces'] = veces
    return render(req, 'counter.html')

def reset_counter(req):
    req.session['veces'] = 0
    return redirect('/counter')