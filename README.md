# AutoBook

## Introduction

This application is automatically creating books given a prompt for the description of the book. It generates chapters, topics for each chapter, and detailed bullet points for each topic. After creating this outline for every topic will be a text generated. this results in the end in a book with between 15-20k words. 

## Prerequisites
- OpenAI Python library

Make sure that you have a valid OpenAI API key as the application uses OpenAI's GPT-4 model for generating the book content.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your_username_/Your-Repo-Name.git
   ```
2. Install the required Python packages:
   ```sh
   pip install openai
   ```

## Configuration
1. Inside the script, set the OpenAI API key by replacing `"api_key"` with your OpenAI API key:
   ```python
   openai.api_key = "YOUR_OPENAI_API_KEY"
   ```
2. Make sure you have a file named `prompt.md` in the same directory as the script. This file should contain the initial content or prompts that will be used to guide the AI in generating the book content.

## Usage
1. Run the script:
   ```sh
   python book.py
   ```
2. The script will create chapters, topics, and detailed bullet points for each topic automatically.
3. The application generates a metadata file (`title_metadata.md`) and a content file (`title.txt`) where "title" is the title of the book defined in `prompt.md`. Both files will be saved in the same directory as the script.

## File Descriptions
- `book.py`: The main Python script file that contains all the code.
- `prompt.md`: A markdown file with the initial prompts for the book, adjust the file to your needs depending which kind of book you want to generate. This file must be in the same directory as the script.
- `title_metadata.md`: A markdown file that contains metadata and an outline of the book.
- `title.txt`: A text file that contains the generated content of the book.

## Contributing
1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/my-new-feature`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin feature/my-new-feature`.
5. Submit a pull request.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer
This application uses OpenAI's GPT-4 to generate content. The generated content may not always meet your expectations or be error-free. Always review the content carefully.
