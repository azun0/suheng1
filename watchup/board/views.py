from django.shortcuts import render

def board_list(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session': login_session }

    return render(request, 'board/board_list.html', context)

def board_write(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session': login_session }
    
    return render(request, 'board/board_write.html', context)
# Create your views here.
