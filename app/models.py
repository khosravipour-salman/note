from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create = models.DateTimeField(auto_now=True)
    modify = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - create: {self.create} - modify: {self.modify}'

# Add category field later


# create urls.py     .....
# create list view url  ....
# connect urls.py to project urls.py   ....
# add view  ....
# setup templates settings  .....
# create base html
# create blocks --> title, navbar, content / body
# get all objects query
# send data into template
# for loop on list objects
# customize front-end
