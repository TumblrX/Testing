const account_icon = '#root > #base-container > .D5eCV > .hlDot > ._3kR_ > .uuWZ2 > .KTRcB:nth-child(6)'
const settings_icon = account_icon + ' > .BPf9u > .ybmTG > .AzqQv > .PsDsm > .noQqZ:nth-child(2) > li:nth-child(3)'
const change_password = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)'
const cancel_password = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(4) > button:nth-child(1)'

const current_pass_input = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(1) > .WJF54 > input:nth-child(1)'
const new_password_input ='#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > .zYSrd > .WJF54 > .gWXwV'
const confirm_password_input = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(3) > .WJF54 > .gWXwV'
const confirm_newpass_button = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(4) > button:nth-child(2)'
const alert_weak_password = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(2) > .LPUrm'
const alert_same_password = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(2) > .LPUrm'

const alert_notmatch_password = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(3) > div:nth-child(2)'
const alert_emptycurrent_password = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(1) > div:nth-child(2)'
const alert_emptynewpassword_password = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(4) > div:nth-child(2) > div:nth-child(1) > .QseG4 > form > div:nth-child(3) > div:nth-child(2)'

const alert_empty_message ="Password is empty."
const alert_nomatch_message ="Passwords don't match."
const alert_weak_message ="The password must be at least 8 characters."
const alert_easyGuess_message ="That password is known to be included in compromised password lists. Please choose something more unique."
const alert_samePassword_message = "Sorry, you've used that password before. You must choose a new password."


const old_password = '211257mennamenna'
const new_password ='211257mennamennaa'
const weak_password = '1122'
const easy_password = 'mennamenna'
const email ='mennaahmedali77@gmail.com'

const settings_variables = {
    account_icon:account_icon,
    settings_icon:settings_icon,
    change_password:change_password,
    current_pass_input:current_pass_input,
    new_password_input:new_password_input,
    confirm_password_input:confirm_password_input,
    confirm_newpass_button:confirm_newpass_button,
    old_password:old_password,
    new_password:new_password,
    weak_password:weak_password,
    alert_weak_password:alert_weak_password,
    alert_notmatch_password:alert_notmatch_password,
    alert_emptycurrent_password:alert_emptycurrent_password,
    cancel_password:cancel_password,
    alert_same_password:alert_same_password,
    email:email,
    alert_nomatch_message:alert_nomatch_message,
    easy_password:easy_password,
    alert_weak_message:alert_weak_message,
    alert_easyGuess_message:alert_easyGuess_message,
    alert_samePassword_message:alert_samePassword_message,
    alert_empty_message:alert_empty_message
}
module.exports={settings_variables}