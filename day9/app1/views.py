from django.shortcuts import render

def home(request):
    # student_details = {
    #     "data":[
    #         ["Sagar",24,"Hyderabd"],
    #         ["Priya",17,"Karachi"],
    #         ["Pramod",23,"Bilaspur"],
    #         ["Virendra",22,"Raipur"]
    #     ]
        
    # }

    student_details = {
        "data":[
            {"name":"Sagar","age":24,"address":"Hyderabd"},
            {"name":"Priyanshu","age":17,"address":"Karachi"},
            {"name":"Pramod","age":23,"address":"Bilaspur"},
            {"name":"Virendra","age":22,"address":"Raipur"}
        ]
        
    }
    return render(request,'index.html',context=student_details)

# Create your views here.
