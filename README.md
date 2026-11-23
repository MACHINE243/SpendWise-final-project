# SpendWise

A front-end finance dashboard prototype with a login/start screen, demo income and expense tracking, budgets, transactions, and analytics.

## Project files
- `index.html` — app structure
- `style.css` — styling and responsive layout
- `app.js` — client-side demo interactions
- `app.py` — optional Flask development server

## Run locally (static)
Open `index.html` in your browser.

## Run with Flask
Install Flask: `pip install flask`
Then run: `python app.py`
Open `http://127.0.0.1:5000`.

## Notes
Authentication buttons and password recovery are demo placeholders. Login accepts any non-empty username/email and password. Transactions are held in browser memory and are not saved to a database.

For Netlify static deployment, publish the project folder with `index.html` at its root. Netlify does not run `app.py`; the frontend files are served as static assets.
