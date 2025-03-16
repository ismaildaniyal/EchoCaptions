# EchoCaption: Audio to Video Caption Generator

EchoCaption is a Streamlit-based application that transcribes audio into text, generates captions using Google's Gemini API, and creates avatar-based videos via the HeyGen API. This tool automates the process of converting spoken audio into dynamic video presentations with captions.

## Features
- 🎤 **Audio Transcription**: Uses Whisper AI to transcribe audio files (.mp3, .wav) to text.
- 📝 **Caption Generation**: Generates captions from the transcribed text using Google's Gemini API.
- 🎬 **Avatar Video Creation**: Creates avatar-based videos using the HeyGen API, synchronizing the text with speech.

## Workflow
1. **Upload Audio**: Users upload an audio file.
2. **Transcription**: The app transcribes the audio into text using OpenAI's Whisper.
3. **Caption Generation**: Captions are generated based on the transcribed text via the Gemini API.
4. **Video Creation**: An avatar video is created using the HeyGen API.
5. **Download**: Users can preview and download the generated video.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/EchoCaption.git
   cd EchoCaption
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up API keys:

Create a `.env` file in the root directory and add the following:

```
GEMINI_API_KEY=your_gemini_api_key
HEYGEN_API_KEY=your_heygen_api_key
```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Upload an audio file and follow the steps to generate your captioned avatar video.

## Dependencies

- Python 3.10+
- Streamlit
- google-generativeai
- requests
- openai-whisper
- python-dotenv

## API Configuration

Ensure you have valid API keys for:

1. **Google Gemini API**: For text-based caption generation.
2. **HeyGen API**: For creating avatar videos.

## Project Structure

```
EchoCaption/
├── app.py             # Main application script
├── requirements.txt   # Python dependencies
└── .env               # API keys configuration
```

## Future Enhancements

- Support for multiple avatars and languages.
- Real-time transcription and video generation.
- Improved error handling and logging.

## License

This project is licensed under the MIT License.

## Author

Developed by [M Ismail Daniyal](https://github.com/ismaildaniyal/).

## Contributions

Contributions and improvements are welcome. Feel free to open a pull request or submit issues.

