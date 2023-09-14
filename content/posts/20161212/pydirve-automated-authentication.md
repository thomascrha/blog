Title: Pydirve Automated Authentication
Date: 2016-12-12 21:36
Tags:
Category: 
Slug: pydirve-automated-authentication
Summary:
Status: published

This seems to be something that is not clearly documented and can be frustrating to set up - especially when involving a crontab. The biggest problem is how the oauth scheme is defined by pydirve itself. It requires the user to have <code>client_secrets.json</code> next to the script you are developing; or create a custom flow in code, which isn't the best practice

The Pydirve module has a convenient way to create custom work flows without having it directly in code; making updates to credentials and keys easier. <code>settings.yaml</code> is the mechanism used to create these custom authentication schemes. This file is fully outlined in [this](http://pythonhosted.org/PyDrive/oauth.html) page. Before you can start defining your own oauth work-flow you'll need to download your <code>client_secrets.json</code> from the [Google API Console](https://console.developers.google.com). The instructions for this are outlined within the Pydirve [docs]('https://pythonhosted.org/PyDrive/quickstart.html').

The <code>client_secrets.json</code> contains several fields which are needed for the <code>settings.yaml</code> file. Below is a copy of my <code>client_secrets.json</code> file - with the sensitive data hashed out.

~~~~
"client_id":"################.apps.googleusercontent.com",
"project_id":"YOUR_PROJECT_NAME",
"auth_uri":"https://accounts.google.com/o/oauth2/auth",
"token_uri":"https://accounts.google.com/o/oauth2/token",
"auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
"client_secret":"#############",
"redirect_uris":["http://localhost:8080/"],
"javascript_origins":["http://localhost:8080"]
~~~~

How Pydirve works out of the box is; you initialize the Class <code>GoogleAuth</code> and then call the Class method <code>LocalWebserverAuth()</code>. What this method does is call the <code>client_secrets.json</code> file and uses it to determine the API endpoint you wish to access. It then starts a local browser session - using the settings provided in <code>client_secrets.json</code> - which then requires the user to confirm the Google Account to be used and whether it can have permission to do so.

What we need to do is automate this user interaction. To do so we need to save the credential/work-flow file produced during the call to <code>LocalWebserverAuth()</code>. Pydrive has a method to do so. To save this file run the code snippet below, keeping note of the outputted file - the file produced is required to automate the oauth process.

~~~~
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
gauth.SaveCredentialsFile('./cred.json')
~~~~

Now we have our credential file, we can finally construct our <code>settings.yaml</code> file. I used this sample provided on the [PyDrive docs site](http://pythonhosted.org/PyDrive/oauth.html#sample-settings-yaml) to create mine.

~~~~
settings.yaml
client_config_backend: settings
client_config:
   #make sure these match the client_secrets.json
   client_id: ###########################.apps.googleusercontent.com
   client_secret: #################
   auth_uri: https://accounts.google.com/o/oauth2/auth
   token_uri: https://accounts.google.com/o/oauth2/token
   redirect_uri: http://localhost:8080/ 

save_credentials: True  
save_credentials_backend: file  
save_credentials_file: /abs/path/to/pydrive-credentials.json

get_refresh_token: True

oauth_scope:
  - https://www.googleapis.com/auth/drive
  - https://www.googleapis.com/auth/drive.file
  - https://www.googleapis.com/auth/drive.install 

~~~~

The main points from this file are that the <code>client_config_backend</code> is set to settings. This tells PyDrive to use the settings listed below; rather than using the <code>client_secrets.json</code> file. If you set it to <code>file</code> you can set the path of it via the <code>client_config_file</code> setting. This method seems to cause a crontab problems; as the <code>client_config_file</code> doesn't seem to be scope-able by the cron daemon - at least that's my experience. 

Now to use this oauth work flow simply issue this code - replacing <code>SETTINGS</code> with your file ( be sure to make it an abs path).

~~~~
gauth = GoogleAuth(SETTINGS)
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
~~~~ 

Now you'll have a <code>Drive</code> object ready to use and upload/manipulate files to your [Google Drive](http://drive.google.com)!
