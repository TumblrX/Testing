/** 
 *  for account icon in the search bar
 * @const 
 * */
const ACCOUNT_ICON = '#root > #base-container > .D5eCV > .hlDot > ._3kR_ > .uuWZ2 > .KTRcB:nth-child(6)'
/** 
 *  for settings icon in the dropdown menu when account icon is clicked
 * @const 
 * */
const SETTINGS_ICON = ACCOUNT_ICON + ' > .BPf9u > .ybmTG > .AzqQv > .PsDsm > .noQqZ:nth-child(2) > li:nth-child(3)'
/** 
 *  for change passsword button in account window
 * @const 
 * */
const CHANGE_PASSWORD = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)'
/** 
 *  for cancel changing button
 * @const 
 * */ 
const CANCEL_PASSWORD = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(4) > button:nth-child(1)'
/** 
 *  for current password input box
 * @const 
 * */
const CURRENT_PASS_INPUT = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(1) > .WJF54 > input:nth-child(1)'
/** 
 *  for new password input box
 * @const 
 * */
const NEW_PASSWORD_INPUT ='#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > .zYSrd > .WJF54 > .gWXwV'
/** 
 *  for confirm new password input box
 * @const 
 * */
const CONFIRM_PASSWORD_INPUT = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(3) > .WJF54 > .gWXwV'
/** 
 *  for confirm password change button
 * @const 
 * */
const CONFIRM_NEWPASS_BUTTON = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(4) > button:nth-child(2)'
/** 
 *  location when alert message appears 
 * @const 
 * */
const ALERT_WEAK_PASSWORD = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(2) > .LPUrm'
/** 
 *  location when alert message appears 
 * @const 
 * */
const ALERT_SAME_PASSWORD = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(2) > .LPUrm'
/** 
 *  location when alert message appears 
 * @const 
 * */
const ALERT_NOMATCH_PASSWORD = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(3) > div:nth-child(2)'
/** 
 *  location when alert message appears 
 * @const 
 * */
const ALERT_EMPTYCURRENT_PASSWORD = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(1) > div:nth-child(2)'
/** 
 * location when alert message appears 
 * @const 
 * */
const ALERT_EMPTYNEWPASSWORD_PASSWORD = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(3) > div:nth-child(2)'
/** 
 *  alert message appears when the password input box left empty
 * @const 
 * */
const ALERT_EMPTY_MESSAGE ="Password is empty."
/** 
 *  alert message appears when the new password dowsn't match with confirm new password
 * @const 
 * */
const ALERT_NOMATCH_MESSAGE ="Passwords don't match."
/** 
 *  alert message appears when the new password is weak
 * @const 
 * */
const ALERT_WEAK_MESSAGE ="The password must be at least 8 characters."
/** 
 *  alert message appears when the new password is easy to be guessed
 * @const 
 * */
const ALERT_EASYGUESS_MESSAGE ="That password is known to be included in compromised password lists. Please choose something more unique."
/** 
 *  alert message appears when the new password is exactly same as old one
 * @const 
 * */
const ALERT_SAMEPASSWORD_MESSAGE = "Sorry, you've used that password before. You must choose a new password."


/** 
 * var to hold the old password
 * 
 * @var */
var oldPassword = '211257mennamenna'
/** 
 * var to hold the new password
 * 
 * @var */
var newPassword ='211257mennamennaa'
/** 
 * var to hold the weak password
 * @var */
var weakPassword = '1122'
/** 
 * var to hold the easy password
 * @var */
var easyPassword = 'mennamenna'
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
    ALERT_EMPTY_MESSAGE:ALERT_EMPTY_MESSAGE
}
module.exports={SETTINGS_VARIABLES}