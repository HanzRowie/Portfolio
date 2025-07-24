from django.shortcuts import render

# Create your views here.

def index(request):
    dict1={
        "name":"Hanz Rowie Gurung",
        "age":25,   
        "place":"India",
        "occupation":"Web Developer",
        "about":"I am a passionate Python Django developer with a strong focus on backend development and building robust, scalable web applications. I specialize in using Django and Django REST Framework to create clean, maintainable APIs and dynamic web applications. I have hands-on experience integrating databases, managing user authentication, implementing permission controls, and connecting third-party APIs.",
        "skills":"Python",
        "skills1":"Django",
        "skills2":"Django Rest Framework",
        "Birthday":"2000-01-01",
        "email":"hanzrowie@gmail.com",
        "phone":"098765432",
        "city":"Nepal",
        "Age":"25",
        "Degree":"Bachelor of Computer Application",
        "Freelance":"Available",  
        "resume":"Dedicated and detail-oriented Python Django Developer with hands-on experience in building dynamic and secure web applications. Proficient in Django and Django REST Framework (DRF) "
        "for developing RESTful APIs, database management, "
        "and implementing authentication and permission systems."
        " Strong understanding of backend logic, clean architecture, "
        "and scalable solutions.",
        "title1":'Custom Web Application Development',
        "description1":'Developed a custom web application using Django, implementing user authentication, database management, and RESTful APIs for seamless data interaction.',
        "title2":'API Development with Django REST Framework',
        "description2":'Created RESTful APIs using Django REST Framework, enabling efficient data exchange between the frontend and backend, with robust authentication and permission controls.',
        "title3":'Database Management and Integration',
        "description3":'Managed database operations using Django ORM, ensuring data integrity and efficient querying. Integrated third-party APIs for enhanced functionality.',
        "title4":"Authentication & Authorization Systems",
        "description4":"I implement user authentication, registration, password reset, and permission control using Django’s built-in auth system and JWT tokens.",
        "title5":"Admin Dashboard Customization",
        "description5":"I create or customize Django Admin interfaces for easy data management, reporting, and monitoring by non-technical users.",
        "title6":"Bug Fixes & Performance Optimization",
        "description6":"I troubleshoot and fix issues in existing Django applications and optimize performance to ensure fast and reliable operations."

    }
    return render(request,"index.html",dict1)
 
def portfoliodetails(request):
    dict2={
        "full_name":"Hanz",
        "age":25,   
        "place":"India",
        "occupation":"Web Developer",
    }
    return render(request,"portfolio-details.html",dict2)
def servicedetails(request):
    return render(request,"service-details.html")
def starterpage(request):
    return render(request,"starter-page.html")

