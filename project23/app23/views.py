from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def main(request):
    players=request.POST.getlist('palyers')
    name=[]
    if players:
        for x in players:
            if x == 'Batsman':
                names = {"batsman": ['Sachin Tendulkar', 'MS Dhoni', 'Virat Kohli', 'Rohit Sharma']}
                name.append(names)
            if x == 'Bowler':
                names = {"Bowlers": ['Jsaprit Bumrah', 'Dale Sten', 'Michel stark', 'Lasith Malinga']}
                name.append(names)
            if x == 'Allrounder':
                names = {"Allrounder": ['Yuvraj Sign', 'Shane Watson', 'Ravindra Jadeja', 'Kapil dev']}
                name.append(names)

        return render(request, 'main.html', {"data": name})
    else:
        return render(request,'err.html')


def my11(request):
    m11=request.POST.getlist('t1')
    if m11:
        return render(request,'my11.html',{"my11":m11})
    else:
        return render(request,'not11.html')
