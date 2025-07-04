# StellarSense

**Team Name:** Jane Streeter  
**Members:**  
- Kaileshwar  
- Gomathi Nayagam S R

**Live URL:** [https://stellarx.onrender.com/](https://stellarx.onrender.com/)  
**GitHub:** [https://github.com/Kaileshwar16/stellarX](https://github.com/Kaileshwar16/stellarX)

---

## 🎯 Project Overview

StellarSense is a comprehensive web platform that transforms how people interact with astronomy by presenting real astronomical events occurring on the current date in history. When users visit our website, they are automatically greeted with significant space milestones, satellite launches, planetary discoveries, and celestial events that happened on that exact date throughout history.

Our platform combines factual accuracy with creative storytelling, making astronomy accessible to everyone while building a vibrant community of sky enthusiasts. Whether you're a beginner stargazer or an experienced astronomer, StellarSense provides the tools, knowledge, and community to enhance your cosmic journey.

---

## 🌌 Core Problem Solved

**The Challenge:** Astronomy is inspiring, but access to engaging, localized space data is limited. Existing apps are too technical or static, and amateurs want to observe, log, and share celestial events easily.

**Our Solution:** StellarSense bridges this gap by providing:
- Date-specific historical astronomy events that automatically update based on the current date
- Interactive sky observation tools with real-time weather integration
- Community-driven platform for sharing and discovering celestial observations
- Educational storytelling that makes complex astronomical concepts accessible
- AI-powered insights for enhanced user experience

---

## ✨ Key Features

### 🗓️ Astronomical Calendar
*Displays historical events for the current date, with rich storytelling, images, and interactive timelines. Browse decades of space exploration milestones by category.*

![Feature: Astronomical Calendar](add-your-image-path-here)

---

### 🔭 Sky Observation Platform
*Personal logbook for recording and sharing observations, image uploads, community interaction (comments, upvotes), and real-time weather integration for stargazing.*

![Feature: Sky Observation](add-your-image-path-here)

---

### 🤖 AI-Powered Chatbot & Smart Features
*AI chatbot answers astronomy questions, suggests tags for observations, and recommends upcoming celestial events using Google Generative AI.*

![Feature: AI Chatbot](add-your-image-path-here)

---

### 🌍 Interactive Features
- **Gravity Simulation:** Educational tool for understanding celestial mechanics.  
  > Gravity is the force that pulls objects toward one another. Every object with mass exerts a gravitational pull — the more mass, the stronger the pull.  
  > In space, gravity keeps planets in orbit around stars, moons around planets, and governs the beautiful dances of galaxies. This simulation shows how particles move under the influence of artificial gravity points you create by clicking — mimicking how real celestial bodies attract one another.

![Feature: Gravity Simulation](add-your-image-path-here)

- **Real-time Sky Map:** Interactive celestial map showing current sky conditions.
- **Crowdfunding Platform:** Support space-related research and community projects.

---

### 🗕️ Astronomical Calendar & Event Tracking
*Comprehensive calendar of upcoming and historical astronomical events, with personalized alerts and detailed documentation.*

![Feature: Event Calendar](add-your-image-path-here)

---

## 🚀 Technical Implementation

### Technology Stack

**Backend:**  
- Django (Python), Django Channels, Daphne (ASGI server)

**Frontend:**  
- Django Templates, HTML5, CSS3, JavaScript  
- Tailwind CSS, React.js

**Database & Storage:**  
- SQLite3, Pillow, Whitenoise

**APIs & External Services:**  
- NASA APOD API, NASA NeoWs API, Open Meteo API, Google Generative AI

**Development Tools:**  
- python-dotenv, python-dateutil, django-widget-tweaks

### Architecture Overview

- `home` – Authentication & event display
- `observations` – User logs & media
- `crowdfunding` – Project support
- `profiles` – User personalization
- `calendar` – Astronomy calendar
- `gravity_simulation` – Physics module
- `admin` – Admin management

---

## 💡 Impact on Users

### 🎓 Educational Impact
- Simplifies astronomy concepts
- Teaching aid for institutions
- Provides historical space context

### 🌐 Community Building
- Collaborative learning
- GitHub-like observation platform
- Facilitates knowledge exchange

### 🔬 Research Contribution
- Citizen science data
- Light pollution insights
- Weather-observation correlations

### 🌟 Personal Growth
- Enhances stargazing skills
- Tracks celestial achievements
- Community recognition

---

## 🛠️ Development Approach

**Phase 1: Foundation**  
- Django setup & NASA APIs  
- Tailwind CSS UI  
- Historical event module

**Phase 2: Core Features**  
- Logbook & image upload  
- Weather API integration  
- Community interaction tools

**Phase 3: Advanced Features**  
- AI tag suggestion  
- Crowdfunding support  
- Real-time features

**Phase 4: Optimization**  
- Responsive & dark mode  
- Render deployment  
- Final documentation

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip
- Git

### Installation

```bash
git clone https://github.com/Kaileshwar16/stellarX.git
cd stellarX
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file:

```
GOOGLE_API_KEY=your_key
NASA_API_KEY=your_key
SECRET_KEY=your_secret
DEBUG=True
```

### Run

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# For async features:
# daphne StellarSense.asgi:application
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🙏 Acknowledgements

- NASA
- Open-Meteo
- Google Generative AI
- ChatGPT
- Django
- Tailwind CSS
- Render

---

## 🛌 Submission Checklist

- [x] Live website URL: [https://stellarx.onrender.com/](https://stellarx.onrender.com/)
- [x] Public GitHub repository: [https://github.com/Kaileshwar16/stellarX](https://github.com/Kaileshwar16/stellarX)
- [x] Fully responsive, interactive, and original
- [x] README with setup, features, and technical details

---

## 🌌 Why StellarSense?

StellarSense transforms everyday curiosity into cosmic discovery. By integrating real-time space data, AI insights, and community contributions, we’ve built an innovative, educational, and visually stunning web platform to bring the universe to your fingertips.

> "Bringing the cosmos closer to everyone, one observation at a time."

---

*Add feature images/screenshots above for a more engaging presentation.*

