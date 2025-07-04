# StellarSense

**Team Name:** Jane Streeter  
**Members:**  
- Kaileshwar  
- Gomathi Nayagam S R

**Live URL:** [https://stellarx.onrender.com/](https://stellarx.onrender.com/)  
**GitHub:** [https://github.com/Kaileshwar16/stellarX](https://github.com/Kaileshwar16/stellarX)

---

## Idea Description

StellarSense is an interactive, responsive web platform that immerses users in the wonders of space history and astronomy. Every time a user visits the homepage, they are greeted with real astronomical events that occurred on that specific date in history—ranging from satellite launches to planetary discoveries and scientific milestones. The platform combines factual accuracy with creative storytelling, using dynamic content, animations, and interactive features to educate and engage users. 

Key features include:
- **Astronomical Calendar:** Displays historical events for the current date.
- **Crowdfunding Module:** Supports space-related projects.
- **Gravity Simulation:** Lets users experiment with celestial mechanics.
- **AI-powered Chatbot:** Assists users and answers astronomy questions.
- **Celestial Observation Logs:** Users can record and share their own sky observations.
- **Media Integration:** NASA APOD and other visual content for daily inspiration.

---

## Planned Technologies and Tools

- **Backend:** Django (Python)
- **Frontend:** Django Templates, HTML, CSS, JavaScript, Tailwind CSS
- **Real-time & Async:** Django Channels, Daphne (ASGI)
- **Database:** SQLite3 (development), scalable to PostgreSQL
- **APIs:** NASA APOD, Open-Meteo, Gemini 2.5 Flash, Google Generative AI
- **AI/ML:** google-generativeai (for chatbot and content)
- **Image Processing:** Pillow
- **Environment Management:** python-dotenv
- **Static File Management:** Whitenoise
- **Date/Time Utilities:** python-dateutil
- **Version Control:** GitHub
- **Deployment:** Render.com

---

## Impact on User

**StellarSense** offers a unique blend of education, engagement, and creativity:
- **Daily Discovery:** Users learn about real astronomical events tied to the current date, making each visit fresh and relevant.
- **Community & Collaboration:** Users can log their own observations and support space projects via crowdfunding.
- **Interactive Learning:** Features like the gravity simulation and AI chatbot make complex concepts accessible and fun.
- **Accessibility:** The site is fully responsive and easy to navigate, ensuring a seamless experience across devices.
- **Inspiration:** Visuals, animations, and storytelling foster curiosity and a deeper appreciation for space science.

---

## Approach Towards Development

1. **Research & Planning:** Identified key user needs—education, engagement, and interactivity. Gathered reliable astronomical datasets and APIs.
2. **Design:** Focused on a visually captivating, modern UI with smooth navigation and responsive layouts using Tailwind CSS and custom styles.
3. **Backend Development:** Built modular Django apps for each feature (calendar, crowdfunding, observations, gravity simulation).
4. **Frontend & Interactivity:** Integrated JavaScript for animations, Swiper.js for logs, and real-time features via Django Channels.
5. **AI Integration:** Used Google Generative AI for chatbot and content generation.
6. **Testing:** Ensured cross-device and cross-browser compatibility, accessibility, and performance.
7. **Deployment:** Deployed on Render.com for public access.

---

## Complete Roadmap

1. **Ideation & Research:** Define features, gather data sources, and plan user journeys.
2. **Design & Prototyping:** Create wireframes and UI mockups.
3. **Backend Setup:** Initialize Django project, set up models for events, logs, users, etc.
4. **Frontend Development:** Build responsive templates, integrate animations and interactive components.
5. **API Integration:** Connect to NASA, Open-Meteo, and Gemini APIs for dynamic content.
6. **AI & Real-time Features:** Implement chatbot and live comments using Django Channels.
7. **Testing & QA:** Manual and automated testing for usability, performance, and accessibility.
8. **Deployment:** Configure for production, deploy to Render.com, and set up environment variables.
9. **Documentation:** Prepare README, user guides, and submission materials.

---

## Resources

- [NASA Open APIs](https://api.nasa.gov/)
- [Open-Meteo API](https://open-meteo.com/)
- [Google Generative AI](https://ai.google/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Swiper.js](https://swiperjs.com/)
- [Render.com](https://render.com/)
- [GitHub](https://github.com/)
- [ChatGPT](https://openai.com/chatgpt)

---

## Special Features

- **Dynamic Historical Events:** Homepage updates daily with real events from space history.
- **Gravity Simulation:** Interactive, animated module for exploring gravitational physics.
- **AI Chatbot:** Real-time Q&A and event explanations.
- **Crowdfunding:** Support for space projects.
- **Celestial Logs:** Community-driven observation sharing.
- **Animations & Media:** NASA APOD, animated backgrounds, and typewriter effects.
- **Accessibility:** Responsive design, keyboard navigation, and clear visual hierarchy.

---

## Installation & Setup

### Prerequisites

- Python 3.8+
- pip

### Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Kaileshwar16/stellarX.git
    cd stellarX
    ```
2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up environment variables:**  
   Create a `.env` file in the root directory and add your API keys (see `.env.example`).
5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```
6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```
7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```
8. **For async features:**
    ```bash
    daphne StellarSense.asgi:application
    ```

The app will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Acknowledgements

- [NASA](https://www.nasa.gov/)
- [Open-Meteo](https://open-meteo.com/)
- [Google Generative AI](https://ai.google/)
- [ChatGPT](https://openai.com/chatgpt)
- [Rogue Space Systems Corporation](https://rogue.space/)
- [Akimitsu Hamamuro] (open-source astronomy datasets)

---

## Submission Checklist

- [x] Live website URL: [https://stellarx.onrender.com/](https://stellarx.onrender.com/)
- [x] Public GitHub repository: [https://github.com/Kaileshwar16/stellarX](https://github.com/Kaileshwar16/stellarX)
- [x] Fully responsive, interactive, and original
- [x] README with setup, features, and technical details

---

## Why StellarSense?

StellarSense transforms space history into a daily, interactive experience. By blending science, storytelling, and technology, it inspires curiosity and learning for users of all backgrounds. The platform’s modular design, real-time features, and creative UI set a new standard for educational astronomy web apps.

---

