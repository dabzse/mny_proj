from django.shortcuts import render
from django.db.models.query import QuerySet
from .models import LearnPlace, Certification
from .card_contact import get_contacts
from .card_affiliate import get_affiliates
from .helper_cv_list import *


def home(request):
    return render(request, "devel/home.html", {})


def cert(request, filter_by=None):
    # Map of filter keys to display names
    sl_tags = {
        'python': 'Python, R, ML, DS',
        'ai': 'AI',
        'cj': 'C, C++, C#, Java',
        'web': 'Web + SQL',
        'other': 'Other',
    }

    ud_tags = {
        'py': 'PYthon related',
        'ai': 'AI related',
        'git': 'Git related',
        'eth': 'Ethical Hacking',
        'web': 'Web related',
        'net': 'Networking',
        'wd': 'WebDev, FullStack',
        'sql': 'SQL related',
        'cj': 'C, CPP, C#, Java, Kotlin',
        'tux': 'Linux related',
        'cms': 'WordPress, Drupal',
        'other': 'Other',
        'dm': 'Digital Marketing, Google Analytics, SEO, Cryptocurrency',
        'mso': 'MSOffice apps: Word, Excel, PowerPoint; Google Office apps: Docs, Sheets, Slides',
    }

    learn_places = LearnPlace.objects.all()

    # Initialize the data structure
    certifications_by_place = {}

    # Filtering logic
    if filter_by is None or filter_by == 'all':
        # Group certifications by LearnPlace
        for place in learn_places:
            certifications_by_place[place.name] = Certification.objects.filter(learnt_from=place.id)
        certifications = Certification.objects.all()  # Used for filtered view
    else:
        # Handle specific filter case
        certifications_by_place = {
            place.name: Certification.objects.filter(learnt_from=place.id) for place in learn_places
        }
        if filter_by == 'sl':
            certifications = Certification.objects.filter(learnt_from=1)
        elif filter_by == 'gh':
            certifications = Certification.objects.filter(learnt_from=2)
        elif filter_by == 'ud':
            certifications = Certification.objects.filter(learnt_from=3)

    # Calculate counts
    sl_count = certifications_by_place.get('SoloLearn', []).count() if isinstance(certifications_by_place.get('SoloLearn'), QuerySet) else len(certifications_by_place.get('SoloLearn', []))
    gh_count = certifications_by_place.get('GrassHopper', []).count() if isinstance(certifications_by_place.get('GrassHopper'), QuerySet) else len(certifications_by_place.get('GrassHopper', []))
    ud_count = certifications_by_place.get('UDemy', []).count() if isinstance(certifications_by_place.get('UDemy'), QuerySet) else len(certifications_by_place.get('UDemy', []))
    all_count = sl_count + gh_count + ud_count

    context = {
        'sl_count': sl_count,
        'gh_count': gh_count,
        'ud_count': ud_count,
        'all_count': all_count,
        'learn_places': learn_places,
        'certifications_by_place': certifications_by_place,
        'certifications': certifications,
        'filter_by': filter_by,
        'sl_tags': sl_tags,
        'ud_tags': ud_tags,
    }

    return render(request, "devel/cert.html", context)


def cv(request):
    self_education = get_self_education()
    computer_skills = get_computer_skills()
    abilities = get_abilities()
    edu_studies = get_edu_studies()

    context = {
        'self_education': self_education,
        'computer_skills': computer_skills,
        'abilities': abilities,
        'edu_studies': edu_studies,
    }
    return render(request, "devel/cv.html", context)


def devel(request):  # helper_contact.py
    cards = get_contacts()

    context = {
        'cards': cards,
    }

    return render(request, "devel/devel.html", context)


def affiliates(request):
    cards = get_affiliates()

    context = {
        'cards': cards,
    }

    return render(request, "devel/affiliates.html", context)
