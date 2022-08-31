from email import contentmanager, message
from multiprocessing import context
from django.shortcuts import render
from .forms import ContatoForms, ProdutoModelForm
from django.contrib import messages
from .models import produto_pre_save, Produto, Base


def index(request):
    context = { 'produtos' : Produto.objects.all()}
    return render (request, 'index.html', context)

def contato(request):
    form = ContatoForms(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print(f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}')

            messages.success(request,'E-mail enviado com sucesso!')
            form = ContatoForms()
        else:
            messages.error('Falha ao envio do E-mail')

            
    context = {'form': form}
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()

            messages.success(request,'Produto cadastado com sucesso!')
            form = ProdutoModelForm()
        else:
            messages.error('Produto negado!')
    else:       
        form = ProdutoModelForm()

    context = {
        'form' : form 
    }
    return render(request,'produto.html', context)

    