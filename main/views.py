from django.shortcuts import render
def show_main(request):
    context = {
        'app1':'Game ',
        'app2':'Collections',
        'name': 'Cyberpunk 2077',
        'amount':'1',
        'desc':'An open-world, action-adventure RPG set in the megalopolis of Night City, where you play as a cyberpunk mercenary wrapped-up in a do-or-die fight for survival.',
        'price':'59.99',
        'cat':'Action RPG, Open World',
        'pub':'CD PROJEKT RED',
        'nama':'Clarence Grady',
        'kelas':'PBP A'

    }

    return render(request, "main.html", context)
# Create your views here.
