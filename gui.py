import tkinter as tk
from tkinter import ttk
import threading
import time
import subprocess
import json

def run_spider_and_update_gui(results_frame, canvas):
    start_time = time.time()

    process = subprocess.Popen(
        ['scrapy', 'crawl', 'your_spider_name'], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    stdout, stderr = process.communicate()

    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    item_count = extract_item_count(stdout)

    result_label = tk.Label(results_frame, text=f"Elapsed Time: {elapsed_time}s, Items Scraped: {item_count}", 
                            bg="#1e3d59", fg="#d4e4f7", font=("Helvetica", 12))
    result_label.pack(fill=tk.X, pady=5)

    display_jobs(results_frame, canvas)


def extract_item_count(log_output):
    """
    Extract the number of items scraped from the Scrapy log output.
    Customize this based on your Scrapy log format.
    """
    for line in log_output.splitlines():
        if "Scraped from" in line:
            return line.split()[-1]
    return 0


def display_jobs(frame, canvas):
    for widget in frame.winfo_children():
        widget.destroy()

    try:
        with open("wuzzufscraper/wuzzufscraper/spiders/raw-jobs.json", "r", encoding="utf-8") as file:
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
            webbrowser.open(job_url)

        link_label.bind("<Button-1>", open_url)

    for job in jobs:
        create_job_block(job, frame)

    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))


def main():
    root = tk.Tk()
    root.title("Wuzzuf Scraper")
    root.configure(bg="#1e3d59")
    root.geometry("800x600")
    root.iconbitmap("C:/Users/Anthony/Documents/GitHub/Web-Scraping/wuzzuf-logo.png")

    canvas = tk.Canvas(root, bg="#1e3d59", highlightthickness=0)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    results_frame = tk.Frame(canvas, bg="#1e3d59")
    canvas.create_window((0, 0), window=results_frame, anchor="nw")

    run_button = tk.Button(root, text="Run Spider", command=lambda: threading.Thread(target=run_spider_and_update_gui, args=(results_frame, canvas)).start(), 
                           bg="#ff6b6b", fg="white", font=("Helvetica", 12, "bold"))
    run_button.pack(pady=10)

    display_jobs(results_frame, canvas)

    root.mainloop()


if __name__ == "__main__":
    main()