"""
optimisation_def.py
-------------------
This module provides functions to optimize and minify various file types such as HTML, JS, CSS, and JSON.
Each function takes a file path, reads the file, applies optimisation, and overwrites the file with the optimised content.
Extend this module by adding new functions for additional file types as needed.
"""
import json
import minify_html
import requests


# Function to optimize HTML files
def optimize_html(file_path):
    """
    Optimize an HTML file by minifying its content, including embedded JS and CSS.
    Args:
        file_path (str): Path to the HTML file to optimize.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        html = file.read()
        optimized_html = minify_html.minify(html, minify_js=True, minify_css=True, keep_comments=False, keep_spaces_between_attributes=True)
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(optimized_html)

# Function to optimize JS files
def optimize_js(file_path):
    """
    Optimize a JavaScript file by minifying its content using an online API.
    Args:
        file_path (str): Path to the JS file to optimize.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        js = file.read()
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"input": js}
        optimized_js = requests.post("https://www.toptal.com/developers/javascript-minifier/api/raw", headers=headers, data=data, timeout=10).text 
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(optimized_js)

# Function to optimize CSS files
def optimize_css(file_path):
    """
    Optimize a CSS file by minifying its content using an online API.
    Args:
        file_path (str): Path to the CSS file to optimize.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        css = file.read()
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"input": css}
        optimized_css = requests.post("https://www.toptal.com/developers/cssminifier/api/raw", headers=headers, data=data, timeout=10).text
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(optimized_css)

# Function to optimize JSON files
def optimize_json(file_path):
    """
    Optimize a JSON file by removing unnecessary whitespace and formatting.
    Args:
        file_path (str): Path to the JSON file to optimize.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        json_data = json.load(file)
        optimized_json = json.dumps(json_data, separators=(',', ':'))
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(optimized_json)

# Extensions to be optimized
mapping = {
    ".html": optimize_html,
    ".js": optimize_js,
    ".css": optimize_css,
    ".json": optimize_json
}
