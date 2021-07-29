# Dev Assessment - Webhook Receiver

Please use this repository for constructing the Flask webhook receiver.

*******************

## Setup

* Create a new virtual environment

```bash
pip install virtualenv
```

* Create the virtual env

```bash
virtualenv venv
```

* Activate the virtual env

```bash
source venv/bin/activate
```

* Install requirements

```bash
pip install -r requirements.txt
```

* Run the flask application (In production, please use Gunicorn)

```bash
python run.py
```

* The endpoint is at:

```bash
POST http://127.0.0.1:5000/webhook/receiver
```

You need to use this as the base and setup the flask app. Integrate this with MongoDB (commented at `app/extensions.py`)

*******************

This is the final look for the web app for showcasing the last actions on the github repository <code> action-repo </code>. I have integrated both Push and Pull Requests. The server will update new information from MongoDB every 15 seconds as specified. 

![image](https://user-images.githubusercontent.com/54668114/127480793-01e38da7-84fa-44d7-89ea-1ee4a1c8bb86.png)
