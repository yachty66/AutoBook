# AutoBook

Automatically generate books with GPT-4

## Introduction

AutoBook is an application that automatically creates books given a prompt describing the book. It generates chapters, topics for each chapter, and detailed bullet points for each topic. After creating this outline, the application generates text for every topic. Ultimately, this results in a book with approximately 15-20k words. The cost for creating one book is around $5. 

## Prerequisites
- OpenAI Python library

Ensure you have a valid OpenAI API key, as the application uses OpenAI's GPT-4 model to generate the book content.

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
1. Within the script, set the OpenAI API key by replacing `"api_key"` with your OpenAI API key:
   ```python
   openai.api_key = "YOUR_OPENAI_API_KEY"
   ```
2. Ensure you have a file named `prompt.md` in the same directory as the script. This file should contain the initial content or prompts that will be used to guide the AI in generating the book content.

## Usage
1. Run the script:
   ```sh
   python book.py
   ```
2. The script will automatically create chapters, topics, and detailed bullet points for each topic.
3. The application generates two files: a metadata file (`title_metadata.md`) and a content file (`title.txt`), where "title" is the title of the book defined in `prompt.md`. Both files will be saved in the same directory as the script.

## File Descriptions
- `book.py`: The main Python script file that contains all the code.
- `prompt.md`: A markdown file with the initial prompts for the book. Adjust this file according to your needs depending on the kind of book you want to generate. This file must be in the same directory as the script.
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