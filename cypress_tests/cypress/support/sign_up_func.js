
import { VARIABLES } from './sign_up_mapping_var';

/**
 * this function allow us to test the ideal case
 */
export function workingSignUp() {
    cy.get(VARIABLES.BEGIN_SIGN_UP).contains('Sign up').click({ force: true })
    cy.get(VARIABLES.INPUT_EMAIL).type("nadaelsayed163@gmail.com").should("be.visible")
    cy.get(VARIABLES.INPUT_PASSWORD).click({ force: true }).type("nadaelsayed147258369").should("be.visible")
    cy.get(VARIABLES.INPUT_BLOGNAME).click({ force: true }).type("Nada-Elsayed-CMP").should("be.visible")
    cy.get(VARIABLES.SIGN_UP_ACTION).contains('Sign up').click({ force: true })
    cy.get(VARIABLES.INPUT_AGE).click({ force: true }).type("20").should("be.visible")
    cy.get(VARIABLES.NEXT_ACTION).contains('Next').click({ force: true })
}
/**
 * this function allow us to change email and other parameter will be ideal
 * @param {string}           emailOption  email that will be tested.
 * @param {string}           msg          massage that expected to appeare.
 */
export function invalidEmailSignUp(emailOption, msg) {
    cy.get(VARIABLES.BEGIN_SIGN_UP).contains('Sign up').click({ force: true })
    if (emailOption != "") {
        cy.get(VARIABLES.INPUT_EMAIL).type(emailOption).should("be.visible")
    }
    cy.get(VARIABLES.INPUT_PASSWORD).click({ force: true }).type("nadaelsayed147258369").should("be.visible")
    cy.get(VARIABLES.INPUT_BLOGNAME).click({ force: true }).type("Nada-Elsayed-CMP").should("be.visible")
    cy.get(VARIABLES.SIGN_UP_ACTION).contains('Sign up').click({ force: true })
    cy.get(VARIABLES.ERROR_MSG_FIRST).contains(msg)
}
/**
 * this function allow us to change password and other parameter will be ideal
 * @param {string}           passOption   password that will be tested.
 * @param {string}           msg          massage that expected to appeare.
 */
export function invalidPasswordSignUp(passOption, msg) {
    cy.get(VARIABLES.BEGIN_SIGN_UP).contains('Sign up').click({ force: true })
    cy.get(VARIABLES.INPUT_EMAIL).type("nadaelsayed163@gmail.com").should("be.visible")
    if (passOption != "") {
        cy.get(VARIABLES.INPUT_PASSWORD).click({ force: true }).type(passOption).should("be.visible")
    }
    cy.get(VARIABLES.INPUT_BLOGNAME).click({ force: true }).type("Nada-Elsayed-CMP").should("be.visible")
    cy.get(VARIABLES.SIGN_UP_ACTION).contains('Sign up').click({ force: true })
    cy.get(VARIABLES.ERROR_MSG_FIRST).contains(msg)
}
/**
 * this function allow us to change blog name and other parameter will be ideal
 * @param {string}           blogNameOption   blog name that will be tested.
 * @param {string}           msg              massage that expected to appeare.
 */
export function invalidBlogNameSignUp(blogNameOption, msg) {
    cy.get(VARIABLES.BEGIN_SIGN_UP).contains('Sign up').click({ force: true })
    cy.get(VARIABLES.INPUT_EMAIL).type("nadaelsayed163@gmail.com").should("be.visible")
    cy.get(VARIABLES.INPUT_PASSWORD).click({ force: true }).type("nadaelsayed147258369").should("be.visible")
    cy.get(VARIABLES.INPUT_BLOGNAME).click({ force: true }).type(blogNameOption).should("be.visible")
    cy.get(VARIABLES.SIGN_UP_ACTION).contains('Sign up').click({ force: true })
    cy.get(VARIABLES.ERROR_MSG_FIRST).contains(msg)
}
/**
 * this function allow us to change age and other parameter will be ideal
 * @param {string}           age_Option   age that will be tested.
 * @param {string}           msg          massage that expected to appeare.
 */
export function invalidAgeSignUp(age_Option, msg) {
    cy.get(VARIABLES.BEGIN_SIGN_UP).contains('Sign up').click({ force: true })
    cy.get(VARIABLES.INPUT_EMAIL).type("nadaelsayed163@gmail.com").should("be.visible")
    cy.get(VARIABLES.INPUT_PASSWORD).click({ force: true }).type("nadaelsayed147258369").should("be.visible")
    cy.get(VARIABLES.INPUT_BLOGNAME).click({ force: true }).type("Nada-Elsayed-CMP2020").should("be.visible")
    cy.get(VARIABLES.SIGN_UP_ACTION).contains('Sign up').click({ force: true })
    if (age_Option != "") {
        cy.get(VARIABLES.INPUT_AGE).click({ force: true }).type(age_Option).should("be.visible")
    }
    cy.get(VARIABLES.NEXT_ACTION).contains('Next').click({ force: true })
    cy.get(VARIABLES.ERROR_MSG_SECOND).contains(msg)
}
