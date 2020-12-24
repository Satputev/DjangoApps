from django.shortcuts import render

def info(request):
    e_Info={"manager":
                {
                    "101":{
                        "name":"Ravi",
                        "salary":185000.00
                    },
                    "102":{
                        "name":"Kumar",
                        "salary":28500.00
                    }
                },
        "Developer":{
            "1001":{
                "name":"mohan",
                "salary":55000.00,
                "project":"CMS"
            },
            "1002":{
                "name":"krushna",
                "salary":85000.00,
                "project":"HMS"
            }
        },
        "Designer": {
            "1AD": {
                "name": "Rani",
                "salary": 15000.00,
            },
            "2AD": {
                "name": "myki",
                "salary": 25000.00,
            }
        },
        "Tester":{
            "01":{
                "name":"murali",
                "salary":30000.00
            }
        }

    }
    return render(request,"index.html",{"data":e_Info})