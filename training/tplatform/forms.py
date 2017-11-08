from django import forms

class JoinForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	institution = forms.CharField(required=True)
	country = forms.CharField(required=True)
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	)
	def __init__(self, *args, **kwargs):
		super(JoinForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "Full name"
		self.fields['contact_email'].label = "Email address"
		self.fields['institution'].label = "Institution"
		self.fields['country'].label = "Country"
		self.fields['content'].label = "What experience, ideas or skills can you offer the training team?"

class RequestTrainingForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	institution = forms.CharField(required=True)
	country = forms.CharField(required=True)
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	)
	def __init__(self, *args, **kwargs):
		super(RequestTrainingForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "Full name"
		self.fields['contact_email'].label = "Email address"
		self.fields['institution'].label = "Institution"
		self.fields['country'].label = "Country"
		self.fields['content'].label = "We would love to run a workshop for your society! Please tell us a little bit more about what you would like from us."


class RequestResourcesForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	institution = forms.CharField(required=True)
	country = forms.CharField(required=True)
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	)
	def __init__(self, *args, **kwargs):
		super(RequestResourcesForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "Full name"
		self.fields['contact_email'].label = "Email address"
		self.fields['institution'].label = "Institution"
		self.fields['country'].label = "Country"
		self.fields['content'].label = "What topics, skills, or areas would you find it useful to have a video or a document on?"


class FeedbackForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	institution = forms.CharField(required=True)
	country = forms.CharField(required=True)
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	)
	def __init__(self, *args, **kwargs):
		super(FeedbackForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "Full name"
		self.fields['contact_email'].label = "Email address"
		self.fields['institution'].label = "Institution"
		self.fields['country'].label = "Country"
		self.fields['content'].label = "Please send us your feedback on a workshop, thoughts on how it could improve, or any ideas on how to develop our training"
