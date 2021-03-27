from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = "Your URL"
iam_apikey_s2t = "Your API Key"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)

audio = 'audio-file.flac'

with open(audio, mode="rb")  as flac:
    response = s2t.recognize(audio=flac, content_type='audio/flac', model='en-US_BroadbandModel', background_audio_suppression=0.5)

transcript = response.result['results'][0]['alternatives'][0]['transcript']
print(transcript)
