from django.shortcuts import render

def studentInfo(request):
    student_data={"101":{"name":"Ravi","marks":[29,85,15,65,95,'A']},
                  "102":{"name":"Kumar","marks":[52,'A',65,99,"A",75]},
                  "103":{"name":"Mohan","marks":[65,95,"A",45,89,12]},
                  "104":{"name":"Krushna","marks":["A","A",96,33,85,75]}
                  }
    return render(request,"marks.html",{"data":student_data})
