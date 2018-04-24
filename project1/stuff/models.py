from django.db import models


class ModelLinks(models.Model):
    link_to_1 = "../pages/1"
    link_to_2 = "../pages/2"
    link_to_3 = "../pages/3"
    link_to_4 = "../pages/4"
    text_to_1 = "Go to page 1"
    text_to_2 = "Go to page 2"
    text_to_3 = "Go to page 3"
    text_to_4 = "4 is Missing..."
    link_to_pages = "../../../stuff/pages/"
    text_to_pages = "Go back to Pages List"


class Page(models.Model):
    page_name = models.CharField(max_length=50)
    page_h1_text = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.page_name