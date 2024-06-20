from django.db import models

class api(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    question = models.TextField()
    correct_answer = models.CharField(max_length=255)
    incorrect_answers = models.JSONField()  


    

# Now you can store the data in your model like this:

# quiz = api(
#     type="multiple",
#     difficulty="easy",
#     category="Animals",
#     question="Which class of animals are newts members of?",
#     correct_answer="Amphibian",
#     incorrect_answers='["Fish", "Reptiles", "Mammals"]'  # Store incorrect answers as a JSON array in a string
# )
# quiz.save()

