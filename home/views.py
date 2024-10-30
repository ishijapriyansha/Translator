from django.shortcuts import render
from googletrans import Translator
# Create your views here.



def translate_view(request):
    translated_text = ""
    if request.method == "POST":
        input_text = request.POST.get("text")
        current_language = request.POST.get("current_language")
        target_language = request.POST.get("target_language")

        translator = Translator()

        result = translator.translate(input_text, src=current_language, dest=target_language)
        translated_text = result.text

    return render(request, "hello.jinja", {"translated_text": translated_text})
