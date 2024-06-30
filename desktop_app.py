"""
This file is for getting information about cryptocurrencies.

Created by: Feliks Voskanyan
Date: 12.06.2024
"""

import os
import tkinter
from tkinter import filedialog
import sys
import xlsxwriter
import requests

def open_file():
    """
    Function: open_file
    Brief: Opens a file dialog for the user to select a file,
    then reads the file and extracts crypto names.
    Params: None
    Return: List of cryptocurrency names
    """
    get_name = []

    def crypto_name():
        """
        Function: crypto_name
        Brief: Reads selected file and extracts crypto names.
        Params: None
        Return: None
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, encoding='utf-8') as file:
                content = file.readlines()
                for i in content:
                    get_name.append(i.strip())
        else:
            get_name.append("Bitcoin")
        root.destroy()

    root = tkinter.Tk()
    root.title("File Opener")
    root.geometry("300x250+200+200")
    open_button = tkinter.Button(root, text="Find File", command=crypto_name)
    open_button.pack()
    root.mainloop()

    return get_name

def get_api(file):
    """
    Function: get_api
    Brief: Reads the API address from a file.
    Params: file (str): The path to the file containing the API address.
    Return: The API address as a string.
    """
    with open(file, "r", encoding='utf-8') as api_file:
        return api_file.read().strip()

def get_crypto_data(api_url):
    """
    Function: get_crypto_data
    Brief: Requests and retrieves cryptocurrency data from the API.
    Params: api_url (str): The URL of the API.
    Return: List of cryptocurrency data or None if the request fails.
    """
    try:
        params = {"vs_currency": "usd", "price_change_percentage": "24h"}
        response = requests.get(api_url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as error:
        print("Error", error)
        return None

def get_data_by_name(crypto_names, content):
    """
    Function: get_data_by_name
    Brief: Searches for cryptocurrencies by name and retrieves their information.
    Params: crypto_names (list): List of cryptocurrency names to search for.
            content (list): List of cryptocurrency data.
    Return: List of cryptocurrency data filtered by the specified names.
    """
    data = []
    try:
        for name in crypto_names:
            for crypto in content:
                if name.lower() == crypto['name'].lower():
                    data.append({
                        'name': crypto['name'],
                        'symbol': crypto['symbol'],
                        'current_price': crypto['current_price'],
                        'market_cap': crypto['market_cap'],
                        'total_volume': crypto['total_volume'],
                        'price_change_24h': crypto['price_change_24h']
                    })
        return data
    except Exception as error:
        print("Error", error)
        return []

def write_in_xlsx(crypto_data):
    """
    Function: write_in_xlsx
    Brief: Opens a dialog for the user to save data to an XLSX file.
    Params: crypto_data (list): List of cryptocurrency data.
    Return: None
    """
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
    if not file_path:
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        file_path = os.path.join(downloads_folder, "default_filename.xlsx")

    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet("Sheet")
    try:
        headers = crypto_data[0].keys()
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)
        for row, crypto in enumerate(crypto_data, start=1):
            for col,(key,value) in enumerate(crypto.items()):
                worksheet.write(row, col, value)
        workbook.close()
    except Exception as error:
        print("Error", error)
        workbook.close()

def main():
    """
    Main function to orchestrate the retrieval and saving of cryptocurrency data.
    """
    crypto_names = open_file()
    api_url = get_api("api.txt")
    data = get_crypto_data(api_url)

    if not data:
        print("Error in request")
        sys.exit(1)

    data_by_name = get_data_by_name(crypto_names, data)
    if not data_by_name:
        print("Error in cryptocurrency name")
        sys.exit(1)

    write_in_xlsx(data_by_name)

if __name__ == "__main__":
    main()
