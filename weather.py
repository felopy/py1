#!/usr/bin/env python3
import sys
import os
import argparse
import datetime
import requests

def check_file_existence(fname):
    answer = True
    if not os.path.isfile(fname):
        print(f"Input file does not exists. Please check {fname}")
        answer = False
    return answer

def get_celsius(kelvin):
    celsius = kelvin -273.15
    return celsius

def get_response(fname,mcity):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    with open(fname, 'r', encoding="utf-8") as mfile:
        api_key = mfile.read().strip()
    url = base_url + "appid=" + api_key + "&q=" + mcity
    response = requests.get(url).json()
    return response

def get_elements(mresponse):
    kelvin = mresponse['main']['temp']
    celsius = get_celsius(kelvin)
    feels_like_kelvin = mresponse['main']['feels_like']
    feels_like_celsius = get_celsius(feels_like_kelvin)
    wind_speed = mresponse['wind']['speed']
    humidity = mresponse['main']['humidity']
    description = mresponse['weather'][0]['description']
    sunrise= datetime.datetime.utcfromtimestamp(mresponse['sys']['sunrise']+mresponse['timezone'])
    sunset= datetime.datetime.utcfromtimestamp(mresponse['sys']['sunset']+mresponse['timezone'])
    return celsius, feels_like_celsius, wind_speed,humidity, description, sunrise, sunset

def showing(mlist,mname,ttrue,htrue,wtrue,dtrue,strue):
    if ttrue == htrue == wtrue == dtrue == strue == False:
        print(f"Temperature in {mname}: {mlist[0]:.2f}°C")
        print(f"Temperature in {mname} feels like: {mlist[1]:.2f}°C")
        print(f"Humidity in {mname}: {mlist[3]}%")
        print(f"Wind Speed in {mname}: {mlist[2]} m/s")
        print(f"General Weather in {mname}:{mlist[4]}")
        print(f"Sun rises in {mname} at {mlist[5]} local time.")
        print(f"Sun setss in {mname} at {mlist[6]} local time.")
    if ttrue:
        print(f"Temperature in {mname}: {mlist[0]:.2f}°C")
        print(f"Temperature in {mname} feels like: {mlist[1]:.2f}°C")
    if htrue:
        print(f"Humidity in {mname}: {mlist[3]}%")
    if wtrue:
        print(f"Wind Speed in {mname}: {mlist[2]} m/s")
    if dtrue:
        print(f"General Weather in {mname}:{mlist[4]}")
    if strue:
        print(f"Sun rises in {mname} at {mlist[5]} local time.")
        print(f"Sun setss in {mname} at {mlist[6]} local time.")

def chcking_api_code(mrespond):
    answer = True
    if mrespond['cod'] == 401:
        print(mrespond['message'])
        answer = False
    elif mrespond['cod'] == '404':
        print("City Not Found!")
        answer = False
    return answer

def main():
    fname = "api_key.txt"
    check = check_file_existence(fname)
    if not check:
        sys.exit()
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--temperature", action="store_true", help="Will show temperature")
    parser.add_argument("-w", "--wind", action="store_true", help="Will show wind speed")
    parser.add_argument("-u", "--humidity", action="store_true", help="Will show humidity")
    parser.add_argument("-d", "--description", action="store_true", help="Will show description")
    parser.add_argument("-s", "--sun",action="store_true", help="Will show sunrise and sunset time")
    parser.add_argument("city", type=str, help="the city name")
    args = parser.parse_args()
    res = get_response(fname,args.city)
    check = chcking_api_code(res)
    if not check:
        sys.exit()
    info = get_elements(res)
    showing(info,args.city,args.temperature,args.humidity,args.wind,args.description,args.sun)

main()
