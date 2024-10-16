## Overview

The **Steganography App** is a web application designed to encode and decode messages within images using Python's Flask framework. The app provides a user-friendly interface for users to upload images and messages, perform encoding and decoding, and download the results. This project demonstrates the principles of steganography and showcases the practical application of web development technologies.

## Features

- **Encode Message**: Users can input a message and select an image to encode the message into the least significant bits of the image pixels.
- **Decode Message**: Users can upload an encoded image to extract and display the hidden message.
- **Web Interface**: A simple and clean user interface built with Bootstrap, making it accessible and easy to use.

## Technologies Used

- **Python**: The primary programming language used for the backend.
- **Flask**: A lightweight web framework for building web applications.
- **Pillow**: A Python Imaging Library (PIL) fork that adds image processing capabilities.
- **HTML/CSS**: Markup and styling languages for creating the web interface.
- **Docker**: Used for containerization of the application, ensuring a consistent development and production environment.

## Application Structure

The project directory includes the following key files:

- **`help.py`**: The main Flask application file that handles routing and logic for encoding and decoding messages.
- **`steganography.py`**: Contains functions for encoding and decoding messages within images.
- **`templates/`**: Directory containing HTML templates for rendering the web interface (index, encode, and decode pages).
- **`static/style.css`**: Custom CSS styles for the web application.
- **`Dockerfile`**: Contains instructions to build a Docker image for the application.

## Usage

1. **To Encode a Message**:
   - Navigate to the "Encode" page.
   - Select an image file and enter the message you wish to hide.
   - Submit the form to receive the encoded image for download.

2. **To Decode a Message**:
   - Navigate to the "Decode" page.
   - Upload the encoded image.
   - Submit the form to reveal the hidden message.
