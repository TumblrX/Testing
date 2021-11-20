
import { settings_variables  } from './settings_mapping_var';

/**
 * This fnction to sign in
 * @param {string}           password password 
 * @param {string}           email    email.
 */

 export function signIn(password,email){
    cy.visit('https://www.tumblr.com/')
    cy.get('.Fygd5 .Z8Ux2').contains('Log in').click({force: true})
    cy.get('input[name="email"]').type(email).should("be.visible")
    cy.get('input[name="password"]').type(password).should("be.visible")
    cy.get('.EvhBA').contains('Log in').click({force: true})
}

/**
 * This fnction test open settings from the search bar icon
 */

export function settingsIconClicked(){
    cy.get(settings_variables.account_icon).click({multiple: true})
    cy.get(settings_variables.settings_icon).click({multiple: true})
}

/**
 * This function test that new password and confirm new password are identical either alert with specific message 
 * @param {string}           old_password password that would be cahnged.
 * @param {string}           new_password new password.
 * @param {string}           alert_nomatch_message alert message that should appear.
 */
 export function doesntMatchPasswords(old_password,new_password,alert_nomatch_message){
    cy.get(settings_variables.change_password).click({multiple:true})
    cy.wait(3000)
    cy.get(settings_variables.current_pass_input).clear().type(old_password)
    cy.get(settings_variables.new_password_input).type(new_password)
    cy.get(settings_variables.confirm_password_input).type(old_password)
    cy.get(settings_variables.confirm_newpass_button).click()
    cy.wait(3000)
    cy.get(settings_variables.alert_notmatch_password).contains(alert_nomatch_message)
    cy.get(settings_variables.cancel_password).click()
}
/**
 * This function test that new password and confirm new password are identical either alert with specific message 
 * @param {string}           old_password password that would be cahnged.
 * @param {string}           new_password new password.
 * @param {string}           alert_nomatch_message alert message that should appear when new password and confirm new password aren't same.
 * @param {string}           alert_empty_message alert message that should appear when old password input left empty.
 */
 export function EmptyPasswordAndNoMatch(old_password,new_password,alert_nomatch_message,alert_empty_message){
        cy.get(settings_variables.change_password).click({multiple:true})
        cy.wait(3000)
        cy.get(settings_variables.current_pass_input).clear()
        cy.get(settings_variables.new_password_input).type(new_password)
        cy.get(settings_variables.confirm_password_input).type(old_password)
        cy.get(settings_variables.confirm_newpass_button).click()
        cy.wait(3000)
        cy.get(settings_variables.alert_emptycurrent_password).contains(alert_empty_message)
        cy.get(settings_variables.alert_notmatch_password).contains(alert_nomatch_message)
        cy.get(settings_variables.cancel_password).click()
}
/**
 * This function test that old password and  new password must be different 
 * @param {string}           old_password password that would be cahnged.
 * @param {string}           alert_samePassword_message alert message that should appear when old password is same as new one.
 */
 export function samePassword(old_password,alert_samePassword_message){
    cy.get(settings_variables.change_password).click({multiple:true})
    cy.wait(3000)
    cy.get(settings_variables.current_pass_input).clear().type(old_password)
    cy.get(settings_variables.new_password_input).type(old_password)
    cy.get(settings_variables.confirm_password_input).type(old_password)
    cy.get(settings_variables.confirm_newpass_button).click()
    cy.wait(5000)
    cy.get(settings_variables.alert_same_password).contains(alert_samePassword_message)
    cy.get(settings_variables.cancel_password).click()
}

/**
 * This function test the error message when the new password is easy to guessed
 * @param {string}           old_password password that would be cahnged.
 * @param {string}           easy_password new password 
 * @param {string}           alert_easyGuessPassword_message alert message that should appear when new password is easy to be guessed.
 */
 export function easyGuessed(old_password,easy_password,alert_easyGuessPassword_message){
    cy.get(settings_variables.change_password).click({multiple:true})
    cy.wait(3000)
    cy.get(settings_variables.current_pass_input).clear().type(old_password)
    cy.get(settings_variables.new_password_input).type(easy_password)
    cy.get(settings_variables.confirm_password_input).type(easy_password)
    cy.get(settings_variables.confirm_newpass_button).click()
    cy.wait(5000)
    cy.get(settings_variables.alert_same_password).contains(alert_easyGuessPassword_message)
    cy.get(settings_variables.cancel_password).click()
}

/**
 * This function test the error message when the new password is less than 8 characters
 * @param {string}           old_password password that would be cahnged.
 * @param {string}           weak_password new password 
 * @param {string}           alert_weakPassword_message alert message that should appear when new password is less than 8 characters.
 */
 export function weakPassword(old_password,weakPassword,alert_weakPassword_message){
    cy.get(settings_variables.change_password).click({multiple:true})
    cy.wait(3000)
    cy.get(settings_variables.current_pass_input).clear().type(old_password)
    cy.get(settings_variables.new_password_input).type(weakPassword)
    cy.get(settings_variables.confirm_password_input).type(weakPassword)
    cy.get(settings_variables.confirm_newpass_button).click()
    cy.wait(5000)
    cy.get(settings_variables.alert_same_password).contains(alert_weakPassword_message)
    cy.get(settings_variables.cancel_password).click()
}

/**
 * This function test changing password successfully
 * @param {string}           old_password password that would be cahnged.
 * @param {string}           new_password new password 
 */
 export function successfulChange(old_password,new_password){
    cy.get(settings_variables.change_password).click({multiple:true})
    cy.wait(3000)
    cy.get(settings_variables.current_pass_input).clear().type(old_password)
    cy.get(settings_variables.new_password_input).type(new_password)
    cy.get(settings_variables.confirm_password_input).type(new_password)
    cy.wait(3000)
    cy.get(settings_variables.confirm_newpass_button).click()

}

