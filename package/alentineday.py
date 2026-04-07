import tkinter as tk
import random
import webbrowser
import time
import math

# --- CONFIGURATION (CUSTOMIZE THIS!) ---
# Replace this URL with a song you both love (e.g., "Perfect", "Lover", etc.)
THEME_SONG_URL = "https://www.youtube.com/watch?v=rtOvBOTyX00" 
PARTNER_NAME = "My Love"

class InnovativeValentine:
    def __init__(self, root):
        self.root = root
        self.root.title(f"A Question for {PARTNER_NAME}")
        self.root.geometry("700x500")
        self.root.configure(bg="#1a1a2e") # Modern dark theme

        # Canvas for animations
        self.canvas = tk.Canvas(root, bg="#1a1a2e", highlightthickness=0)
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Title
        self.title_id = self.canvas.create_text(350, 100, text=f"Hey {PARTNER_NAME}...", 
                                font=("Montserrat", 30, "bold"), fill="#e94560")
        self.subtitle_id = self.canvas.create_text(350, 160, text="Will you be my Valentine?", 
                                   font=("Montserrat", 20), fill="#ffffff")

        # The YES Button
        self.yes_btn = tk.Button(root, text="YES! ❤️", font=("Arial", 16, "bold"), 
                                 bg="#e94560", fg="white", activebackground="#ff2e63",
                                 width=12, height=1, bd=0, command=self.celebrate)
        self.yes_btn.place(x=200, y=300)

        # The SMART NO Button
        self.no_btn = tk.Button(root, text="No...", font=("Arial", 16), 
                                bg="#555", fg="white", width=12, height=1, bd=0)
        self.no_btn.place(x=400, y=300)
        
        # Bind hover event
        self.no_btn.bind("<Enter>", self.evade_and_plead)

        # List of pleas for the No button
        self.pleas = ["Really?", "Think again!", "I cook!", "Please?", 
                      "Don't do it!", "I'm cute!", "Wrong button!", "Miss click?"]

    def evade_and_plead(self, event):
        """Moves button and changes text to beg the user."""
        # 1. Move to random spot
        win_w = self.root.winfo_width()
        win_h = self.root.winfo_height()
        new_x = random.randint(50, win_w - 150)
        new_y = random.randint(50, win_h - 100)
        self.no_btn.place(x=new_x, y=new_y)

        # 2. Change text
        new_text = random.choice(self.pleas)
        self.no_btn.config(text=new_text, bg="gray")

    def celebrate(self):
        """Triggers the finale."""
        # Hide buttons
        self.yes_btn.destroy()
        self.no_btn.destroy()
        
        # Change text
        self.canvas.itemconfig(self.title_id, text="BEST CHOICE EVER! 🥰")
        self.canvas.itemconfig(self.subtitle_id, text="Playing our song...")
        
        # Launch Song in Browser
        webbrowser.open(THEME_SONG_URL)

        # Start Confetti Loop
        self.animate_confetti()

    def animate_confetti(self):
        """Creates a simple particle explosion effect."""
        colors = ["#ff0000", "#ff69b4", "#ffd700", "#00ffff", "#ffffff"]
        particles = []

        # Create 100 particles
        for _ in range(100):
            x = 350 # Center X
            y = 300 # Center Y
            speed_x = random.uniform(-10, 10)
            speed_y = random.uniform(-15, -5) # Shoot up first
            color = random.choice(colors)
            size = random.randint(5, 15)
            # Draw particle
            p_id = self.canvas.create_oval(x, y, x+size, y+size, fill=color, outline="")
            particles.append([p_id, x, y, speed_x, speed_y])

        # Animation Loop
        def update_particles():
            if not particles: return
            
            for p in particles:
                p_id, x, y, sx, sy = p
                
                # Apply Gravity
                sy += 0.5 
                
                # Move
                x += sx
                y += sy
                
                # Update Canvas coords
                self.canvas.coords(p_id, x, y, x+10, y+10)
                
                # Update list data
                p[1], p[2], p[3], p[4] = x, y, sx, sy

            # Remove particles that fall off screen to save memory
            # (Simple clean up not included for brevity, but particles fall infinitely)
            
            self.root.after(30, update_particles)

        update_particles()

if __name__ == "__main__":
    root = tk.Tk()
    app = InnovativeValentine(root)
    root.mainloop()