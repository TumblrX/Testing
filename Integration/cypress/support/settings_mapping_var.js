/** 
 *  for account icon in the search bar
 * @const 
 * */
 const ACCOUNT_ICON = '#root > div > .NavBar_navbar__2Ztou > .NavBar_container__1Z4JI > div:nth-child(4) > .NavBar_icons__2zmsz > span:nth-child(6) > svg '
 /** 
  *  for settings icon in the dropdown menu when account icon is clicked
  * @const 
  * */
 const SETTINGS_ICON = '#root > div > .NavBar_navbar__2Ztou > .NavBar_container__1Z4JI > div:nth-child(4) > .NavBar_icons__2zmsz > div:nth-child(9) > div > ul:nth-child(2) > a:nth-child(3) > div'
 /** 
  *  for change passsword button in account window
  * @const 
  * */
 const CHANGE_PASSWORD = '#root > div:nth-child(2) > div > div > form:nth-child(3) > div:nth-child(3) > img:nth-child(4)'
 /** 
  *  for cancel changing button
  * @const 
  * */ 
 const CANCEL_PASSWORD = '.Account_cancel-button__2eK0S'
 /** 
  *  for current password input box
  * @const 
  * */
 const CURRENT_PASS_INPUT = 'input[id="currentpassword"]'
 /** 
  *  for new password input box
  * @const 
  * */
 const NEW_PASSWORD_INPUT ='input[id="newpassword"]'
 /** 
  *  for confirm new password input box
  * @const 
  * */
 const CONFIRM_PASSWORD_INPUT = 'input[id="confirmpassword"]'
 /** 
  *  for confirm password change button
  * @const 
  * */
 const CONFIRM_NEWPASS_BUTTON = '.Account_save-button__24Zzk'
 /** 
  *  location when alert message appears 
  * @const 
  * */
 const ALERT_WEAK_PASSWORD = '#root > div:nth-child(2) > div > div > form:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > div'
 /** 
  *  location when alert message appears 
  * @const 
  * */
 const ALERT_SAME_PASSWORD = '#root > div:nth-child(2) > div > div > form:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > div'
 /** 
  *  location when alert message appears 
  * @const 
  * */
 const ALERT_NOMATCH_PASSWORD = '#root > div:nth-child(2) > div > div > form:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(2)'
 /** 
  *  location when alert message appears 
  * @const 
  * */
 const ALERT_EMPTYCURRENT_PASSWORD = '#root > div:nth-child(2) > div > div > form:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)'
 /** 
  * location when alert message appears 
  * @const 
  * */
 const ALERT_EMPTYNEWPASSWORD_PASSWORD = '#root > div:nth-child(2) > div > div > form:nth-child(3) > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > div'
 /** 
  *  alert message appears when the password input box left empty
  * @const 
  * */
 const ALERT_EMPTY_MESSAGE ="Please Enter your password Correctly"
 /** 
  *  alert message appears when the new password dowsn't match with confirm new password
  * @const 
  * */
 const ALERT_NOMATCH_MESSAGE ="Please Enter Identical Passwords"
 /** 
  *  alert message appears when the new password is weak
  * @const 
  * */
 const ALERT_WEAK_MESSAGE ="Please Enter Strong Password"
 /** 
  *  alert message appears when the new password is easy to be guessed
  * @const 
  * */
 const ALERT_EASYGUESS_MESSAGE ="Please Enter Strong Password"
 /** 
  *  alert message appears when the new password is exactly same as old one
  * @const 
  * */
 const ALERT_SAMEPASSWORD_MESSAGE = "Sorry, you've used that password before. You must choose a new password."
 
 
 /** 
  * var to hold the old password
  * 
  * @var */
 var oldPassword = '1234567menna'
 /** 
  * var to hold the new password
  * 
  * @var */
 var newPassword ='1234567menna'
 /** 
  * var to hold the weak password
  * @var */
 var weakPassword = '1234'
 /** 
  * var to hold the easy password
  * @var */
 var easyPassword = '1234567890'
 /** 
  * var to hold the email
  * @var */
 var email ='mennaahmedali77@gmail.com'
 
 /** @const */const SETTINGS_VARIABLES = {
     ACCOUNT_ICON:ACCOUNT_ICON,
     SETTINGS_ICON:SETTINGS_ICON,
     CHANGE_PASSWORD:CHANGE_PASSWORD,
     CURRENT_PASS_INPUT:CURRENT_PASS_INPUT,
     NEW_PASSWORD_INPUT:NEW_PASSWORD_INPUT,
     CONFIRM_PASSWORD_INPUT:CONFIRM_PASSWORD_INPUT,
     CONFIRM_NEWPASS_BUTTON:CONFIRM_NEWPASS_BUTTON,
     oldPassword:oldPassword,
     newPassword:newPassword,
     weakPassword:weakPassword,
     ALERT_WEAK_PASSWORD:ALERT_WEAK_PASSWORD,
     ALERT_NOMATCH_PASSWORD:ALERT_NOMATCH_PASSWORD,
     ALERT_EMPTYCURRENT_PASSWORD:ALERT_EMPTYCURRENT_PASSWORD,
     CANCEL_PASSWORD:CANCEL_PASSWORD,
     ALERT_SAME_PASSWORD:ALERT_SAME_PASSWORD,
     email:email,
     ALERT_NOMATCH_MESSAGE:ALERT_NOMATCH_MESSAGE,
     easyPassword:easyPassword,
     ALERT_WEAK_MESSAGE:ALERT_WEAK_MESSAGE,
     ALERT_EASYGUESS_MESSAGE:ALERT_EASYGUESS_MESSAGE,
     ALERT_SAMEPASSWORD_MESSAGE:ALERT_SAMEPASSWORD_MESSAGE,
     ALERT_EMPTY_MESSAGE:ALERT_EMPTY_MESSAGE,
     ALERT_EMPTYNEWPASSWORD_PASSWORD:ALERT_EMPTYNEWPASSWORD_PASSWORD
 }
 module.exports={SETTINGS_VARIABLES}