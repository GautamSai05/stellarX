# StellarSense

**Team Name:** Jane Streeter  
**Members:**  
- Kaileshwar  
- Gomathi Nayagam S R

**Live URL:** [https://stellarx.onrender.com/](https://stellarx.onrender.com/)  
**GitHub:** [https://github.com/Kaileshwar16/stellarX](https://github.com/Kaileshwar16/stellarX)

---

## 🚨 **Admin Access **

> **To access the admin panel and moderate users:**  
> **Username:** `root`  
> **Password:** `root`  
>  
> 👉 [Go to Admin Panel](https://stellarx.onrender.com/admin/)  
>  
> **This is provided for demo and evaluation purposes.**

---

## 🎯 Project Overview

StellarSense is a comprehensive web platform that transforms how people interact with astronomy by presenting real astronomical events occurring on the current date in history. When users visit our website, they are automatically greeted with significant space milestones, satellite launches, planetary discoveries, and celestial events that happened on that exact date throughout history.

Our platform combines factual accuracy with creative storytelling, making astronomy accessible to everyone while building a vibrant community of sky enthusiasts. Whether you're a beginner stargazer or an experienced astronomer, StellarSense provides the tools, knowledge, and community to enhance your cosmic journey.

---

## 🌟 **Most Important Features**

### 🗓️ Astronomical Calendar & Date Explorer
*Displays historical events for the current date, with rich storytelling, images, and interactive timelines. Browse decades of space exploration milestones by category.  
The calendar and date explorer are tightly integrated: users can pick a date or ask about any day in space history, and get instant, AI-powered answers and event details.*

![Astronomical Calendar & Date Explorer](https://drive.google.com/uc?id=1TVaY5BGeIO7OUny8_jR1a-hzlNvFv2p8)

---

### 🔭 Sky Observation Platform
*Personal logbook for recording and sharing observations, image uploads, community interaction (comments, upvotes), and real-time weather integration for stargazing.*

![Sky Observation Platform](https://drive.google.com/uc?id=1Hx1qJubyYH2gzBoHwbvJs2cW8OLk27jG)

---

### 🌍 Gravity Simulation
*Educational tool for understanding celestial mechanics.  
Gravity is the force that pulls objects toward one another. Every object with mass exerts a gravitational pull — the more mass, the stronger the pull.  
In space, gravity keeps planets in orbit around stars, moons around planets, and governs the beautiful dances of galaxies. This simulation shows how particles move under the influence of artificial gravity points you create by clicking — mimicking how real celestial bodies attract one another.*

![Gravity Simulation](https://drive.google.com/uc?id=1EuM6jOz3TjONSsUmziO5XbDByWmdfgrs)

---

### 🪐 Around Earth (Stuff in Space)
*Explore a real-time, interactive map of satellites, debris, and celestial objects orbiting Earth.  
Click on any object to learn about its name, type, orbital parameters, and more. This feature helps users visualize the density and diversity of objects in Earth's orbit and discover details about stars, planets, and satellites in our galaxy and universe.*

![Around Earth](https://drive.google.com/uc?id=1iqZhs93TaFRoamaIfphgNYGhdWv0s04L)

---

### 💬 Live Comments (Not a Chatbot)
> **A standout feature!**  
The "Live Comments" feature (`chatbot.html`) is a real-time public chat system, not a traditional AI chatbot.  
- **Real-Time Messaging:** Users can send and receive messages instantly across devices, similar to a group chat.
- **WebSocket Powered:** Built using Django Channels and WebSockets for instant delivery.
- **Open to All:** Both logged-in and anonymous users can participate; usernames are shown if logged in.
- **Community Wall:** All messages are visible to everyone currently online, fostering open discussion and collaboration.
- **Info Panel:** Users can view chat guidelines and how the system works.

![Live Comments](https://drive.google.com/uc?id=1dnJdOA3-90J5cAm1K2sENlFe_wxi5Cti)

---

### 🆕 Social Astronomy Feed (Instagram/Facebook-like Posting)
> **A unique, community-driven feature!**
>
> Users can **create accounts and post their own astronomy observations, discoveries, or thoughts**—just like on Instagram or Facebook, but tailored for astronomy.  
> Each post is presented in a way that's easy for anyone to understand, with clear explanations, images, and interactive elements.  
> This makes sharing and learning about the cosmos accessible and engaging for all ages and backgrounds.

![Social Astronomy Feed](https://drive.google.com/uc?id=1Cr7Imq3t-DDghhD0JIL871IgQ3vlCQ8H)

---

## 🚀 Technical Implementation

### Technology Stack

**Backend:**  
- Django (Python), Django Channels, Daphne (ASGI server)

**Frontend:**  
- Django Templates, HTML5, CSS3, JavaScript  
- Tailwind CSS, React.js

**Database & Storage:**  
- SQLite3 (local testing), PostgreSQL (deploying), Pillow, Whitenoise

**APIs & External Services:**  
- NASA APOD API, NASA NeoWs API, Open Meteo API, Google Generative AI

**Development Tools:**  
- renderer, nvim, postman

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

### Installation (linux)

```bash
git clone https://github.com/Kaileshwar16/stellarX.git
cd stellarX
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Installation (windows)

```bash
git clone https://github.com/Kaileshwar16/stellarX.git
cd stellarX
python -m venv venv
venv\Scripts\activate
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

## ⚡️ **Important Note About Website Loading Time**

> **StellarSense is deployed on [Render](https://render.com/) using their free plan.**  
> Because of this, the website may experience slower loading times, especially during peak usage periods. We recommend being patient as the site loads, and we appreciate your understanding.
>
> **For the best experience, consider contributing to our crowdfunding campaign to help us upgrade to a paid plan for faster, more reliable access.**

---

## 🙏 Acknowledgements & Credits

- [NASA Open APIs](https://api.nasa.gov/) (APOD, NeoWs, and more)
- [Open-Meteo](https://open-meteo.com/) (Weather data)
- [Stuff in Space](https://stuffin.space/) (Satellite visualization)
- [Google Generative AI](https://ai.google/)
- [ChatGPT](https://chat.openai.com/)
- [Swiper.js](https://swiperjs.com/) (for carousel/logs)
- [FontAwesome](https://fontawesome.com/) (icons)
- [Rogue Space Systems Corporation](https://rogue.space/) (satellite data)
- [Various open-source astronomy datasets and community resources]

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

*Feature images are linked from Google Drive. For best results on GitHub, upload images to your repository or use a dedicated image hosting service.*