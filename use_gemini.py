from configparser import ConfigParser
import google.generativeai as genai

config = ConfigParser()
config.read('credentials.ini')
api_key = config['API_KEY']['google_api_key']
genai.configure(api_key=api_key)

gemini_pro_model = genai.GenerativeModel('gemini-pro')


def getOutput(prompt: str):
    response = gemini_pro_model.generate_content(
        prompt,
        safety_settings=[
            {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
             'threshold': 'block_none'
             },
            {'category': 'HARM_CATEGORY_HATE_SPEECH',
             'threshold': 'block_none'
             },
            {'category': 'HARM_CATEGORY_HARASSMENT',
             'threshold': 'block_none'
             },
            {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',
             'threshold': 'block_none'
             }
        ],
        generation_config=genai.types.GenerationConfig(
            temperature=0.3
        )
    )
    return response.text


