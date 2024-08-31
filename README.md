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

---

### ⚠️⚠️⚠️ Disclaimer ⚠️⚠️⚠️
This guide and the accompanying information are provided for educational and informational purposes only. **They are not intended for commercial use**. The author does not endorse or support any use of this information that may violate the terms and conditions of Onlyfans, GitHub, or any other platform mentioned.

By using this guide, you acknowledge that:
- You are solely responsible for how you choose to use the information provided.
- Any actions taken based on this guide are done at your own risk.
- The author is not liable for any direct or indirect damages, including but not limited to account suspension, legal consequences, or any other issues arising from the use of this information.
- You agree to comply with all applicable laws and regulations in your jurisdiction. Any legal repercussions resulting from the use or misuse of this information are solely your responsibility, and the author assumes no liability.

This guide is intended to foster learning and understanding. It should not be used to engage in any illegal or unethical activities. If you have any doubts or concerns, please consult with legal professionals or refer to the terms and conditions of the respective platforms before proceeding.

coding need my help, pls dm me on tg. [@shineho](https://t.me/shineho).
