from django.shortcuts import render
from django.http import HttpResponse
from web3 import Web3
from eth_account.messages import encode_defunct

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        public_key = request.POST.get('public_key')
        user = User.objects.filter(username=username, public_key=public_key).first()
        if user is None:
            return HttpResponse("Invalid username or password")
        else:
            return HttpResponse("Logged in successfully")
    return render(request, 'login.html')

def verify_signature(address, signature, message):
    message_hash = encode_defunct(text=message)
    try:
        public_key = Account.recover_message(message_hash, signature=signature)
        recovered_address = Web3.toChecksumAddress(Account.from_key(public_key).address)
        if address == recovered_address:
            return True
    except:
        pass
    return False

@csrf_exempt
def authenticate(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        signature = request.POST.get('signature')
        message = request.POST.get('message')
        if verify_signature(address, signature, message):
            user = User.objects.get_or_create(address=address)
            login(request, user)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error'})