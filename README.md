# onlyfans-login-has-solved-recaptcha-captcha-and-sign-signature
onlyfans login has solved recaptcha captcha and sign signature.  
There are two difficulties in logging in to onlyfans:  

**1. recaptcha captcha**
**2. sign signature.**

recaptcha recaptcha is easy to do, just use the captcha service.  
 
**The signature method of sign is: dynamic string + unix timestamp + api url + userid**  
like this:  
"
  T3x8fDeLQdpTIWo7dUT36xpsQlCt9vpD
  1720664157785
  /api2/v2/users/login
  0
"  
Here are the steps:  
1. String sha1 encryption
2. Checksum the encrypted sha1 hex string
3. Combining Strings
   
# like this: 26344:663774d8b0111c9bb23b59f4256a320f8dfa8d61:b51:668ec169    
**26344** is fixed  
**663774d8b0111c9bb23b59f4256a320f8dfa8d61** is sha1 hex  
**b51**  is checksum  
**668ec169** is fixed  
In the code, I have extracted the js code of the checksum part, so it can be solved by calling the js code  

If you need my help, please DM me on tg. [@shineho](https://t.me/shineho)
