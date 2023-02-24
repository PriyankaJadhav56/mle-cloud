# Deploying Flask App in Azure Linux VM

# Setting up the VM
Boot a linux VM in azure. In the portal, navigate to the VM page, go to networking. Add inbound rule for port 5000 in the security group of the VM.

Port 5000 and Host 0.0.0.0 will be used for testing flask application.

# Install dependencies
`$ sudo apt-get install python python3-pip`

# Create virtualenv
`$ mkdir -p www/flaskapp `
`$ cd www/flaskapp`
`$ pip3 install virtualenv	`
`$ python3 -m virtualenv flaskenv 	`
`$ chmod 755 flaskenv/ `

# Install python dependencies
`$ source flaskenv/bin/activate`
`$ python -V`
`$ pip install flask`
`$ pip install azure-storage`


# Run the flask application
`$ FLASK_APP=app.py`
`$ flask run -h 0.0.0.0`

# Billing Cost 
Below is the screenshot of the billing cost of all the resources associated with this project

![screencapture-portal-azure-2023-02-24-17_13_21 (1)](https://user-images.githubusercontent.com/111682825/221185278-5a297425-7055-4988-aa54-ce88067de342.png)

