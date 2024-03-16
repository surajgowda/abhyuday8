from django.db import models

class TeamDetails(models.Model):
    department = models.CharField(max_length=100,null=True, blank=True)
    lead_name_1 = models.CharField(max_length=100,null=True, blank=True)
    lead_name_2 = models.CharField(max_length=100,null=True, blank=True)
    lead_name_3 = models.CharField(max_length=100,null=True, blank=True)
    lead_name_4 = models.CharField(max_length=100,null=True, blank=True)
    lead_phone_1 = models.CharField(max_length=20,null=True, blank=True)
    lead_phone_2 = models.CharField(max_length=20,null=True, blank=True)
    lead_phone_3 = models.CharField(max_length=20,null=True, blank=True)
    lead_phone_4 = models.CharField(max_length=20,null=True, blank=True)
    
    def __str__(self):
        return self.department

class Task(models.Model):
    dept = models.ManyToManyField('TeamDetails')
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
class Objectives(models.Model):
    team_name = models.ForeignKey(TeamDetails, on_delete=models.CASCADE)
    objectives_list = models.TextField()

    def __str__(self):
        return f"Objectives for {self.team_name}"