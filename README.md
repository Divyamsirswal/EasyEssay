# AI Essay Generator CLI

#### A feature-rich, minimalistic command-line tool that leverages Cohere’s powerful text-generation API to create high-quality essays. Designed for writers, students, researchers, and professionals, this tool offers a suite of advanced features—including batch generation, outline/summary production, side-by-side essay comparison, and more—while maintaining a clean and efficient user interface.

## Features

- **High-Quality Essay Generation:**  
  Generate essays by providing a topic and word limit. The tool builds a refined prompt that factors in your desired writing style, language, and target audience.

- **Advanced Settings:**  
  Customize the output by choosing from multiple writing styles (Formal, Creative, Casual), languages, and audience types (Academic, Business, General). Toggle features like auto-save and output format (TXT or PDF).

- **Batch Mode:**  
  Generate multiple essays in one run by supplying a comma-separated list of topics.

- **Outline & Summary Generation:**  
  Optionally produce a concise bullet-point outline or a summary of the generated essay.

- **Essay Comparison:**  
  Compare two essays side-by-side—either by generating them on-the-fly or by pasting pre-written texts—to evaluate differences in tone, structure, or content.

- **Plagiarism Check (Placeholder):**  
  Run a placeholder plagiarism check on the generated content, simulating an integration with an external plagiarism detection service.

- **Ephemeral and Minimal UI:**  
  Enjoy a clean, minimal, and responsive user interface with typed-out transitions and ephemeral screens for a smooth user experience.

- **Modular Design:**  
  Organized into separate modules (configuration, ASCII art, CLI utilities, Cohere API interactions, generation logic, menus), making the project easy to maintain and extend.

---

## Requirements

- **Python 3.7+**
- **Cohere API Key:**  
  Sign up at [Cohere](https://dashboard.cohere.com/) to obtain an API key.
- Required Python packages:
  - `cohere`
  - `questionary`
  - `rich`
  - `fpdf`
  - `pyfiglet` (optional, for an ASCII logo)

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/ai-essay-generator-cli.git
   cd ai-essay-generator-cli
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key and Settings:**
   - Open `config.py` and replace `"your-cohere-api-key-here"` with your actual Cohere API key.
   - Adjust any default advanced settings if necessary.

---

## Usage

Run the tool by executing:

```bash
python main.py
```

### Main Menu Options

- **Generate Single Essay:**  
  Enter a topic and word limit to generate a single essay.
- **Generate Multiple Essays (Batch):**  
  Provide a comma-separated list of topics and a common word limit to generate essays for each topic.
- **Compare Two Essays:**  
  Choose to either generate two essays or paste existing ones to see a side-by-side comparison.
- **Advanced Settings:**  
  Customize writing style, language, audience, auto-save options, output format (TXT/PDF), and more.
- **Exit:**  
  Quit the application gracefully.

During the process, the CLI provides typed-out feedback and ephemeral screens to guide you through each step.

---

## Advanced Features

- **Customizable Prompts:**  
  The generation prompt automatically incorporates your selected style, language, and audience, ensuring the essay output meets your specific requirements.

- **Output Options:**  
  Choose to save your essays automatically or manually. Export essays in plain text or PDF format for easy sharing and archiving.

- **Comparison Mode:**  
  Easily compare two essays side-by-side to highlight differences and evaluate quality.

- **Modular Architecture:**  
  The project is split into multiple modules (e.g., `ascii_art.py`, `cli_utils.py`, `cohere_api.py`, `generation.py`, `menus.py`, `config.py`, `main.py`), making it highly maintainable and extensible.

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Please follow the coding style and include tests for new features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, feature requests, or bug reports, please open an issue on the [GitHub repository](https://github.com/Divyamsirswal/EasyEssay) or contact the maintainer at divyamsirswal361@gmail.com.

---
