from django.db import models
from django.utils import timezone

class UserFeedbacks(models.Model):
    FEEDBACK_CHOICE =(
        (None, ''),
        (True, 'Good'),
        (False, 'Bad')
    )
    feedback = models.BooleanField(choices=FEEDBACK_CHOICE, null=True, blank=True)
    offer_id = models.IntegerField(default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['created_at']

    def __str__(self):
        feedback_val = self.feedback
        if feedback_val is None:
            feedback_val = 'No Feedback'
        elif feedback_val is True:
            feedback_val = 'Good'
        else:
            feedback_val = 'Bad'
        return feedback_val
