# WYLink

## Description

WYLink is a simple and minimalistic URL shortener built using Django and Python. This project is perfect for those who want to have a private URL shortener or want to understand the basics of how URL shorteners work.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with WYLink, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. Build the Docker image: `docker build -t wylink .`
4. Run the Docker image: `docker run -p 8000:8000 wylink`

## Usage

To use WYLink:

1. Navigate to `http://localhost:8000` in your web browser.
2. Enter the URL you want to shorten.
3. Click "Shorten URL".

## Contributing

Contributions to WYLink are welcomed and appreciated! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes.
4. Submit a pull request.

Before submitting a pull request, please ensure your code adheres to the Python style guide (PEP 8) and all tests pass.

## License

WYLink is open-source software licensed under the MIT License.
