from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Choices for categories
    WORK = 'Work'
    STUDY = 'Study'
    PERSONAL = 'Personal'
    WORKOUT = 'Workout'  # Combined category
    TRAVEL = 'Travel'
    APPOINTMENT = 'Appointment'
    ENTERTAINMENT = 'Entertainment'

    CATEGORY_CHOICES = [
        (WORK, 'Work'),
        (STUDY, 'Study'),
        (PERSONAL, 'Personal'),
        (WORKOUT, 'Workout'),
        (TRAVEL, 'Travel'),
        (APPOINTMENT, 'Appointment'),
        (ENTERTAINMENT, 'Entertainment'),
    ]


    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
    )

    task_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Allow for an optional description

    starting_time = models.TimeField()
    ending_time = models.TimeField()

    # Choices for priorities
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default=MEDIUM,
    )

    # Choices for status
    TODO = 'To Do'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'

    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=TODO,
    )

    starting_date = models.DateField()
    ending_date = models.DateField()

    # Choices for days of the week
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    DAYS_OF_WEEK_CHOICES = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]

    days_of_week = models.CharField(
        max_length=20,
        choices=DAYS_OF_WEEK_CHOICES,
        blank=True,
        null=True,
    )

    # Add a field for additional notes or comments related to the task
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.task_name



