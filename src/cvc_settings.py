from src.sidebar_related import *
class CVC:
    NAME = "John Doe"
    PROFESSION = "Developer"
    CITY = "Berlin"
    COUNTRY = "Germany"
    PHONE_NUMBER = "+49abcxyz"
    MAIL = "john.doe@xyz.com"
    SUMMARY_CONTENT = "This is my summary"
    SIDEBAR_ELEMENTS = [
        Head('Profiles'),
            Links(['xyz.de','xyz.en'], ['GitHub', 'LinkedIn']),
        Head('Technical Skills'),
            Title('Programming Languages'),
                Content('Python, Java, C, Kotlin'),
            Title('Web Development'),
                Content('HTML, CSS, Javascript, jinja'),
            Title('Frameworks & Libraries'),
                Content('Flask, tkinter, win32api, selenium, sqlite3, pytest'),
            Title('Databases'),
                Content('SQLite, SQLAlchemy'),
            Title('Project & Development Tools'),
                Content('Git, GitHub, Git Actions'),
            Title('OS'),
                Content('Windows, Linux, Mac OS X, WSL Ubuntu'),
            Title('Other'),
                Content('OOP'),
        Head('Soft Skills'),
            Title('Problem-solving'),
            Title('Teamwork'),
            Title('Communication'),
            Title('Analytical thinking'),
            Title('Fast learner'),
        Head('Languages'),
            Title('German'),
                Content('Native'),
            Title('English'),
                Content('B2'),
    ]
    PROJECTS = []
    EDUCATION = []
    EXPERIENCE = []