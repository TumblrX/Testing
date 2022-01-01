
import { SETTINGS_VARIABLES  } from './settings_mapping_var';

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
    cy.get(SETTINGS_VARIABLES.ACCOUNT_ICON).click({multiple: true})
    cy.get(SETTINGS_VARIABLES.SETTINGS_ICON).click({multiple: true})
}

/**
 * This function test that new password and confirm new password are identical either alert with specific message 
 * @param {string}           oldPassword password that would be cahnged.
 * @param {string}           newPassword new password.
 * @param {string}           alertNoMatchMessage alert message that should appear.
 */
 export function doesntMatchPasswords(oldPassword,newPassword,alertNoMatchMessage){
    cy.get(SETTINGS_VARIABLES.CHANGE_PASSWORD).click({multiple:true})
    cy.wait(3000)
    cy.get(SETTINGS_VARIABLES.CURRENT_PASS_INPUT).clear().type(oldPassword)
    cy.get(SETTINGS_VARIABLES.NEW_PASSWORD_INPUT).type(newPassword)
    cy.get(SETTINGS_VARIABLES.CONFIRM_PASSWORD_INPUT).type(oldPassword)
    cy.get(SETTINGS_VARIABLES.CONFIRM_NEWPASS_BUTTON).click()
    cy.wait(3000)
    cy.get(SETTINGS_VARIABLES.ALERT_NOMATCH_PASSWORD).contains(alertNoMatchMessage)
    cy.get(SETTINGS_VARIABLES.CANCEL_PASSWORD).click()
}
/**
 * This function test that new password and confirm new password are identical either alert with specific message 
 * @param {string}           oldPassword password that would be cahnged.
 * @param {string}           newPassword new password.
 * @param {string}           alertNoMatchMessage alert message that should appear when new password and confirm new password aren't same.
 * @param {string}           alertEmptyMessage alert message that should appear when old password input left empty.
 */
 export function EmptyPasswordAndNoMatch(oldPassword,newPassword,alertNoMatchMessage,alertEmptyMessage){
        cy.get(SETTINGS_VARIABLES.CHANGE_PASSWORD).click({multiple:true})
        cy.wait(3000)
        cy.get(SETTINGS_VARIABLES.CURRENT_PASS_INPUT).clear()
        cy.get(SETTINGS_VARIABLES.NEW_PASSWORD_INPUT).type(newPassword)
        cy.get(SETTINGS_VARIABLES.CONFIRM_PASSWORD_INPUT).type(oldPassword)
        cy.get(SETTINGS_VARIABLES.CONFIRM_NEWPASS_BUTTON).click()
        cy.wait(3000)
        cy.get(SETTINGS_VARIABLES.ALERT_EMPTYCURRENT_PASSWORD).contains(alertEmptyMessage)
        cy.get(SETTINGS_VARIABLES.ALERT_NOMATCH_PASSWORD).contains(alertNoMatchMessage)
        cy.get(SETTINGS_VARIABLES.CANCEL_PASSWORD).click()
}
/**
 * This function test that old password and  new password must be different 
 * @param {string}           oldPassword password that would be cahnged.
 * @param {string}           alertSamePasswordMessage alert message that should appear when old password is same as new one.
 */
 export function samePassword(oldPassword,alertSamePasswordMessage){
    cy.get(SETTINGS_VARIABLES.CHANGE_PASSWORD).click({multiple:true})
    cy.wait(3000)
    cy.get(SETTINGS_VARIABLES.CURRENT_PASS_INPUT).clear().type(oldPassword)
    cy.get(SETTINGS_VARIABLES.NEW_PASSWORD_INPUT).type(oldPassword)
    cy.get(SETTINGS_VARIABLES.CONFIRM_PASSWORD_INPUT).type(oldPassword)
    cy.get(SETTINGS_VARIABLES.CONFIRM_NEWPASS_BUTTON).click()
    cy.wait(5000)
    cy.get(SETTINGS_VARIABLES.ALERT_SAME_PASSWORD).contains(alertSamePasswordMessage)
    cy.get(SETTINGS_VARIABLES.CANCEL_PASSWORD).click()
}

/**
 * This function test the error message when the new password is easy to guessed
 * @param {string}           oldPassword password that would be cahnged.
 * @param {string}           easyPassword new password 
 * @param {string}           alertEasyGuessPasswordMessage alert message that should appear when new password is easy to be guessed.
 */
 export function easyGuessed(oldPassword,easyPassword,alertEasyGuessPasswordMessage){
    cy.get(SETTINGS_VARIABLES.CHANGE_PASSWORD).click({multiple:true})
    cy.wait(3000)
    cy.get(SETTINGS_VARIABLES.CURRENT_PASS_INPUT).clear().type(oldPassword)
    cy.get(SETTINGS_VARIABLES.NEW_PASSWORD_INPUT).type(easyPassword)
    cy.get(SETTINGS_VARIABLES.CONFIRM_PASSWORD_INPUT).type(easyPassword)
    cy.get(SETTINGS_VARIABLES.CONFIRM_NEWPASS_BUTTON).click()
    cy.wait(5000)
    cy.get(SETTINGS_VARIABLES.ALERT_SAME_PASSWORD).contains(alertEasyGuessPasswordMessage)
    cy.get(SETTINGS_VARIABLES.CANCEL_PASSWORD).click()
}

/**
 * This function test the error message when the new password is less than 8 characters
 * @param {string}           oldPassword password that would be cahnged.
 * @param {string}           weakPassword new password 
 * @param {string}           alertWeakPasswordMessage alert message that should appear when new password is less than 8 characters.
 */
 export function weakPassword(oldPassword,weakPassword,alertWeakPasswordMessage){
    cy.get(SETTINGS_VARIABLES.CHANGE_PASSWORD).click({multiple:true})
    cy.wait(3000)
    cy.get(SETTINGS_VARIABLES.CURRENT_PASS_INPUT).clear().type(oldPassword)
    cy.get(SETTINGS_VARIABLES.NEW_PASSWORD_INPUT).type(weakPassword)
    cy.get(SETTINGS_VARIABLES.CONFIRM_PASSWORD_INPUT).type(weakPassword)
    cy.get(SETTINGS_VARIABLES.CONFIRM_NEWPASS_BUTTON).click()
    cy.wait(5000)
    cy.get(SETTINGS_VARIABLES.ALERT_SAME_PASSWORD).contains(alertWeakPasswordMessage)
    cy.get(SETTINGS_VARIABLES.CANCEL_PASSWORD).click()
}

/**
 * This function test changing password successfully
 * @param {string}           oldPassword password that would be cahnged.
 * @param {string}           newPassword new password 
 */
 export function successfulChange(oldPassword,newPassword){
    cy.get(SETTINGS_VARIABLES.CHANGE_PASSWORD).click({multiple:true})
    cy.wait(3000)
    cy.get(SETTINGS_VARIABLES.CURRENT_PASS_INPUT).clear().type(oldPassword)
    cy.get(SETTINGS_VARIABLES.NEW_PASSWORD_INPUT).type(newPassword)
    cy.get(SETTINGS_VARIABLES.CONFIRM_PASSWORD_INPUT).type(newPassword)
    cy.wait(3000)
    cy.get(SETTINGS_VARIABLES.CONFIRM_NEWPASS_BUTTON).click()

}

