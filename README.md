# Wedding Website Project

Welcome to the repository for Martina & Matteo's wedding website! This project showcases a modern, elegant, and user-friendly wedding website designed to provide guests with all the necessary information about the event. Below, I’ll walk you through the design, structure, and features of the website, highlighting the thought process and technical decisions behind it.

---

## **Project Overview**
This website was created to serve as a central hub for wedding details, including the event schedule, location information, FAQs, and an RSVP form. The goal was to create a visually appealing, responsive, and easy-to-navigate site that reflects the couple's style while ensuring a seamless experience for guests.

---

## **Key Features**
1. **Responsive Design**  
   - The website is fully responsive, ensuring a smooth experience across devices (desktop, tablet, and mobile).  
   - Media queries and flexible layouts adapt to different screen sizes, maintaining readability and usability.

2. **Elegant Visuals**  
   - A fixed background image creates an immersive experience, with a fallback for mobile devices to optimize performance.  
   - Custom fonts (`Great Vibes`, `Cinzel Decorative`, and `Roboto`) add a touch of sophistication and personality.

3. **Interactive Timeline**  
   - The event schedule is presented as a visually engaging timeline, with alternating content blocks and dots to guide the user.  
   - On mobile, the timeline adjusts to a single-column layout for better readability.

4. **Image Slideshow**  
   - A simple JavaScript-powered slideshow displays images of the wedding location, allowing users to manually navigate between slides.

5. **FAQ Section**  
   - The FAQ section uses JavaScript to toggle answers, keeping the page clean and user-friendly.  
   - Icons and smooth transitions enhance the interactivity.

6. **RSVP Form**  
   - A clean, accessible form allows guests to RSVP, indicate attendance preferences, and provide additional notes (e.g., dietary restrictions).  
   - Custom radio buttons and input fields ensure a consistent look and feel.

7. **Copy-to-Clipboard Feature**  
   - Guests can easily copy the couple’s IBAN for wedding gifts by clicking on the underlined text, with a confirmation alert.

---

## **Technical Details**
- **HTML5 & CSS3**: The website is built with semantic HTML and modern CSS, including Flexbox for layout and custom animations for interactivity.  
- **JavaScript**: Used for interactive features like the slideshow, FAQ toggles, and clipboard functionality.  
- **Django Template Tags**: The `{% static %}` tag is used to load static files (images, CSS, etc.), making the site easy to deploy in a Django environment.  
- **Responsive Images**: Images are optimized for performance and lazy-loaded to improve page speed.  
- **Accessibility**: The site includes ARIA labels, semantic HTML, and keyboard-friendly navigation to ensure accessibility for all users.

---

## **Design Philosophy**
The design prioritizes simplicity, elegance, and usability. Key decisions include:  
- **Color Scheme**: Neutral tones with white and soft grays allow the content to stand out against the background image.  
- **Typography**: A combination of serif and sans-serif fonts creates a balance between formality and readability.  
- **Spacing**: Ample whitespace and padding ensure the content feels uncluttered and easy to navigate.  
- **Mobile-First Approach**: The design was built with mobile users in mind, ensuring a seamless experience on smaller screens.

---

## **How to Run the Project**
1. Clone the repository to your local machine.  
2. Ensure you have Django installed (`pip install django`).  
3. Run the Django development server:  
   ```bash
   python manage.py runserver
