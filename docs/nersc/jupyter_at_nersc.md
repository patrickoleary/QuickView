# Using JupyterHub to log in to NERSC

To use the QuickView family of tools at NERSC, you first need to login to JupyterHub using
[this link](https://jupyter.nersc.gov/hub/login), which will bring you to a page like the screenshot below.

![JupyterHub login](./login/login-00.png)

Clicking on the orange "Sign in with Federated Identity at NERSC" button will
bring you to a new page to enter your __username__ and __password__;
after that, you will need to fill an OTP (One Time Password):

![](./login/login-01.png)

After a successful login, you will be presented with a list of options for where you would like to run your application.
For the QuickView family, it is better to have hardware with a GPU to allow interactive rendering.
Keep in mind, though, that time spent on anywhere else than a login node will be charged to your project's allocation.
Hence, after you are done with the analysis, remember to
[shut down the service](#shut-down-the-server-when-you-are-done) to avoid wasteful use of the resources. 

![](./login/login-02.png)

After clicking on one of the "start" buttons in the image above,
you will see something like the screenshot below and will
likely have to wait for some seconds for the service to be ready.

![](./login/login-03.png)

# Shut down the server when you are done

::: warning Reminder: Shut down the server when you are done.
After finishing your analysis, please remember to shut down the connection to your selected
server (node) to stop the charging of hours to your project's allocation.
This is explained at the end of
[this video](https://docs.nersc.gov/beginner-guide/#keypad-entry-log-in-using-jupyter),
and below is a recap of the steps (clicks):
- go to the JupytherHub window/tab in your browser,
- click `File` in the top-left corner,
- scroll down and choose `Hub Control Panel`,
- in the Control Panel brought up in a new browser tab/window, click on the red "stop" button
  for the server to be shut down. An example is shown in the screenshot below.

![](./login/login-04.png)
:::

