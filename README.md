# StellarSense

StellarSense is a comprehensive web platform built with Django, designed to bring together astronomy enthusiasts. It offers a suite of features for tracking celestial observations, fostering community-driven crowdfunding for space-related projects, providing an astronomical calendar, and even simulating gravitational interactions.

## Login as Admin (go to /admin to acess to admin page)

username : root 
password : root

## Features

*   **User Authentication & Profiles:** Secure user registration, login, logout, and personalized user profiles.
*   **Astronomical Observations:** Users can record, manage, and share their astronomical observations, including the ability to upload images.
*   **Crowdfunding Platform:** A dedicated module for launching and supporting crowdfunding campaigns related to space exploration, research, or community projects.
*   **Astronomical Calendar:** A calendar feature to keep track of significant astronomical events, meteor showers, eclipses, and more.
*   **Gravity Simulation:** An interactive module to visualize and experiment with gravitational forces and celestial mechanics.
*   **Real-time Capabilities:** Leverages WebSockets for potential real-time updates and interactive features.
*   **AI Integration:** Incorporates Google Generative AI for enhanced functionalities (e.g., intelligent insights, content generation).

## Technical Stack

*   **Backend Framework:** Django (Python)
*   **Asynchronous & Real-time:** Django Channels, Daphne (ASGI server)
*   **Database:** SQLite3 (for development/local, scalaled to PostgreSQL)
*   **Frontend:** Django Templates, HTML, CSS, JavaScript (with `django-widget-tweaks` for enhanced form rendering)
*   **Image Processing:** Pillow
*   **Environment Management:** `python-dotenv`
*   **Date/Time Utilities:** `python-dateutil`
*   **AI/ML:** `google-generativeai`
*   APIS: APOD, OPEN-METEO, GEMINI-2.5 FLASH
*   **Static File Management:** Whitenoise
*   **Deployment Considerations:** Configured for potential deployment on platforms like Render (indicated by `CSRF_TRUSTED_ORIGINS`).

## Technical Implementation

StellarSense is structured as a modular Django project, with distinct applications for each core feature:

*   **`home`**: Handles core functionalities like user authentication, routing, and the main landing page.
*   **`observations`**: Manages the creation, storage, and display of user-submitted astronomical observations, including image uploads.
*   **`crowdfunding`**: Implements the logic for creating, managing, and contributing to crowdfunding campaigns.
*   **`profiles`**: Manages user-specific data and profile settings.
*   **`calender`**: Provides the framework for the astronomical events calendar.
*   **`gravity_simulation`**: Contains the logic and frontend for the gravity simulation.
*   **`Admin Page`**: Accessible via `/admin`, provides an interface for site administration and content management.

The project utilizes Django's built-in ORM for database interactions and leverages Django Channels for handling asynchronous tasks and real-time communication, enabling features like live updates or interactive simulations. Static and media files are served efficiently, with configurations for both development and production environments. Integration with Google Generative AI is set up to potentially power intelligent features across the platform.

## Getting Started

### Prerequisites

*   Python 3.8+
*   pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/StellarSense.git
    cd StellarSense
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add any necessary environment variables (e.g., API keys for Google Generative AI, if required).
    ```
    # Example .env content
    # GOOGLE_API_KEY=your_google_api_key_here
    ```
5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    When prompted, use `username: root` and `password: root` (or your desired credentials).

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
8.  **Run the development server(async):**
    ```bash
    daphne StellarSense.asgi:application
    ```

The application will be accessible at `http://127.0.0.1:8000/`.

## 🙏 Acknowledgements

This project would not have been possible without the contributions, data, and tools provided by the following:

- [ChatGPT](https://openai.com/chatgpt) – for AI-assisted brainstorming, development support, and guidance throughout the project.
- [Rogue Space Systems Corporation](https://rogue.space/) – for their pioneering work and inspiration in autonomous orbital robotics and space systems.
- [Akimitsu Hamamuro] – for providing open-source astronomy datasets and code that helped accelerate development.
- [NASA](https://www.nasa.gov/) – for their extensive open data, APIs, and research that form the backbone of many space-related applications.
- [Open-Meteo](https://open-meteo.com/) – for providing free, high-resolution weather forecast APIs used in this project.

We deeply appreciate the open knowledge and technology shared by these individuals and organizations.

