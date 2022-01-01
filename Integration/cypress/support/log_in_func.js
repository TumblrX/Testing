
import { VARIABLES } from './log_in_mapping_var';

/**
 * this function allow us to test the ideal case
 */
export function workingLogIn() {
    cy.get(VARIABLES.BEGIN_LOG_IN).contains('Log in').click({ force: true })
    cy.get(VARIABLES.INPUT_EMAIL).type("Ammar@gmail.com").should("be.visible")
    cy.get(VARIABLES.INPUT_PASSWORD).click({ force: true }).type("123456").should("be.visible")
    cy.get(VARIABLES.LOG_IN_ACTION).contains('Log in').click({ force: true })
    cy.url().should('include', '/dashboard')
}
/**
 * this function allow us to change email and other parameter will be ideal
 * @param {string}           emailOption  email that will be tested.
 * @param {string}           msg          massage that expected to appeare.
 */
export function invalidEmailLogIn(emailOption, msg) {
    cy.get(VARIABLES.BEGIN_LOG_IN).contains('Log in').click({ force: true })
    if (emailOption != "") {
        cy.get(VARIABLES.INPUT_EMAIL).type(emailOption).should("be.visible")
    }
    cy.get(VARIABLES.INPUT_PASSWORD).click({ force: true }).type("nadaelsayed147258369").should("be.visible")
    cy.get(VARIABLES.LOG_IN_ACTION).contains('Log in').click({ force: true })
    if(emailOption == ""){
        cy.get(VARIABLES.ERROR_MSG_EMPTY_EMAIL).contains(msg)
    }else{
        cy.get(VARIABLES.ERROR_MSG_WRONG_DATA).contains(msg)
    }
}
/**
 * this function allow us to change password and other parameter will be ideal
 * @param {string}           passOption   password that will be tested.
 * @param {string}           msg          massage that expected to appeare.
 */
export function invalidPasswordLogIn(passOption, msg) {
    cy.get(VARIABLES.BEGIN_LOG_IN).contains('Log in').click({ force: true })
    cy.get(VARIABLES.INPUT_EMAIL).type("nadaelsayed163@gmail.com").should("be.visible")
    if (passOption != "") {
        cy.get(VARIABLES.INPUT_PASSWORD).click({ force: true }).type(passOption).should("be.visible")
    }
    cy.get(VARIABLES.LOG_IN_ACTION).contains('Log in').click({ force: true })
    if(passOption == ""){    
        cy.get(VARIABLES.ERROR_MSG_EMPTY_PASSWORD).contains(msg)
    }else{
        cy.get(VARIABLES.ERROR_MSG_WRONG_DATA).contains(msg)
    }
}
