from django.shortcuts import render

def index(request):
    return  render(request,'index.html')

def main(request):
    mt=request.GET.get("m")
    if mt=='1':
        movie="Telgu Movies"
        title=["1","Fida","Racegurram","Rular"]

        return render(request,"main.html",{"movie":movie,"title":title})

    elif mt=='2':
        movie="Hindi Movies"
        title=["3 Idiots","Dangal","MS Dhoni","Sachin"]

        return render(request,"main.html",{"movie":movie,"title":title})

    else :
        movie = "English Movies"
        title = ["Rambo","Babel","Doom","Magic Man"]

        return render(request,"main.html",{"movie":movie,"title":title})



def video(request):
    m=request.GET.get("m")
    if m=='1':
        url = "https://www.youtube.com/embed/xcxyCh1Lc3c"
        title="1"
    elif m== '2':
        url= "https://www.youtube.com/embed/AVtvjfoXNXc"
        title="Fida"


    elif m == '3':
        url = "https://www.youtube.com/embed/yCt-YUbs7H4"
        title="Racegurram"

    elif m == '4':
        url="https://www.youtube.com/embed/T-Hg8HzWM8M"
        title="Rular"

    elif m == '9':
        url = "https://www.youtube.com/embed/4vWg5yJuWfs"
        title="Rambo"
    elif m=='10':
        url="https://www.youtube.com/embed/gzrHrTVaqJs"
        title="Babel"
    elif m=='11':
        url="https://www.youtube.com/embed/FkklG9MA0vM"
        title="Doom"
    elif m=='12':
        url="https://www.youtube.com/embed/Q9t5EUwrDiM"
        title="Magic Man"
    elif m=='5':
        url="https://www.youtube.com/embed/K0eDlFX9GMc"
        title="3-Idiots"
    elif m=='6':
        url="https://www.youtube.com/embed/x_7YlGv9u1g"
        title="Dangal"


    elif m=='7':
        url="https://www.youtube.com/embed/6L6XqWoS8tw"
        title="MS Dhoni"

    else:
        url= "https://www.youtube.com/embed/8gTeE6pa4Kg"
        title="Sachin"


    return render(request,"video.html",{"url":url})
