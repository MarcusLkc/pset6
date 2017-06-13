# Sentiments
tweet analyzer
Problem set 6 from Harvards cs50 online course used to Analyze the tweets of existing or non-Pirvate twitter users

Find Twitter USers
![image](https://user-images.githubusercontent.com/26131181/27068613-f8799bc6-4fde-11e7-89a5-4ca1d4290c66.png)


Analyze their Tweets for Sentiments

![image](https://user-images.githubusercontent.com/26131181/27069380-6de9e02a-4fe2-11e7-8fe2-4ad585f6981c.png)



Or got to the command line ./tweets screen_name       to find screen name tweets colord in red and green or orange where screen_name is equal to the person's screen name you are looking for
![image](https://user-images.githubusercontent.com/26131181/27069530-3477d5a8-4fe3-11e7-9ebe-663c54b3af16.png)

To actively use you must apply for twitter keys from apps.twitter.com if you have an account if not just sign up for one then access it

after following steps 
Click Keys and Access Tokens.

Click modify app permissions.

Select Read only, then click Update Settings.

Highlight and copy the value to the right of Consumer Key (API Key).

In a terminal window, execute

export API_KEY=value
where value is that (pasted) value, without any space immediately before or after the =.

Highlight and copy the value to the right of Consumer Secret (API Secret).

In a terminal window, execute

export API_SECRET=value
where value is that (pasted) value, without any space immediately before or after the =

(Instructions taken from http://docs.cs50.net/problems/sentiments/sentiments.html#code-smile-code-2)

to run server test just use

flask run

in designated folder
