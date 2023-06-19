from django.contrib import admin
from django.urls import path, include
from theme import views

urlpatterns = [
    path('', views.index, name="home"),
    path('profile', views.profile, name="profile"),
    path('about', views.about, name="about"),
    path('resources', views.resources, name="resources"),


    path('courses', views.courses, name="courses"),
    path('course-data-analytics', views.course1, name="course1"),
    path('course-ibm-data-science', views.course2, name="course2"),
    path('course-ethical-hacking', views.course3, name="course3"),
    path('course-joy-computing', views.course4, name="course4"),
    path('course-meta-ar', views.course5, name="course5"),
    path('course-machine-learning', views.course6, name="course6"),
    path('course-google-ux', views.course7, name="course7"),
    path('course-seo-marketing', views.course8, name="course8"),

    path('event-iem-sportify', views.event1, name="event1"),
    path('event-mlh-hack4u', views.event2, name="event2"),
    path('event-meta-seminar', views.event3, name="event3"),
    path('event-ge-autocad', views.event4, name="event4"),

    
    path('contact', views.contact, name="contact"),
    path('thanks', views.thanks, name="thanks"),
    path('login', views.signin, name="login"),
    path('logout', views.signout, name="logout"),
    path('signup', views.signup, name="signup")
]