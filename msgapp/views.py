from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from msgapp.models import Message

# Create your views here.
def about(request):
    return HttpResponse("This is from about page")

def delete(request,eid):
    m=Message.objects.filter(id=eid)
    print(m)
    m.delete()
    return redirect('/dashboard')


    #return HttpResponse("Employee id is:"+eid)    

class ContactFrom(View):
    def get(self,request,eid):
       # return HttpResponse("This is from class Base view")
       return HttpResponse("Employee id is:"+eid)

def hello(request):
    d={}
    d['x']='itvedant'
    #return render(request,'hello.html',{'x':'itvedant'})  
    d['y']={10,20,30}
    d['a']=10
    d['b']=20
    d['c']=30
   #lst=[{ 'id':1, 'name':'hardik','city':'pune'},{'id':2,'name':'divya','city':'jalgaon'}]
   #d['data']=lst
   #return render(request,'hello.html',d)


def main(request):
    return render(request,'main.html')

def product(request):
    return render(request,'product.html')

def cart(request):
    return render(request,'cart.html')


#def gm(request): 
   # x='itvedant'
    #d={}
    #d['x']='itvedant'
    #d={'x':'itvedant'}
   # return render(request,'gm.html',d)  
  
def gm(request):

    if request.method=='GET':
         return render(request,'gm.html')
    else:
        n=request.POST['uname']
        e=request.POST['uemail']
        mob=request.POST['mob']
        msg=request.POST['msg']
        '''print(n)
        print(e)
        print(m)
        print(msg)'''

        m=Message.objects.create(name=n,email=e,mob=mob,msg=msg)
        m.save()

        return HttpResponse("Data Fatched..!!")


def dashboard(request):
    m=Message.objects.all()
    #print(m)
    contaxt={}
    contaxt['data']=m
    #return HttpResponse("Data Fatched from database..!!")
    return render(request,'dashboard.html',contaxt)



def edit(request,eid):
    if request.method == 'GET':
        m=Message.objects.filter(id=eid)
        #print(m)
        contaxt={}
        contaxt['data']=m
        return render(request,'edit.html',contaxt)

    else:
       n=request.POST['name']
       e=request.POST['uemail']
       mob=request.POST['mob']
       msg=request.POST['msg']
       
       m=Message.objects.filter(id=eid)
       m.update(name=n,email=e,mob=mob,msg=msg)
       return redirect('/dashboard')
