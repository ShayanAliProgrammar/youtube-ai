from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

# Initialize The Gemini Model

model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=1, top_p=0.9)


PROMPT_TEMPLATE = """
You are a helpful Q&A AI assistant that only generate response based on the provided video transcription.

Follow these instructions:
1. Get the video transcript from user.
2. Answer only based on that video transcription.
3. Make sure that you get your response for the user query from the transcription or generate one on your own.

TRANSCRIPTION: {video_transcription}

QUERY: {query}

ANSWER: """


def get_video_transcription():
    video_url = input("Enter a Youtube Video Url from youtube.com only: ").strip()

    while video_url.startswith("https://www.youtube.com/watch") != True:
        video_url = input(
            "\nPlease Enter a valid Youtube video (eg: https://www.youtube.com/watch?v=video_id): "
        ).strip()

    video_id = video_url.split("?v=")[1]

    try:
        video_transcript = YouTubeTranscriptApi.get_transcript(video_id)

        return TextFormatter().format_transcript(video_transcript)
    except Exception as e:
        raise e


def get_answer(query, video_transcription):

    prompt = (PromptTemplate.from_template(PROMPT_TEMPLATE)).format_prompt(
        query=query, video_transcription=video_transcription
    )

    try:

        return model.invoke(prompt).content

    except Exception as e:
        return "Something went wrong!"


if __name__ == "__main__":
    transcript = get_video_transcription()

    while True:
        print(
            "\n--------------------------------------------------------------------------------------------------------------------------\n"
        )
        prompt = input("Prompt (q to quit): ").strip()

        if prompt.lower() == "q":
            break

        answer = get_answer(prompt, video_transcription=transcript)

        print("\nAnswer: ", answer)
