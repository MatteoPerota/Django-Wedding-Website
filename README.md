# Wedding Website Project

Hey there! 👋 Welcome to the repository for a Django wedding website I created for my wedding invites. 
This project is a simple, clean, and user-friendly website designed to give guests all the info they need about the big day. Let me walk you through the design, features, and tech behind it!

---

## **What’s This All About?**
This website is the go-to spot for wedding details like the schedule, location, FAQs, and RSVP. The goal? To create something beautiful, easy to use, and reflective of our style while making sure guests have a smooth experience.

---

## **Cool Features**
Here’s what makes this website stand out:

1. **Responsive Design**  
   - Works flawlessly on desktops, tablets, and phones.  
   - Flexbox and media queries make sure everything looks great, no matter the screen size.

2. **Pretty Visuals**  
   - A stunning fixed background image sets the tone, with a mobile-friendly fallback for better performance.  
   - Fancy fonts add a touch of elegance.

3. **Interactive Timeline**  
   - The event schedule is displayed as a sleek timeline with alternating blocks and dots.  
   - On mobile, it switches to a single-column layout for easy reading.

4. **Image Slideshow**  
   - A simple JavaScript slideshow shows off the wedding venue. Guests can click through the images manually.

5. **FAQ Section**  
   - Questions and answers are toggled with JavaScript, keeping things clean and interactive.  
   - Smooth transitions and icons make it fun to use.

6. **RSVP Form**  
   - A clean form lets guests RSVP, choose their attendance level, and add notes (like dietary needs).  
   - Custom radio buttons and inputs keep everything looking consistent.

7. **Copy-to-Clipboard Feature**  
   - Guests can copy the couple’s IBAN for wedding gifts with a single click. A handy alert confirms it worked.

---

## **Tech Stuff**
Here’s what’s under the hood:  
- **HTML5 & CSS3**: Semantic HTML and modern CSS (Flexbox, animations, etc.) for structure and style. I'm not an expert in neither of the two languages, gen AI helped a bit here ;D
- **JavaScript**: Powers the slideshow, FAQ toggles, and clipboard feature.  
- **Django Template Tags**: The `{% static %}` tag loads static files (images, CSS, etc.) for easy deployment.  
- **Responsive Images**: Optimized and lazy-loaded for faster performance.  
- **Accessibility**: ARIA labels, semantic HTML, and keyboard-friendly navigation make the site inclusive.

---

## **Design Vibes**
The design is all about simplicity, elegance, and usability.
- **Colors**: Neutral tones (white, soft grays) let the content shine against the background.  
- **Fonts**: A mix of serif (`Great Vibes`, `Cinzel Decorative`) and sans-serif (`Roboto`) fonts balances elegance with readability.  
- **Spacing**: Plenty of whitespace and padding keep things clean and easy to navigate.  
- **Mobile-First**: Designed with mobile users in mind, so it looks great on smaller screens.

---

## **How to Run It**
Want to check it out locally? Here’s how:  
1. Clone the repo to your machine.  
2. Make sure you have Django installed (`pip install django`).  
3. Run the Django dev server:  
   ```bash
   python manage.py runserver
   ```
4. Open your browser and head to http://127.0.0.1:8000/ to see the site in action.

Thanks for checking out this project! If you have any questions or feedback, feel free to reach out. 😊
