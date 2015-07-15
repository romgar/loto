from django.shortcuts import render

# Create your views here.
from algo.logic import LotoGrid


def generate_grids(request):

    grids = []
    for i in range(100):
        grid = LotoGrid()
        grid.generate_numbers()
        disp_grid = grid.export_for_display()
        grids.append(disp_grid)

    return render(request, 'algo/grid.html', {
        'grids': grids
    })
