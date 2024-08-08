# Video to Text Transcription with Streamlit

## Overview

This Streamlit app allows users to upload a video file, extracts audio from it, and transcribes the audio to text using speech recognition. The transcribed text can be downloaded as a text file.

## Features

- **Upload Video**: Upload a video file in MP4 format.
- **Extract Audio**: Extract audio from the uploaded video.
- **Speech Recognition**: Convert the extracted audio to text.
- **Download Transcription**: Download the transcribed text as a text file.

## Requirements

- Python 3.7+
- `streamlit` library
- `moviepy` library
- `speech_recognition` library
- `pydub` library (optional for audio file format conversion)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/video-to-text-transcription.git
    cd video-to-text-transcription
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install streamlit moviepy speechrecognition
    ```

## Usage

1. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

2. **Upload a video file** (MP4 format) using the file uploader on the Streamlit interface.

3. **View the transcription**: The app will display the transcribed text on the page.

4. **Download the transcription**: Click the "Download Transcription" button to download the text file.

## Script Details

- **File Uploader**: Allows users to upload a video file.
- **Video to Audio Extraction**: Uses `moviepy` to extract audio from the video.
- **Speech Recognition**: Utilizes the `speech_recognition` library to transcribe audio to text.
- **Error Handling**: Handles cases where the audio is not understood or there are issues with the speech recognition service.

## Troubleshooting

- **Ensure Video Format**: The app currently supports MP4 video files. Other formats may need conversion.
- **Speech Recognition Limitations**: The quality of transcription may vary based on the audio quality and clarity of speech.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## Contact

For any questions or inquiries, please contact [njnagaraj007@gmail.com].
