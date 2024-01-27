# Venmurasu Programming Contest Website 🚀

Welcome to the Venmurasu Programming Contest website – your gateway to a world of coding excellence and innovation!

## Overview

This website is a replication of the Tamil Wiki, specifically tailored for the Venmurasu Programming Contest. We've harnessed the power of Hugo and the Book-Master theme to bring you an immersive and visually appealing experience.

## Hugo Themes Repository

The themes used in this project are sourced from the official Hugo Themes repository. You can explore and find more themes at [Hugo Themes](https://themes.gohugo.io/).

## Getting Started

Follow these steps to set up the project locally:

### Step 1: Convert XML to MD

To convert your XML content to Markdown, we've utilized Pandoc and a PHP script. Run the following commands:

```bash
# Install Pandoc
sudo apt-get install pandoc

# Run the PHP script for conversion
php convert.php input.xml output.md
```

### Step 2: Install Hugo

Follow the [official Hugo installation guide](https://gohugo.io/getting-started/installing/) to install Hugo on your machine.

### Step 3: Create a New Hugo Site

```bash
hugo new site venmurasu-programming-contest
cd venmurasu-programming-contest
```

### Step 4: Install Hugo Themes

```bash
git submodule add https://github.com/murugavel123/hugo-wiki-theme
```

### Step 5: Modify HTML and CSS

Navigate to the `themes/book-master` directory and customize the HTML and CSS files according to your needs.

## Running the Hugo Server

```bash
hugo server -D
```

Open your browser and visit `http://localhost:1313` to see the website in action.

## Website Features

- **Responsive Design:** Enjoy a seamless experience on various devices.
- **Custom Styling:** We've fine-tuned the visuals to reflect the spirit of the Venmurasu Programming Contest.
- **Content-rich Pages:** Explore the Home, About, and Contest pages for comprehensive information.

## Contest Information

### Home 🏠
Discover the latest updates, announcements, and highlights of the Venmurasu Programming Contest. Your starting point for this exciting journey!

### About ℹ️
Uncover the story behind the contest. Learn about its origins, objectives, and the passionate individuals driving it forward.

### Contest 🏆
Get ready for the coding challenge of a lifetime! Find detailed information about the rules, registration, and important dates.

## Contributing

We welcome contributions! If you have suggestions, bug reports, or want to add features, please reach out to us at [contact@kavinT.com](mailto:22i326@psgtech.ac.in).

## License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.

## Contact Us

Have questions, feedback, or just want to chat? Feel free to reach out to us at [contact@kavinT.com](mailto:22i326@psgtech.ac.in).

Happy coding!
