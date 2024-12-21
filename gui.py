import tkinter as tk
from tkinter import ttk
import json

def display_jobs():
    try:
        with open("wuzzufscraper/wuzzufscraper/spiders/jobs.json", "r", encoding="utf-8") as file:
            jobs = json.load(file)
    except FileNotFoundError:
        jobs = []

    def create_job_block(job, frame):
        job_frame = tk.Frame(frame, bg="#1e3d59", bd=2, relief=tk.RIDGE)
        job_frame.pack(pady=10, padx=15, fill=tk.BOTH, expand=True)

        tk.Label(job_frame, text=f"Job: {job.get('name', 'N/A')}", bg="#1e3d59", fg="#d4e4f7",
            font=("Helvetica", 12, "bold"), anchor="w").pack(fill=tk.X, padx=10, pady=2)

        tk.Label(job_frame, text=f"Company: {job.get('company_name', 'N/A')}", bg="#1e3d59", fg="#d4e4f7",
            font=("Helvetica", 12), anchor="w").pack(fill=tk.X, padx=10, pady=2)

        tk.Label(job_frame, text=f"Type: {job.get('type', 'N/A')}", bg="#1e3d59", fg="#d4e4f7",
            font=("Helvetica", 12), anchor="w").pack(fill=tk.X, padx=10, pady=2)

        tk.Label(job_frame, text=f"Location: {job.get('location', 'N/A')}", bg="#1e3d59", fg="#d4e4f7",
            font=("Helvetica", 12), anchor="w").pack(fill=tk.X, padx=10, pady=2)

        tk.Label(job_frame, text=f"Mode: {job.get('mode', 'N/A')}", bg="#1e3d59", fg="#d4e4f7",
            font=("Helvetica", 12), anchor="w").pack(fill=tk.X, padx=10, pady=2)

        job_url = job.get('url', '#')
        link_label = tk.Label(job_frame, text=f"URL: {job_url}", bg="#1e3d59", fg="#8ecae6",
                    font=("Helvetica", 12, "italic"), anchor="w", cursor="hand2")
        link_label.pack(fill=tk.X, padx=10, pady=2)

        def open_url(event):
            import webbrowser
            webbrowser.open(f"https://wuzzuf.net{job_url}")

        link_label.bind("<Button-1>", open_url)

    root = tk.Tk()
    root.title("Scraped Jobs Viewer")
    root.configure(bg="#1e3d59")
    root.geometry("800x600")

    canvas = tk.Canvas(root, bg="#1e3d59", highlightthickness=0)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="#1e3d59")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    for job in jobs:
        create_job_block(job, scroll_frame)

    root.mainloop()


if __name__ == "__main__":
    display_jobs()