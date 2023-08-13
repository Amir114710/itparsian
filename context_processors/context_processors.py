from apps.mysite.models import Question , Footer 


def query(request):
    question = Question.objects.all() [:1]
    footer = Footer.objects.all()
    for item in footer:
        attribute1=item.attribute.all()[:5]
        attribute2=item.attribute.all()[5:10]
    return {'footer':footer , 'question':question , 'attribute1':attribute1 , 'attribute2':attribute2}
