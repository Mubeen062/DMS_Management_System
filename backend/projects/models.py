from django.db import models

class Company(models.Model):
    Cmpny_Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Cmpny_Name


class Project(models.Model):
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    prjct_Name = models.CharField(max_length=255)

    def __str__(self):
        return self.prjct_Name

class Project_detail(models.Model):
    drctry_Name = models.CharField(max_length=255)
    prjct_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    prnt_ID = models.PositiveIntegerField(null=True, blank=True)  # Set null=True here
    file_Name = models.CharField(max_length=100, null=True, blank=True)
    output_Name = models.CharField(max_length=100, null=True, blank=True)



    def __str__(self):
        return self.drctry_Name
