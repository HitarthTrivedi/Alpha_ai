import ollama
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set to the first voice


def career_advisor_chatbot(user_input):
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "system",
             "content": "You are a career advisor who will briefly answer the questions asked in a manner the user feels human-like interaction."},
            {"role": "user", "content": user_input},
        ],
    )
    return response['message']['content']


def finance_advisor(user_input):
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "system",
             "content": "You have to act like a finance advisor, who will advise the user about his finance-related queries in simple language."},
            {"role": "user", "content": user_input},
        ],
    )
    return response['message']['content']
def gym_advisor(user_input):
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "system",
             "content": "You have to act like professional gym trainer and advice user about dos and donts according to the query and briefly advice them.You can also provide a plan they could follow accordin to their bulk or cut phase."},
            {"role": "user", "content": user_input},
        ],
    )
    return response['message']['content']


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print("User  said:", query)
        return query.lower()  # Return the recognized query in lowercase

    except Exception as e:
        print(e)
        print("Pardon me, sir.")
        return None  # Return None if recognition fails


if __name__ == "__main__":
    speak("Welcome, to Alpha, AI")
    speak("Which field do you need me to advise you? Career, finance, or gym")

    while True:
        
        query = take_command()

        if query is None:
            continue

        if query in ["exit", "quit"]:
            speak("Goodbye!")
            break

        if query == "career":
            speak("Please ask your career-related question.")
            while True:
                user_query = take_command()
                if user_query is None:
                    continue
                if user_query in ["exit", "quit"]:
                    speak("Goodbye!")
                    break
                response = career_advisor_chatbot(user_query)
                if response:
                    speak("Advisor: " + response)
                else:
                    speak("I didn't get a response from the advisor.")

        elif query == "finance":
            speak("Please ask your finance-related question.")
            while True:
                user_query = take_command()
                if user_query is None:
                    continue
                if user_query in ["exit", "quit"]:
                    speak("Goodbye!")
                    break
                response = finance_advisor(user_query)
                if response:
                    speak("Advisor: " + response)
                else:
                    speak("I didn't get a response from the advisor.")



        elif query == "gym":
            speak("Please ask your gym related question.")
            while True:
                user_query = take_command()
                if user_query is None:
                    continue
                if user_query in ["exit", "quit"]:
                    speak("Goodbye!")
                    break
                response = gym_advisor(user_query)
                if response:
                    speak("Advisor: " + response)
                else:
                    speak("I didn't get a response from the advisor.")
