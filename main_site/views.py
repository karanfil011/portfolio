from django.shortcuts import render
from .models import MyExperience, MyEducation, MySkills, AboutMe, Portfolio, Status



def index(request):
    template_name = 'home.html'
    about_me = AboutMe.objects.last()
    my_skills = MySkills.objects.last()
    my_education = MyEducation.objects.all()
    my_education_about = MyEducation.objects.last()
    my_experience = MyExperience.objects.all()
    my_experience_about = MyExperience.objects.last()
    status = Status.objects.last()
    portfolio = Portfolio.objects.all()
    portfolio_about = Portfolio.objects.last()

    args = {
        'about_me': about_me,
        'my_skills': my_skills,
        'my_education': my_education,
        'my_education_about': my_education_about,
        'my_experience': my_experience,
        'my_experience_about': my_experience_about,
        'status': status,
        'portfolio': portfolio,
        'portfolio_about': portfolio_about,
    }

    return render(request, template_name, args)
