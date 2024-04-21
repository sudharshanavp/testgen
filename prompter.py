import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models

generation_config = {
    "max_output_tokens": 2048,
    "temperature": 0.7,
    "top_p": 0.4,
    "top_k": 32,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}


def generate(no_of_cases, regex):
    vertexai.init(project="refined-outlet-420415", location="us-central1")
    model = GenerativeModel("gemini-1.0-pro-vision-001")

    input_prompt = f'You are a software QA expert, I want you to write a set of {no_of_cases} test cases to test if the regex is correctly witten for an entity with given requirement. The given requirements is must be a "{regex}" Please cover the edge cases and corner cases as much as possible while generating the test cases and segregate them in positive and negative classes. Generate the output in a format easy to display on a webpage such as a markdown table.'

    responses = model.generate_content(
        [input_prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    return responses
