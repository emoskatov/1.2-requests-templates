from django.http import HttpResponse
from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}


def dish_views(request, dish):
    servings = request.GET.get('servings')
    new_data = {}
    for ing, amo in DATA[dish].items():
        if servings:
            new_data[ing] = amo * (int(servings))
            context = {'recipe': new_data}
        if not servings:
            new_data[ing]=amo
            context = {'recipe': new_data}

    return render(request, template_name='calculator/index.html', context=context)


def home_view(request):

    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}

    return render(request, template_name='home/home.html', context=context)





# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:







