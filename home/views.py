# translate_app/views.py
from django.shortcuts import render
from googletrans import Translator

def translate_view(request):
    translated_text = ""
    input_text = ""
    current_language = ""
    target_language = ""

    if request.method == "POST":
        input_text = request.POST.get("text")
        current_language = request.POST.get("current_language")
        target_language = request.POST.get("target_language")

        # Initialize translator
        translator = Translator()

        # Translate text
        result = translator.translate(input_text, src=current_language, dest=target_language)
        translated_text = result.text

    # Render template with translated text and form data
    return render(request, "hello.jinja", {
        "translated_text": translated_text,
        "input_text": input_text,
        "current_language": current_language,
        "target_language": target_language
    })
