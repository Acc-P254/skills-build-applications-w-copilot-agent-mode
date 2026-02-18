from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Usuń istniejące dane
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Tworzenie drużyn
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Tworzenie użytkowników
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Tworzenie treningów
        workout1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout', difficulty='Medium')
        workout2 = Workout.objects.create(name='Strength Builder', description='Full body strength training', difficulty='Hard')

        # Tworzenie aktywności
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date=timezone.now().date())

        # Tworzenie leaderboard
        Leaderboard.objects.create(user=users[0], score=120)
        Leaderboard.objects.create(user=users[1], score=150)
        Leaderboard.objects.create(user=users[2], score=110)
        Leaderboard.objects.create(user=users[3], score=130)

        self.stdout.write(self.style.SUCCESS('Baza octofit_db została wypełniona przykładowymi danymi!'))
