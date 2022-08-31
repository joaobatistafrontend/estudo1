from dataclasses import fields
from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Nensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        mail = EmailMessage (
            subject= 'E-mail enviando pelo sistema Django ',
            body= conteudo,
            from_email= 'contatodjango@gmail.com',
            to =['contatodjango@gmail.com',],
            headers={'Replay-To', email},
        )
        mail.send()
        
class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['nome','preco','estoque','imagem']