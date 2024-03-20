# Youtube Transcript Q&A Assistant

You may use this Python script to create a useful AI Q&A assistant that answers questions based on YouTube video transcriptions. The langchain_google_genai and youtube_transcript_api libraries are used to retrieve transcripts and offer answers.

## Features.

- Get transcripts of YouTube videos from URLs.
- Respond to customer inquiries and create video transcripts.

## Installation

1. Clone the repository:

    ```bash
   git clone https://github.com/ShayanAliProgrammar/youtube-ai.git
   ```

2. Install the essential prerequisites.

    ```bash
    pip install -r requirements.txt
   ```

## Usage

1. Run this script:

    ```bash
   python main.py
   ```

2. When asked, provide the URL to an allowed YouTube video.
3. Submit your question to the helper here.
4. Receive the response generated from the video transcription that was provided.

## Example

Here's a sample usage of the script:

```bash
Enter a YouTube video URL from youtube.com only: https://www.youtube.com/watch?v=video_id

--------------------------------------------------------------------------------------------------------------------------

Prompt (q to quit): How does the AI assistant work?

Answer: The AI assistant retrieves the video transcript from the specified YouTube URL and generates responses depending on the transcript content.

--------------------------------------------------------------------------------------------------------------------------

Prompt (q to quit): q
```
