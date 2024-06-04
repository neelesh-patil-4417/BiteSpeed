# BiteSpeed
Bitespeed needs a way to identify and keep track of a customer's identity across multiple purchases.

## Description

This project is designed to help Bitespeed identify and track a customer's identity across multiple purchases on FluxKart.com. Given the scenario where a customer might use different email addresses and phone numbers for different purchases, this service reconciles those identities into a single customer profile.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/bitespeed-identity-reconciliation.git](https://github.com/neelesh-patil-4417/BiteSpeed.git
    ```
2. Navigate to the project directory:
    ```sh
    cd BiteSpeed
    ```
3. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Apply the database migrations:
    ```sh
    python manage.py migrate
    ```
2. Start the development server:
    ```sh
    python manage.py runserver
    ```
3. The API will be available at `http://127.0.0.1:8000/`.

## Endpoints

### POST /identify

**Description:** Receives a JSON body containing an email and/or phone number and returns the consolidated contact information.

**Case 1** When a new entry is added

<img width="431" alt="image" src="https://github.com/neelesh-patil-4417/BiteSpeed/assets/104721593/76e828dc-e98b-46b0-820b-86a1b4d8cfb3">


**result 1**

<img width="455" alt="image" src="https://github.com/neelesh-patil-4417/BiteSpeed/assets/104721593/fa2dc658-938c-44d1-aeec-4ff8e243dcb4">


**Case 2** When a new entry with either same phone or email is added

<img width="417" alt="image" src="https://github.com/neelesh-patil-4417/BiteSpeed/assets/104721593/cb268e20-c2d1-497b-ac3c-f3fbf8921bbc">


**result 2**

<img width="453" alt="image" src="https://github.com/neelesh-patil-4417/BiteSpeed/assets/104721593/de418692-5323-4df0-b13d-574fd18f2677">


**Case 3** When there are two primary entries and one to be converted to secondary

<img width="487" alt="image" src="https://github.com/neelesh-patil-4417/BiteSpeed/assets/104721593/45dd4930-6811-4862-a6b2-c98cf7f3d679">

<img width="521" alt="image" src="https://github.com/neelesh-patil-4417/BiteSpeed/assets/104721593/102439ec-4baa-4a04-a748-e940c7b4ed70">


**Result 3**

<img width="454" alt="image" src="https://github.com/neelesh-patil-4417/BiteSpeed/assets/104721593/00c3bc62-1882-48b1-bb26-d4ccc7c67b6e">



