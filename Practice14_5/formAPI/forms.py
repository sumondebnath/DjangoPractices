from django import forms
import datetime

class djangoFormApi(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder":"Enter Your Name "}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Enter Your Email "}))
    comment = forms.CharField(label="Your Comments Type Here...",widget=forms.Textarea(attrs={"row":2, "default":10}))
    # date = forms.DateField(label="Select Date:",widget=forms.DateInput(attrs={"type":"date"}))
    Date = forms.DateField(widget=forms.NumberInput(attrs={"type":"date"}))

    Years = ["1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005"]
    birthYear = forms.DateField(widget=forms.SelectDateWidget(years=Years))

    day = forms.DateField(initial=datetime.date.today)

    colors = [("red","RED"), ("yellow","YELLOW"), ("blue","BLUE")]
    color = forms.ChoiceField(choices=colors, widget=forms.RadioSelect)
    color1 = forms.ChoiceField(choices=colors)
    color2 = forms.MultipleChoiceField(choices=colors, widget=forms.CheckboxSelectMultiple)

    check = forms.BooleanField(label="Check Box")

    TypeChoice = [(1, "one"), (2, "two"), (3, "three")]
    typeChoice = forms.TypedChoiceField(choices=TypeChoice)

    dateTime = forms.DateTimeField(widget=forms.DateInput(attrs={"type":"datetime-local"}))

    decimel = forms.DecimalField()

    duretion = forms.DurationField()

    file = forms.FileField(widget=forms.FileInput())
    filePath = forms.FilePathField(path="formAPI/")

    float = forms.FloatField()
    integer = forms.IntegerField()

    ipAddress = forms.GenericIPAddressField(label="Enter IP Address ")

    nullBool = forms.NullBooleanField()

    regex = forms.RegexField

    slug = forms.SlugField()

    time = forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))

    url = forms.URLField(widget=forms.URLInput())

    uuid = forms.UUIDField()