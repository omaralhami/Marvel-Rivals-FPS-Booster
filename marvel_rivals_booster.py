import tkinter as tk
from tkinter import messagebox
import os
import shutil
import webbrowser

class MarvelRivalsBooster:
    def __init__(self, root):
        self.root = root
        self.root.title("Marvel Rivals FPS Booster")
        self.root.geometry("350x320")
        
        # Colors - GitHub Dark theme
        self.bg_color = "#0d1117"      # Dark background
        self.text_color = "#c9d1d9"    # Light text
        self.accent_blue = "#1f6feb"   # GitHub button blue
        self.success_green = "#238636"  # GitHub green
        self.error_red = "#f85149"     # GitHub red
        self.warning_yellow = "#d29922" # Warning color
        self.button_hover = "#30363d"   # Button hover
        self.remove_btn_bg = "#21262d"  # Remove button bg
        self.twitter_blue = "#1d9bf0"   # Twitter blue for handle
        
        # Configure window
        self.root.configure(bg=self.bg_color)
        self.root.resizable(False, False)
        
        # Center window
        window_width = 350
        window_height = 320
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # Setup paths
        self.source_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Scalability.ini")
        self.target_dir = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Marvel', 'Saved', 'Config', 'Windows')
        self.target_file = os.path.join(self.target_dir, "Scalability.ini")

        # Main container
        main_frame = tk.Frame(root, bg=self.bg_color)
        main_frame.pack(expand=True, fill='both', padx=25, pady=20)

        # Title
        title_label = tk.Label(main_frame, 
                             text="Marvel Rivals FPS Booster",
                             font=("Segoe UI", 18, "bold"),
                             bg=self.bg_color,
                             fg=self.text_color)
        title_label.pack(pady=(0, 15))

        # Warning message with icon
        warning_frame = tk.Frame(main_frame, bg=self.bg_color)
        warning_frame.pack(pady=(0, 25))
        
        warning_icon = tk.Label(warning_frame,
                              text="▲",
                              bg=self.bg_color,
                              fg=self.warning_yellow,
                              font=("Segoe UI", 12))
        warning_icon.pack(side=tk.LEFT, padx=(0, 5))
        
        subtitle = tk.Label(warning_frame,
                          text="Make sure the game is closed",
                          font=("Segoe UI", 10),
                          bg=self.bg_color,
                          fg=self.warning_yellow)
        subtitle.pack(side=tk.LEFT)

        # Apply Button
        self.boost_button = tk.Button(main_frame,
                                    text="Apply Boost",
                                    command=self.apply_boost,
                                    width=15,
                                    bg=self.accent_blue,
                                    fg=self.text_color,
                                    font=("Segoe UI", 10),
                                    relief="flat",
                                    activebackground="#388bfd",
                                    activeforeground=self.text_color,
                                    cursor="hand2")
        self.boost_button.pack(pady=(0, 8))

        # Remove Button
        self.remove_button = tk.Button(main_frame,
                                     text="Remove Boost",
                                     command=self.remove_boost,
                                     width=15,
                                     bg=self.remove_btn_bg,
                                     fg=self.text_color,
                                     font=("Segoe UI", 10),
                                     relief="flat",
                                     activebackground=self.button_hover,
                                     activeforeground=self.text_color,
                                     cursor="hand2")
        self.remove_button.pack()

        # Status Label
        self.status_label = tk.Label(main_frame,
                                   text="The FPS Boost is Not Active",
                                   bg=self.bg_color,
                                   fg=self.error_red,
                                   font=("Segoe UI", 9))
        self.status_label.pack(pady=20)

        # Bottom container for proper spacing
        bottom_container = tk.Frame(main_frame, bg=self.bg_color)
        bottom_container.pack(side=tk.BOTTOM, fill="x")

        # Made by label with social links in center
        made_by_frame = tk.Frame(bottom_container, bg=self.bg_color)
        made_by_frame.pack(side=tk.BOTTOM, pady=(0, 2))
        
        made_by_label = tk.Label(made_by_frame,
                               text="Made with  ❤  by mar",
                               bg=self.bg_color, 
                               fg="#8b949e",
                               font=("Segoe UI", 9))
        made_by_label.pack()

        # Social links frame
        social_frame = tk.Frame(made_by_frame, bg=self.bg_color)
        social_frame.pack(pady=(2, 0))
        
        github_link = tk.Label(social_frame,
                             text="Github",
                             cursor="hand2",
                             bg=self.bg_color,
                             fg=self.twitter_blue,
                             font=("Segoe UI", 9))
        github_link.pack(side=tk.LEFT)
        github_link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/omaralhami"))

        separator = tk.Label(social_frame,
                           text=" • ",
                           bg=self.bg_color,
                           fg="#8b949e",
                           font=("Segoe UI", 9))
        separator.pack(side=tk.LEFT)
        
        discord_link = tk.Label(social_frame,
                              text="Discord",
                              cursor="hand2",
                              bg=self.bg_color,
                              fg="#5865F2",
                              font=("Segoe UI", 9))
        discord_link.pack(side=tk.LEFT)
        discord_link.bind("<Button-1>", lambda e: webbrowser.open("https://discord.com/users/672868164161372171"))

        # Info button (absolute position)
        info_button = tk.Label(main_frame,
                             text="ⓘ",
                             cursor="hand2",
                             bg=self.bg_color,
                             fg="#8b949e",
                             font=("Segoe UI", 12))
        info_button.place(relx=1.0, rely=1.0, x=-28, y=-28)
        info_button.bind("<Button-1>", self.show_info)

        # Update status on startup
        self.update_status()

    def show_info(self, event=None):
        info_text = """Marvel Rivals FPS Booster

This application helps optimize your gaming experience in Marvel Rivals by applying performance-enhancing settings.

What it does:
• Applies optimized graphics settings
• Improves FPS stability
• Reduces input lag
• Safe to use - only modifies game settings

How to use:
1. Close Marvel Rivals if it's running
2. Click 'Apply Boost' to enhance performance
3. Click 'Remove Boost' to restore default settings

Note: All changes are reversible and safe for your system."""

        messagebox.showinfo("About", info_text)

    def apply_boost(self):
        try:
            os.makedirs(self.target_dir, exist_ok=True)
            shutil.copy2(self.source_file, self.target_file)
            messagebox.showinfo("Success", "FPS boost has been applied successfully!")
            self.update_status()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply boost: {str(e)}")

    def remove_boost(self):
        try:
            if os.path.exists(self.target_file):
                os.remove(self.target_file)
                messagebox.showinfo("Success", "FPS boost has been removed successfully!")
            else:
                messagebox.showinfo("Info", "Boost is not currently active.")
            self.update_status()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove boost: {str(e)}")

    def update_status(self):
        if os.path.exists(self.target_file):
            self.status_label.config(text="The FPS Boost is Active", fg=self.success_green)
        else:
            self.status_label.config(text="The FPS Boost is Not Active", fg=self.error_red)

if __name__ == "__main__":
    root = tk.Tk()
    app = MarvelRivalsBooster(root)
    root.mainloop()
