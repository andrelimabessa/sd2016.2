from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponse

def start(request):
    html = """
    <h1>Bem vindo</h1>        
    <a href="/admin/">Admin</a><br>
    <label>Na sessão admin você pode cadastrar novos usuários utilizando o login do super usuário criado</label><br><br>

    <a href="/login">Login</a><br>    
    <label>Tela de login</label><br><br>

    <a href="/app/">Jogo</a><br>    
    <label>Na sessão jogo você pode cadastrar novo jogo e então realizar jogadas</label>
    
    """
    return HttpResponse(html)

def home(request):
    html = """
    <h1>Batalha Naval APP</h1>
    <a href="/app/jogo/">CRUD Jogo</a><br>                
    """
    return HttpResponse(html)

def sair(request):
    logout(request)
    return redirect('/login')