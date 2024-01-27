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

Convert MediaWiki pages to GitHub flavored Markdown (or other formats supported by Pandoc). The conversion uses an XML export from MediaWiki and converts each wiki page to an individual markdown file. Directory structures will be preserved. The generated export can also include frontmatter for Github pages.

You may also be interested in a forked version of this codebase available at https://github.com/outofcontrol/mediawiki-to-gfm

## Requirements

* PHP
* Pandoc


## Export MediaWiki Pages

You'll export all your pages as a single XML file following these steps: http://en.wikipedia.org/wiki/Help:Export


## Installation

### Install Pandoc

http://johnmacfarlane.net/pandoc/installing.html


### Get Composer

`curl -sS https://getcomposer.org/installer | php`


### Install Composer Packages

`php composer.phar install`


## Run

####--filename####
The only required parameter is `filename` for the name of the xml file you exported from MediaWiki, eg: 

`php convert.php --filename=mediawiki.xml`

####--output####
You can also use `output` to specify an output folder since each wiki page in the XML file will generate it's own separate markdown file.

`php convert.php --filename=mediawiki.xml --output=export`


####--indexes####
You can set `indexes` as `true` if you want pages with the same name as a directory to be renamed as index.md and placed into their directory

`php convert.php --filename=mediawiki.xml --output=export --indexes=true`

####--frontmatter####
You can specify whether you want frontmatter included. This is automatically set to `true` when the output format is `markdown_github`

`php convert.php --filename=mediawiki.xml --output=export --format=markdown_phpextra --frontmatter=true`


####--format####
You can specify different output formats with `format`. The default is `markdown_github`. See 

`php convert.php --filename=mediawiki.xml --output=export --format=markdown_phpextra`

Supported pandoc formats are: 

* markdown
* mediawiki


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
